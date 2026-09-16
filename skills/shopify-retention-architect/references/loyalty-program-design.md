# Designing the loyalty program

Read this once the audit has justified loyalty as a mechanism. The audit decides
*whether*; this file decides *what*, and holds the numbers to a standard so the program
is affordable rather than merely attractive.

The visual skin of a rewards program is wide open. The arithmetic is not — it converges
across the market, and a program that ignores that convergence either bankrupts its
margin or feels worthless to members.

## Derive the numbers from the audit, not from a template

Every threshold below should be traceable to something you measured. If you cannot point
at the number in the audit that produced a threshold, you are guessing, and you should
say so rather than presenting it as designed.

| Program decision | Audit input that determines it |
|---|---|
| Tier thresholds | actual trailing-12-month spend distribution — put tier 2 near the 15–20th percentile of purchasers and tier 3 near the top 4–5% |
| Reward ladder rungs | AOV, so the first rung is reachable in 1–2 orders |
| Point expiry window | median time to second order — expiry must land *after* the natural repurchase point, never before |
| Earn multiplier ceiling | contribution margin; the multiplier multiplies your cost, not just their delight |
| Referral reward size | AOV and, when known, paid CAC — referral only makes sense below paid CAC |
| Whether to run missions | size of the non-purchaser base; missions monetize attention you already have |

## The arithmetic

```
redemption_ROI = (reward_value / (units_required / earn_rate)) × 100
```

**~1% is the safe default.** Osea (500 pts = $5 at 1 pt/$1) and EATABLE (100 pts = $1)
both land there. Stay within 0.25 percentage points of your stated target, or state
plainly that you are deliberately running richer and why the margin supports it.

Richer programs do exist in market — Three Ships runs 100 pts = $5 at 1 pt/$1, which is
**5%**. That is a real, working program, but it is a margin decision, not a default. At
5% ROI plus a 1.5× top-tier multiplier, the effective giveaway on your best customers
approaches 7.5% of revenue. Only recommend that when contribution margin is comfortably
above it and you have said the number out loud.

Benchmark ranges for the rest:

| Quantity | Safe range |
|---|---|
| Earn rate | 1–5 units per $1 |
| Signup bonus | 25–100 units (≈ $0.50–1.00 of value) |
| Referral, each side | $8–15 of value |
| Reward ladder rungs | at least 5 |
| Top rung | not convertible to money |

## Tiers are earned by spend, never by accumulated points

This is the single most common design error, and it is self-defeating: if tier status is
driven by the same points members spend, then redeeming a reward demotes them. Members
learn to hoard, the currency stops circulating, and the program's whole purpose inverts.

Split the two axes — **spend determines status, points are for spending** — over a
**trailing 12-month window**, not a calendar-year reset. Chubbies ($150/$300), 100% Pure
($250/$750) and Three Ships ($150/$350) all do exactly this.

## The program object to produce

```yaml
club_name:          # brand-voiced, not "Rewards Program"
currency_name:      # a noun the brand would actually use
earn_rate:          # units per $1, plus any multipliers
signup_bonus:
ladder:             # >=5 rungs, cheapest first, top rung non-monetary
tiers:              # exactly 3; threshold = trailing-12mo spend; each adds a real perk
referral:           # symmetric give/get, both sides stated
missions:           # non-purchase earning: review, photo, video, social, birthday
subscription_hook:  # how subscribers are advantaged (multiplier or auto-tier)
rules:              # expiry, stacking, returns, fraud, tier decay
cost_model:         # redemption_ROI, expected breakage, cost as % of revenue
metrics_90d:        # what you will read to judge it
```

### Choosing perks that cost little and signal much

Rank candidate perks by *perceived value ÷ marginal cost*, and prefer the top of that
ratio. Free shipping is usually the strongest perk on a low-AOV catalog, because shipping
is a real friction on a small basket. Early access and pre-production sample groups cost
essentially nothing and confer status — Three Ships uses both. A free full-size product
at the top tier is expensive per redemption but rare enough to be affordable, and it is
the most concrete reason to climb.

