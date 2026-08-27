# examples/ — 单文件跑法示例

## 干跑（mock + 参考实现）

```bash
cd momozi-3A-GamegenBench
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml --agent mock
```

## 真跑（claude code / codex）

```bash
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml \
  --agent claude --rounds R1,R2 --judge-agent claude
```

## leaderboard

```bash
python3 -m momozi leaderboard --out leaderboard.json
```
