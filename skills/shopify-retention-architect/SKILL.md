---
name: shopify-retention-architect
description: Audit Shopify retention, then build safely with Joy MCP.
version: 0.1.0
author: Thomas Nguyen (thomasavada), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [shopify, retention, loyalty, subscription, referral, joy-mcp]
---

# Shopify Retention Architect

Diagnose a Shopify brand's retention stage, quantify second purchase, choose the right retention mechanism, design an on-brand loyalty system, and—only after approval—configure Joy programs and widget through Joy MCP.

This skill does not sell loyalty by default. It may recommend lifecycle marketing, AOV/CRO, subscription, referral, loyalty, paid membership, a hybrid, or no retention build yet.

## When to use

Use when the user asks to:

- Audit a Shopify brand's retention or repeat-purchase performance.
- Decide whether the brand is ready for loyalty.
- Choose subscription vs. referral vs. loyalty.
- Calculate CAC/referral economics.
- Segment customers for Shopify or Klaviyo.
- Design an original on-brand loyalty program.
- Configure Joy programs or widget with Joy MCP.
- Prepare or seed a realistic Shopify development store for a retention demo.

Do not use for a generic loyalty feature explanation with no store, no data and no intent to diagnose.

## Prerequisites

Use available capabilities; never pretend a missing integration exists.

- Shopify store access through Shopify CLI/Admin API or merchant-supplied analytics.
- Joy MCP for configuration and widget writes.
- Klaviyo's official MCP server for segment/flow reads and approved writes.
- Browser/storefront access for brand-story and visual audit.
- Optional Klaviyo access. Without it, return segment/flow definitions only.
- For demo seeding, a dedicated Shopify development store. Never seed a production merchant.

Before any write, establish whether the run is:

- `AUDIT_ONLY`
- `PLAN_ONLY`
- `BUILD_DRAFT`
- `PUBLISH_APPROVED`
- `DEMO_SEED`

Default to `AUDIT_ONLY`.

Read only the references the mode actually reaches. `references/joy-mcp-execution.md` and
`references/klaviyo-mcp-execution.md` describe build phases that `AUDIT_ONLY` and
`PLAN_ONLY` never enter — loading them up front is a few hundred lines of context spent on
instructions you will not execute. Open them when you reach Phase 8.

## Core guardrails

1. Never recommend loyalty merely because Joy can build it.
2. Never invent margin, ad spend, CAC, reorder cadence, segment counts or benchmarks.
3. Never call assisted/associated revenue incremental revenue.
4. Never compute churn as `100% - returning-customer rate`.
5. Never seed or modify a live merchant without explicit scope confirmation.
6. Joy MCP config tools preview first. Apply only after the merchant/user approves the exact diff.
7. Use draft widget target first. Live widget writes require a separate explicit approval because they change the storefront immediately and have no publish/undo step.
8. Read back every MCP write and report unconfirmed fields.
9. Preserve existing balances, tiers and useful mechanics when migrating.
10. Separate facts, merchant inputs, estimates and creative proposals.

## Workflow

### Phase 1 — Audit store maturity

Collect 6–12 months where available:

- Orders, customers, revenue and overall AOV.
- Customers with exactly one order.
- Customers with two or more orders.
- `second_purchase_rate = customers_with_2plus_orders / customers_with_1plus_order`.
- Returning-customer revenue share.
- Purchase frequency and time to second order.
- Top products/categories and bundle performance.
- Discount dependency — what share of orders carry a discount, split by first versus repeat.
- Trend direction and data sufficiency.

Contribution margin belongs in Phase 3, not here: it exists nowhere in the Shopify API and
only the merchant can supply it. Listing it as something to "collect" sends you hunting for
a number that is not there.

Then three checks that constrain what you are allowed to recommend. Skipping them is how
an audit ends up proposing a channel the brand cannot reach, a program it already has, or
a subscription it has no mechanism to sell.

- **Email/SMS marketing consent among purchasers.** Read `emailMarketingConsent
  .marketingState` while paginating customers. A lifecycle-first recommendation assumes a
  reachable audience; if most purchasers are `NOT_SUBSCRIBED`, the first job is consent
  capture, and any flow you design reaches almost nobody. Report the subscribed count
  alongside the segment sizes, not as a footnote. Divide by purchasers, not by total
  records — the denominator rule governs every rate in the report, not only the repeat
  rate. A run that states the record count is meaningless and then reports consent against
  it has contradicted itself in its own table, which is exactly how a reader stops trusting
  the rest.
