# Agent Prompt — Set Up a Realistic Shopify Retention Demo Store

Copy everything below into Codex or Claude Code from a clean working directory. Attach or install the `shopify-retention-architect` plugin first.

---

You are setting up a **dedicated Shopify development store** so we can exercise the `shopify-retention-architect` skill against real Shopify data, real ShopifyQL/Admin API results, Joy ingestion, Joy MCP, and Klaviyo MCP.

This is an execution task, not a planning exercise. Build the seeder, run it against the confirmed development store, verify the resulting analytics, and leave a reproducible manifest and cleanup/resume tooling. Do not stop after scaffolding code.

## Repositories and product context

Retention plugin:

```text
https://github.com/thomasavada/shopify-retention-architect
```

Read first:

```text
skills/shopify-retention-architect/SKILL.md
skills/shopify-retention-architect/references/demo-store-data.md
skills/shopify-retention-architect/references/joy-mcp-execution.md
skills/shopify-retention-architect/references/klaviyo-mcp-execution.md
```

Joy source, if present locally:

```text
/Users/thomas/Projects/joy
```

Joy already contains a BigQuery-only demo analytics service:

```text
packages/functions/src/services/devZone/analyticsSeedService.js
```

That service does **not** create Shopify customers/orders and does not populate ShopifyQL. The work here must create actual products, customers, and orders in Shopify first. Joy analytics may be seeded or reconciled separately afterward.

## Non-negotiable safety gate

Before writing anything:

1. Discover the connected Shopify CLI/account/store state.
2. Print the exact target `*.myshopify.com` domain and store type.
3. Prove it is a Shopify development/test store. Use Shopify CLI/Partner metadata or another authoritative signal; do not infer from the domain name.
4. Query current order/product/customer counts and inspect for real merchant data.
5. Refuse to proceed if it is production, transfer-ready merchant data, or ambiguous.
6. If more than one eligible development store exists and no target is supplied, stop and ask Thomas to select one.
7. Never echo or commit credentials. Reuse existing Shopify CLI/auth setup or environment-secret references.

No seed mutation is allowed until the development-store check passes.

## API and permissions

Use Shopify Admin GraphQL API, a currently supported stable API version, and the store's existing authenticated app/session. Required access should include at least:

```text
read_products
write_products
read_customers
write_customers
read_orders
write_orders
read_analytics   # if the chosen ShopifyQL path requires it
```

Do not invent an access token. If the existing app lacks a required scope, report the exact missing scope and complete the proper reinstall/re-authorize flow.

Use the official `orderCreate` mutation for historical orders. `OrderCreateOrderInput.processedAt` accepts an ISO-8601 timestamp in the past, and Shopify uses it as the date displayed on orders and in analytics reports. Do not try to backdate immutable `createdAt`.

Official references:

```text
https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCreate
https://shopify.dev/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput
https://shopify.dev/docs/api/usage/limits
```

Use:

- `processedAt` for the historical timeline.
- Existing variant IDs for line items.
- The same customer identity for repeat orders.
- `financialStatus: PAID` and a successful SALE transaction where supported.
- Fulfilled status/details appropriate to the chosen API schema.
- `options.sendReceipt: false` and `options.sendFulfillmentReceipt: false`.
- A deterministic `sourceIdentifier`, tags, note, and/or metafield containing `SHOPX_RETENTION_DEMO` and the fixture version.
- A deterministic idempotency key in local state even if the mutation has no server-side idempotency header.

Do not send customer email/SMS. Use reserved synthetic addresses under `example.com` and never opt profiles into marketing.

## Historical timeline

Create a deterministic 12-month history ending at the actual current time on execution day.

- Oldest order: approximately 365 days before execution.
- Newest fulfilled order: 1–3 days before execution.
- No future `processedAt` values.
- Respect timezone and store currency.
- Spread orders naturally across weekdays/months; include moderate seasonality rather than a flat histogram.
- Save timestamps in the fixture before mutation so retries do not change history.

The history must be visible in Shopify analytics/queries by `processedAt`. After seeding, verify monthly order counts from oldest month through current month.

## Store scenario

Create a fictional, original functional-beverage brand. Do not copy a real merchant, Sun Bum, OLIPOP, or their assets/copy.

Suggested concept:

```text
Brand: FizzyRoot
Promise: playful botanical soda for everyday shared rituals
Visual character: colorful, sociable, retro-futurist
Currency: store currency discovered at runtime
```

### Catalog

Create realistic product/variant records, inventory where needed, images that are original or safe placeholders, costs/prices, SKUs, handles, tags, and collections:

1. Starter 6-Pack — entry product
2. Core 12-Pack — replenishment product
3. Discovery Variety Pack — discovery product
4. Daily Ritual Bundle — high-AOV bundle SKU
5. Build-a-Table Bundle — a multi-line basket pattern
6. Limited Seasonal Flavor — drop product
7. Glass & Tote Set — durable merchandise
8. Subscription-eligible replenishment product/plan if the installed subscription setup supports it

