# Handoff prompt — continue from existing Shopify CLI connection

You are continuing a Shopify retention-demo setup on Thomas Nguyen's Mac. Shopify CLI is already installed, authenticated, and connected to the intended Shopify app/store. Reuse the existing session/config; do not ask Thomas to reconnect unless a live command proves it is missing or expired.

## Goal

Create and verify a realistic, synthetic retention dataset in the already-connected **Shopify development store**, then use it to run a retention audit and prepare approved Joy MCP + Klaviyo MCP setup.

Do real execution. Do not stop at a plan or code scaffold.

## Source of truth

Plugin repository:

```text
https://github.com/thomasavada/shopify-retention-architect
```

If it is not available locally, clone it. Then read:

```text
skills/shopify-retention-architect/SKILL.md
skills/shopify-retention-architect/references/demo-store-data.md
skills/shopify-retention-architect/references/joy-mcp-execution.md
skills/shopify-retention-architect/references/klaviyo-mcp-execution.md
prompts/setup-realistic-demo-store.md
```

Joy source may be available at:

```text
/Users/thomas/Projects/joy
```

Joy's existing `analyticsSeedService.js` seeds BigQuery only; it does not create Shopify products, customers, or orders and does not populate ShopifyQL.

## Existing connection — inspect before asking

Start by finding the current Shopify app directory and active CLI configuration. Check the current working directory, likely Shopify project directories, `shopify app info`, active app config, and the authenticated Partner/store context.

Do not print access tokens or secrets.

Report:

```text
App:
Client ID:
Connected *.myshopify.com store:
Store type:
API version:
Current product/customer/order counts:
```

### Hard safety gate

Before any mutation, prove through authoritative Shopify/Partner/CLI metadata that the target is a development/test store. Also inspect current data for signs of a real merchant.

- If it is clearly the intended development store: continue without asking again.
- If it is production, transfer-ready merchant data, or ambiguous: stop before writes and ask Thomas to select/confirm the target.
- Never seed a production merchant.

## Build location

Implement the reusable seeder inside the cloned plugin repository under:

```text
demo-store/
```

Required artifacts:

```text
demo-store/README.md
demo-store/config.example.*
demo-store/fixture.json
demo-store/seed.*
demo-store/verify.*
demo-store/cleanup.*
demo-store/state/manifest.json   # runtime, gitignored
demo-store/tests/
```

Use TypeScript or Python based on the existing authenticated Shopify project/toolchain. Reuse the established app/session rather than creating a second Shopify app.

## Dataset

Create a fictional functional-beverage store called **FizzyRoot** or another clearly fictional original brand.

Catalog:

1. Starter 6-Pack
2. Core 12-Pack
3. Discovery Variety Pack
4. Daily Ritual Bundle — dedicated high-AOV bundle SKU
5. Build-a-Table Bundle — represented through multi-line baskets
6. Limited Seasonal Flavor
7. Glass & Tote Set
8. Subscription-eligible replenishment item only if the installed subscription setup supports it honestly

Use original/safe placeholder assets and synthetic data only.

Create:

```text
300 purchasing customers
500 paid and fulfilled qualifying orders
12 months of historical order dates through the present
```

Exact customer distribution:

```text
180 customers × exactly 1 order = 180
75 customers × exactly 2 orders = 150
30 customers × exactly 3 orders = 90
15 customers × at least 5 orders = 80 total orders across this cohort
Total                              = 500 orders
```

For the 15-customer high-frequency cohort, deterministically distribute the 80 orders while every customer has at least 5.

Expected second-purchase rate, to be verified from Shopify rather than copied from this prompt:

```text
customers with 2+ orders / customers with 1+ orders
= 120 / 300
= 40%
```

## Historical orders

Use Shopify Admin GraphQL `orderCreate` with `OrderCreateOrderInput.processedAt`.

- Oldest `processedAt`: approximately 365 days before execution.
- Newest fulfilled order: 1–3 days before execution.
- No future timestamps.
- Use ISO-8601 with the store timezone handled explicitly.
- `processedAt` must drive the date shown on orders and Shopify analytics.
- Do not attempt to mutate/backdate `createdAt`.

Official references:

```text
https://shopify.dev/docs/api/admin-graphql/latest/mutations/orderCreate
https://shopify.dev/docs/api/admin-graphql/latest/input-objects/OrderCreateOrderInput
https://shopify.dev/docs/api/usage/limits
```

For repeat orders, link all orders to the same Shopify customer identity. Use variant IDs, paid status/successful SALE transaction where supported, fulfilled status, and realistic line items.

Every object/order must have deterministic markers such as:

```text
SHOPX_RETENTION_DEMO
SHOPX_RETENTION_DEMO_V1
```

Use a deterministic `sourceIdentifier`, tags, notes, or metafields so reruns can detect existing records.

Never send email/SMS:

```text
options.sendReceipt = false
options.sendFulfillmentReceipt = false
```

Use only synthetic `example.com` addresses. Do not add marketing consent. Do not charge a real gateway.

## Realistic customer journeys

Generate complete customer journeys first, then derive orders. Do not generate 500 independent random orders.

Include:

- Replenishment cohort: repeat around 28–45 days, often same category.
- Discovery cohort: Variety Pack first, then favorite 12-Pack/flavor.
- Bundle-upgrade cohort: Starter 6-Pack → 12-Pack or Daily Ritual Bundle.
- Subscription candidates: at least three same-category purchases and at least two stable intervals.
- VIP cohort: high frequency and spend across multiple orders.
- At-risk repeaters: last purchase over about 1.5× normal cadence.
- Lapsed repeaters: last purchase over about 2.5× cadence.
- Recent first-time buyers who are not due yet.
- Older one-time buyers who failed to repeat.

AOV ranges:

