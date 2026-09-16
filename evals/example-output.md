# FizzyRoot retention architecture

## Executive verdict

- **Store/mode:** FizzyRoot, `demo.fizzyroot.example`; fictional fixture; `PLAN_ONLY`, as of 2026-09-16. Source throughout: `tests/demo-brand.json`. No external APIs, store changes, seeding, or MCP calls.
- **Primary stage:** Second purchase. 180 of 300 purchasers have ordered only once; observed repeat behavior supports helping them establish a ritual.
- **Transition stage:** Subscription ready for a selected cohort, with a small loyalty pilot after lifecycle activation. Category repeat is stronger than same-SKU repeat, so flexible replenishment and discovery matter.
- **Main constraint:** Converting the first order into a second while protecting contribution. Paid CAC exceeds the average-order contribution proxy. Lifecycle weakness is a hypothesis to audit, not a supplied fact.
- **Recommended mechanism:** Lifecycle-led hybrid: second-order activation, selective subscription, then restrained loyalty and referral experiments. Loyalty is not the primary fix.
- **Confidence:** Moderate. Twelve months and 500 fulfilled-status-unverified orders support a descriptive audit, but timestamps, acquisition cohorts, discount detail, subscriber behavior and flow performance are absent. History exceeds the skill's provisional-history threshold; confirm fulfilled-order eligibility before implementation.

## Retention evidence

Values below are fixture facts or explicitly shown calculations. Trends are unavailable throughout; no external benchmarks are used. “12m” means the supplied 12-month reporting window, whose exact boundary dates are not specified.

| Metric | Value | Window | Trend | Source | Interpretation |
|---|---:|---|---|---|---|
| Customers with 1+ orders | 300 | 12m | Unavailable | store_metrics_12m | Purchaser denominator |
| Customers with exactly 1 order | 180 (60%) | 12m | Unavailable | store_metrics_12m | Large second-order opportunity; not churn |
| Customers with 2+ orders | 120 | 12m | Unavailable | store_metrics_12m | Repeat purchaser numerator |
| Second-purchase rate | **120 / 300 = 40% exactly** | 12m | Unavailable | Calculated | Cross-sectional purchaser rate, not a mature acquisition-cohort conversion rate |
| Order distribution | 75 exactly 2; 30 exactly 3; 15 with 5+ | 12m | Unavailable | store_metrics_12m | Counts reconcile to 300; 5+ group implies 80 orders in total if buckets are exhaustive |
| Orders / net sales | 500 / $36,250 | 12m | Unavailable | store_metrics_12m | Fulfillment, tax, refund and discount definitions need confirmation |
| Overall AOV | $36,250 / 500 = $72.50 | 12m | Unavailable | Calculated; matches fixture | Not necessarily first-order AOV |
| Returning revenue share | $19,200 / $36,250 = 52.965517…% | 12m | Unavailable | Calculated | Fixture's 52.97% is rounded; not incremental revenue |
| Orders/customer | 500 / 300 = 1.666666… | 12m | Unavailable | Calculated | Fixture's 1.6667 is rounded |
| Time to second order | Median 39 days; p25 31; p75 58 | Repeat observation window unspecified | Unavailable | repeat_behavior | Useful initial timing; excludes non-repeaters and does not establish individual cadence |
| Same-category / same-SKU repeat | 74% / 46% | Unspecified | Unavailable | repeat_behavior | Variable replenishment plus flavor discovery; denominators unspecified |
| Variety → 12-pack | 42 customers | Unspecified | Unavailable | repeat_behavior | Concrete cross-sell path; conversion rate unavailable |
| Daily Ritual Bundle | 85 orders; $102 AOV | Product window unspecified | Unavailable | products | $29.50 / 40.69% above overall AOV; margin and conversion lift unproven |
| Other product activity | Starter 145; 12-Pack 130; Discovery 110; Seasonal 20; Glass & Tote 10 orders | Unspecified | Unavailable | products | No traffic, units or product margins; low volume alone is not weak conversion |
| Subscription | 15 active; 45 candidates | Snapshot / candidate window unspecified | Unavailable | brand; repeat_behavior | Candidate/subscriber overlap unknown |

No low-performing comparison bundle is supplied. Do not import the demo-seeding reference's target metrics as observations. Confirm whether purchaser counts mean orders within the window or lifetime counts for customers observed in the window.

## Economics

All monetary values use the fixture's dollar units; currency code is unspecified. Calculations retain precision until display.

