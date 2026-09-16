# Klaviyo MCP execution

Use Klaviyo's official MCP server. Do not build or trust an unofficial server unless the official service cannot meet a verified requirement.

## Official connection

Remote server:

```text
https://mcp.klaviyo.com/mcp
```

Authentication: OAuth with dynamic client registration. The connected Klaviyo user must have Owner, Admin or Manager role.

For audit/research, prefer a custom connector URL with writes disabled:

```text
https://mcp.klaviyo.com/mcp?read-only=true&disable-tools-with-user-generated-content=true&core-tools-only=true
```

Official docs:

- https://developers.klaviyo.com/en/docs/klaviyo_mcp_server
- https://developers.klaviyo.com/en/docs/connect_to_the_klaviyo_mcp_server
- https://developers.klaviyo.com/en/docs/klaviyo_mcp_server_available_tools

## Architecture

The agent/client connects to both servers:

```text
Shopify data / merchant inputs
        ↓
Retention audit and approved plan
        ├── Joy MCP      → programs, tiers, referral, widget
        └── Klaviyo MCP  → segments, flows, templates, reporting
```

Joy MCP should not call Klaviyo MCP server-to-server. The client orchestrates both and keeps one approval record.

## Read phase

Use read-only mode to discover:

- Existing segments: `get_segments`, `get_segment`
- Existing flows: `get_flows`, `get_flow`, `get_flows_triggered_by_segment`
- Segment size/trend: `query_segment_values`, `query_segment_series`
- Metrics and flow performance: `get_flow_report`
- Existing profile properties and event names through the applicable profile/metric tools

Verify the exact Joy-synced property names in the target account. Expected concepts may include points balance, membership status, VIP tier, referral link and birthday, but names must not be guessed.

## Plan phase

Before write access, return a table for every proposed segment and flow:

| Object | Exact definition/trigger | Count | Exit rule | Messages/actions | Offer | Metric |
|---|---|---:|---|---|---|---|

Required segment candidates:

- First-time buyers
- Second purchase due
- Active repeaters
- Subscription candidates
- VIP candidates
- At-risk
- Lapsed
- Advocates/referrers
- High reward balance with no recent redemption

Do not create all segments blindly. Keep only those supported by available properties and the approved retention architecture.

## Approval gate — Klaviyo writes

Ask the user to approve:

- Segment definitions
- Flow triggers and exit rules
- Message count/timing
- Incentives and expiry
- Suppression/frequency rules
- Draft-only status

Klaviyo write tools may not offer a dry-run. Treat the rendered plan as the dry-run. Never call a create/update tool before approval.

## Write phase

After approval and after reconnecting without `read-only=true`:

1. Re-list segments/flows to prevent duplicates.
2. Create one segment at a time with `create_segment`.
3. Read it back with `get_segment` and query its membership count.
4. Create one flow at a time with `create_flow`.
5. Keep each flow draft/inactive when the tool/API supports status control.
6. Read back trigger, filters, actions and status.
7. Create/update templates only after content approval.
8. Do not activate a flow, send a campaign or create customer-facing communications without a separate explicit approval.

Relevant official tools include:

- `create_segment`, `update_segment`, `delete_segment`
- `query_segment_values`, `query_segment_series`
- `create_flow`, `update_flow`, `delete_flow`
- `get_flows_triggered_by_segment`
- `create_email_template`, `create_dnd_email_template`, template update tools
- Campaign tools including `send_campaign`

`send_campaign` is always a separate destructive action and is outside the retention-build approval.

## Recommended lifecycle build order

1. First-order education
2. Second-purchase-due flow around the observed reorder window
3. Reward/balance education
4. Subscription-candidate education
5. At-risk flow at about 1.5× personal/category cadence
6. Lapsed win-back at 2–3× cadence
7. VIP/tier progress
8. Referral/advocacy ask after a verified positive signal

Avoid overlapping incentives. Exclude customers already receiving a stronger subscription/referral/reward offer when appropriate.

## Cross-system consistency

Before launch verify:

- Joy program economics match Klaviyo offer copy.
- Point/currency and tier names match exactly.
- Referral qualification matches both systems.
- Expiry dates and reminder timing are consistent.
- Subscription customers are included/excluded as designed.
- Segment filters use real synced properties.
- Flow status remains draft until approved.

## Completion report

Return:

- Klaviyo account/company
- Read-only or write-enabled connection
- Existing objects reused
- Segments created and verified counts
- Flows created and status
- Templates created/updated
- Objects not created and why
- Activation/send status
- Remaining approvals
