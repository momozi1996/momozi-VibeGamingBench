# 自动评测协议

## API Key

评分 LLM 默认使用 `deepseek-v4-flash`。在仓库根目录创建 `.env`：

```env
DEEPSEEK_API_KEY=sk-your-key
DEEPSEEK_JUDGE_MODEL=deepseek-v4-flash
DEEPSEEK_BASE_URL=https://api.deepseek.com
```

`.env` 已加入 `.gitignore`，不要在 `.env.example`、脚本、结果 JSON 或命令行中写真实 key。
`--judge-model` 与 `--judge-base-url` 可以覆盖 `.env`。

## 被测模型接入

使用 `profiles.yaml`：

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --agent codex \
  --model-label model-name \
  --workers 4
```

使用任意 harness：

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --harness-command 'my-harness --prompt {prompt_file} --output {product_dir}' \
  --model-label model-name \
  --workers 4
```

支持的命令占位符：

| 占位符 | 内容 |
|---|---|
| `{prompt_file}` | 当前单语提示词文件 |
| `{product_dir}` | 应写入两个交付文件的目录 |
| `{workspace}` | 当前题目的隔离工作区 |
| `{task_file}` | 当前 task YAML |
| `{task_id}` | 当前 task ID |

同样的信息会写入 `MOMOZI_PROMPT_FILE`、`MOMOZI_PRODUCT_DIR`、
`MOMOZI_WORKSPACE`、`MOMOZI_TASK_FILE`、`MOMOZI_TASK_ID` 环境变量。

## 题目选择

```bash
# 单题
python3 scripts/auto_evaluate.py --task TASK_ID --agent codex

# 指定语言与难度
python3 scripts/auto_evaluate.py \
  --language zh --difficulty high --agent codex --model-label model-name

# 从筛选结果第 101 题开始跑 50 题
python3 scripts/auto_evaluate.py \
  --all --offset 100 --limit 50 --agent codex --model-label model-name

# 只打印选择结果，不生成、不调用 judge
python3 scripts/auto_evaluate.py --all --agent mock --dry-run
```

必须显式传 `--all`、`--task` 或至少一个筛选条件。

## 断点续跑

```bash
python3 scripts/auto_evaluate.py \
  --all \
  --agent codex \
  --model-label model-name \
  --run-id model-name-full \
  --resume
```

`--resume` 会跳过 `runs/auto/<run-id>/` 中已经存在的每题结果。不要在同一个 run ID
中更换被测模型、judge 模型或协议参数。

## 打分标准

DeepSeek 为四个维度给 0-5 分：

| 分数 | 标准 |
|---:|---|
| 0 | 缺失、不可用或没有可验证实现 |
| 1 | 名义存在，但严重损坏或几乎只有表面效果 |
| 2 | 部分实现，缺少主要需求或系统连接 |
| 3 | 主要需求已实现，形成可用的核心体验 |
| 4 | 完成度强，具备有意义的深度、反馈与打磨 |
| 5 | 证据充分、完成优秀，并实质超过基础要求 |

每个维度必须返回：

- `score`
- `reason`
- `evidence`
- `missing`

judge 只能使用代码证据，不能根据变量名、标签、注释、TODO 或模型自述推断功能存在。

## 分数计算

```text
rubric_score_100 =
  100 × (
    completeness / 5 × 0.15 +
    richness     / 5 × 0.35 +
    player_exp  / 5 × 0.15 +
    visual      / 5 × 0.35
  )

overall_score = BUILD × CONTRACT × rubric_score_100
```

`BUILD` 检查：

- `index.html` 存在。
- `game_logic.js` 存在。
- 页面有 Canvas/WebGL 呈现信号。
- 页面不使用被禁止的重型运行时外部资源。

`CONTRACT` 检查：

- `game_logic.js` 可被 Node.js 导入。
- 导出 `createGame(opts)`。
- 导出 `advance(game, input, dt)`。
- 初始状态和推进后状态为对象。

BUILD 为 0 或 CONTRACT 为 0 时跳过付费主观 judge。CONTRACT 部分通过时作为 0-1
乘数降低总分。

## 每题结果

```json
{
  "evaluation_protocol": "auto-v1",
  "model_label": "model-name",
  "task": "task-id",
  "family": "strategy",
  "difficulty": "high",
  "language": "zh",
  "generation": {},
  "build_gate": {},
  "contract": {
    "pass_rate": 1.0,
    "results": []
  },
  "dimensions": {},
  "scores": {
    "completeness": 0.0,
    "richness": 0.0,
    "player_exp": 0.0,
    "visual": 0.0,
    "rubric_score_100": 0.0,
    "build_multiplier": 0.0,
    "contract_multiplier": 0.0,
    "overall_score": 0.0
  },
  "judge": {
    "provider": "deepseek",
    "model": "deepseek-v4-flash",
    "usage": {}
  }
}
```

## 排行榜

自动评测结束后更新：

- `leaderboard.json`
- `LEADERBOARD.md`
- `runs/auto/<run-id>/leaderboard.json`

正式榜单只接收有效 `auto-v1` 结果。`--mock-judge` 只用于 CI 和接入调试，结果不会
进入排行榜。