- **Contribution margin:** Supplied gross margin 65%; variable costs excluding COGS $6/order. Average contribution before acquisition incentives = `$72.50 × 0.65 − $6 = $41.125`, or **56.7241379%** of AOV. This is derived, not a supplied contribution-margin field.
- **Paid spend/new paid customers:** $15,000 / 300 over the supplied 90 days.
- **Paid CAC:** `$15,000 / 300 = $50 exactly` per reported new paid customer. Attribution and first completed purchase qualification need verification.
- **First-order contribution:** Using overall AOV as a first-order proxy and treating the $5 acquisition discount as additional: `$72.50 × 56.7241379% − $5 = $36.125` (**$36.13**). After paid CAC: **−$13.875**. Because AOV comes from net sales, the $5 may already be included; if so, avoid subtracting it again and use **$41.125**, or **−$8.875** after CAC. Neither is a measured first-order cohort result.
- **Contribution LTV proxy:** Measured 12m spend/customer = `$36,250 / 300 = $120.833333…`; variable cost/customer = `500 × $6 / 300 = $10`. Proxy = `$120.833333… × 0.65 − $10 = $68.541666…` (**$68.54**). This is observed-window contribution before CAC, overhead and new rewards, not forecast lifetime value; do not subtract discounts again from net sales.
- **Target CAC and safety factor:** Proposed safety factor **60%**, a planning choice rather than a benchmark. `$68.541666… × 0.60 = $41.125` (**$41.13**). Current $50 is $8.875 above this provisional ceiling. It combines an all-customer 12m proxy with 90d paid CAC, so validate matched cohorts before budget decisions.
- **Proposed referral CAC:** Give friend **$3**, give referrer **$3 credit**, each requiring a $130 eligible merchandise basket. Friend reward assumed used on every qualified referred first order; assumed referrer redemption 60%. Expected incentive CAC = `$3 + $3 × 0.60 = $4.80`; range **$3–$6** at 0–100% referrer redemption. After the $3 friend discount, the minimum basket produces $127 net merchandise revenue. At 100% referrer redemption, $6 / $127 = **4.7244%**; expected rate $4.80 / $127 = **3.7795%**. Book both rewards against the originating referral order, conservatively ignoring subsequent redemption-order revenue. No base points or other discounts on either rewarded order. This high basket threshold protects the cap but may limit adoption; test it explicitly. Do not compare $4.80 to paid CAC as total channel cost: referral operations/platform costs are missing, and customer qualification must match the paid denominator.
- **Assumptions/missing inputs:** Use a single implementation intake to confirm first-order AOV and discount accounting, SKU/bundle contribution, variable-cost coverage, subscription discount/cost, cohort dates and paid attribution, customer-level cadence and fulfillment/refunds, and the budget treatment of perk/platform costs. The 300 paid customers in 90d equaling all 300 purchasers in 12m merits scope reconciliation; it is not proof they are the same cohort. No user input or external lookup is required for this fixture-only plan.

## Customer segments

Definitions are conceptual business logic, not verified Shopify/Klaviyo/Joy property filters. Segments can overlap; counts must not be added. The supplied candidate/risk counts have unknown underlying definitions and must be recounted against the proposed logic. Use customer-specific cadence when available; 39 days is only an initial fallback. For whole-day fallback rules, at-risk begins day 59 and lapsed day 98.

| Segment | Logic, entry and exit | Count | Activation | Offer | Metric |
|---|---|---:|---|---|---|
| New non-buyers | Enter at opted-in profile with zero orders; exit on first order or consent withdrawal | unavailable | Welcome and flavor finder | Education, no automatic discount | First-order conversion |
| First-time buyers | Enter at first completed order; exactly one order; exit on second order | 180 | Usage, meal pairing, discovery follow-up | Favorite-flavor recommendation | Mature 60-day second-purchase rate |
| Second-purchase due | Exactly one order; enter day 31 since first order; exit on second order or after day 58 into a separate one-time-buyer reactivation flow | unavailable (subset of 180) | Reminders near days 31, 39 and 52, with consent and frequency caps | Variety → favorite 12-pack; conditional earned reward | Second order within 60 days |
| Active repeaters | 2+ orders and recency ≤1.5× observed cadence; exit when overdue | unavailable (subset of 120) | Discovery and ritual content | Access and eligible base points | Orders/customer and contribution |
| Subscription candidates | 3+ same-category purchases with at least two reasonably stable intervals; proposed interval tolerance ±25%; exclude active subscribers from acquisition flow; exit on subscription or loss of fit | 45 supplied candidates; eligible non-subscriber count unavailable | Flexible cadence, flavor swaps and skip education | Convenience; no new discount assumption | Subscription starts and renewals |
| VIP candidates | 3+ orders plus rolling-12m net spend ≥$217.50; exit when qualification expires | unavailable | Recognize routine and solicit feedback | Access-based tier invitation | Qualified retention and perk cost |
| At-risk | 2+ orders; recency >1.5× and ≤2.5× personal cadence; exit on purchase or transition to lapsed | 28 supplied; proposed-rule count unverified | Ask about taste, timing and stock | Relevant replenishment, no blanket coupon | Reactivation contribution |
| Lapsed | 2+ orders; recency >2.5× personal cadence; exit on purchase | 16 supplied; proposed-rule count unverified | Limited win-back sequence, then suppress if unengaged | Discovery message; controlled reward test only | Incremental reactivation contribution |
| Advocates/referrers | Enter on verified positive feedback or qualified referral behavior; exit on opt-out/fraud; separately mark candidate vs actual referrer | 24 supplied candidates; actual referrers unavailable | Invite sharing after positive experience | Proposed $3/$3 qualified referral | New qualified buyers and referral CAC |
| High balance/no redemption | Proposed balance ≥250 points and no redemption in 60 days; exit on redemption or balance <250 | unavailable; new-program segment | Explain available $5 reward | Redeem earned value | Redemption and incremental contribution |

## Retention architecture

### Build now

