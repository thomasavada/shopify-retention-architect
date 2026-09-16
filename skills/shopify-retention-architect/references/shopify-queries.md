# Shopify query mechanics for the audit

Everything here was verified against a live store on API version 2025-10. Each item is a
silent failure — the query returns something plausible rather than an error — which is why
they are written down rather than left to be rediscovered.

**1. `customersCount` does not support the filters you want.** This pattern looks
reasonable and is wrong:

```graphql
# DO NOT TRUST — returns a number, but the filter was ignored
customersCount(query: "orders_count:>=2")
```

Measured on 2025-10: the response carries `extensions.search[].warnings` saying
`orders_count` and `tag` are `invalid_field`, yet still returns a count — and
`>=1` and `>=2` return the *identical* number. A wrong second-purchase rate then flows
into every downstream conclusion.

**Never put `orders_count` in a `query:` string at all.** On `customersCount` it is
ignored with a warning; on the `customers` connection it is worse — the response carries
**no** `extensions.search` block, so `customers(query: "orders_count:>=2")` simply returns
`edges: []` with nothing to tell you the filter was bogus. An agent that trusts it reports
"zero repeat customers" and concludes the brand has no retention at all.

Instead, paginate customers and do the counting yourself on `numberOfOrders`, which is a
real field rather than a search-index term:

```graphql
query($cursor: String) {
  customers(first: 250, after: $cursor) {
    edges { cursor node { id numberOfOrders amountSpent { amount } } }
    pageInfo { hasNextPage }
  }
}
```

Two cautions on that pagination. Tag filters silently exclude records that lost the tag —
on a store where another app had rewritten customer tags, `query: "tag:MARKER"` returned
3,492 of 3,506 customers, and the 14 missing were exactly the ones that mattered. Prefer
unfiltered pagination and filter in your own code where you can see what you dropped. And
`amountSpent` is lifetime, not trailing-12-month, so do not use it directly for tier
sizing without recomputing from orders in the window you care about.

**2. Reading orders silently truncates to 60 days.** An app without the
`read_all_orders` scope can only see orders from the last 60 days. Nothing errors —
the older orders are simply absent, so a "12-month" audit quietly becomes a 60-day one
and every cohort, AOV and trend is wrong. Confirm the scope before trusting any window
longer than 60 days.

**3. ShopifyQL needs this exact wrapper.** Verified working on 2025-10 — copy the shape,
not just the statement, because the surrounding selection set is where it usually breaks:

```graphql
query {
  shopifyqlQuery(query: "FROM sales SHOW total_sales, orders SINCE -365d UNTIL today") {
    tableData { columns { name dataType } rows }
    parseErrors
  }
}
```

Three things that will cost you a round trip each if you improvise instead:
`parseErrors` is a list of strings, so selecting `{ code message }` on it fails with
"Selections can't be made on scalars"; there is no `TableResponse` type to spread an
inline fragment on; and the rows field is `rows`, not `rowData`. In the statement itself,
`SHOW ... BY <column>` is a parse error — use `GROUP BY`. Read `parseErrors` before
trusting `tableData`, and note ShopifyQL bills to its own budget
(`extensions.shopifyqlCost`), separate from the GraphQL cost bucket.

