# Freeze Audit

Status: **PASS**

- Source files checked: **5941**
- Task concepts/tasks: **711 / 1422**
- EN/ZH counts: `{'en': 711, 'zh': 711}`
- Release hash match: **True**
- Parse errors: **0**
- Syntax errors: **0**
- Broken relative links: **0**

## Freeze Warning

runs/ and workspaces/ are ignored for new files but historical files are still tracked; exclude them from a freeze archive or remove from the release index explicitly.

## Commands

```text
python3 scripts/freeze_audit.py
python3 -m unittest discover -s tests -v
bash scripts/smoke.sh
python3 scripts/validate_pool.py --only-mz --workers 8
```
