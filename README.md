# momozi-3A-GamegenBench

一道题 = 一句话需求 + 12 页任务书 + 14 条三档锚点 rubric + 4 项 HTML 静态门控。
度量 AI 造游戏的能力：**让 agent 造出的游戏从零开始「能玩」，并在连续修改中守住已经做好的玩法。**

## 目录

```
momozi-3A-GamegenBench/
├── momozi/                # 评测引擎 (runner / judge / leaderboard)
│   ├── run.py             # 一题跑一轮，出三分 B/S/P + 回归矩阵
│   ├── judge.py           # rubric judge (claude / codex 盲评)
│   ├── leaderboard.py     # 榜单聚合
│   └── task.py            # *.task.yaml 加载
├── bench/                 # 公共资产
│   ├── tasks/             # 题目池（140 题 × 4 维锚点 rubric）
│   ├── rubrics/           # 维度锚点细则
│   └── tests/             # HTML 静态门控 / 行为套件
├── profiles.yaml          # agent 适配 claude / codex
├── scripts/               # 门禁 / 辅助
│   ├── validate_pool.py   # 全量 mz 题的 HTML 门控 140/140
│   ├── run_opus5.py       # opus5 headless 实跑示例
│   └── convert_gc_to_html.py
├── LICENSE
└── README.md
```

## 环境

```bash
brew install node@25       # 或 nvm
pip install -r requirements.txt
claude --version           # v2.1+
```

## 30 秒跑一趟

```bash
# 门禁：140 题 HTML 静态合规全过
python3 scripts/validate_pool.py --only-gc --workers 16

# 拿 opus5 打一场
python3 -m momozi run bench/tasks/mz_sports-fishing-tournament/mz_sports-fishing-tournament.task.yaml --agent claude

# 生成榜单
python3 -m momozi leaderboard --out leaderboard.json
```

## 三维评分公式

```
score = BUILD · (0.15mean(M) + 0.35mean(D) + 0.15mean(V) + 0.35mean(A))
```

`BUILD = 1` 当 HTML 4 项门控通过 (index.html / game_logic.js / canvas_or_webgl / no_external_heavy_refs)。

## 提交流程

1. 把 `runs/*.json` + 产物索引 `product/` tar 成 `submissions/<team>__<agent>__<task>.tar.gz`
2. 评审侧重跑 `python3 -m momozi run <task> --agent <agent>` 复算
3. 榜单由 `momozi leaderboard` 自动聚合

## 维度锚点见

`bench/rubrics/mz_*.rubric.md`（M/D/V/A 各 0/0.5/1 三档锚点）。

## 授权

BSD-2.
