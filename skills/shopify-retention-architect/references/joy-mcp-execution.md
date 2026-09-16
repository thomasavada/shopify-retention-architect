# Joy MCP execution

Use only when Joy MCP is connected and the target shop is confirmed.

## Available configuration tools

- `joy_configure_shop_settings`
- `joy_configure_earning_program`
- `joy_configure_redemption_program`
- `joy_configure_tier`
- `joy_configure_tier_settings`
- `joy_configure_tier_reward`
- `joy_configure_tier_perks`
- `joy_configure_referral_program`
- `joy_configure_referral_widget`
- `joy_scan_brand_design`
- `joy_configure_widget_draft`
- `joy_get_widget_fields`
- `joy_set_widget_fields`
- `joy_upload_image`
- `joy_check_theme_setup`

Tool availability can differ by server build and environment. List tools first; do not assume this inventory is current.

## Program build order

1. Read current overview, programs, tiers, referral and widget settings.
2. Map approved strategy to the smallest set of changes.
3. Create/update shop settings and program identity.
4. Configure earning programs.
5. Configure redemption programs.
6. Configure tiers, rewards, perks and tier settings.
7. Configure referral program and referral widget.
8. Configure widget draft.
9. Verify every write.
10. Publish/live-write only after separate approval.

## Dry-run protocol

For every configuration tool:

1. Call without `apply:true`.
2. Capture current → proposed values.
3. Explain storefront/customer impact.
4. Wait for explicit approval.
5. Call with `apply:true`.
6. Read the object back.
7. If any requested field is unconfirmed, stop.

Apply one write at a time. Never batch multiple unreviewed writes.

## Widget protocol

1. Scan the brand with `joy_scan_brand_design`.
2. Present detected colors/fonts/button style as evidence, not visual proof.
3. Discover allowed fields with `joy_get_widget_fields`.
4. Use draft target by default.
5. Upload only merchant-approved imagery.
6. Read back field values.
7. Ask for a visual review in Joy admin or storefront preview.
8. Require a second approval before any live target.

`joy_configure_widget_draft` can write live only with explicit `target: 'live'`. A live save changes the storefront immediately; the MCP tool has no publish/undo step.

## Account/header protocol

### Existing account icon

Use widget fields:

- `links.replaceAccountLink = true`
- Optional `links.accountLinkSelector` when the theme's account link is not detected

This intercepts an existing account entry point and opens the Joy drawer.

### Separate rewards icon

MCP widget fields do not create a new theme-header icon. A new rewards icon requires:

- Theme/app-block implementation, or
- Shopify CLI theme code change

Inspect the target theme and request explicit approval before editing it.

### Customer account page

Enabling/configuring Joy's Customer Account Loyalty Hub may require adding the extension in Shopify's customer account editor. Do not claim MCP alone enabled it unless a corresponding tool exists and read-back confirms it.

## Completion report

Return:

- Shop/environment
- Approved plan
- Dry-run diffs
- Applied tools and arguments (redact secrets)
- Read-back verification
- Draft/live target
- Account/header changes
- Manual steps remaining
- Rollback limitations