- **What is already installed and live.** Query `appInstallations`. Recommending a program
  the merchant already runs — or a tier structure that collides with live tiers and
  balances — destroys credibility immediately. If a program exists, the task changes from
  design to diagnosis and migration.

  When the loyalty app's own API is not authenticated, read its state from Shopify
  directly. Joy keeps the **live program configuration in a shop metafield** — namespace
  `joy_loyalty_avada`, keys `data` and `loyalty_data` — which holds the earning rules,
  reward ladder and tier definitions as JSON. That is the authoritative source for what the
  merchant is actually running today, and reading it turns "there is a program" into "here
  is the program".

  Member state lives in `avada_joy` customer metafields, but **pick the field carefully**.
  Measured on a store with 789 members: `point` covered 789 customers and `vipTier` 732,
  while `customerType` covered **1** and the `joy_tag_member` tag covered **14**. Counting
  members by tag would have understated the program by more than fifty times. Use the
  presence of `point`, corroborate with `vipTier`, and treat tags as decoration.

  Check the app embed is enabled in the published theme too — an installed app with the
  embed off is a program nobody can see. And cross-check the config against store
  capability: an earning rule like "2× points on subscription orders" is inert if
  `sellingPlanGroups` is empty, which is the kind of contradiction worth leading with.
- **Selling-plan groups.** `sellingPlanGroups(first: 10)` returning nothing means the
  store has no subscription mechanism at all. On a catalog with a monthly consumption
  cycle that absence is itself a headline finding, and "offer subscription" becomes a
  build task with real scope rather than a toggle.

#### Use `processedAt` for every date in the audit

An order carries two dates and they mean different things. `processedAt` is when the
transaction happened and is what Shopify shows as the order date and reports in analytics.
`createdAt` is when the record was written to the database.

For a store that has ever been migrated, imported or seeded, those diverge completely, and
`createdAt` silently destroys the audit: sort or filter by it and a year of trading
collapses into however long the import took. There is no error — you get a plausible,
tiny, wrong history. Cohorts, time-to-second-order, seasonality and trend are all built on
order dates, so this one field choice decides whether any of them mean anything.

Use `processedAt` for windowing, sorting and every interval you compute. The one honest
use of `createdAt` is as a diagnostic: comparing its spread against `processedAt`'s is how
you detect an imported dataset in the first place.

The counting looks trivial and is not: several of these queries return a plausible wrong
number rather than an error. Read `references/shopify-queries.md` before writing the first
query — it has the verified shapes for customer counting, order-window scope and ShopifyQL,
and the specific traps that silently corrupt a headline metric.

#### Report the denominator explicitly

`second_purchase_rate` divides by customers with at least one order. Most stores hold far
more customer *records* than purchasers — email captures, account signups, abandoned
checkouts. Dividing by total records understates the rate several-fold and points the
whole strategy at the wrong problem.

So report both numbers side by side: total customer records, and purchasers. The gap
between them is itself a finding — a base that is mostly non-purchasers is usually an
activation problem, and no loyalty mechanic addresses it.

**Test that conclusion before you draw it.** The rule is right and its naive application
is confidently wrong, because a low purchaser ratio can be an artifact of how the data
arrived rather than a fact about the business. Compare the spread of customer `createdAt`
against the spread of order `processedAt`: a real store accumulates both together, while a
store where customers all appeared in one recent burst and orders trail behind is mid-import.
Check too whether the non-purchasers differ systematically from purchasers — if they all
lack marketing consent, or all share a creation timestamp, they are a seeding artifact and
not a dormant audience. Only call it an activation problem once the shape survives that test.

#### Check that the dataset is not moving under you

Probe `ordersCount` at the start and again later in the run. If it moved, you are auditing
a store still being written to — a seed in progress, a migration, a live sale — and every
figure needs a snapshot timestamp beside it. Trends are meaningless in that state; say so
rather than reporting one.

Do not wait for a timer if the answer already arrived. Any two counts of the same thing
that disagree — a paginated pull returning more rows than a `ordersCount` taken minutes
earlier, for instance — have already told you the table is growing. Record it and move on;
sitting out a ten-minute interval to confirm what you have observed three times is dead
time.

Treat this as routine rather than paranoid. Any store being seeded is written at roughly
five orders a minute, so a dataset of real size is under construction for hours and an
audit started in the same session is almost certainly reading a partial table. Without the
check you will spend real time hunting for cancelled or archived orders to explain a
discrepancy that is just the table growing.

#### Count what you claim to count

