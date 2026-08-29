"""校验器：静态检查（文件/内容/依赖） + 行为套件（node 跑 task 自带 .mjs）。

行为套件协议（node 脚本 stdout JSON 数组）：
  [{"id": "B1", "ok": true, "detail": "..."}, ...]
脚本从 env.ARTIFACT 读产物目录；脚本 args: ARTIFACT。
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


class StaticChecker:
    """按 task.static 列表执行检查。"""
    def __init__(self, static_items: list):
        self.items = static_items or []

    def run(self, workspace: Path, req: dict) -> list:
        results = []
        files = {
            p.relative_to(workspace).as_posix(): p
            for p in workspace.rglob("*")
            if p.is_file()
        }
        for item in self.items:
            kind = item.get("kind")
            rid = item.get("id", kind)
            if kind == "required_file":
                rel = item["path"]
                want = Path(rel).as_posix()
                ok = want in files
                results.append({
                    "id": rid, "ok": ok, "weight": item.get("weight", 1.0),
                    "detail": f"file {rel} {'present' if ok else 'MISSING'}",
                })
            elif kind == "contains":
                path_field = item.get("check_in", item["path"])
                target = Path(path_field).as_posix()
                needle = item["pattern"]
                if target not in files:
                    ok = None                       # 文件缺失 → 不计分母，weight 归零
                    weight = 0.0
                else:
                    ok = needle in files[target].read_text(encoding="utf-8", errors="ignore")
                    weight = item.get("weight", 1.0)
                results.append({
                    "id": rid, "ok": ok, "weight": weight,
                    "detail": f"{path_field} contains {needle!r}: {ok}" if ok is not None
                              else f"{path_field} MISSING — contains check not covered",
                })
            elif kind == "no_external_js":
                target = Path(item.get("path", req["entry"])).as_posix()
                text = files.get(target, None)
                text = text.read_text(encoding="utf-8", errors="ignore") if text else ""
                bad_tags = re.findall(r"(https?://|src=[\"'][^\"']*cdnjs)", text)
                ok = not bad_tags
                results.append({
                    "id": rid, "ok": ok, "weight": item.get("weight", 1.0),
                    "detail": f"no external js tags: {not bad_tags}",
                })
            elif kind == "max_size_kb":
                limit = int(item["kb"])
                overs = [p.name for p in files.values() if p.stat().st_size / 1024 > limit]
                ok = not overs
                results.append({
                    "id": rid, "ok": ok, "weight": item.get("weight", 1.0),
                    "detail": f"files over {limit}KB: {overs or 'none'}",
                })
            elif kind == "line_budget":
                limit = int(item["max_lines"])
                rel = item.get("path", req["logic"])
                target = Path(rel).as_posix()
                if target in files:
                    lines = len(files[target].read_text(encoding="utf-8", errors="ignore").splitlines())
                else:
                    lines = None                      # 文件缺失 → 该检查“未覆盖”，不计分母
                ok = lines is not None and lines <= limit
                results.append({
                    "id": rid, "ok": ok if lines is not None else None,
                    "weight": item.get("weight", 0.0 if lines is None else 1.0),
                    "detail": f"{target} lines={lines} (<= {limit})" if lines is not None
                              else f"{target} MISSING — not covered",
                })
            else:
                results.append({"id": rid, "ok": None, "weight": 0.0, "detail": f"unknown static kind {kind}"})
        return results


class BehaviorSuite:
    """跑 task 自带的行为套件脚本（每任务 scripts/*.mjs）。"""
    def __init__(
        self,
        workspace: Path,
        suite_rel: str,
        timeout: int = 60,
        artifact_dir: Path | None = None,
        script_path: Path | None = None,
    ):
        self.workspace = workspace
        self.suite_rel = suite_rel
        self.timeout = timeout
        self.artifact_dir = artifact_dir or workspace
        self.script_path = script_path

    def run(self) -> list:
        script = self.script_path or (self.workspace / self.suite_rel)
        if not script.exists():
            return [{"id": "suite_exists", "ok": False, "detail": f"missing {self.suite_rel}"}]
        try:
            proc = subprocess.run(
                ["node", str(script), str(self.artifact_dir)],
                cwd=self.workspace, capture_output=True, text=True, timeout=self.timeout,
            )
            raw = proc.stdout.strip()
            if not raw:
                return [{"id": "suite_json", "ok": False, "detail": f"no JSON stdout; stderr={proc.stderr[-300:]}"}]
            data = json.loads(raw)
            if not isinstance(data, list):
                return [{"id": "suite_json", "ok": False, "detail": "JSON output must be an array"}]
            out = []
            for d in data:
                out.append({"id": d.get("id", "?"), "ok": bool(d.get("ok")), "detail": d.get("detail", "")})
            return out
        except subprocess.TimeoutExpired:
            return [{"id": "suite_timeout", "ok": False, "detail": "behavior suite timed out"}]
        except json.JSONDecodeError as e:
            return [{"id": "suite_json", "ok": False, "detail": f"invalid JSON: {e}"}]
        except OSError as e:
            return [{"id": "suite_process", "ok": False, "detail": str(e)}]
