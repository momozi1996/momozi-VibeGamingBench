"""MockAdapter: 用参考实现（demo_solution）快速联调 harness。"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Optional

from .adapters import BaseAdapter


class MockAdapter(BaseAdapter):
    name = "mock"

    def __init__(self, reference_dir: Optional[Path]):
        self.reference_dir = Path(reference_dir) if reference_dir else None

    def generate(self, workspace: Path, prompt: str, round_idx: int) -> dict:
        if not self.reference_dir or not self.reference_dir.exists():
            return {"ok": False, "agent": "mock", "stderr": "no reference dir"}
        # 产物根：优先 product/，否则 workspace
        target = workspace / "product"
        target.mkdir(parents=True, exist_ok=True)
        copied = []
        for item in sorted(self.reference_dir.iterdir()):
            if item.is_file() and not item.name.startswith("_"):
                shutil.copy(item, target / item.name)
                copied.append(item.name)
        return {"ok": True, "agent": "mock", "stdout": "copied " + ", ".join(copied)}