Represent bundles in two useful ways:

- A dedicated bundle product/variant so bundle-level Shopify reporting is available.
- Multi-line baskets containing complementary products so cross-sell/basket analysis is possible.

Do not claim Shopify Bundles component semantics unless the store actually has a supported bundle implementation. If not, label the dedicated SKU as a demo bundle and document the limitation.

## Required population

Target approximately:

```text
300 purchasing customers
500 fulfilled, paid orders
12 months of processedAt history
```

Customer distribution should be deterministic and internally consistent:

```text
180 customers with exactly 1 order
75 customers with exactly 2 orders
30 customers with exactly 3 orders
15 customers with 5 or more orders
```

Ensure the exact total equals 500 orders. Do not merely sample each order independently; generate customer journeys first, then orders.

Expected second-purchase rate:

```text
customers with 2+ orders / customers with 1+ orders
= 120 / 300
= 40%
```

Verify this from Shopify after seeding rather than hard-coding it in the report.

## Behavioral cohorts

Create coherent repeat behavior:

### First-order-only cohort

- 180 customers.
- Mix of recent customers not yet due and older customers who failed to repeat.
- Do not make every one-order customer look lapsed.

### Replenishment cohort

- Repeat in roughly 28–45 days.
- Often repurchase the Core 12-Pack or same category.
- Some become plausible subscription candidates after three stable intervals.

### Discovery cohort

- First order is a Discovery Variety Pack.
- Later order selects one or two favorite core flavors/products.

### Bundle-upgrade cohort

- Starts with Starter 6-Pack.
- Moves to 12-Pack or Daily Ritual Bundle.
- Bundle AOV should be materially above overall AOV.

### VIP cohort

- High frequency and spend across multiple orders.
- Not just one unusually expensive order.

### At-risk cohort

- Previously repeated.
- Last order is over approximately 1.5× the customer's normal interval.

### Lapsed cohort

- Previously repeated.
- Last order is over approximately 2.5× normal interval.

### Subscription candidates

- At least three same-category purchases.
- At least two reasonably stable intervals.
- Keep a small active-subscriber-like cohort only if the installed subscription implementation can represent it honestly; otherwise mark candidates without fabricating subscription contracts.

## Economics and order realism

Generate realistic variability:

```text
Entry orders: 25–40
Pack orders: 45–75
Bundle orders: 80–130
VIP/large orders: 130–220
Target overall AOV: roughly 65–80
```

Include:

- Quantities greater than one in some orders.
- Multi-line orders.
- Shipping lines and addresses that are synthetic but structurally valid.
- A limited percentage of discounts, with several clearly named demo discount patterns.
- Most repeat orders without heavy discounting.
- A small number of cancelled/refunded orders only if the API path is implemented and verified; exclude them from the fulfilled-order target and retention denominator.
- No real payment gateway charge.
- No receipts or fulfillment emails.

Keep all names, phone numbers and addresses fictional. Prefer one or two synthetic regions sufficient for tax/shipping shape rather than pretending global operations.

## Idempotency, resume, and cleanup

Build a deterministic seeder in a new `demo-store/` directory in this repository. Use TypeScript or Python, whichever best fits the installed Shopify toolchain.

Required files:

```text
demo-store/README.md
demo-store/config.example.*
demo-store/fixture.json             # generated deterministic fixture
demo-store/seed.*                   # create/resume
 demo-store/verify.*                 # query actual results
 demo-store/cleanup.*                # best-effort cleanup
demo-store/state/manifest.json      # gitignored runtime IDs/state
demo-store/tests/                   # generation/math/unit tests
```

Do not commit secrets or runtime state.

Seeder requirements:

- Fixed random seed.
- Dry-run default; explicit `--apply` required.
- `--store` required; no implicit production target.
- Preflight development-store gate inside the script, not only in documentation.
- Create products first and persist product/variant IDs.
- Generate the complete customer journey fixture before API writes.
- Persist each successful customer/order mapping immediately.
- Resume safely after interruption without duplicating objects.
- Search by deterministic marker/source identifier before creating.
- Continue after transient errors; stop on schema/auth/business errors.
- Progress counters and ETA.
- Final reconciliation against Shopify, not local counters alone.

Cleanup must be honest about Shopify limitations. If an object cannot be deleted through the available API, tag/archive/cancel it as appropriate and document the residual data. Never promise perfect cleanup without testing it.

## Throttling

Shopify Admin GraphQL uses calculated query cost and a leaky-bucket throttle.

Current documented baseline:

```text
Standard: 100 points/second
Advanced: 200 points/second
Plus: 1,000 points/second
Enterprise: 2,000 points/second
Mutation base cost: 10 points, plus selected fields/manual costs
Single query maximum: 1,000 points
Maximum input array size: 250
```

