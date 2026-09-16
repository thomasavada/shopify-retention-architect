# Shopify Retention Architect

A Claude/Codex-compatible plugin for auditing Shopify retention, quantifying second purchase, choosing the right retention system, and safely executing approved changes through Joy MCP and Klaviyo's official MCP server.

## What it does

```text
Shopify audit
→ second-purchase rate
→ brand stage
→ AOV/CAC and repeat economics
→ lifecycle vs subscription vs referral vs loyalty
→ customer segments
→ brand story and creative territory
→ cashback, missions, VIP, referral and subscription blueprint
→ merchant approval
→ Joy MCP dry-runs
→ Klaviyo MCP segment/flow plan
→ exact-diff approval
→ apply Joy programs + create Klaviyo drafts
→ build and visually review widget draft
→ explicit live approval
→ publish/live widget write
→ optional account/header touchpoints
→ verification and 90-day measurement
```

The skill may recommend **not** building loyalty when the brand's actual constraint is acquisition, conversion, AOV, product quality, insufficient data, or a structurally one-time product.

## Install

### Codex plugin

```bash
codex plugin marketplace add thomasavada/shopify-retention-architect
codex plugin add shopify-retention-architect@shopify-retention
```

### Claude Code plugin

```bash
claude plugin marketplace add thomasavada/shopify-retention-architect
claude plugin install shopify-retention-architect@shopify-retention
```

The repository contains both marketplace manifests, both plugin manifests, and the skill at:

```text
skills/shopify-retention-architect/SKILL.md
```

### Git clone

```bash
git clone https://github.com/thomasavada/shopify-retention-architect.git
```

## Run it on your own store

Three steps from a cold start to an audit of your own data.

**1. Install the plugin** using the commands above.

**2. Connect the store.** Shopify CLI is the quickest route for an audit, because nothing
has to be created first:

```bash
shopify store auth --store your-store.myshopify.com \
  --scopes read_products,read_customers,read_orders,read_all_orders,read_reports
```

⚠️ **`read_all_orders` is not optional.** Without it Shopify returns only the last 60 days
of orders — silently, with no error. A "12-month audit" then quietly becomes a 60-day one,
and every cohort, AOV figure and trend in the report is wrong. This is the easiest way
available to get a confident, wrong answer.

`read_reports` is what makes the ShopifyQL sales queries work. Without it the audit falls
back to computing the same figures from raw orders — slower, equivalent.

**3. Ask for the audit** in the same directory:

> Audit this Shopify store's retention and tell me whether it should build loyalty.
> Store: your-store.myshopify.com

The run defaults to `AUDIT_ONLY`: it reads, and writes nothing. You will be asked a short
set of questions the store data cannot answer — contribution margin, ad spend, what has
already been tried. Answer what you can; anything skipped is reported as unsized rather
than guessed.

### What comes back

One report: your second-purchase rate with the denominator stated, customer segments with
real counts, dated actions for the next 30/60/90 days, a loyalty program specified closely
enough to hand to a developer, subscription and bundle strategy, expected impact per lever
with measured and modelled figures kept apart, and a monitoring table naming each symptom,
the instinct that usually makes it worse, and the one job that addresses it.

If the store already runs a loyalty program, the audit diagnoses that program instead of
designing over the top of it — who is enrolled, what has actually been issued, and which
rules are running against capability the store does not have.

### If you want it to build, not just audit

Writes are a separate mode and a separate credential. Shopify CLI sessions are rejected by
some write mutations, so create a custom app in the store admin (Settings → Apps → Develop
apps), grant the matching `write_*` scopes, and use its `shpat_…` Admin API token. Every
build step previews a diff and applies only after you approve it.

## Trigger examples

- “Audit this Shopify store's retention.”
- “How many customers buy a second time?”
- “Should this brand use subscription, referral, loyalty, or a hybrid?”
- “Build customer segments and lifecycle flows for this store.”
- “Design a loyalty program that speaks the brand's character.”
- “Build the approved Joy program and on-brand widget with MCP.”
- “Prepare a realistic Shopify development store for a retention demo.”

## Integrations

### Joy MCP

The skill can orchestrate the shipped Joy MCP setup tools when the connected server exposes them:

- Programs and shop settings
- VIP tiers, rewards and perks
- Referral program and referral widget
- Storefront brand scan
- Widget field discovery and writes
- Image uploads to Shopify Files
- Draft/live widget configuration

All configuration writes preview first, require approval, apply one at a time and read back afterward.

### Klaviyo MCP

Klaviyo provides an official remote MCP server:

```text
https://mcp.klaviyo.com/mcp
```

The workflow uses read-only mode for discovery, then separately approved writes for segments, draft flows and templates. Flow activation and campaign sending are never included in the build approval.

Official documentation:

- https://developers.klaviyo.com/en/docs/klaviyo_mcp_server
- https://developers.klaviyo.com/en/docs/connect_to_the_klaviyo_mcp_server
- https://developers.klaviyo.com/en/docs/klaviyo_mcp_server_available_tools

## Guardrails

- Never seed a production merchant.
- Never recommend loyalty by default.
- Never fabricate margin, CAC, cadence, segment counts or benchmarks.
- Assisted revenue is not incremental revenue.
- Joy writes use dry-run and read-back.
- Klaviyo writes require a reviewed plan; flows remain draft/inactive.
- Live widget writes require a separate approval and have no MCP undo.
- `links.replaceAccountLink` intercepts an existing account icon; it does not add a separate header rewards icon.
- A new header icon requires separately approved theme/app-block work.

## Repository structure

```text
.claude-plugin/plugin.json
.codex-plugin/plugin.json
skills/shopify-retention-architect/
  SKILL.md
  references/
    decision-framework.md
    demo-store-data.md
    joy-mcp-execution.md
    klaviyo-mcp-execution.md
    output-template.md
evals/
  demo-brand.json
  test-prompt.md
  example-output.md
  validate_output.py
prompts/
  handoff-existing-shopify-cli.md
  setup-realistic-demo-store.md
```

## Realistic demo store

Use [`prompts/setup-realistic-demo-store.md`](prompts/setup-realistic-demo-store.md)
to give Codex or Claude Code the full execution context for creating a deterministic
12-month Shopify dataset with 300 customers, 500 paid/fulfilled orders, bundles,
repeat cohorts, adaptive API throttling, Joy reconciliation, and Klaviyo draft setup.

If Shopify CLI is already authenticated and connected, use the shorter continuation
brief: [`prompts/handoff-existing-shopify-cli.md`](prompts/handoff-existing-shopify-cli.md).

## Evaluation

The included fictional functional-drink fixture contains:

- 300 purchasing customers
- 500 orders
- Bundles and replenishable products
- Exact one-order and repeat-customer counts
- Reorder-cadence evidence
- Paid-spend, margin and CAC inputs

Codex produced the included example output and passed the validator:

```bash
python3 evals/validate_output.py
```

The example is synthetic and must never be presented as a real merchant case.

## License

MIT
