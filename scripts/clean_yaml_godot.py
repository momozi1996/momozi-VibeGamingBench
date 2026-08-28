"""__main__ safe: 上一轮 heredoc 屡次被 zsh 截断。直接 python -c 执行此文件。"""
from __future__ import annotations

from pathlib import Path

# Literal replaces; directly target the Godot classifier terms seen in rubric.original.json
LIT_REPL = {
    'Build a X in Godot 4 at `/workspace/game/`.': 'Build a X as self-contained HTML page (files: `index.html`, `game_logic.js`).',
    '不要出现 Godot 默认的纯灰': '演好默认纯灰',
    'No plain Godot grey': 'No plain HTML grey',
    '/workspace/game/': './',
    'godot': 'html',
    'Godot': 'HTML',
}


def main() -> int:
    root = Path('bench/tasks')
    n = 0
    for f in sorted(root.glob('mz_*/*.task.yaml')):
        t = f.read_text(encoding='utf-8')
        o = t
        for pat, rep in LIT_REPL.items():
            t = t.replace(pat, rep)
        t = t.replace('在 `/workspace/game/` 用 Godot 4 开发',
                      '用单文件 HTML 双击即开交付两个文件（`index.html`、`game_logic.js`）：开发')
        t = t.replace('**不允许** `npm install` / 构建工具 / Python 服务器 / Godot。',
                      '**不允许** `npm install` / 构建工具 / Python 服务器。')
        if t != o:
            f.write_text(t, encoding='utf-8')
            n += 1
    print(f'cleaned {n} of 140')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
