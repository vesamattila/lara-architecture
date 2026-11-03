# Repository validation

LARA v0.2 is documentation-first, so validation focuses on internal links, example behavior, structured-data syntax, and publication hygiene.

Run from the repository root:

```powershell
# Exercise the synthetic example.
python -m unittest discover -s examples/illustrative-order-import/tests -v

# Parse every source-controlled YAML file (requires PyYAML).
@'
from pathlib import Path
import yaml

for path in Path('.').rglob('*.yaml'):
    if '.git' not in path.parts:
        with path.open(encoding='utf-8') as stream:
            yaml.safe_load(stream)
        print(path)
'@ | python -

# Find relative Markdown links that point to missing local files.
@'
from pathlib import Path
import re

missing = []
for document in Path('.').rglob('*.md'):
    if '.git' in document.parts:
        continue
    text = document.read_text(encoding='utf-8')
    for target in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', text):
        target = target.split('#', 1)[0]
        if not target or '://' in target or target.startswith('mailto:'):
            continue
        if not (document.parent / target).resolve().exists():
            missing.append(f'{document}: {target}')
if missing:
    raise SystemExit('\n'.join(missing))
print('All relative Markdown links resolve.')
'@ | python -
```

Before publishing any LARA run output, review it separately for credentials, proprietary material, personal information, and source excerpts that cannot be redistributed. Passing these repository checks does not make target-repository output safe to publish.
