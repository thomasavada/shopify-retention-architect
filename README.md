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
```

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
