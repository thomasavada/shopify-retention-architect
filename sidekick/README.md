# Sidekick variants

Two paste-in **Shopify Sidekick Skills**, run in Shopify admin rather than installed as a
plugin:

| File | Shortcut | What it does |
|---|---|---|
| [`retention-audit.txt`](retention-audit.txt) | `retention-audit` | Diagnoses. Names the one binding constraint, and is allowed to conclude that no program is needed. **4,965 / 5,500 chars.** |
| [`loyalty-program.txt`](loyalty-program.txt) | `loyalty-program` | Designs the program, once the audit has justified one. **5,492 / 5,500 chars.** |

**They are deliberately two skills, not one.** A single skill that both diagnoses and designs
has a thumb on the scale: the same instructions that tell it to size a reward ladder make
"build a ladder" the expected output, and the six verdicts collapse to one. Splitting them
means the audit can end with *"you do not need this"* and simply not hand over — which is
the whole reason the audit is worth running. It also fits: neither half survives the 5,500
character limit with the other one attached, so the split is what the runtime allows as well
as what the method wants.

Order matters. `retention-audit` first; `loyalty-program` opens by saying so, and stops if
the evidence points at acquisition, basket size, lifecycle timing or subscription.

They exist as separate artifacts because the two runtimes are not interchangeable, and the
difference is not cosmetic.

## Why a separate file instead of the same SKILL.md

