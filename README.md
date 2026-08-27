# momozi-3A-GamegenBench

> **三维评分 · 多轮增量 · 行为回归验证 的 3A 游戏生成 benchmark**
> 度量 AI coding agent「创造类任务」的能力：**让 agent 造出的游戏从零开始「能玩」，并在连续修改中守住已经做好的玩法。**
>
> 一道题 = 一段自然语言需求 + 隐藏评分锚点。**140 道生产级真题**（含 12 页任务书 + 隐藏 M*/D*/V*/A* 共 ~14 条评分锚点 + HTML 4 项静态门控）。判分沿用题源 BMK 三档制（0/0.5/1）与公式 `score = BUILD · (0.15mean(M) + 0.35mean(D) + 0.15mean(V) + 0.35mean(A))`。

[![CI](https://github.com/momozi/momozi-3A-GamegenBench/actions/workflows/ci.yml/badge.svg)](https://github.com/momozi/momozi-3A-GamegenBench/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/license-BSD--2-blue)

---

## 30 秒看版本

```bash
git clone https://github.com/momozi/momozi-3A-GamegenBench && cd momozi-3A-GamegenBench
pip install -r requirements.txt
npm i -g node@25     # 或 nvm（Node ≥ 20）

# smoke（mock）：走完整 harness，参考实现全过 = 题目可信
python3 scripts/smoke.sh

# 任一真 agent 跑一道真题（claude code）
python3 -m momozi run bench/tasks/mz_cardgame-autobattler/mz_cardgame-autobattler.task.yaml \
    --agent claude

# 门禁：140 道题的 HTML 静态合规全部过
python3 scripts/validate_pool.py --workers 16 --only-gc

# 生成 leaderboard
python3 -m momozi leaderboard --out leaderboard.json
```

---

## 目录 & 架构

```
momozi-3A-GamegenBench/
├─ README.md                     ← 你在这
├─ DESIGN.md                     方法论深版（论文级写法）
├─ LICENSE (BSD-2)
├─ requirements.txt
├─ profiles.yaml                 agent adapter 配置（首选 claude code / codex）
│
├─ momozi/                       harness 包（评测器本体）
│  ├─ __init__.py
│  ├─ __main__.py                CLI 入口
│  ├─ cli.py                     run / leaderboard 子命令
│  ├─ task.py                    task.yaml → Task（含多轮 rounds）
│  ├─ run.py                     逐轮执行 · 打分 · 回归矩阵 · 落盘
│  ├─ verifiers.py               StaticChecker + BehaviorSuite（node）
│  ├─ adapters.py                claude-code / codex / 自定义 CLI 适配层
│  ├─ mock_adapter.py            mock：直接复刻参考实现联调（0 token）
│  ├─ judge.py                   rubric judge 盲评（claude -p / codex exec）
│  ├─ leaderboard.py             榜单聚合 + 导出 markdown
│  └─ verify.py                  提交包复评（防止虚报）
│
├─ bench/                        公共资产
│  ├─ tasks/                     主榜单题目池（140 道 mz_*）
│  │  └─ mz_<name>/             GameBench 140 题（prompt.md + rubric.original.json + rubric.mapping.json + beh_html.mjs）
│  ├─ tests/beh_*.mjs            家族行为套件（deterministic golden suite）
│  ├─ rubrics/                   逐题 rubric（人可读）
│  ├─ references/<family>/       每题参考实现（mock 复刻）
│  └─ POOL_AUDIT.md              140 gc 题一次性门禁结果
│
├─ scripts/
│  ├─ validate_pool.py           全题门禁：140 gc 题全过 HTML 门控
│  ├─ import_bundle.py        从 题源 BMK 原生 bundle 导入 140 题
│  ├─ convert_mz_to_html.py      把原 bundle 从 Godot 2D 转成 HTML/three.js 单页
│  ├─ import_bundle.py        拉入题源 BMK rubric
│  ├─ gen_site.sh                生成展示站 site/data/
│  └─ smoke.sh                   mock 端到端冒烟
│
└─ site/                         低门槛展示站（GitHub Pages）
   ├─ index.html                 playground + leaderboard + findings + 案例
   ├─ data/leaderboard.json      自动聚合
   └─ data/playables.json        可玩游戏索引（来自 runs/ + references/）
```

---

## 题目分布

### v0.1 主榜单（GC，真实生产级题）

**140 道 Godot 2D 游戏题**，题目改编自题源 BMK 家族化模板。每道包含:

- 一份 12 页《开发任务书》(`prompt.md`)，含核心愿景、7 条玩家体验、场景定义、资产清单；
- 一份**隐藏 grading rubric**（`rubric.original.json`，含 M*/D*/V*/A* 共 ~14 条 requirement，每条一段三档锚点）；
- 一份 `beh_build.mjs` build gate（`godot --headless --path <game> --quit-after 5` 0 fatal → BUILD=1）；
- 原 BMK 的 judge prompt 结构（SYSTEM + USER + rubric 全量），见 `momozi/judge_gc.py`。

| 家族 | 数量 | 族样本 |
|---|---:|---|
| platformer 平台 | 19 | `knight-quest` / `momentum-lab` |
| strategy 策略 | 17 | `spell-tactics` / `siege-engineer` |
| tycoon 经营 | 16 | `potion-shop` / `pirate-port` |
| openworld 开放世界 | 15 | `airship-trader` / `ghost` |
| roguelike | 14 | `action-void-harvest` / `garden-crawl` |
| visualnovel 视觉小说 | 11 | `spy-handler` / `courtroom-clue-trial` |
| puzzle 解谜 | 8 | `sokoban-dungeon` / `circuit-wizard` |
| shooter 射击 | 7 | — |
| simulation 模拟经营 | 6 | `kitchen-rush` / `border-check` |
| cardgame 卡牌 | 5 | `poker-roguelike` / `spire-descent` |
| horror 恐怖 | 5 | `dollhouse` / `lighthouse` |
| rhythm 音游 | 5 | `beat-dungeon` / `note-highway` |
| idle 放置 | 4 | `ant-empire` / `factory-planet` |
| racing 竞速 | 4 | `rocket-trials` |
| sports 运动 | 4 | `fishing-tournament` |
| **合计** | **140** | — |

### 赛道规划

| 赛道 | 观测 | 状态 |
|---|---|---|
| **01 GameGen** | 单轮造 | ✅ v0.1 全量 |
| **02 GameFix** | 单轮改（保持既有行为） | 🟡 harness 已支持，独立题库 v0.3 |
| **03 GameOpt** | 多轮优化逼近目标 | 🟡 harness 已支持，独立题库 v0.3 |

---

## 打分标准（三维）

一次跑的总分

```
Total = 0.55·B + 0.20·S + 0.25·P         （P 缺失时其他两维按 0.75 归一）
```

| 维度 | 权重 | 定义 | 当轮靠什么保证 |
|---|---:|---|---|
| **B（Behavior 行为）** | **0.55** | 末轮 golden 行为集合通过率 × (1 − 0.2 × 回归率) | 确定性 node 套件，不调用 LLM judge |
| **S（Structure 结构）** | **0.20** | 静态检查加权通过率（required_file / contains / line_budget） | 缺文件、超预算、缺引用直接扣 |
| **P（Presentation 呈现）** | **0.25** | 4 维 rubric 加权中位（completeness/richness/player_exp/visual，各 0–5） | judge adapter（claude / codex）盲评 |

### 回归率（核心机制）

- `regression_rate` = 前一轮 PASS、本轮 FAIL 的关键行为数 ÷ 本轮 PASS 的总数
- **乘法硬扣**：改着改着玩法崩了，总分按比例缩水（这就是"multi-round regression"的核心）
- **3D 落盘**：每跑的 `runs/<ts>/<task>.<agent>.json` 里都带 `regressions: [...]`、`newly_passing: [...]`、per-round 行为明细

### 维度落盘

- `scores.B / scores.S / scores.P` 本维原始分
- `scores.dimensions` 4 维 rubric 原始分（0-5）
- `scores.total` 最终分
- `scores.weights` 权重明示

### 特殊情况的透明化处理

以下情形不会偷偷灌水，一律按界写扣：

- **无 index.html / 缺 game_logic.js → 静态分 0**
- **0 个行为过 → B=0，且不分维度**
- **judge 拉闸 → judge 出 `P=null`**，并在总分里"动态归一"，不会偷懒算 0

---

## 常用工作流

### 1) 联调（不花 token）
`mock` adapter 直接把 `bench/references/<family>` 的参考实现复制到 `product/`，跑通整条 chain：

```bash
python3 -m momozi run bench/tasks/mz_cardgame-autobattler/mz_cardgame-autobattler.task.yaml --agent mock
```

### 2) 真实 agent 跑（claude code）
仓库自带的 `profiles.yaml` 已写好两类默认 adapter：

```yaml
# profiles.yaml
claude:
  label: claude-code
  argv: [claude, -p, $PROMPT_FILE]
  write_args: [--permission-mode, acceptEdits, --allowedTools, "Edit,Write"]
  timeout: 1800

codex:
  label: codex
  argv: [codex, exec, --sandbox, workspace-write, --skip-git-repo-check, $PROMPT_FILE]
  timeout: 1800
```

跑：

```bash
python3 -m momozi run <task.yaml> --agent claude --rounds R1,R2
```

Adapter 支持的占位符：`$PROMPT_FILE`（prompt 已落盘的文件）、`$PROMPT`（直接 inline）、`$WORKDIR`（本轮工作目录）。任何 CLI 只需这 3 个占位符，就能接入 `momozi`。

### 3) 门禁：140 题全部过 HTML 静态门控

```bash
python3 scripts/validate_pool.py --workers 16 --only-gc
# 输出 bench/POOL_AUDIT.md：
# 总题数 140 · 通过 140 · 失败 0
```

### 4) 提交 leaderboard（3 种）

**(a) 仓库内**：直接 `python3 -m momozi leaderboard --out leaderboard.json`

**(b) 外部提交包（评审方复算）**
把 `runs/<ts>/xxx.<agent>.json` tar 成 `submissions/<team>__<agent>__<task>.tar.gz`（里面就一个 `product/`），
评审方用 `python3 -m momozi.verify submissions/<name>.json submissions/<name>.tar.gz` 重新跑 B/S，不一致按验算排名。

**(c) CI**：推 `.github/workflows/ci.yml` 让 GitHub Actions 自动产出 leaderboard artifact

### 5) 展示站（GitHub Pages）

```bash
bash scripts/gen_site.sh      # 从 runs/ 与 references/ 收集可玩游戏副本
python3 -m http.server        # 打开 127.0.0.1:8000/site/index.html
```

把仓库推到 GitHub，在 Settings → Pages 里 Source 选 "GitHub Actions"，push 到 main 后自动发。

---

## 环境要求

- **必装**：Node ≥ 20（跑 behavior 套件）+ Python ≥ 3.9 + PyYAML
- **adapter**：默认内置 `claude` / `codex` 两个 profile；mock 联调不需要任何真实 agent
- **network**：none（离网沙箱）。mock 优先跑通 harness 时不需要，跑真实 agent 需要被隔离在 sandbox 内（`--sandbox workspace-write`）
- **可选**：无需 Godot UE5 也能烤 mock 行为分；要跑 `mz_*` Godot 题再到 Godot 4 本地 + `godot --headless --quit-after 5`（原 BMK 的 BUILD gate）——Momozi 会接 `beh_build.mjs`。

---

## Leaderboard 长这样

| # | 排位 | Agent | 总分 | B（行为） | S（结构） | P（呈现） | 回归率 |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | 🏆 | 参考实现（过样板） | 1.0000 | 1.00 | 1.00 | 1.00 | 0 |
| 2 | 🥈 | claude-code（claude opus） | 0.4157 | 0.60 | 0.43 | null | 0 |
| 3 | 🥉 | codex | 0.0000 | 0.00 | 0.00 | null | 1 |

> 成绩持续刷新：`site/data/leaderboard.json`。

---

## 已知边界（honest disclosure）

- `mock` adapter 的参考实现**本身**就是地板：它能过所有行为、静态，但**不代表真 agent 不能更优**。mock 只用于门禁 harness。
- `mz_*` 的 Godot BUILD gate（`godot --headless --quit-after 5`）需要本地安装 Godot 4；在没装的环境里，本仓只能跑 `t####_*` 三种规则题。
- 评测**不测**模型"美术素养"，只测行为正确性、结构合规和呈现分（P 维度里视觉只占 0.20/0.25 权重）。
- 权重 0.55/0.20/0.25 是 starter set，任何题族都可以在 yaml 里覆盖 `rubric` weights。
- 回归分支题（R2+）**永远强制**前置几轮 PASS 的行为不能崩，但**没有严格反作弊**（agent 可能"改完先骗过 judge"，这需要后续加 behavior diff 引入规则）。

---

## 参与方式

- **出题**：新建 `bench/tasks/<id>/<id>.task.yaml`；参考 `bench/tasks/tg1_paddle_breakout/`。
- **改判分**：家族行为套件 `bench/tests/beh_*.mjs` + rubric 权重的 yaml。
- **自定义 agent**：`profiles.yaml` 加 adapter。
- **提 issue / PR**：发现行为套件误判、rubric 不公、adapter 不工作 → 请在 issue 里附 `runs/<ts>/xxx.<agent>.json` 日志。

---

## 引用

```bibtex
@misc{momozi-3A-GamegenBench,
  title  = {momozi-3A-GamegenBench: Multi-round Incremental Game Generation Benchmark with Behavior Regression},
  author = {momozi},
  year   = {2026},
  url    = {https://github.com/momozi/momozi-3A-GamegenBench}
}
```