The provisional rule below talks about **fulfilled** orders while the collection list above
says "orders". Those differ, and the gap hides real problems: a store can show a thousand
orders and zero fulfilments, which usually means an import or an operational stall rather
than a retention story. Read `displayFulfillmentStatus` alongside the counts and report
both, because a dataset that is 100% unfulfilled is telling you something about its
provenance.

#### When to refuse

Two independent tests. A dataset can pass one and fail the other, so check both.

**Provisional** — under six months of usable history, or fewer than 100 fulfilled orders.
Report normally, labelled provisional.

**Stop** — no customer has a second order. This is a separate condition, not a subset of
the one above: a store can hold eleven months of history and five hundred fulfilled orders
and still have zero repeat customers, which is exactly the state a half-finished import
produces. When it holds, second-purchase rate, time-to-second-order, repeat AOV and the
at-risk and lapsed segments are all structurally unfillable, and a long report with
"unavailable" in most sections reads as authoritative while saying nothing.

A stop is still a deliverable, not a blank page. Report what you did measure and what it
constrains — order and customer counts with their snapshot times, AOV, discount
dependency, consent coverage, any incumbent program and its configuration, whether selling
plans exist, and the `createdAt`-versus-`processedAt` comparison that explains the shape.
Those findings do not depend on repeat behaviour and are often the most useful thing in the
document. What you withhold is the verdict, the mechanism recommendation and the program
design: name what is missing, say what would have to exist, and stop there.

### Phase 2 — Diagnose repeatability and brand stage

Classify the product model:

- Replenishable
- Routine/serviceable
- Collectible/expanding
- Durable/infrequent
- One-time/occasion
- Subscription-native

Use observed reorder behavior over category assumptions.

Assign one primary stage:

| Stage | Constraint | Build next |
|---|---|---|
| Foundation | Data, product or operations unreliable | Stabilize and measure |
| Acquisition/conversion | Traffic or first-order conversion | Acquisition/CRO |
| AOV/offer | Basket cannot support CAC/rewards | Bundle, threshold, cross-sell |
| Second purchase | Product repeats but buyers stop after order one | Lifecycle/Klaviyo |
| Subscription ready | Predictable replenishment | Subscription + supporting loyalty |
| Loyalty ready | Organic repeat and margin already exist | Rewards + referral + touchpoints |
| Community/VIP | Strong value and affinity | VIP, membership, access, experiences |

### Phase 3 — Interview the merchant, then compute economics

Store data answers *what happened*. It cannot tell you margin, what they have already
tried, what they are willing to give away, or what they are actually trying to achieve —
and a recommendation built without those is confident guesswork. Ask before you design.

Put the questions in one batch rather than trickling them out, and say why each matters so
the merchant can see you are not interrogating them for form's sake. Where you can already
answer a question from the data, do not ask it — show your number and ask them to confirm
or correct it. That turns a questionnaire into a conversation and surfaces disagreements
between their mental model and their data, which is often the most valuable moment in the
whole audit.

**Economics — needed to size anything**

1. Contribution margin after COGS, shipping and payment fees — the ceiling on every reward.
2. Monthly paid spend and new customers acquired from it, so CAC is measured not assumed.
3. Current discounting: standing codes, welcome offer, sale cadence. Rewards stack on top
   of whatever already exists.

**History — stops you recommending what already failed**

4. What retention has been tried before, and what happened? A program that was launched
   and quietly died tells you more than any benchmark.
5. Is there an existing loyalty/subscription tool, and does it hold balances or tiers that
   must be migrated?
6. What does post-purchase communication look like today — flows, cadence, who owns it?

**Product reality — the data cannot see this**

7. What is the genuine consumption cycle of the hero product? If observed reorder gaps and
   the merchant's answer disagree, that gap is a finding.
8. Which products do they *want* to sell more of, and which are loss leaders?
9. Anything seasonal, supply-constrained or being discontinued?

**Intent and constraints — determines what is even buildable**

10. What does success look like in 90 days, in their words?
11. Who executes this, and how much time do they actually have each week?
12. Any hard limits — margin floor, brand rules against discounting, platform or agency
    constraints?

Record every answer as **merchant-claimed** and keep it visibly separate from measured
data. When a claim contradicts the store data, say so and show both; do not silently pick
one. If the merchant cannot answer the margin question, stop short of recommending a
reward rate and say what you would need.

**When nobody is there to answer** — an unattended `AUDIT_ONLY` run, a demo, a first pass
before a call — do not walk through the economics formulas producing a column of
"unavailable". None of margin, ad spend or new-paid-customer counts exist anywhere in the
Shopify API, so that section is guaranteed empty and costs real time to fill with nothing.
Emit a short stub instead: the questions, why each is needed, and what each unlocks. Then
carry on with the parts the data can answer, and mark every downstream recommendation that
depends on economics as unsized rather than omitting it.