Within this plan, prepare a lifecycle audit and day-31–58 second-order flow, prioritizing the 42-customer variety-to-12-pack path as supporting evidence. Test the $102-AOV Daily Ritual Bundle without claiming proven conversion or margin superiority. Establish matched acquisition cohorts and incentive accounting. Offer a small, convenience-led subscription test to eligible candidates using existing subscription infrastructure.

### Build later

After strategy/economic approval and baseline instrumentation, pilot the proposed Joy identity, 2% rewards and controlled referrals. Expand VIP access and subscription tenure benefits after demonstrating repeat contribution and confirming operating costs. “Later” is gated by evidence, not merely a calendar date.

### Do not build now

Do not launch a broad points program as the cure for weak second purchase, add a paid membership, replace the subscription platform, create perpetual discount stacking, or expand paid acquisition on an unvalidated LTV forecast. No store configuration, imagery upload, theme edit or publishing occurs in this run.

## Brand story

- **Brand promise:** Supplied story describes botanical soda, everyday gut-friendly rituals, shared meals and unexpected flavors. This is merchant narrative, not independently substantiated health efficacy.
- **Character:** Playful, sociable, curious; bright retro-futurist packaging.
- **Rituals/community:** A soda with a meal; discovering a favorite after a variety pack; sharing new flavors with friends.
- **Visual language:** Story is supplied; real colors, fonts, spacing, buttons, mascot and storefront layout are unavailable. All design below is a creative proposal, not a live scan.
- **Scoring:** Subjective 1–5, higher is better; equal weights. Joy feasibility scores are provisional pending tool/feature discovery.

| Original territory | Currency / progression | Brand fit | Motivation | Distinctiveness | Joy feasibility | Margin safety | Total /25 |
|---|---|---:|---:|---:|---:|---:|---:|
| **The Daily Orbit** | Sparks; First Sip → Ritual Regular → Table Host | 5 | 5 | 4 | 4 | 5 | **23** |
| Botanical Field Notes | Seeds; Taster → Flavor Scout → Garden Guide | 4 | 4 | 4 | 4 | 5 | 21 |
| The Flavor Frequency | Beats; Listener → Mixer → Broadcast Host | 4 | 4 | 5 | 3 | 4 | 20 |

**Chosen territory: The Daily Orbit.** It ties daily ritual to retro-futurist identity while making the shared table the highest status. “Sparks” is countable; access and recognition can motivate without raising cashback. These are original proposals, not copied assets or copy from other programs.

## Program blueprint

- **Club name:** FizzyRoot Daily Orbit.
- **Currency:** Sparks. Proposed 1 Spark per $1 eligible net merchandise spend; 100 Sparks = $2 reward. Exclude tax, shipping, gift cards, refunded amounts and disallowed promotional transactions. Confirm fractional rounding support before configuration.
- **Cashback/reward rate:** **2% nominal reward value**. Assumed 70% redemption implies **1.4% expected purchase-reward cost**; sensitivity 0–2%. At $72.50 AOV, issue $1.45 nominal value and expect $1.015 redeemed. At constant eligibility, $36,250 annual sales imply $725 nominal / $507.50 expected purchase rewards; these are scenarios, not forecasts of enrollment or incrementality.
- **Cost cap:** The supplied maximum is 5%. Maintain a single incentive ledger: purchase rewards, mission issuance, referral liabilities and direct perk costs. Reserve full reward face value for cap control rather than relying on breakage. Pause discretionary issuance/perks if liabilities plus booked costs would exceed 5% of eligible net merchandise revenue; hold fulfillment of existing earned obligations. Model subscription discounts in this same conservative budget until the merchant confirms otherwise. On referral baskets, reserve both $3 rewards and suppress all other earn/discount mechanics. Verify support for exclusions before activating.
- **Earn missions:** “Set your orbit” profile/preferences: 10 Sparks once; “Tell us your flavor” verified review: 20 once/year, never conditional on positive sentiment; “Bring a ritual to the table” approved UGC: 20 once/year with separate permission to reuse; birthday: 10 once/year, after a verified purchase. Total maximum 60 Sparks = **$1.20 face value/customer/year**, $0.84 at assumed 70% redemption. These missions require confirmed Joy events/integrations or a documented manual verification process. Do not award points for unverified social follows. Referral earning uses its own reward, not extra mission points.
- **Mission economics:** For 300 qualifying customers at maximum completion: $360 face-value missions. Combined with all-sales base rewards: `$725 + $360 = $1,085`, **2.9931%** of $36,250, before referral/perks. Expected at 70% redemption: $759.50, **2.0952%**. This simplified non-referral baseline leaves $727.50 nominal headroom under the $1,812.50 annual cap; it is not authorization to spend it. Referral and subscription scenarios must be modeled without double counting excluded base rewards.

| Reward ladder | Cost | Redemption condition | Reachability / funding |
|---|---:|---|---|
| Tiny Spark | 100 Sparks → $2 | ≥$40 eligible basket | About two average orders before missions |
| Ritual Boost | 250 Sparks → $5 | ≥$100 eligible basket | About four average orders before missions |
| Table Treat | 500 Sparks → $10 | ≥$200 eligible basket | About seven average orders; group/large basket reward |
| Future Flavor Table | Invitation, no cash purchase | Limited feedback/tasting session for engaged members | Aspirational co-creation; selection rules and actual cost approved before launch |

