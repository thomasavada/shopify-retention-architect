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

### When 1% and "reachable" collide

These two constraints — a ~1% redemption ROI and a first rung reachable in one or two
orders — are incompatible below a certain basket size, and the arithmetic says so plainly.
At a $58 AOV, two orders earn 116 points at 1 point per dollar; at 1% ROI that buys a
**$1.16** reward. Nobody joins a program for that, and presenting it signals you did not
check.

Resolve it deliberately, and say which lever you pulled:

- **Move the first rung further out.** Three to five orders to the first reward is honest
  on a low-AOV catalog, provided the ladder shows the next rung clearly so progress is
  visible from order one.
- **Run richer than 1%.** Defensible when contribution margin covers it — Three Ships runs
  5% — but state the cost as a percentage of revenue rather than burying it in a points
  table.
- **Make the first rung non-monetary.** Free shipping, a sample, early access: perceived
  value well above marginal cost, which sidesteps the ratio entirely. This is usually the
  best answer on a low-AOV catalog and the one most often overlooked.

What is not acceptable is quietly keeping both constraints and shipping a $1 reward, or
keeping the 1% label while the ladder actually pays 5%.

Benchmark ranges for the rest:

| Quantity | Safe range |
|---|---|
| Earn rate | 1–5 units per $1 |
| Signup bonus | 25–100 units (≈ $0.50–1.00 of value) |
| Referral, each side | $8–15 of value |
| Reward ladder rungs | at least 5 |
| Top rung | not convertible to money |

### Rung spacing and whether ROI rises up the ladder

Two questions the benchmarks above do not answer, and both change how the program feels.

**Spacing.** Keep the monetary rungs on a flat arithmetic step — $5, $10, $15, $20, $25 at
100-point intervals, as Three Ships does — so the next reward is always the same distance
away and progress reads as steady. Geometric spacing (100, 250, 600, 1500) makes each
subsequent reward feel further than the last, which is the opposite of what a ladder is
for. Save the jump for the non-monetary rungs at the top, where the distance is the point.

**Curve.** Hold the redemption ROI flat across the monetary rungs. If it rises — $5 for 100
points but $30 for 500 — you have built an incentive to hoard, and hoarding is the failure
mode that kills currency circulation and leaves you carrying a growing liability. Let the
escalation live in the **tier multiplier** instead, which rewards sustained spend rather
than sitting on a balance, and costs you only on customers who are already worth it.

State both choices explicitly in the program object. An agent that copies the shape of a
worked example without deciding these has not designed a program, it has reskinned one.

### The remaining numbers, and where each comes from

These are the values most often lifted wholesale from whatever example was to hand. Each
has a rule.

**Tier multipliers** multiply your cost, so read them as ROI. A 1% base program with a 1.5×
top tier pays 1.5% on your highest-spending customers, and that number has to survive the
margin conversation. Steps of roughly 0.25× are perceptible without compounding sharply;
anything past 2× usually means the base rate was set too low to feel worthwhile and is
being rescued at the top.

**Mission values** should reflect what the action is worth to you, not a flat gesture. A
written review with a photo produces reusable content and deserves several times a social
follow. Then apply the cap that matters: the total a member can earn without buying
anything should stay below your first reward rung, or you have built a way to farm rewards
instead of a reason to purchase.

**Tier-entry bonuses** are a welcome, not a windfall — size them near the signup bonus.
Their job is to make promotion feel like an event on the day it happens.

**Referral minimum order** belongs above your AOV, otherwise the reward subsidises a
below-average basket. Three Ships gives $15 on orders over $60 against an AOV comfortably
under that; the threshold is what stops referral becoming a discount channel.

**Point expiry** follows the reorder cycle, not the calendar. Expire after roughly two to
three times the median gap between orders — long enough that a normal customer never loses
points, short enough to bound the liability — and warn before it happens.

## Tiers are earned by spend, never by accumulated points

This is the single most common design error, and it is self-defeating: if tier status is
driven by the same points members spend, then redeeming a reward demotes them. Members
learn to hoard, the currency stops circulating, and the program's whole purpose inverts.

Split the two axes — **spend determines status, points are for spending** — over a
**trailing 12-month window**, not a calendar-year reset. Chubbies ($150/$300), 100% Pure
($250/$750) and Three Ships ($150/$350) all do exactly this.

### Size the thresholds from your own distribution, never by copying dollars

Borrowing another brand's thresholds imports their AOV and order frequency along with the
numbers. Compute the trailing-12-month spend for every purchaser, sort it, and read the
thresholds off the percentiles you want to address.

A worked example from a real 1,000-purchaser store with $54 AOV:

| Threshold | Customers above it | Share of revenue |
|---|---:|---:|
| $150 | 9.9% | 32.3% |
| $200 | 4.8% | 22.4% |
| $350 | 3.5% | 18.5% |

Three Ships' $150/$350 happen to land at the top 10% and top 3.5% here, which is a
defensible shape — but that is coincidence, not design. On a store with twice the AOV the
same dollars would capture a third of the base and the top tier would stop signalling
anything.

Aim for a tier 2 that a motivated regular can actually reach (roughly the top 10–20%) and
a tier 3 that stays scarce enough to mean something while still holding meaningful revenue
— a top tier covering 3–5% of customers but a fifth of revenue is worth its perks. If your
top decile holds barely a third of revenue, there is no whale class: keep three tiers and
resist the temptation to add a fourth.

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
