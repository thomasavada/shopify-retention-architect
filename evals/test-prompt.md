# Evaluation prompt

Read `skills/shopify-retention-architect/SKILL.md` and every file in
`skills/shopify-retention-architect/references/` first.

Audit the fictional demo brand in `evals/demo-brand.json` using the skill. This is a `PLAN_ONLY` run:

- Do not call external APIs.
- Do not modify any store.
- Compute the exact second-purchase rate and CAC economics from the fixture.
- Assign the primary stage and mechanism.
- Create the required customer-segment map.
- Propose three brand territories and choose one.
- Design a Joy program: cashback/reward rate, VIP tiers, non-purchase missions, referral economics and subscription relationship.
- Propose widget/account/header touchpoints.
- End with an `MCP_HANDOFF` JSON object whose Joy writes are dry-run only (`apply: false`, widget target `draft`).
- Include a Klaviyo MCP plan that uses read-only audit first, then proposes segments/flows as drafts with activation and sends unapproved.
- Do not claim Sidekick itself invoked Joy MCP or Klaviyo MCP.
- Explicitly state that a separate header rewards icon cannot be created by `links.replaceAccountLink`.

Write the result to `evals/example-output.md` using
`skills/shopify-retention-architect/references/output-template.md`.
