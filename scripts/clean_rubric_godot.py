"""清洗 rubric.original.json 里的 Godot 词：'Godot widgets' / 'Godot grey' 都改成
'default widgets' / 'plain grey'，避免 public 出现原 BMK 痕迹。"""
from __future__ import annotations

from pathlib import Path

LIT_REPL = {
    'Godot widgets': 'default widgets',
    'Godot grey': 'plain grey',
    'Godot 默认': '默认',
    'Godot': 'HTML 引擎',
    'godot': 'html 引擎',
    '/workspace/game/': './',
}


def main() -> int:
    root = Path('bench/tasks')
    n = 0
    for f in sorted(root.glob('mz_*/rubric.original.json')):
        t = f.read_text(encoding='utf-8')
        o = t
        for pat, rep in LIT_REPL.items():
            t = t.replace(pat, rep)
        if t != o:
            f.write_text(t, encoding='utf-8')
            n += 1
    print(f'cleaned {n} of 140 (rubric.original.json)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
