# Demo development-store data

Seed only after confirming the target is a Shopify development store.

## Scenario

A fictional colorful functional-drink brand with bundles, subscriptions and enough repeat behavior to produce a meaningful retention diagnosis.

All records must include a marker such as `SHOPX_DEMO` in tags, note or product metadata where the API supports it.

## Products

Create a coherent catalog:

- Single can/entry product
- 6-pack
- 12-pack
- Variety pack
- Discovery bundle
- Monthly subscription product/plan if supported
- Limited seasonal flavor
- Merchandise/accessory item

Use realistic but fictional names and imagery. Do not imitate a real brand.

## Customer/order population

Target:

- 300 customers
- 500 fulfilled orders
- 12 months of order dates
- 60% customers with exactly one order
- 25% with exactly two orders
- 10% with three or four orders
- 5% with five or more orders

This creates a target second-purchase rate around 40% among purchasers, but calculate the actual result after seeding instead of assuming it landed exactly.

## Repeat patterns

Use coherent behavior, not random independent orders:

- Replenishment cohort: repeat 28–45 days, often same pack.
- Discovery cohort: first variety pack, then a favorite flavor.
- Bundle cohort: first single pack, then 12-pack or bundle.
- Subscription candidates: at least three purchases of the same category at stable intervals.
- At-risk cohort: previously repeated, now beyond 1.5× normal interval.
- Lapsed cohort: beyond 2.5× normal interval.
- VIP cohort: high frequency and spend, not just one expensive order.

## AOV distribution

Use a mixture rather than one fixed subtotal:

- Entry orders: 25–40
- Packs: 45–75
- Bundles: 80–130
- VIP/large orders: 130–220

Include some discounts, but do not make every repeat order discount-driven.

## Bundle evidence

Create orders that make a bundle recommendation defensible:

- A bundle with higher AOV and healthy conversion.
- A low-performing bundle for contrast.
- Cross-sell paths from first product to complementary product.

## Referral/loyalty evidence

Seed Joy analytics separately when available:

- Members and guests
- Earn/redeem activities
- Assisted orders
- Referral clicks/pending/completed orders
- Reward ladder usage
- Tier distribution

Joy's existing `analyticsSeedService` writes BigQuery only. It does not create Shopify customers/orders and therefore does not populate ShopifyQL.

## Verification

After Shopify seeding, query actual values:

- Customers with one or more orders
- Customers with two or more orders
- Second-purchase rate
- Orders/customer
- AOV
- First-time vs returning revenue
- Product and bundle performance
- Time to second order if obtainable

After Joy seeding, verify:

- Member count
- Cohort retention
- Reward ROI
- Referral funnel
- Assisted orders/revenue
- Program/tier config

If any expected metric is zero, inspect the underlying data path instead of altering the report output.

## Cleanup

Keep a manifest of created product/customer/order IDs. Provide a cleanup script or documented deletion path. Development-store orders may have platform restrictions on deletion; confirm before promising full cleanup.
