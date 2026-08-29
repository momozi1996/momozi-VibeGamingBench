"""Task loader: 把 *.task.yaml 解析为 Task.

Task 结构见 bench/tasks/README.md:
  - id / title / family / difficulty
  - static[]    静态检查（required_file/contains/max_size/no_*）
  - behavior{script} 行为套件（node）
  - rubric[]    主观评审维度
  - rounds[]    多轮增量 spec（关键：R2+ 常规实现要「保证 R1 行为不破」）
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import yaml


@dataclass
class RoundSpec:
    name: str
    spec: str


@dataclass
class Task:
    id: str
    title: str
    family: str
    difficulty: str
    engine: str
    language: str = ""
    base_task_id: str = ""
    provenance: dict = field(default_factory=dict)
    rounds: list = field(default_factory=list)
    static: list = field(default_factory=list)
    behavior: dict = field(default_factory=dict)
    rubric: list = field(default_factory=list)
    evaluation: dict = field(default_factory=dict)
    reference_dir: str = ""
    path: Path = None

    @classmethod
    def load(cls, path: Path) -> "Task":
        path = Path(path)
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError(f"{path}: task YAML must contain a mapping")
        if not raw.get("rounds"):
            raise ValueError(f"{path}: task must contain non-empty rounds[]")
        if not raw.get("id"):
            raise ValueError(f"{path}: task id is required")
        rounds = [RoundSpec(name=r["name"], spec=r["spec"].strip())
                  for r in raw["rounds"]]
        task = cls(
            id=raw["id"],
            title=raw.get("title", raw["id"]),
            family=raw.get("family", "unspecified"),
            difficulty=raw.get("difficulty", "medium"),
            engine=raw.get("engine", "three.js"),
            language=raw.get("language", "") or "",
            base_task_id=raw.get("base_task_id", raw["id"]) or raw["id"],
            provenance=raw.get("provenance", {}) or {},
            rounds=rounds,
            static=raw.get("static", []) or [],
            behavior=raw.get("behavior", {}) or {},
            rubric=raw.get("rubric", []) or [],
            evaluation=raw.get("evaluation", {}) or {},
            reference_dir=raw.get("reference_dir", "") or "",
            path=path,
        )
        if task.difficulty not in {"low", "medium", "high"}:
            raise ValueError(f"{path}: unsupported difficulty {task.difficulty!r}")
        if task.language and task.language not in {"en", "zh"}:
            raise ValueError(f"{path}: unsupported language {task.language!r}")
        return task

    def artifact_requirements(self) -> dict:
        """从 static 检查项推导必需产物路径角色。"""
        req = {"entry": "index.html", "logic": "game_logic.js"}
        for item in self.static:
            if item.get("kind") == "required_file":
                rel = item.get("path", "")
                if item.get("role") == "entry" and rel.endswith(".html"):
                    req["entry"] = rel
                elif item.get("role") == "logic" and rel.endswith(".js"):
                    req["logic"] = rel
        return req