One monetary redemption/order; minimum baskets limit direct redemption discount to 5%. No earning on redemption orders, referral-discount orders, or discounted subscription orders. Minimum baskets are before the proposed reward, excluding tax/shipping; a 5% pre-discount basket reduction exceeds 5% of post-discount net revenue, so these basket rules alone do not enforce the program cap. Monitor portfolio liability cost against net revenue and adjust minimums or issuance if needed. Do not promise free shipping or physical gifts without cost inputs.

**VIP tiers, proposed rolling 12 months:** First Sip at first completed purchase; Ritual Regular at **3 orders and $217.50 net spend** (3 × AOV); Table Host at **5 orders and $362.50** (5 × AOV). Regular offers flavor previews and voting; Host adds priority invitations to the Future Flavor Table. Keep 2% base earn across tiers. At most 45 customers meet the 3+ frequency threshold and 15 meet 5+ in the supplied distribution; spend eligibility is unknown, so tier counts remain unavailable. Recount the distribution before setting final thresholds. If Joy cannot combine spend and order count or support the window, present a revised diff rather than silently substituting rules. Review annually, notify ahead of expiry and propose a 30-day grace period subject to support.

**Referral:** $3 friend / $3 referrer credit, each ≥$130 basket, as calculated above. Release referrer credit only after the first friend's fulfilled, non-refunded order clears the verified return window. The $130 threshold exceeds both overall and bundle AOV; low take-up is a material tradeoff. Do not lower it without revisiting economics. Deduplicate identities and flag shared payment/address patterns for review; cap a referrer at five qualified rewards/month initially. Exclude self-referrals, cancellations and repeated “new” accounts.

**Subscription relationship:** Preserve the installed subscription and its 15 active subscribers. Promote flexible flavor, cadence and skip/pause benefits. Subscription-discount rate is unavailable: combined nominal rate would be `subscription discount + 2%` plus mission/perk costs if rewards stacked. Suppress base points on discounted renewals until the combined budget is verified. Qualifying renewal spend/order count may count toward status if supported, even when no points accrue. Avoid promising automated tenure events without integration verification.

**Expiry/returns:** Propose 12 months of inactivity before points expiry, with advance reminders, subject to policy and tool validation. Reverse earning on returns; document redeemed-points/refund handling, negative balances and partial returns before launch. Preserve any balances/configuration discovered during later reads despite the fixture reporting no installed loyalty program. All mechanics remain unapproved proposals.

## Widget and touchpoints

- **Widget draft direction:** Proposed cream `#FFF4DA`, dark plum `#30203D`, citrus `#E5F35B` and coral `#F97762`; use plum for body copy, validate contrast and keyboard behavior. Proposed rounded display headings, readable sans-serif body, pill buttons and orbit/flavor illustrations. Fonts and asset rights are unverified. Launcher “Your Daily Orbit”; cards for balance, next reachable reward, flavor discovery, status and qualified referrals. Show earn rate, minimum baskets and exclusions clearly; label locked rewards honestly. No invented widget paths/enums.
- **Product/cart/checkout:** Explain eligible Sparks near purchase decisions, show net eligible cart progress and exclusions, and offer variety-to-favorite recommendations. Checkout placement depends on confirmed extension availability; do not claim it is installed.
- **Customer account:** Propose Loyalty Hub with balance, activity, rewards and status. Verify available tools and add the extension in the customer account editor if required; MCP alone is not presumed sufficient.
- **Existing account icon behavior:** Optional `links.replaceAccountLink` interception opens the Joy drawer instead of the existing account destination. Confirm that losing the direct account entry is acceptable and retain access to order/subscription management. Discover the field before use; `links.accountLinkSelector` is only a fallback after theme detection fails and an actual selector is inspected.
- **Separate header rewards icon:** **A separate header rewards icon cannot be created by `links.replaceAccountLink`.** It requires an independently reviewed and approved Shopify theme/app-block change. No theme edit is proposed as an MCP widget side effect.
- **Klaviyo/wallet/POS/social:** Provide conceptual consent-aware flows only; verify actual event/property names before implementing filters. Email carries ritual reminders and earned-balance education. Social invites voluntary sharing and permission-based UGC. Wallet/POS are deferred because only Shopify DTC is supplied.

## Approval

- Strategy: **pending**.
- Program economics: **pending**, including subscription budget, referral threshold and first-order accounting.
- Widget draft: **pending**.
- Publish live: **pending; not authorized**.
- Theme/account changes: **pending**.

No approval is requested interactively during this evaluation. The future merchant approval packet must cover mechanism, economics, structure, chosen territory and touchpoints. After strategy approval, obtain exact current → proposed dry-run diffs and approval of those diffs before any apply operation. Live widget approval is separate from draft approval: a live save changes the storefront immediately, with no publish step and no undo in the MCP tool.

## MCP execution

All entries are future handoff steps. No tools were discovered or called, and no current configuration was read. **Sidekick itself did not invoke Joy MCP.** No schema-valid executable payload or real diff can be produced from this fixture alone.

