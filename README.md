# momozi-VibeGamingBench

`momozi-VibeGamingBench` 用于评测 coding agent 从自然语言需求生成完整浏览器游戏的能力。
当前版本为 **v0.4.0**，包含 **491 个游戏概念、982 道中英文独立题目、21 个游戏类型**。

每道题要求交付：

- `index.html`：完整的可玩界面和渲染层。
- `game_logic.js`：导出 `createGame(opts)` 与 `advance(game, input, dt)` 的规则层。

## 目录

```text
momozi-VibeGamingBench/
├── momozi/                         # runner、自动评测、judge、verify、leaderboard
├── bench/
│   ├── tasks/                      # 982 道语言独立题
│   ├── tests/beh_html.mjs          # 通用两文件逻辑合同
│   ├── POOL_AUDIT.md               # runner/build gate 全量兼容性报告
│   └── TASK_DISTRIBUTION.md        # 设计组成、类型与难度分布
├── scripts/
│   ├── auto_evaluate.py            # 自动生成、检查、评分和出榜
│   ├── split_bilingual_tasks.py    # 中英文任务对一致性检查
│   ├── generate_task_distribution.py
│   └── validate_pool.py
├── .env.example                    # DeepSeek judge 配置模板
├── profiles.yaml                   # coding agent CLI 适配
├── AUTO_EVALUATION.md              # 自动评测协议与接入说明
└── DESIGN.md
```

## 环境

```bash
python3 --version   # 3.11+
node --version      # 20+
pip install -r requirements.txt
```

真实生成需要安装 `profiles.yaml` 中对应的 agent CLI。`mock` 仅用于验证 runner、合同和
计分链路，不代表题目已经被真实模型完成。

## 自动评测

先在仓库根目录创建 `.env`，API key 填在 `DEEPSEEK_API_KEY`：

```bash
cp .env.example .env
```

```env
DEEPSEEK_API_KEY=sk-your-key
DEEPSEEK_JUDGE_MODEL=deepseek-v4-flash
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

使用现有 agent profile 评测全部题目：

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --agent codex \
  --model-label your-model-name \
  --workers 4
```

接任意外部 harness：

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --harness-command 'your-harness --prompt {prompt_file} --output {product_dir}' \
  --model-label your-model-name \
  --workers 4
```

harness 也可读取 `MOMOZI_PROMPT_FILE`、`MOMOZI_PRODUCT_DIR`、`MOMOZI_WORKSPACE`、
`MOMOZI_TASK_FILE` 和 `MOMOZI_TASK_ID` 环境变量。命令以参数数组执行，不经过 shell。

先跑一题检查接入：

```bash
python3 scripts/auto_evaluate.py \
  --task mz_sports-fishing-tournament-en \
  --agent codex \
  --model-label your-model-name
```

输出位于：

```text
runs/auto/<run-id>/<task-id>.json
runs/auto/<run-id>/summary.json
leaderboard.json
LEADERBOARD.md
```

断点续跑：

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --agent codex \
  --model-label your-model-name \
  --run-id my-run \
  --resume
```

完整参数和评分 JSON 协议见 [`AUTO_EVALUATION.md`](AUTO_EVALUATION.md)。

## 计分

四个 LLM 盲评维度均为 0-5：

| 维度 | 权重 | 关注点 |
|---|---:|---|
| `completeness` | 0.15 | 核心机制是否存在、可操作且互相连接 |
| `richness` | 0.35 | 内容变化、升级、资源、风险和策略深度 |
| `player_exp` | 0.15 | 状态可读、输入反馈、失败恢复和完整闭环 |
| `visual` | 0.35 | 构图、美术一致性、动效、镜头和完成度 |

```text
rubric_score_100 = 100 × Σ(dimension_score / 5 × dimension_weight)
overall_score = BUILD × CONTRACT × rubric_score_100
```

`BUILD` 为 0 或 1。`CONTRACT` 是通用逻辑合同通过率，范围 0-1。排行榜按
`overall_score` 降序展示，并同时展示四维均分、BUILD 通过率和 CONTRACT 均值。

## 双语题池

每个概念拆成两个独立样本：

- `*-en`：只提供英文提示词。
- `*-zh`：只提供中文提示词。

两种语言共享 `base_task_id`、游戏类型、难度和 rubric 结构，但拥有独立 task ID、
运行目录与榜单记录。完整统计见
[`bench/TASK_DISTRIBUTION.md`](bench/TASK_DISTRIBUTION.md)。

## 验证

```bash
# 快速语法、题池生成器、runner 和自动评测协议检查
bash scripts/smoke.sh

# 491 对中英文任务与统计报告
python3 scripts/split_bilingual_tasks.py
python3 scripts/generate_task_distribution.py --check

# 982 题 runner/build gate 兼容性门禁
python3 scripts/validate_pool.py --only-mz --workers 16
```

## 授权

BSD-2-Clause，见 `LICENSE`。
