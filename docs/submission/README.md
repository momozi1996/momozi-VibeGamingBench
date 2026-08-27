# 提交自动化测试方案（完整规范）

## 方式 A：仓库内跑

```bash
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml \
  --agent claude --judge-agent claude
```

`profiles.yaml` 里可以加自定义 adapter（占位符 `$PROMPT_FILE/$PROMPT/$WORKDIR` 由 runner 替换）：

```yaml
myagent:
  label: my-agent
  argv: [ "/path/to/myagent", "--print", "$PROMPT_FILE" ]
  timeout: 1800
```

## 方式 B：提交包（评审复算）

产物布局（tar.gz 内部是 `product/` 目录 + 元数据 JSON）：

```
submissions/<team>__<agent>__<task>.tar.gz
submissions/<team>__<agent>__<task>.json
```

`<task>.json` 结构（schema）：

```jsonc
{
  "benchmark": "momozi-3A-GamegenBench",
  "version": "0.1.0",
  "task": "tg1_paddle_breakout",
  "agent": "<agent>",
  "timestamp": "20260825-205045",
  "scores": { "B": 0.6, "S": 0.43, "P": null, "total": 0.42, "weights": { "behavior": 0.55, "structure": 0.2, "presentation": 0.25 } },
  "behavior_pass_rate_final": 0.6,
  "regression_rate": 0.0,
  "task_path": "bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml"
}
```

评审侧复算（tar 里 `product/index.html`、`product/game_logic.js` 重跑 static+behavior）：

```bash
python3 -m momozi verify submissions/<team>__<agent>__<task>.json submissions/<team>__<agent>__<task>.tar.gz
```

不一致 → 以验算值为准（防"虚报分数"）。

## 方式 C：GitHub Actions

```yaml
name: momozi
on: [push, pull_request]
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install -r requirements.txt
      - run: python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml --agent claude --judge-agent claude
      - run: python3 -m momozi leaderboard --out leaderboard.json
      - uses: actions/upload-artifact@v4
        with: { name: leaderboard, path: leaderboard.json }
```

## 榜单复现

```bash
python3 -m momozi leaderboard --out leaderboard.json
```

输出示例：

```json
{
  "leaderboard": [
    { "agent": "reference", "runs": 1, "B_mean": 1.0, "S_mean": 1.0, "P_mean": 1.0, "total": 1.0 },
    { "agent": "claude",    "runs": 1, "B_mean": 0.6, "S_mean": 0.43, "P_mean": null, "total": 0.42 }
  ],
  "n_runs": 2
}
```