| Tool | Dry-run | Approved | Applied | Read-back | Notes |
|---|---|---|---|---|---|
| Available read tools, discovered later | Not run | No | No | Not run | Confirm target shop/environment; read overview, settings, programs, balances, tiers, referrals and widget |
| joy_scan_brand_design; joy_get_widget_fields; joy_check_theme_setup | Not run | No | No | Not run | Read/discovery phase; validate actual branding, paths, enums and theme |
| joy_configure_shop_settings | Planned only | No | No | Not run | Identity and currency; preserve existing configuration |
| joy_configure_earning_program | Planned only | No | No | Not run | Base earn and supported missions; preview exclusions |
| joy_configure_redemption_program | Planned only | No | No | Not run | Three monetary rewards, minimum baskets and stacking |
| joy_configure_tier; joy_configure_tier_settings; joy_configure_tier_perks | Planned only | No | No | Not run | Three proposed levels, period and access perks; verify compound rules |
| joy_configure_referral_program; joy_configure_referral_widget | Planned only | No | No | Not run | Reward cost, basket rules, qualification and anti-abuse |
| joy_configure_widget_draft; joy_set_widget_fields | Planned only | No | No | Not run | Draft target only; account interception remains a separate optional proposal |

For a later approved build: discover actual tool contracts, map proposals to supported fields, preview each configuration without `apply:true`, present all diffs and risks, and only then seek exact-diff approval. Apply one authorized write at a time and read back after each; stop on any unconfirmed field. The following handoff authorizes no such apply step.

## Klaviyo MCP execution

**PLAN_ONLY; proposed execution, not completed work.** FizzyRoot is fictional; Klaviyo account/company ID is unavailable. No connection, discovery, segment creation, flow creation, template write, activation or send occurred. **Sidekick itself did not invoke Klaviyo MCP or Joy MCP.** The future agent/client orchestrates the two servers and records approvals together; Joy MCP does not call Klaviyo MCP server-to-server.

### Read-only discovery first

In a separately authorized real-account run, confirm the target company and connect to the official server using OAuth with an Owner, Admin or Manager user. Initial connection mode must be read-only:

```text
https://mcp.klaviyo.com/mcp?read-only=true&disable-tools-with-user-generated-content=true&core-tools-only=true
```

1. Discover available tool schemas. Use `get_segments` and `get_segment` to inventory definitions/IDs, then `get_flows`, `get_flow` and `get_flows_triggered_by_segment` to inspect triggers, filters, timing and status. Record reuse candidates; no existing object is verified here. Do not replace existing functioning flows blindly.
2. Use `query_segment_values` and `query_segment_series` for supported membership counts/trends and `get_flow_report` for existing flow performance. Discover applicable profile/metric read tools for order events, fulfillment/refunds, consent, category/SKU, subscription status, cadence and spend. If the restricted connector hides a required read capability, report the gap and seek a scoped read-only configuration change; do not enable writes to finish discovery.
3. Verify exact Joy property/event names, types, units and freshness for membership, Sparks balance, redemption history, tier, referral link/qualification and birthday. **Exact Joy properties/events used: none; unavailable and unverified.** These are business concepts, not copy-paste property names. Missing cadence or interval calculations may require separately approved upstream data preparation; do not invent a Klaviyo filter or silently weaken eligibility.
4. Reconcile the fixture's 12m order counts with the account's order-count window before mapping eligibility. Recount every proposed segment after mapping fields; supplied candidate counts are not verified segment membership or consent-qualified audiences.

### Proposed segments

All rows are proposed definitions only, not created objects. Existing versus new is **unknown pending discovery**; reuse an equivalent object after review, otherwise propose a new object named `FizzyRoot | <segment>`. Verification is **not run** for every row. Segments do not have a presumed draft status: draft/inactive controls apply to flows, and even segment creation requires write approval. Entry occurs when the definition first becomes true; global marketing exclusions below apply to flow eligibility.

| Segment | Definition | Count | Exit rule | Planned action / offer | Metric |
|---|---|---:|---|---|---|
| First-time buyers | Exactly one completed, non-refunded order in the reconciled purchaser window | 180 fixture; verified unavailable | Second order or qualifying order reversed | First-order education; no discount | 60-day second-purchase rate |
| Second purchase due | First-time buyer; 31–58 whole days since first order | unavailable; subset of 180 | Second order, day 59 or order reversal | Due flow; favorite 12-pack, no new incentive | Second order within 60 days |
| Active repeaters | 2+ qualifying orders; recency ≤1.5× personal cadence, fallback 39 days (whole days ≤58) | unavailable; subset of 120 | Recency exceeds threshold or order eligibility lost | Reporting/suppression segment initially; no standalone flow or offer | Repeat frequency and contribution |
| Subscription candidates | 3+ same-category purchases; ≥2 intervals each within ±25% of their mean; exclude active subscribers | 45 fixture candidates; eligible count unavailable | Subscription starts or cadence/category fit fails | Subscription education; convenience only | Starts and first two renewals |
| VIP candidates | ≥3 qualifying orders AND ≥$217.50 net spend in rolling 12m | unavailable | Either threshold no longer met | Later tier recognition; approved access perks | Qualified retention and perk cost |
| At-risk | 2+ qualifying orders; recency >1.5× and ≤2.5× personal cadence; fallback days 59–97 | 28 fixture; proposed-rule count unavailable | Purchase, day 98 fallback or loss of repeat eligibility | At-risk flow; relevant replenishment without coupon | Reactivation contribution |
| Lapsed | 2+ qualifying orders; recency >2.5× personal cadence; fallback day 98 onward | 16 fixture; proposed-rule count unavailable | Purchase or loss of repeat eligibility | Limited win-back; discovery without coupon | Reactivation versus holdout |
| Advocates/referrers | Verified positive feedback OR qualified referral; distinguish candidates from actual referrers | 24 fixture candidates; verified unavailable | Opt-out, signal invalidated or fraud flag | Later referral ask; approved $3/$3 terms only | Qualified buyers and referral CAC |
| High reward balance/no redemption | Verified balance ≥250 Sparks AND zero redemptions in preceding 60 days | unavailable | Redemption or balance <250 | Later earned-balance education; $5 on ≥$100 eligible basket | Redemption and contribution versus holdout |

