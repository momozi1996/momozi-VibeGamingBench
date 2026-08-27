"""agent 适配层：把任意 coding agent CLI 打成同一接口。

profile (profiles.yaml) 示例：
  claude:
    label: claude-code
    argv: ["claude", "-p", "$PROMPT_FILE"]
    write_args: ["--permission-mode", "acceptEdits"]
    timeout: 1800
另外提供 MockAdapter 用于联调 harness（不花 token）。
"""

from __future__ import annotations

import shutil
import subprocess
import time
from pathlib import Path
from typing import Optional

import yaml


class AdapterResult(dict):
    pass


class BaseAdapter:
    name = "base"

    def generate(self, workspace: Path, prompt: str, round_idx: int) -> dict:
        raise NotImplementedError


class MockAdapter(BaseAdapter):
    """校验 harness 本体时用：直接产出预置的参考实现。"""

    name = "mock"

    def __init__(self, reference_dir: Optional[Path] = None):
        self.reference_dir = reference_dir

    def generate(self, workspace: Path, prompt: str, round_idx: int) -> dict:
        if self.reference_dir and self.reference_dir.exists():
            for artifact in self.reference_dir.glob("*"):
                if artifact.is_file() and not artifact.name.startswith("_"):
                    shutil.copy(artifact, workspace / artifact.name)
        return {"ok": True, "stdout": "[mock] reference copied", "agent": "mock"}


class CliAdapter(BaseAdapter):
    """把任意 CLI agent 套成统一接口：prompt 写成 _prompt.md，argv 里的 $PROMPT 由
    agent 自己读文件（profiles.yaml 用 '$PROMPT_FILE' 占位）。"""

    def __init__(self, argv: list, write_args: list = None, timeout: int = 1800, label="cli"):
        self.argv = argv
        self.write_args = write_args or []
        self.timeout = timeout
        self.name = label

    def generate(self, workspace: Path, prompt: str, round_idx: int) -> dict:
        prompt_file = workspace / "_prompt.md"
        prompt_file.write_text(prompt, encoding="utf-8")
        # 占位替换：$PROMPT_FILE / $PROMPT / $WORKDIR
        def subst(arg: str) -> str:
            return (arg.replace("$PROMPT_FILE", str(prompt_file))
                       .replace("$PROMPT", prompt)
                       .replace("$WORKDIR", str(workspace)))
        argv = [subst(a) for a in self.argv] + [subst(a) for a in self.write_args]
        t0 = time.time()
        try:
            proc = subprocess.run(
                argv, cwd=workspace, capture_output=True, text=True,
                timeout=self.timeout,
            )
            return {
                "ok": proc.returncode == 0,
                "returncode": proc.returncode,
                "stdout": proc.stdout[-4000:],
                "stderr": proc.stderr[-2000:],
                "duration_s": round(time.time() - t0, 1),
                "agent": self.name,
            }
        except subprocess.TimeoutExpired:
            return {"ok": False, "stderr": "timeout", "duration_s": self.timeout, "agent": self.name}
        except FileNotFoundError as e:
            return {"ok": False, "stderr": f"adapter cli not found: {e}", "agent": self.name}


def build_adapter(name: str, profiles: dict, reference_dir: Optional[Path] = None) -> BaseAdapter:
    if name == "mock":
        return MockAdapter(reference_dir)
    profile = profiles.get(name)
    if not profile:
        raise SystemExit(f"unknown adapter profile: {name}")
    timeout = int(profile.get("timeout", 1800))
    return CliAdapter(
        argv=profile["argv"],
        write_args=profile.get("write_args", []),
        timeout=timeout,
        label=name,
    )


def load_profiles(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
