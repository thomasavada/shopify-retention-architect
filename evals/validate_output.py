#!/usr/bin/env python3
from pathlib import Path
import re

p = Path(__file__).with_name('example-output.md')
assert p.exists(), 'evals/example-output.md was not created'
s = p.read_text()
required = [
    'Executive verdict',
    'Retention evidence',
    'Economics',
    'Customer segments',
    'Program blueprint',
    'Widget',
    'Approval',
    'MCP_HANDOFF',
    '40%',
    '$50',
    'apply',
    'draft',
    'links.replaceAccountLink',
    'Klaviyo MCP',
    'read-only',
]
for item in required:
    assert item.lower() in s.lower(), f'missing: {item}'
assert re.search(r'"apply"\s*:\s*false', s), 'MCP handoff must be dry-run'
assert 'incremental revenue' not in s.lower() or 'not incremental revenue' in s.lower()
print('output validation OK')