Calculate:

- `paid_CAC = paid_spend / new_paid_customers`
- `first_order_contribution = AOV × contribution_margin - acquisition_discount`
- `contribution_LTV_proxy = measured_customer_spend × contribution_margin - variable_costs`
- `target_CAC = contribution_LTV_proxy × explicit_safety_factor`
- `referral_CAC = expected_friend_reward_cost + expected_redeemed_referrer_reward_cost`

State the window and every assumption.

### Phase 4 — Choose the retention mechanism

- **Lifecycle first:** plausible second purchase, weak post-purchase communication.
- **Subscription first:** predictable same-SKU/category replenishment and convenience.
- **Loyalty first:** multi-SKU, discovery, progress, status or community-driven repeat.
- **Referral first:** high satisfaction/shareability or durable/high-consideration product; referral CAC below paid CAC.
- **Hybrid:** subscription for replenishment, loyalty for relationship, referral for acquisition, Klaviyo for activation.
- **Not yet:** no credible repeat/referral loop, insufficient margin/data, or a more urgent acquisition/conversion problem.

### Phase 5 — Segment the customer base

Return definitions and actual counts when available:

1. New non-buyers
2. First-time buyers
3. Second-purchase due
4. Active repeaters
5. Subscription candidates
6. VIP candidates
7. At-risk
8. Lapsed
9. Advocates/referrers
10. High reward balance with no recent redemption

For each provide logic, count or `unavailable`, entry/exit, activation, offer and success metric. Verify Joy/Klaviyo property names before giving copy-paste filters.

### Phase 6 — Understand the brand story

Audit the live storefront:

- Brand origin, promise, rituals, community, mascot, ingredients/materials and cultural symbols.
- Real colors, fonts, button style, spacing, imagery and tone.
- Product use occasions and moments customers identify with.

**When the storefront is password-protected** — which is the normal state of a development
store, so expect it during any demo — do not silently skip this phase or invent a brand
voice. Fall back in this order: read the published theme's `config/settings_data.json`
through the Admin API for real color, font and radius tokens (note it is JSONC — it
carries a generated `/* */` header that breaks a strict JSON parser, so strip comments
first); read product descriptions, page content and metafields for voice; ask the merchant
for the password or a staging link.

State which source you used. A brand section built from theme tokens alone is thin, and
saying so is better than presenting stock theme defaults as if they were a brand identity
— `#ffffff`, `#000000` and Inter are what an unconfigured Horizon theme ships with, not a
design language.

Create three original loyalty territories. Score each for brand fit, motivation, distinctiveness, Joy feasibility and margin safety. Learn principles—not assets or copy—from creative programs such as Sun Bum and OLIPOP.

### Phase 7 — Structure the program

Only when justified, propose:

- Club and currency name.
- Cashback/reward rate and implied program cost.
- Three to five reachable rewards.
- VIP tiers based on actual AOV/frequency.
- Non-purchase missions: review, UGC, social, birthday, referral, receipt, community actions.
- One aspirational/non-purchasable reward where appropriate.
- Referral give/get and expected referral CAC.
- Subscription interaction.
- Expiry, returns, fraud and stacking rules.
- 90-day success metrics.

Read `references/loyalty-program-design.md` before proposing any of the above. It holds the
arithmetic the market converges on (redemption ROI, earn rates, referral sizing), the rule
that tiers must be earned by trailing-12-month **spend** rather than accumulated points,
how to derive thresholds from the audit's own spend distribution, the rewards-page block
structure, and a worked teardown of a live program. Designing the numbers without it
produces programs that are either unaffordable or unmotivating.

Also use `references/decision-framework.md` and `references/output-template.md`.

### Phase 7B — Subscription, AOV, impact and monitoring

A report proposing only a rewards program has usually skipped the two levers with faster
payback, and one that ends at a list of metrics leaves the merchant knowing what to watch
but not what to do when it moves.

Read `references/recommendations.md` and produce all four: subscription strategy (or an
explicit statement that the cadence does not support one), AOV/bundle strategy, expected
impact per lever with measured/claimed/modelled labelled separately, and a monitoring table
in symptom / trap / one-job form.


### Approval gate 1 — Strategy

Present the audit and proposed build. Ask the user to approve:

- Mechanism
- Economics
- Program structure
- Creative territory
- Storefront/account touchpoints

Do not call Joy MCP writes before approval.

### Phase 8 — Build with Joy MCP

Follow `references/joy-mcp-execution.md`.

Required sequence:

