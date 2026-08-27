"""把 140 道 GameCraft prompt.md 从 Godot 2D 规范转成 HTML/three.js 单文件规范。

保留的段落（评分锚点所在，不动）:
  Cardgame xxx / Core Vision / What the Player Experiences / 中文标题 / ... / 轨迹文件格式之前的主干

替换的段落（头一级 "##" 起始，到下一个同级/更高级 "##" 之前）:
  - Assets        → HTML 提交格式 或 中文版提交格式
  - Project layout→ 删（已并入 Assets 的契约）
  - Demos         → 删
  - Scenarios     → 删
  - Trace format  → 删

字面替换：Godot 2D/Godot → HTML/three.js
任务 yaml: engine: godot → engine: html；behavior 段：beh_build.mjs → beh_html.mjs
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "bench" / "tasks"

HEADER_HTML_EN = """## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server, no Godot.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Same pattern as `bench/references/tg1/game_logic.js`.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.
"""

HEADER_HTML_ZH = """## 提交格式（HTML）

交付物 **两个文件**：

- `index.html` —— 双击即开的单文件页面, 走 CDN 引入 `three.js`
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  **不允许** `npm install` / 构建工具 / Python 服务器 / Godot。普通笔记本 3 秒内必须渲染出来。
- `game_logic.js` —— 纯逻辑层 `createGame(opts)` / `advance(game, input, dt)`,
  由 `index.html` import。规范参考 `bench/references/tg1/game_logic.js`。

约束：
- 全部资产程序化生成(颜色、立方体、球体), 不运行时外取图像/音频。
- 键盘输入 `WASD + 空格 + Enter + ESC`。
- `index.html` 不发生运行时 `fetch/XHR`; 除 three.js 外不引入别的 CDN。
- 体量：`game_logic.js ≤ 220 行`, `index.html ≤ 120 KB`。
"""

REPLACE_SECTIONS = {
    "Assets": HEADER_HTML_EN,
    "资产": HEADER_HTML_ZH,
}
DELETE_SECTIONS = {
    "Project layout", "Demos", "Scenarios", "Trace file format",
    "项目结构", "演示", "场景（Scenarios）", "轨迹文件格式",
}


def convert_one(path: Path) -> tuple[int, int, bool]:
    txt = path.read_text(encoding="utf-8")
    n_replaced = n_deleted = 0
    for header, body in REPLACE_SECTIONS.items():
        pat = re.compile(r"(?ms)^#{1,3}\s+" + re.escape(header) + r"\s*$.*?(?=^#{1,3}\s|\Z)")
        txt, n = pat.subn(body.strip() + "\n\n", txt)
        n_replaced += n
    for header in DELETE_SECTIONS:
        pat = re.compile(r"(?ms)^#{1,3}\s+" + re.escape(header) + r"\s*$.*?(?=^#{1,3}\s|\Z)")
        txt, n = pat.subn("", txt)
        n_deleted += n
    # 首行替换:"Build a X in Godot 4 at `/workspace/game/`" 一句话需求那段
    txt = re.sub(r"\bin\s+Godot\s*2?D?\s*4?\s+at\s+`/workspace/game/`\s*\.?",
                 "as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).", txt)
    txt = re.sub(r"\bin\s+Godot\s*4?\s*\.?", "as a self-contained HTML page.", txt)
    txt = re.sub(r"\bHTML/three\.js\b", "HTML/three.js", txt)  # idempotent
    path.write_text(txt, encoding="utf-8")
    return n_replaced, n_deleted, True


def convert_yaml(path: Path):
    txt = path.read_text(encoding="utf-8")
    txt = re.sub(r"engine:\s*godot", "engine: html", txt)
    txt = re.sub(r"script:\s*beh_build\.mjs", "script: beh_html.mjs", txt)
    path.write_text(txt, encoding="utf-8")


def main():
    total_r = total_d = 0
    for d in sorted(TASKS.glob("gc_*/")):
        pmd = d / "prompt.md"
        if pmd.exists():
            r, dd, _ = convert_one(pmd)
            total_r += r; total_d += dd
        for y in d.glob("*.task.yaml"):
            convert_yaml(y)
    print(f"converted: replaced {total_r} HTML-format sections, deleted {total_d} Godot-specific sections")


if __name__ == "__main__":
    main()