New non-buyers remain in the customer-segment map above; inspect/reuse an existing welcome journey before proposing a separate build. Do not create all candidates automatically. First-time/due segments are the initial priority; subscription/risk segments require verified history and subscription mapping. VIP, advocate and balance segments are deferred until Joy mechanics and synced data exist and are approved.

### Proposed draft flows

Existing versus new is **unknown pending discovery** for every flow. Every row has **count unavailable**, **status proposed draft/inactive, not created**, and **verification not run**. Message timing describes an eventual separately approved launch, not scheduled delivery in this run. No historical backfill/enrollment is authorized.

| Flow | Trigger and timing | Exit rule (also checked before each message) | Messages/actions and offer | Success metric |
|---|---|---|---|---|
| First-order education | Verified first completed-order event; exactly one qualifying order; +3 and +10 days | Second purchase, order reversal or global exclusion | 2 emails: serving/meal ritual, then flavor discovery; no discount | Mature 60-day second-purchase rate |
| Second-purchase due | Entry into due segment; target order-age days 31, 39 and 52 | Second order, age >58 days or global exclusion | 3 emails: favorite 12-pack, ritual reminder, final discovery prompt; no new discount | Second purchase and contribution within 60 days |
| Subscription education | Entry into verified non-subscriber candidate segment; +0 and +7 days | Subscription starts, eligibility lost or global exclusion | 2 emails: flexible replenishment, then skip/pause and flavor choices; no assumed subscription discount | Starts and renewal retention |
| At-risk replenishment | Entry into at-risk segment; +0 and +7 days | Purchase, lapsed transition or global exclusion | 2 emails: taste/timing check, then relevant pack recommendation; no coupon | Reactivation contribution |
| Lapsed discovery | Entry into lapsed segment; +0 and +14 days | Purchase or global exclusion | 2 emails: new flavor discovery, then final invitation; no incentive test until separately costed/approved; stop this sequence afterward | Holdout-adjusted reactivation contribution |
| Earned-balance education — later | Entry into verified high-balance segment; +0 and +7 days | Redemption, balance <250 or global exclusion | 2 emails: explain 250 Sparks → $5, then reminder; ≥$100 basket, no stacking; no artificial expiry | Redemption and contribution |
| VIP recognition — later | Entry into verified VIP segment and confirmed Joy tier qualification; +0 days | Qualification lost or global exclusion | 1 email: Ritual Regular recognition and approved access perks; no new monetary reward | Qualified retention and perk cost |
| Referral invitation — later | Verified positive-feedback/qualified-referral event while eligible; +2 days | Fraud/invalid signal, opt-out or global exclusion | 1 email: $3 friend/$3 referrer, each ≥$130 basket; qualification/return-window terms must match Joy | Qualified referred buyers and incentive CAC |

Due-flow scheduling must use order age: on late entry, skip past milestones and wait for the next future day-31/39/52 milestone; never compress missed messages. Verify supported branching/delay controls before drafting. One-time buyers reaching day 59 exit this flow; their separate reactivation flow remains deferred pending data and a new plan, and must not enter the 2+ order risk flows.

**Proposed shared controls, subject to approval:** Require valid email marketing consent and deliverability; exclude suppressed/unsubscribed profiles, unresolved order/service issues and the persistent experiment holdout. Recheck eligibility before every message. Exclude active subscribers from due, subscription-acquisition and generic replenishment/win-back flows until subscriber-specific logic is approved. Limit combined marketing to one email per 72 hours and two per seven days across campaigns/flows; skip rather than queue a message that would exceed the cap. Verify implementation support or block the affected draft. Keep transactional messaging separate. Prevent overlapping incentive journeys: prioritize earned-balance education over referral, subscription acquisition and generic replenishment, and suppress competing offer messages while a stronger approved offer is active. No first-order/due re-entry; subscription, risk, lapsed and balance flows at most once per 90 days; VIP once per qualification period and referral once per 180 days, subject to verified controls.

### Approval, future writes and completion status

Klaviyo write approval is **pending** and separate from Joy approval. The approval packet must include exact mapped segment definitions/counts, flow triggers/exits, message count/timing, final content, incentives/expiry, suppression/frequency rules and draft-only status. No interactive approval is requested in this evaluation. Klaviyo tools may have no dry-run: this rendered plan is the review artifact, not a claimed tool preview; do not pass Joy's `apply: false` convention to unverified Klaviyo schemas.