| | Claude Code / Codex plugin | Shopify Sidekick Skill |
|---|---|---|
| Instruction budget | no practical limit (this skill's `SKILL.md` is ~517 lines) | **5,500 characters**, hard, per skill |
| Bundled `references/` | yes — progressive disclosure, loaded on demand | **none.** No files, no links followed |
| Store access | whatever you authenticate: Admin GraphQL, ShopifyQL, `read_all_orders` | already inside the merchant's admin, reads its own data |
| Can it write? | yes, through Joy MCP / Klaviyo MCP with per-step approval | no — diagnosis only |
| Who runs it | someone with a terminal | the merchant, in a chat box they already use |

So the Sidekick version is not a trimmed copy — the reference files that carry most of the
plugin's method (`decision-framework.md`, `loyalty-program-design.md`, `shopify-queries.md`)
cannot travel with it at all. Everything that survives had to be rewritten as *rules a model
can apply from memory*, and everything that only works with a lookup table was dropped.

`retention-audit.txt` sits at **4,965 / 5,500** characters and the headroom is deliberate —
room to add a guard when a real run gets something wrong.

`loyalty-program.txt` sits at **5,492 / 5,500**, which is effectively full. That is worth
knowing before editing it: adding a rule there means removing one, so decide which of the
existing rules earns its place less than the new one rather than trimming prose until it
fits. The arithmetic, the percentile procedure and the spend-not-points rule are the three
that must never be the thing that gets cut.

## What was kept, and why those and not others

### `retention-audit` — kept, and why each one changes the answer

- **The denominator rule.** Purchasers, not customer records. Most stores hold several times
  more records than buyers, and dividing by records understates the repeat rate severalfold,
  which aims the whole strategy at the wrong problem. Stated once, then applied to *every*
  rate in the report including consent — because the first version applied it only to the
  repeat rate and then quoted consent against total records two paragraphs later.
- **`processedAt`, not `createdAt`.** On any migrated or seeded store the two diverge and a
  year of trading collapses into however long the import took, silently. This one is the
  reason the audit of the demo store was right the second time.
- **Percentile monotonicity check.** A stricter percentile must have a higher threshold. A
  real Sidekick run reported the top-4% spend *below* the top-15% figure — arithmetically
  impossible, and it read as authoritative. Now it is checked before reporting.
- **The three constraint checks** — consent, an incumbent loyalty/subscription app, whether
  any selling plan exists. Each one can invalidate the recommendation, so they come before it.
- **The two tests** — cadence vs basket, artifact vs behaviour. Both catch a plausible reading
  that leads to the opposite build.
- **The Stop rule.** If no customer has a second order, the repeat rate, time-to-second and
  every lapsed segment are structurally unfillable; report what was measured and stop. A long
  report whose headline metric is 0% reads authoritative while saying nothing.
- **Loyalty is not the default answer**, with the six verdicts including "nothing yet."

Dropped, deliberately:

- Query shapes and GraphQL field names — Sidekick reads the store itself and does not need them.
- ROI arithmetic, rung spacing and the margin procedure — these need the tables in
  `references/loyalty-program-design.md`, and a half-remembered version of them invents margin.
- Every write path. Sidekick diagnoses; the plugin builds.

## What `loyalty-program` carries

Same compression test, applied to the design half. What survived is what changes the
program a merchant ends up with:

- **Thresholds from your own distribution, never copied dollars.** Compute trailing-12-month
  spend per purchaser, sort, and read tier 2 off the top 15% and tier 3 off the top 4%.
  Borrowing another brand's $150/$350 imports their basket and order frequency with it — on
  a higher-AOV catalog it puts most purchasers in tier 2 and makes the top tier ordinary.
- **Tiers by spend, never by accumulated points.** If status runs on the same points members
  spend, redeeming demotes them, so they hoard, the currency stops circulating, and the
  program inverts its own purpose.
- **The redemption-ROI formula and the ~1% default**, plus the collision nobody checks: at a
  $58 AOV, "1% ROI" and "first rung reachable in two orders" are arithmetically incompatible
  and produce a $1.16 reward. The skill has to name which lever it pulled — a non-monetary
  first rung, or a richer rate stated out loud — and knows that pushing the rung further out
  does not fix it.
- **Flat rung spacing, flat ROI up the ladder**, with escalation living in the tier
  multiplier, because a rising ROI is an instruction to hoard.
- **The missing-margin procedure**: design at a stated planning assumption, show the cost at
  a low/middle/high margin with the break-even at each, and make margin confirmation a
  launch gate. Never invent a margin, and never refuse to design because one input is absent.
- **Seven definitions that get decided silently otherwise** — what earning applies to, how
  the multiplier compounds, product rewards at COGS vs retail, breakage, redemption
  stacking, eligible SKUs by name, capacity for an experiential rung. Left unstated, one of
  these shipped a program at 6% that was modelled at 1%.

Dropped: the worked example, the benchmark tables in full, and every brand name. A model
that half-remembers a table invents one, which is the failure the split is meant to avoid.

## Install

Shopify admin → Sidekick → Skills → New skill, once per skill.

| Shortcut (max 50 chars) | Instructions |
|---|---|
| `retention-audit` | paste the whole of [`retention-audit.txt`](retention-audit.txt) |
| `loyalty-program` | paste the whole of [`loyalty-program.txt`](loyalty-program.txt) |

Then type `/retention-audit` in Sidekick, and `/loyalty-program` only if the verdict earned
it.

## What it returns

A verdict naming the one binding constraint, an evidence table with the window and source for
each figure, three to five actionable findings, segments with real counts, and what it could
not measure. It closes by naming the next step the verdict implies.

It will tell a merchant with healthy organic repeat that they do **not** need a loyalty
program. That is the point — a diagnosis that can only conclude "build loyalty" is a sales
pitch, and merchants can tell.

## Keeping the two in sync

When a real run produces a wrong number, fix it in **both** places — the guard belongs in
`skills/shopify-retention-architect/SKILL.md` and in the matching Sidekick file. Both bugs
listed above were found in Sidekick first and were live in the plugin too.

Measurement, not estimate: check the length in characters, not bytes. Every em dash costs
three bytes and one character, so a file that is 5,735 bytes can be 5,711 characters — and
a byte count will tell you a passing file has failed.

```bash
python3 -c "print(len(open('sidekick/loyalty-program.txt',encoding='utf-8').read()))"
```
