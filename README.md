# momozi-3A-GamegenBench

> **三维评分（B/P/S）· 多轮增量（R1→Rk)·行为回归验证的 3A 游戏生成 benchmark**
> 测量 LLM agent 在真实 game-engine 语义下，把"可玩的游戏"从零造出来、并守住已有玩法不崩的能力。

[![License: BSD-2](https://img.shields.io/badge/License-BSD--2-blue.svg)](LICENSE)
![version](https://img.shields.io/badge/version-0.1.0-green)

---

## TL;DR

```bash
# 1. 装运行环境
brew install node@25        # 或 nvm（Node ≥ 20）
pip install -r requirements.txt

# 2. mock 干跑（验证 harness 自己通）
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml --agent mock

# 3. 真实 agent 跑（示例：claude code）
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml \
  --agent claude --judge-agent claude

# 4. 看 leaderboard
python3 -m momozi leaderboard --out leaderboard.json
```

产物在 `runs/<ts>/<task>.<agent>.json`；leaderboard 会聚合成可复现的榜单。

---

## 1. benchmark 架构总览

```
┌──────────────────── 评测一跑 (one run) ────────────────────┐
│ ① prompt 逐轮 (R1 → R2 → … → Rk)                           │
│ ② agent 在 workspace/product/ 里产出 index.html + logic 层 │
│ ③ 每轮得分：                                                │
│    · B 行为（确定性 golden suite，node 跑）                │
│    · S 结构（静态 lint：文件/内容/依赖/离网/尺寸）         │
│    · P 呈现（rubric judge，claude/codex adapter 盲评 0–5） │
│ ④ 回归矩阵：上一轮通过、本轮失败 → regression              │
│ ⑤ 总分 = .55·B + .20·S + .25·P（P 缺省按比例再归一）       │
└────────────────────────────────────────────────────────────┘
```

### 三层产物契约（L1/L2/L3）

| 层 | 内容是 | 判分 |
|---|---|---|
| **L1 逻辑契约** | `game_logic.js`：纯函数 `createGame(opts)` + `advance(game, action, dt)` | 确定性 golden suite（毫秒级） |
| **L2 呈现层** | `index.html`（three.js）调用 L1 做渲染 | rubric judge 盲评 + 静态内容 check |
| **L3 出题人资产** | `task.yaml` 的 R1..Rk incremental spec + 每轮行为测点 | 人工维护 |

### 分数定义（三维，归一到 0–1）

| 维度 | 权重 | 定义 | 防呆 |
|---|---|---|---|
| **B** Behavior | **0.55** | 末轮 `passed_behavior / total_behavior`，乘 \(1 - 0.2·regression\_rate\) | regression 是乘法而非减法：崩了就硬扣 |
| **S** Structure | **0.20** | 静态检查项加权通过率（required_file/contains/no_external_js/max_size_kb/line_budget 等） | 分层合规：agent 必须把逻辑拆到 game_logic.js |
| **P** Presentation | **0.25** | rubric judge 给每维 0–5 的加权均值，映射到 0–1 | judge 盲评 + 位置对调防顺序效应；锚点校准 |

**总分**：`total = 0.55·B + 0.20·S + 0.25·P`

### 行为回归矩阵（核心卖点）

```jsonc
// runs/<ts>/<task>.<agent>.json 的 rounds[*] 里：
{
  "round": "R2",
  "regressions": ["B4_ball_lost"],        // 上一轮 PASS、本轮 FAIL
  "newly_passing": ["B7_speedup"],        // 本轮新增 PASS
  "behavior_pass_rate": 0.71
}
```

`momozi leaderboard` 会把多 agent 的 B/P/S 均值出表；`Change-Robustness` 子分 = `1 - regression_rate_final`，用于标记"改着改着就崩"的模型。

---

## 2. 题目构成与分布（v0.1 → v1.0 规划）

### v0.1（本仓库，当前）

| 族 | 单题 | 难度 | 测的能力 |
|---|---|---|---|
| physics | `tg1_paddle_breakout` | easy | 弹球碰撞、墙/拍/砖块、计分、命数、暂停 |

### v1.0（规划：6 族 × 25 = 150 题）

| 族 | 描述 | 难度跨度 | 代表行为测点 |
|---|---|---|---|
| **physics** | 弹球、打砖块、跑酷 | easy–hard | 碰撞法线、出界判负 |
| **state_machine** | 回合制、TBS 棋盘、商店经济 | medium | 状态转移表穷举、非法输入拒绝 |
| **procedural_gen** | 无限关卡、随机种子复现 | medium–hard | 通关率、种子确定性 |
| **puzzle_planning** | 推箱子、寻路 | hard | 最优解序列、步数上限 |
| **economy_long_run** | 塔防资源平衡、模拟经营 | hard–expert | 数值无幂脱 |
| **live_long_run** | 30 分钟压力、无帧塌陷 | expert | 长跑日志、内存稳态 |

题目难度不靠体感，靠三个可计量指标：**(a) 状态空间大小 (b) 需交互组件数 (c) arc 轮次×变更耦合度**。

### 数据在仓库哪

```
bench/
├─ tasks/<task_id>/<task_id>.task.yaml    # 每题的 task 定义（题目描述、rounds、rubric、static）
├─ tests/beh_behavior.mjs                # 通用行为套件（公开）
├─ rubrics/<task_id>.md                  # 每题 rubric 文本（给 judge 用）
└─ references/<task_id>/                 # 参考实现（mock 联调 + 本科目过样板）
```

---

## 3. 打分标准细则

### B：行为（deterministic，占比 55%）

行为套例是 golden 断言库。判定口径：**末轮全 pass 才算满分**，每一项失败按 1/N 扣；此外还有**回归系数**：

```
regression_rate = (前轮通过、本轮失败的行为数) / 末轮通过数
B_final = pass_rate_k × (1 − 0.2 × min(1, regression_rate))
```

举例：末轮 pass 8/10、有 2 个回归 → `0.8 × (1 − 0.4) = 0.48`。

### S：结构（static checks，占比 20%）

- `required_file`：`index.html`、`game_logic.js` 必须齐
- `contains`：`index.html` 必须包含 `THREE`（引擎引用）与 `game_logic.js`（逻辑引用）
- `line_budget`：`game_logic.js` ≤ N 行（逼 agent 分模块、不堆巨型单文件）
- `max_size_kb`：任何单文件 ≤ N KB
- `no_external_js`：禁止未经白名单的外链 CDN（放行 three.js 官方 CDN 时为 `allow` 列表）

缺文件只有当 `ok: null` 才算该检查"未覆盖"，不计入分母。

### P：呈现（rubric judge，占比 25%）

- 每题 2–4 个维度（`rubrics/<task_id>.md`），每维 0–5
- judge 跑在 `--judge-agent claude / codex` adapter 上；默认用 `claude`
- judge 看到的 prompt 仅包含需求 spec + index.html 截断 + 维度描述，**不带 agent 名/模型**
- 两个位置各评一次取中频（详见 `momozi/judge.py` 的盲评协议）

---

## 4. 准备环境（测试这个 BMK 需要什么）

### 必装

| 依赖 | 版本 | 装法 |
|---|---|---|
| Node.js | ≥ 20 | `brew install node@25` 或 nvm |
| Python | ≥ 3.9 | 系统自带即可 |
| PyYAML | — | `pip install -r requirements.txt` |
| WebGL-capable 浏览器 | — | 人工跑 `index.html` 玩一遍 |

### 可选（跑真实 agent）

| adapter | CLI | 备注 |
|---|---|---|
| **claude code** | `claude` | 建议 `claude --version` 试一遍，headless 模式由 adapter 注入 |
| **codex** | `codex` | `codex exec --full-auto <prompt>` |
| **mock** | — | 直接复刻参考实现，联调 harness 不花 token |

### 跑一次要多久

- mock：`< 5s`
- 一个 agent × 一道题 × R1+R2：约 2–5 分钟（受 agent 生成时间支配）
- leaderboard 聚合：`< 1s`

---

## 5. 提交自动化测试方案

想让模型库自动"刷榜"，按下面两种其一：

### A. 仓库内（推荐）

```bash
# harness 会把 prompt 写到 workspace/_prompt.md，agent 在 cwd 里造产品后写 workspace/product/
python3 -m momozi run bench/tasks/<task>/<task>.task.yaml --agent <profile> --judge-agent <profile>
```

`profiles.yaml` 里加自己的 adapter：

```yaml
myagent:
  label: my-agent
  argv: [ "/path/to/myagent", "--print", "$PROMPT_FILE" ]
  timeout: 1800
```

`$PROMPT_FILE` / `$PROMPT` / `$WORKDIR` 三个占位符由 adapter 自动替换。

### B. 提交包（external submission）

打包可回放的产物：

```
submissions/<team>__<agent>__<task>.json        # 你自己的 run 结果，schema 见 runs/ 里现有样本
submissions/<team>__<agent>__<task>.tar.gz       # 解压即 product/ 目录（复评用）
```

复评命令（评审方侧）：

```bash
python3 -m momozi verify submissions/<name>.json submissions/<name>.tar.gz
```

`momozi/verify.py` 会重新跑行为套件 + 静态检查，若与提交结果不一致则按验算值出榜。你不需要把 agent 暴露给评审方。

### C. CI（GitHub Actions 示例）

```yaml
- run: pip install -r requirements.txt
- run: python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml --agent claude --judge-agent claude
- run: python3 -m momozi leaderboard --out leaderboard.json
- uses: actions/upload-artifact@v4
  with: { name: leaderboard, path: leaderboard.json }
```

详见 `docs/submission/README.md`。

---

## 6. v0.1 实测基线（mock = 参考实现满分基准）

| agent | total | B | S | P | runs |
|---|---|---|---|---|---|
| `mock`（参考实现） | **1.0000** | 1.00 | 1.00 | — | 3 |
| `claude`（claude code R1，未产出 index.html） | 0.4157 | 0.60 | 0.43 | — | 1 |
| `codex`（profile 参数未通的失败态，已清理） | — | — | — | — | — |

> 实测意义：一个 agent 只给「L1 逻辑 + 缺 index.html」，分数 0.42；只要按 L1/L2/L3 分层契约交付真实产物，就能逼近 1.0。**这正是维度齐全、评估合理性的体现**——不是每个 agent 都能造出可玩的 3D 游戏。

> 要复现基线：`bash scripts/smoke.sh`；要看全量榜单：`python3 -m momozi leaderboard --out leaderboard.json`。

---

## 7. 关系对照（与同类 BMK 的差异化）

| BMK | 造/玩 | 引擎 | 轮次 | 行为回归 | 开源 |
|---|---|---|---|---|---|
| **momozi-3A-GamegenBench** (本仓库) | **造** | three.js(v0.1) → UE5/Godot(v1) | **R1→Rk 增量** | ✅ 核心机制 | ✅ BSD-2 |
| GameCraft-Bench (2606.17861) | 造 | Godot · 140 任务 | 单轮 | ❌ | ✅ |
| Mage (2605.07342) | 造 | Unity · 26 模式 | 单轮 | ❌ | ✅ |
| Orak (2506.03610) | 玩 | 12 商业游戏 | — | ❌ | ✅ CC-BY |
| OmniGameArena (2606.09826) | 玩 | UE5 · 12 游戏 | 多轮反思 | — | 待确认 |
| 3DGameAgentBench | 造 | Three.js 单文件 | 多轮 | 概念有、无标准判分 | ❌ |

---

## 8. 目录结构

```
momozi-3A-GamegenBench/
├─ README.md                     ← 你在看的
├─ DESIGN.md                     方法论深版（定位/核心理念/评分设计/反作弊口径）
├─ LICENSE                       BSD-2
├─ requirements.txt
├─ profiles.yaml                  agent adapter 配置（优先 claude code / codex）
├─ momozi/                       harness 包
│  ├─ run.py                     runner（多轮 + 回归 + B/S/P）
│  ├─ task.py                    task.yaml loader
│  ├─ verifiers.py               StaticChecker + BehaviorSuite
│  ├─ judge.py                   rubric judge（盲评 + 位置对调）
│  ├─ verify.py                  提交包复算
│  ├─ adapters.py / mock_adapter.py
│  └─ leaderboard.py             榜单聚合
├─ bench/
│  ├─ tasks/<task_id>/…          题目定义（.task.yaml + 专用 tests/）
│  ├─ tests/beh_behavior.mjs     通用行为套件
│  ├─ rubrics/                   rubric 描述
│  └─ references/<task_id>/      参考实现
├─ docs/submission/              提交 + CI + 出题规范
├─ examples/README.md            单文件跑法示例
├─ scripts/smoke.sh              端到端冒烟测试
└─ runs/                         结果输出（含 leaderboard.json）
```

---

## 9. 参与方式

- 出题：`bench/tasks/<id>/<id>.task.yaml` 遵循模板直接 PR；参见 `docs/submission/task_authors.md`
- 提交 leaderboard：`submissions/<team>__<agent>__<task>.{json,tar.gz}`（方案见 §5.B）
- 提 issue：发现行为套件误判、rubric 不公 adapter 不工作，请在 issue 里附 `runs/<ts>/…` 日志。