After explicit approval in a future build, reconnect with only the approved write capabilities enabled and without `read-only=true`. Re-list segments/flows to prevent duplicates and document approved reuse/updates. Create one approved segment with `create_segment`, read it back with `get_segment`, and query membership with `query_segment_values`; investigate unexpected counts before proceeding. Then create one approved flow with `create_flow` only if draft/inactive status for the flow and every message/action can be guaranteed. Read back trigger, filters, delays, actions and status with `get_flow`; stop on any mismatch or unconfirmed status. If safe inactive creation is unsupported, leave the object uncreated and report the blocker. Template creation/update requires separate content approval and read-back; no template is created here.

Before any separately approved launch, verify Daily Orbit/Sparks/tier naming, the 2% reward economics and 5% budget, $5/250-Spark redemption and basket conditions, $3/$3 referral qualification, subscription exclusions, actual expiry dates and synced-property freshness against Joy. Do not turn the proposed 12-month inactivity expiry into an invented fixed coupon deadline. Activation, campaign sending (including `send_campaign`) and all customer-facing delivery require separate explicit approval; **activation/send approval: not granted; no activation or sends authorized**.

Completion ledger: company/account unverified; connection not established (read-only planned first); existing objects reused **0**; segments created **0**, verified counts **unavailable**; flows created **0**, draft/inactive status only proposed; templates created/updated **0**; read-backs **not run**. All objects remain uncreated because this is a fictional `PLAN_ONLY` fixture. Remaining gates are real-account discovery, supported data mappings, exact Klaviyo build/content approval and separate activation/send approval.

## Verification

- **Storefront checked:** No. Fictional domain; no external access permitted.
- **Program config checked:** No. Fixture says loyalty not installed; no live confirmation.
- **Widget target:** Draft, proposed only. No draft created and no live change.
- **Publish status:** Not published; no publish authorization.
- **Completed checks:** Recalculated 40% second-purchase rate, $50 paid CAC, revenue share, AOV, contribution, proxy LTV, referral sensitivity and reward-budget scenarios from supplied inputs.
- **Remaining manual steps:** Confirm shop/environment and APIs; reconcile reporting windows and net discount treatment; inspect flows and consent; recount segments and tier eligibility; confirm return/expiry/anti-fraud policies; validate subscription exclusions and cap monitoring; obtain approvals; run real previews/read-backs; review draft visually on mobile/desktop and test earn, redemption, referral, refunds and account navigation with controlled test orders.
- **Rollback limitations:** Nothing changed here. Future live widget saves are immediate and have no MCP undo; capture prior settings and plan a separately approved restoration. Points, redeemed rewards and customer communications may not be reversible simply by restoring config.

## 90-day measurement plan

- **Baseline window:** Supplied 12m ending as of 2026-09-16, exact start/date semantics to confirm. Descriptive baseline: 40% second-purchase rate, $72.50 AOV, 52.9655% returning revenue share; CAC baseline uses the separate supplied 90d window. Obtain timestamped first-order cohorts before experimentation.
- **Primary metric:** Fraction of new first-order purchasers making a second completed, non-refunded purchase within 60 days. Existing 40% is not this metric's baseline. Compare only fully observed cohorts and report counts/uncertainty; this dataset does not justify a numeric lift promise.
- **Secondary metrics:** Median time to second order; contribution/customer after incentives; orders/customer; reward issuance/liability/redemption and all-in incentive rate ≤5%; referral qualification/CAC; non-discount repeat share; subscription starts, first/second renewals, skips and cancellations; unsubscribe/complaint rates. Define subscription churn only from subscribers and cancellations at risk, never as 100% minus returning-customer rate.
- **Holdout/comparison:** Proposed persistent randomized 80/20 eligible customer treatment/control split for lifecycle activation, preserving transactional messages in both. Check sample feasibility; 300 historical purchasers may provide insufficient power. Stage reward/referral experiments separately to avoid confounding lifecycle impact; otherwise report only the combined treatment effect. Do not call Joy-assisted or associated revenue incremental; incremental contribution requires the comparison design.
- **Review dates:** If the pilot starts on 2026-09-16: day 30 on 2026-10-16 for delivery, eligibility and budget QA; day 60 on 2026-11-15 for early mature cohorts; day 90 on 2026-12-15 for primary and contribution results. At day 90, only entrants through day 30 have a full 60-day outcome. Shift dates if approval delays launch. Expand only with positive contribution evidence and verified budget compliance; otherwise revise or keep lifecycle-only.

## MCP_HANDOFF

This is declarative planning JSON, not a tool-schema claim or an execution request. `proposal` values must be translated using discovered schemas; every configuration preview explicitly has `apply: false`. Unsupported controls block that program's preview/build until resolved.