Redeem in *product and access*, not only in dollars off. A free item at a known retail
price reads as more valuable than the same cost given as a discount, and it does not
train members to wait for markdowns.

### The aspirational rung

A ladder that tops out at "$25 off" has no horizon. The last one or two rungs should be
things money does not straightforwardly buy: a 1:1 session with an in-house expert, a
year of product, a name on something, an experience. Sun Bum's 30,000-point billboard is
the canonical example. Few members will ever reach it; its job is to make the middle of
the ladder feel like progress toward something rather than a coupon dispenser.

## Anti-patterns the audit will usually expose

- **Points for the non-purchaser base.** If most records have never bought, they did not
  fail to convert for lack of a loyalty account. Fix activation instead.
- **Stacking points on already-discounted bundles.** A bundle at 25–30% off plus a
  redemption is a compounding giveaway. State the stacking rule explicitly.
- **Rewarding repeat behaviour that already happens unprompted.** If a large share of
  repeat orders are already discounted, adding points pays people to do what they were
  doing anyway. Quantify that deadweight before recommending a rate.
- **Expiry before the natural reorder.** Points that die at 30 days on a 45-day reorder
  cycle generate resentment, not urgency.
- **Four or five tiers on a base that cannot fill them.** If the top decile holds roughly
  a third of revenue rather than half, there is no whale class to justify a long ladder.
  Three tiers.

## Rewards page structure

When the deliverable includes the customer-facing page, use this block order. It is drawn
from a corpus of live DTC programs and each block earns its place.

| # | Block | Contents |
|---|---|---|
| 1 | Hero | club name, one-sentence promise, Join / Sign in |
| 2 | Manifesto | why the club exists, in brand voice |
| 3 | How it works | Sign up → Earn → Redeem |
| 4 | Ways to earn | grid of actions, brand-voiced names, point values |
| 5 | Ways to redeem | cheap → aspirational; at least one non-monetary rung |
| 6 | Tier ladder | 3 tiers, thresholds, perks, current tier marked |
| 7 | Referral | symmetric give/get |
| 8 | Proof | reviews, ratings, press — next to the decision point |
| 9 | FAQ | ~8 questions including the uncomfortable ones |
| 10 | Join CTA | close the page |

The FAQ should answer what members actually worry about: what one unit is worth, whether
points expire and with what warning, whether rewards work on subscription orders, what
happens to spent points on a return, whether slowing down costs them their tier, whether
rewards stack with discount codes, and — if a program already exists — how the old
balance converts. Dodging these reads as evasive; answering them plainly builds trust.

Do not impose a layout on the brand. Read heading alignment, heading size and whether the
brand uses dark sections from the live storefront before composing — many editorial DTC
brands use modest 32–36px headings and no dark sections at all, and a full-bleed black
band dropped into that rhythm reads as someone else's page.

## Worked example — Three Ships, Natural Champions Club

Useful because it is real, complete, and gets the structure right while running unusually
rich economics.

- **Earn:** 1 pt/$1, 2× on subscription orders
- **Missions:** review 50, photo review 25, video review 25, social follow 10 each,
  birthday 200, subscribe to a product 50
- **Ladder:** $5/100, $10/200, $15/300, $20/400, $25/500 — all monetary, ROI 5%
- **Tiers by spend:** Natural Explorer (account) 1× · Natural Enthusiast ($150) 1.25×,
  tier-entry 50 pts, birthday 300, $25 off · Natural Leader ($350) 1.5×, tier-entry
  100 pts, birthday 400, pre-production sample group, free full-size product
- **Referral:** give $15 / get $15 on orders $60+

What to copy: spend-based tiers, escalating multiplier, tier-entry bonuses, non-purchase
missions, the subscription multiplier, symmetric referral.

What to fix: the ladder is entirely monetary and tops out at $25 off, so there is no
aspirational rung; and at 5% ROI compounding with a 1.5× multiplier, the program needs a
margin most brands do not have. Keep the architecture, size the numbers to the audit.
