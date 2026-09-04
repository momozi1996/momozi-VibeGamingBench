#!/usr/bin/env python3
"""Upgrade existing prompts with a consistent Vibe Gaming quality bar.

The original gameplay brief remains byte-for-byte intact before the inserted
section. Only the presentation/engineering contract is augmented, then the
same prompt is written to ``rounds[0].spec`` to preserve the native task
contract.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
TASKS_ROOT = ROOT / "bench" / "tasks"
MARKERS = (
    "## Vibe Gaming Quality Bar",
    "## Vibe Gaming Implementation Requirements",
    "## Vibe Gaming 实现要求",
)


def quality_bar(language: str) -> str:
    if language == "zh":
        return """\
## Vibe Gaming Quality Bar

本题的玩法、逻辑和验收锚点优先于下面的表达规范。不要重写或删减上面的核心
机制；这些要求用于把同一玩法稳定地落成一个可玩的 Vibe Gaming 垂直切片。

- **先玩后美化**：先保证开始、核心输入、状态变化、成功/失败和重玩闭环，再做视觉与动效。
- **技术栈按玩法选最小充分方案**：
  - 2D 规则游戏优先 `HTML5 Canvas 2D + Vanilla JS`；
  - 面板、卡牌、对话和菜单密集时可用 `DOM + CSS + Vanilla JS`；
  - 图标、线稿和几何动画可用 `纯 SVG + CSS 动画 + Vanilla JS`；
  - 连续碰撞、镜头、粒子或街机物理可用 `PhaserJS`；
  - 3D 或空间镜头可用 `Three.js + WebGL`；
  - 只有确实需要 GPU 大规模并行或自定义 GPU 管线时才用原生 `WebGPU`；
  - 可以混合 Canvas、DOM、CSS、SVG，但必须明确每层职责，禁止为了“技术炫技”增加无关复杂度。
- **规则层独立**：`game_logic.js` 保存唯一真相，暴露 `createGame(opts)` 和
  `advance(game, input, dt)`；渲染层只读取状态并呈现，不能偷偷维护第二套规则。
- **每帧可解释**：输入要映射到明确动作，动作要产生可观察状态变化；无效输入、
  边界条件、资源耗尽、受伤、胜利和失败都要有反馈。
- **Vibe 不是装饰**：至少使用两种反馈通道（动画、位移、缩放、粒子、声音、
  HUD 或镜头）表达关键动作；反馈不能遮挡目标或破坏可读性。
- **移动端优先**：关键点击目标至少 44×44 CSS px，支持触摸和鼠标，不能依赖 hover；
  390×844、360×800、430×932 和 1280×800 不得横向滚动或出现控件重叠。
- **确定性与测试**：随机内容使用 seed；至少验证核心规则、胜负条件、重开/恢复、
  输入边界和一个异常状态；不要用截图存在或文字出现冒充功能完成。
- **原创与合规**：使用原创名称、角色、图形、音效和关卡，或明确许可的素材；
  不复制任何原作商标、角色、文本、美术、音乐、关卡数据或代码。

完成后报告：实际文件路径、启动命令、测试命令与结果、关键截图、已知限制、
技术栈取舍和原创资产来源。
"""
    return """\
## Vibe Gaming Quality Bar

The gameplay, logic, and acceptance anchors above take priority over this
presentation contract. Do not rewrite or remove the core mechanics above; use
these rules to turn the same brief into a playable Vibe Gaming vertical slice.

- **Play first, polish second:** establish start, core input, state changes,
  success/failure, and replay before adding visual polish or effects.
- **Choose the smallest sufficient stack**:
  - `HTML5 Canvas 2D + Vanilla JS` for 2D rule-driven games;
  - `DOM + CSS + Vanilla JS` for card, dialogue, menu, and information-heavy games;
  - `pure SVG + CSS animation + Vanilla JS` for icons, diagrams, and geometric motion;
  - `PhaserJS` for continuous collision, cameras, particles, or arcade physics;
  - `Three.js + WebGL` for 3D or spatial camera experiences;
  - native `WebGPU` only when large-scale GPU parallelism or a custom GPU pipeline is genuinely required;
  - Canvas, DOM, CSS, and SVG may be mixed when each layer has a clear responsibility.
    Do not add complexity for technology spectacle.
- **Keep rules independent:** `game_logic.js` is the single source of truth and
  exposes `createGame(opts)` and `advance(game, input, dt)`. Rendering reads state;
  it must not maintain a second hidden rules system.
- **Make every frame explainable:** inputs map to explicit actions, actions
  produce observable state changes, and invalid input, edge cases, resource
  depletion, damage, victory, and failure are visible.
- **Vibe is not decoration:** use at least two feedback channels (animation,
  motion, scale, particles, audio, HUD, or camera) for important actions without
  obscuring the goal or reducing readability.
- **Mobile first:** pointer targets are at least 44×44 CSS px, touch and mouse
  both work, hover is never required, and 390×844, 360×800, 430×932, and
  1280×800 have no horizontal scrolling or overlapping controls.
- **Determinism and tests:** seed random content; verify the core rule, outcome
  conditions, restart/restoration, input boundaries, and at least one error state.
  Do not treat a screenshot or visible label as proof of functionality.
- **Originality and compliance:** use original names, characters, graphics,
  audio, and levels, or explicitly licensed assets. Do not copy trademarks,
  characters, text, artwork, music, level data, or source code.

Finish by reporting actual file paths, launch and test commands/results, key
screenshots, known limitations, stack tradeoffs, and original-asset provenance.
"""


def upgrade_task(task_dir: Path, write: bool) -> bool:
    yaml_files = list(task_dir.glob("*.task.yaml"))
    if len(yaml_files) != 1:
        raise ValueError(f"{task_dir}: expected exactly one task YAML")
    yaml_path = yaml_files[0]
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    language = raw.get("language", "en")
    prompt_path = task_dir / "prompt.md"
    prompt = prompt_path.read_text(encoding="utf-8").rstrip()
    if any(marker in prompt for marker in MARKERS):
        return False
    marker = "## HTML Submission Format"
    if marker not in prompt:
        marker = "## HTML 提交格式"
    section = quality_bar(language).strip()
    if marker in prompt:
        upgraded = prompt.replace(marker, f"{section}\n\n{marker}", 1)
    else:
        upgraded = f"{prompt}\n\n{section}"
    raw["rounds"][0]["spec"] = upgraded
    if write:
        prompt_path.write_text(f"{upgraded}\n", encoding="utf-8")
        yaml_path.write_text(
            yaml.safe_dump(
                raw,
                allow_unicode=True,
                sort_keys=False,
                width=1000,
                default_flow_style=False,
            ),
            encoding="utf-8",
        )
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks-root", type=Path, default=TASKS_ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    paths = sorted(path for path in args.tasks_root.glob("mz_*") if path.is_dir())
    changed = sum(upgrade_task(path, args.write) for path in paths)
    print(f"{'upgraded' if args.write else 'would upgrade'} {changed}/{len(paths)} task prompts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