```json
{
  "MCP_HANDOFF": {
    "mode": "PLAN_ONLY",
    "shop": "demo.fizzyroot.example",
    "fictional_demo": true,
    "as_of": "2026-09-16",
    "execution_authorized": false,
    "external_api_calls_made": false,
    "sidekick_invoked_joy_mcp": false,
    "strategy_approval": "pending",
    "exact_diff_approval": "pending",
    "publish_approval": "pending",
    "payload_kind": "declarative_proposals_not_verified_tool_arguments",
    "prerequisites": [
      "Confirm real target shop and environment before any future connection",
      "Obtain strategy and economics approval",
      "Discover available tools and input schemas",
      "Read current settings, programs, balances, tiers, referrals and widget",
      "Reconcile cohort economics and subscription costs",
      "Verify exclusions, combined tier criteria and cost-cap enforcement",
      "Scan brand design, discover widget fields and inspect theme setup"
    ],
    "writes": [
      {
        "tool": "joy_configure_shop_settings",
        "apply": false,
        "proposal": {"club_name": "FizzyRoot Daily Orbit", "currency_name": "Sparks"}
      },
      {
        "tool": "joy_configure_earning_program",
        "apply": false,
        "proposal": {
          "sparks_per_eligible_currency_unit": 1,
          "nominal_reward_rate": 0.02,
          "exclude": ["tax", "shipping", "gift_cards", "refunds", "reward_redemption_orders", "referral_discount_orders", "discounted_subscription_orders"],
          "missions": [
            {"action": "verified_profile_preferences", "sparks": 10, "limit": "once"},
            {"action": "verified_review_any_sentiment", "sparks": 20, "limit": "once_per_year"},
            {"action": "approved_ugc_separate_reuse_consent", "sparks": 20, "limit": "once_per_year"},
            {"action": "birthday_after_verified_purchase", "sparks": 10, "limit": "once_per_year"}
          ],
          "mission_support": "unverified_create_separate_previews_only_for_supported_actions"
        }
      },
      {
        "tool": "joy_configure_redemption_program",
        "apply": false,
        "proposal": {
          "separate_preview_per_reward": true,
          "rewards": [
            {"sparks": 100, "value": 2, "minimum_merchandise_basket": 40},
            {"sparks": 250, "value": 5, "minimum_merchandise_basket": 100},
            {"sparks": 500, "value": 10, "minimum_merchandise_basket": 200}
          ],
          "stacking": false,
          "earn_on_redemption_order": false
        }
      },
      {
        "tool": "joy_configure_tier",
        "apply": false,
        "proposal": {
          "separate_preview_per_tier": true,
          "tiers": [
            {"name": "First Sip", "minimum_orders": 1},
            {"name": "Ritual Regular", "minimum_orders": 3, "minimum_net_spend": 217.5},
            {"name": "Table Host", "minimum_orders": 5, "minimum_net_spend": 362.5}
          ],
          "criteria_operator": "AND",
          "qualification_window": "rolling_12_months",
          "compound_criteria_support": "unverified"
        }
      },
      {
        "tool": "joy_configure_tier_settings",
        "apply": false,
        "proposal": {"qualification_window": "rolling_12_months", "grace_days": 30, "preserve_existing_balances_and_tiers": true}
      },
      {
        "tool": "joy_configure_tier_perks",
        "apply": false,
        "proposal": {
          "Ritual Regular": ["flavor_previews", "flavor_voting"],
          "Table Host": ["priority_future_flavor_table_invitation"],
          "fulfillment": "manual_until_supported_and_costed",
          "base_earn_multiplier": 1
        }
      },
      {
        "tool": "joy_configure_referral_program",
        "apply": false,
        "proposal": {
          "friend_reward_value": 3,
          "referrer_reward_value": 3,
          "minimum_basket_for_each_reward": 130,
          "assumed_referrer_redemption": 0.6,
          "expected_incentive_cac": 4.8,
          "maximum_face_value_cac": 6,
          "stacking": false,
          "base_earning_on_rewarded_orders": false,
          "qualification": "unique_new_customer_first_fulfilled_non_refunded_order_after_verified_return_window",
          "maximum_qualified_rewards_per_referrer_month": 5,
          "reserve_both_rewards_against_origin_order": true
        }
      },
      {
        "tool": "joy_configure_referral_widget",
        "apply": false,
        "target": "draft",
        "requires_verified_draft_support": true,
        "proposal": {"copy": "Bring a friend to the table: $3 for them, $3 for you. $130 minimum baskets; terms apply."}
      },
      {
        "tool": "joy_configure_widget_draft",
        "apply": false,
        "target": "draft",
        "proposal": {
          "launcher_copy": "Your Daily Orbit",
          "palette": ["#FFF4DA", "#30203D", "#E5F35B", "#F97762"],
          "sections": ["balance", "rewards_and_conditions", "flavor_discovery", "tier_progress", "qualified_referrals"],
          "field_paths_and_enums": "discover_before_preview"
        }
      },
      {
        "tool": "joy_set_widget_fields",
        "apply": false,
        "target": "draft",
        "conditional_on": "separate_account_navigation_approval_and_field_discovery",
        "proposal": {
          "links.replaceAccountLink": true,
          "links.accountLinkSelector": "omit_unless_detection_fails_and_actual_selector_is_verified",
          "creates_separate_header_rewards_icon": false
        }
      }
    ],
    "execution_rules": {
      "dry_run_only": true,
      "if_draft_target_unsupported": "omit_widget_preview_and_report_blocker",
      "no_schema_guessing": true,
      "no_image_upload_authorized": true,
      "no_theme_edit_authorized": true,
      "separate_header_rewards_icon": "requires_separately_approved_theme_or_app_block_implementation",
      "future_apply_requires": "exact_diff_approval_then_one_write_at_a_time_and_readback_after_each",
      "unconfirmed_field_action": "stop_and_report",
      "live_widget": "not_authorized_immediate_storefront_change_with_no_MCP_publish_or_undo"
    },
    "status": {"dry_runs": "not_run", "applied_writes": 0, "read_backs": "not_run", "published": false}
  }
}
```
