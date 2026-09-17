# Sidekick variant

[`retention-audit.txt`](retention-audit.txt) is the audit half of this skill, compressed to
run as a **Shopify Sidekick Skill** — pasted into Shopify admin rather than installed as a
plugin.

It exists because the two runtimes are not interchangeable, and the difference is not cosmetic.

## Why a separate file instead of the same SKILL.md

| | Claude Code / Codex plugin | Shopify Sidekick Skill |
|---|---|---|
| Instruction budget | no practical limit (this skill's `SKILL.md` is ~517 lines) | **5,500 characters**, hard |
| Bundled `references/` | yes — progressive disclosure, loaded on demand | **none.** No files, no links followed |
| Store access | whatever you authenticate: Admin GraphQL, ShopifyQL, `read_all_orders` | already inside the merchant's admin, reads its own data |
| Can it write? | yes, through Joy MCP / Klaviyo MCP with per-step approval | no — diagnosis only |
| Who runs it | someone with a terminal | the merchant, in a chat box they already use |

So the Sidekick version is not a trimmed copy — the reference files that carry most of the
plugin's method (`decision-framework.md`, `loyalty-program-design.md`, `shopify-queries.md`)
cannot travel with it at all. Everything that survives had to be rewritten as *rules a model
can apply from memory*, and everything that only works with a lookup table was dropped.

The current file is **4,993 / 5,500 characters**. The remaining headroom is deliberate: leave
room to add a guard when a real run gets something wrong.

## What was kept, and why those and not others

Kept — each one is a rule that changes the answer:

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

## Install

Shopify admin → Sidekick → Skills → New skill.

- **Shortcut** (max 50 chars): `retention-audit`
- **Instructions**: paste the whole of [`retention-audit.txt`](retention-audit.txt)

Then type `/retention-audit` in Sidekick.

## What it returns

A verdict naming the one binding constraint, an evidence table with the window and source for
each figure, three to five actionable findings, segments with real counts, and what it could
not measure. It closes by naming the next step the verdict implies.

It will tell a merchant with healthy organic repeat that they do **not** need a loyalty
program. That is the point — a diagnosis that can only conclude "build loyalty" is a sales
pitch, and merchants can tell.

## Keeping the two in sync

When a real run produces a wrong number, fix it in **both** places — the guard belongs in
`skills/shopify-retention-architect/SKILL.md` and in this file. Both bugs listed above were
found in Sidekick first and were live in the plugin too.