1. Read current Joy settings/programs first.
2. Run every `joy_configure_*` tool without `apply:true` to obtain dry-run diffs.
3. Present all diffs and risks.
4. Apply one approved write at a time.
5. Read back after each write.
6. Stop and report any unconfirmed field; do not continue blindly.

### Phase 8B — Build lifecycle with Klaviyo MCP

Follow `references/klaviyo-mcp-execution.md`.

1. Connect the official Klaviyo MCP in read-only mode first.
2. Read existing segments, flows, metrics and exact Joy-synced property names.
3. Present proposed segment definitions, flow triggers, exits, timing, offers and counts.
4. Wait for explicit Klaviyo approval.
5. Reconnect with write tools enabled only for the approved build.
6. Create one segment/flow at a time, keep flows draft/inactive, and read back each object.
7. Activation, campaign sending and customer-facing delivery require separate approval.

The client orchestrates Joy MCP and Klaviyo MCP. Joy MCP does not call Klaviyo MCP server-to-server.

### Phase 9 — Design the widget on-brand

1. Call `joy_scan_brand_design`.
2. Call `joy_get_widget_fields`; never guess paths or enums.
3. Propose program identity, colors, fonts, buttons, corner radius, launcher, cards, imagery and visible sections.
4. Upload merchant-approved imagery with `joy_upload_image` when needed.
5. Dry-run `joy_configure_widget_draft` / `joy_set_widget_fields` using draft target.
6. Apply to draft after approval.
7. Read back and visually review in Joy admin/storefront preview.

### Approval gate 2 — Publish

A live widget write is separate from draft approval. State clearly:

- It changes the storefront immediately.
- There is no publish step and no undo in the MCP tool.

Use live target only after explicit `PUBLISH_APPROVED` confirmation. Then verify storefront behavior.

### Phase 10 — Account and header touchpoints

Offer, do not force:

- Customer Account Loyalty Hub/app extension where available.
- Replace the existing Shopify account icon behavior with the Joy drawer using `links.replaceAccountLink`.
- If theme detection fails, use the approved `links.accountLinkSelector` field.

Important: `replaceAccountLink` intercepts an existing account link; it does **not** add a new rewards icon. A separate rewards icon in the header requires theme/app-block implementation through Shopify theme tooling, review and explicit approval.

## Demo mode

For `DEMO_SEED`, read `references/demo-store-data.md`.

- Confirm the target is a development store.
- Create realistic products, bundles, customers and historical orders.
- Make repeat behavior coherent enough to produce a real second-purchase rate.
- Label all records as synthetic demo data.
- Seed Joy analytics separately if needed; BigQuery seed data does not populate ShopifyQL.
- Never use a production store.

## Required output

Use `references/output-template.md`.

**Precedence, so this list never overrides the verdict.** Read in this order, and let the
earlier rule win:

1. **The data floor.** If the dataset cannot support a verdict — no customer has a second
   order, so repeat rate, time-to-second, repeat AOV and the at-risk and lapsed segments
   are all structurally unfillable — then the correct output is a short refusal: what you
   measured, what is missing, what would have to exist, and a stop. Do not produce the
   twenty sections below with "unavailable" in most of them. A long document whose headline
   metric is 0.0% reads as authoritative and is empty, which is worse than a short honest
   one. This outranks any brief asking for a full report.
2. **Guardrail 1 and Phase 7.** A program is proposed only where the evidence justifies it.
   A section whose recommendation is "not yet" is still present — it carries the refusal
   and the reason instead of a design. "Proposed program: none — the constraint is
   activation, not retention; revisit when second-purchase rate exceeds X" is a complete
   answer to that heading.
3. **This list**, which describes what a complete report contains when the data supports one.

Inventing a program, or padding headings to look thorough, is the failure this ordering
exists to prevent.

Include:

- Executive stage verdict
- Second-purchase count/rate, reported alongside the total customer-record count
- Evidence table
- Merchant-claimed inputs, kept visibly separate from measured data
- Economics and CAC
- Segment map
- Build-now/build-later/not-now
- Dated actions for the next 30/60/90 days, each with an owner and a finish line
- Proposed Joy program, including VIP tiers and their perks
- Subscription strategy, or an explicit statement that the cadence does not support one
- AOV/bundle strategy
- Expected business impact per lever, with measured/claimed/modelled labelled
- Strategic monitoring table: symptom, trap, one job, review date
- Creative territory and widget direction
- Approval status
- MCP writes/dry-runs/read-backs
- Klaviyo segments/flows and activation state
- Publish status
- Verification and 90-day measurement plan