```text
Entry orders: 25–40
Pack orders: 45–75
Bundle orders: 80–130
VIP/large orders: 130–220
Target overall AOV: roughly 65–80
```

Include quantities >1, multi-line baskets, a modest discount rate, and mostly non-discount-driven repeat. Do not claim native Shopify Bundles semantics unless the store actually supports them.

## Seeder behavior

- Fixed random seed.
- Dry-run by default; `--apply` required.
- Explicit `--store` required.
- Development-store check implemented in code.
- Save the entire fixture before writes.
- Persist every successful remote ID immediately.
- Resume after interruption without duplicates.
- Search by deterministic marker/source identifier before creating.
- Stop on auth/schema/business validation errors.
- Retry only transient network/429/5xx/`THROTTLED` errors.
- Provide progress, ETA, actual GraphQL costs, and a final reconciliation.

## Shopify API throttling

Admin GraphQL uses calculated query cost and a leaky bucket. Do not send all orders concurrently.

Start at one or two `orderCreate` mutations per second and adapt using every response's:

```text
extensions.cost.requestedQueryCost
extensions.cost.actualQueryCost
extensions.cost.throttleStatus.currentlyAvailable
extensions.cost.throttleStatus.maximumAvailable
extensions.cost.throttleStatus.restoreRate
```

If capacity is insufficient:

```text
sleep ≈ point deficit / restoreRate + jitter
```

On GraphQL `THROTTLED` or HTTP 429, honor `Retry-After` if present; otherwise use capped exponential backoff with jitter. Keep concurrency bounded. A several-minute run is acceptable.

## Pilot gate

Do not seed all 500 orders immediately.

1. Generate fixture and pass unit/math tests.
2. Create catalog and verify variants.
3. Create 3 customers and 10 orders spanning historical and recent dates.
4. Query Shopify to verify customer linkage, `processedAt`, paid/fulfilled state, line items, analytics visibility, and absence of email delivery.
5. Confirm how Joy ingests those orders if Joy is installed.
6. Only then continue the remaining dataset.

If Joy receives the webhook now but incorrectly treats all imported orders as current instead of using Shopify `processedAt`, stop before the full seed and report evidence. Reconcile through a supported ingestion fix or Joy's separate analytics seeder using the same IDs/timestamps; do not falsify data.

## Verification — query actual Shopify data

Do not report fixture numbers as observed results. Query Shopify and independently calculate:

- Demo products and variants.
- Demo customers.
- Paid/fulfilled demo orders.
- Orders by month across the full 12-month period.
- Customers with ≥1 order.
- Customers with ≥2 orders.
- Exact second-purchase rate.
- Orders per customer.
- Overall AOV.
- First-time vs returning revenue if available.
- Median/p25/p75 time to second order from actual order timestamps.
- Same-category and same-SKU repeat.
- Dedicated bundle performance.
- Multi-line basket performance.
- Discounted vs non-discounted repeat.
- Subscription candidates.
- At-risk and lapsed counts.

Rerun the seeder once to prove idempotency: it must create zero duplicates.

## Run the retention skill

After Shopify verification, run the plugin's retention workflow against actual queried data:

1. Retention stage.
2. AOV/CAC and contribution economics; request only genuinely missing merchant inputs.
3. Lifecycle vs subscription vs referral vs loyalty decision.
4. Segment definitions/counts.
5. Brand story and three creative territories.
6. Cashback, rewards, missions, VIP, referral and subscription blueprint.
7. Stop at strategy approval before writes.

## Joy MCP

After strategy approval:

1. Read current Joy settings/programs first.
2. Dry-run all proposed config changes.
3. Present exact diffs.
4. Apply only approved writes, one at a time.
5. Read back each write and stop on unconfirmed fields.
6. Scan the storefront brand and build widget draft.
7. Visually verify draft.
8. Live widget publish requires separate explicit approval.
9. `links.replaceAccountLink` may intercept an existing account icon; it does not add a new rewards icon. A separate header icon requires separately approved theme/app-block work.

## Klaviyo MCP

Use Klaviyo's official MCP server:

```text
https://mcp.klaviyo.com/mcp
```

Start read-only:

```text
https://mcp.klaviyo.com/mcp?read-only=true&disable-tools-with-user-generated-content=true&core-tools-only=true
```

Read existing segments, flows, metrics, events, and exact Joy-synced property names. Propose the segment/flow plan first. After separate approval, create one segment/flow at a time, read it back, and keep flows draft/inactive. Do not activate flows or send campaigns.

## Git and delivery

- Keep secrets and `demo-store/state/` out of git.
- Run tests and verification scripts.
- Commit the implementation on a focused branch.
- Push and open a PR against `thomasavada/shopify-retention-architect` unless Thomas explicitly asks to push directly to main.
- Include exact execution evidence in the PR/report.

## Definition of done

Do not stop until either the task is fully verified or a real external blocker requires Thomas.

Completion requires:

- Target development store proven.
- Seeder implemented and tested.
- 300 synthetic customers and exactly 500 qualifying orders, unless an evidenced Shopify limit blocks it.
- Historical `processedAt` spans the past 12 months through present.
- Actual Shopify calculation shows the intended 40% second-purchase rate, or discrepancy is explained and corrected.
- Bundle and repeat cohorts appear in actual data.
- Rerun creates zero duplicates.
- Throttle handling is evidenced in logs/telemetry.
- Joy ingestion/reconciliation is measured.
- Klaviyo remains read-only/draft until approval.
- Final report provides exact counts, elapsed time, API costs, retries, discrepancies, cleanup limitations, reproduction commands, branch/PR URL, and remaining approvals.

When blocked, report the exact command/API error, evidence, and the minimum human action required. Do not replace missing execution with plausible-looking numbers.