Do not assume the theoretical maximum. Implement adaptive throttling from every response's:

```text
extensions.cost.requestedQueryCost
extensions.cost.actualQueryCost
extensions.cost.throttleStatus.currentlyAvailable
extensions.cost.throttleStatus.maximumAvailable
extensions.cost.throttleStatus.restoreRate
```

Rules:

1. Start conservatively at one or two order mutations per second.
2. Before the next call, estimate whether enough points are available.
3. Sleep based on the deficit divided by `restoreRate`, plus jitter.
4. On GraphQL `THROTTLED` or HTTP 429, honor `Retry-After` when present; otherwise exponential backoff with jitter.
5. Bound concurrency; do not fire 500 promises at once.
6. Retry network/429/5xx failures with a cap.
7. Do not retry validation/user errors unchanged.
8. Log costs and retry reasons without credentials.

At 500 orders, expect thousands of GraphQL cost points. A safe sequential/adaptive run can take several minutes; correctness and resumability matter more than speed.

## Pilot before full seed

Run staged gates:

1. Dry-run generation and unit tests.
2. Create catalog only; verify variants.
3. Create 3 synthetic customers and 10 orders spanning old/recent dates.
4. Verify `processedAt`, financial status, fulfillment, customer linkage, line items, analytics visibility and no email delivery.
5. Confirm Joy receives/processes the intended order events if Joy is installed.
6. Only then seed the remaining dataset.

If historical `orderCreate` webhooks reach Joy now but Joy interprets creation time instead of `processedAt`, stop and document the mismatch before full seeding. Fix the demo ingestion path or use Joy's separate analytics seeder with a clearly documented cross-system mapping; do not falsify reports.

## Joy setup

After Shopify verification:

1. Confirm Joy is installed on this dev store and identify the environment.
2. Wait for or trigger only the normal supported ingestion path; do not write directly to production Firestore.
3. Compare Shopify order/customer counts with Joy member/order/activity counts.
4. Use Joy MCP read tools first.
5. Present the recommended points, rewards, tiers, referral and widget as dry-run diffs.
6. Apply only after explicit approval.
7. Read back every write.
8. Build the widget in draft first and visually verify it.
9. Do not live-publish without separate approval.

If Joy's BigQuery demo seeder is used, use the same customer/order IDs and fixture timestamps where its schema permits, then prove that Shopify and Joy reports reconcile.

## Klaviyo setup

Use Klaviyo's official MCP server:

```text
https://mcp.klaviyo.com/mcp
```

Start read-only:

```text
https://mcp.klaviyo.com/mcp?read-only=true&disable-tools-with-user-generated-content=true&core-tools-only=true
```

1. Confirm the correct Klaviyo company/account.
2. Read existing segments, flows, events and exact Joy-synced profile properties.
3. Do not guess property names.
4. Present segment definitions and draft flow plan.
5. After explicit approval, create one segment/flow at a time.
6. Read back objects and segment counts.
7. Keep flows draft/inactive.
8. Do not activate flows or send campaigns without separate approval.

Synthetic `example.com` profiles must never receive email/SMS.

## Required verification queries

Use Shopify/Admin GraphQL/ShopifyQL as supported to report actual values:

- Total demo products/variants.
- Total demo customers.
- Total demo orders.
- Orders by month across 12 months.
- Customers with one or more orders.
- Customers with two or more orders.
- Exact second-purchase rate.
- Orders per customer.
- Overall AOV.
- First-time vs returning customer revenue if available.
- Median/p25/p75 time to second order, calculated from order timestamps if ShopifyQL does not expose it directly.
- Same-category and same-SKU repeat.
- Dedicated bundle performance.
- Multi-line basket performance.
- Discounted vs non-discounted repeat.
- Subscription candidates.
- At-risk/lapsed counts.

Do not read the answer from the fixture. Query Shopify and independently recalculate it from returned data.

## Definition of done

Do not report completion until all of these are true:

- Development-store identity proven.
- No credentials committed.
- Catalog exists and is verified.
- Approximately 300 synthetic customers and exactly 500 qualifying paid/fulfilled orders exist unless a platform limit is documented.
- Orders span the past 12 months through the present via `processedAt`.
- Resume/idempotency tested by rerunning the seeder.
- Throttling telemetry captured and no unhandled throttle failures remain.
- Shopify verification reports a 40% second-purchase rate from actual data, or explains and fixes any discrepancy.
- Bundle and repeat cohorts appear in actual query results.
- Joy ingestion/reconciliation status is verified.
- Klaviyo remains read-only/draft until separately approved.
- A final Markdown report includes exact counts, API costs, elapsed time, discrepancies, residual cleanup limitations, and commands to reproduce.

If blocked, return the exact blocker, evidence, and minimum human action. Never substitute fixture numbers for actual API results.
