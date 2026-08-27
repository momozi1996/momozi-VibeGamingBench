# 题目模板（贡献者速查）

## 文件布局

```
bench/tasks/<task_id>/<task_id>.task.yaml     # 题目本体
bench/tasks/<task_id>/tests/beh_<x>.mjs       # 可选：该题的专项行为套件
bench/rubrics/<task_id>.md                    # 主观维度与锚点
bench/references/<task_id>/                   # 参考实现（mock 联调 + 过样板）
```

## task.yaml 字段

```yaml
id: tg1_paddle_breakout
title: 3D 打砖块（Paddle/Ball/Brick 多轮增量）
family: physics          # 题族：physics / state_machine / procedural_gen / puzzle_planning / economy_long_run / live_long_run
difficulty: easy         # easy / medium / hard / expert
engine: three.js

rounds:                  # R1 必须可玩；Rk+ 是增量 delta，且要求“R1 行为不破”
  - name: R1
    spec: |
      # Round 1：基础可玩
      ...
  - name: R2
    spec: |
      # Round 2：增量（保持 R1 行为不破）
      ...

static:                  # 静态检查（缺一项-S 分；不合规扣 S）
  - { kind: required_file, role: entry,   path: index.html,          weight: 1.0 }
  - { kind: required_file, role: logic,   path: game_logic.js,       weight: 1.0 }
  - { kind: contains,      path: index.html, pattern: "THREE",       weight: 0.5 }
  - { kind: line_budget,   path: game_logic.js, max_lines: 200,      weight: 0.5 }
  - { kind: max_size_kb,   kb: 256 }

behavior:                 # 行为套件（node 脚本，stdout JSON 数组）
  script: tests/beh_behavior.mjs
  timeout: 60

rubric:
  - { id: render_polish, weight: 0.5, max: 5 }
  - { id: input_feel,    weight: 0.5, max: 5 }

reference_dir: bench/references/<task_id>    # 参考实现目录（mock 用；也可不给→没有 mock 跑法）
```

## 出题七原则

1. **R1 独立可玩**：一个 agent 从零一轮就能做出能玩的版本
2. **行为可断言**：每轮目标行为必须能被 `beh_*.mjs` 的纯函数断言覆盖
3. **增量强耦合**：R2+ 必须强制 agent 改老代码（而不是另写文件）
4. **回归敏感**：R2 里藏“诱使 agent 打破 R1 行为”的角落（改得分公式、改碰撞方向）
5. **rubric 少数**：每 task 至多 4 个 rubric 维度，能转确定性的转确定性
6. **难度可计量**：按状态空间 × 组件数 × 轮次耦合度给难度标签
7. **参考实现自证**：`bench/references/<id>` 里的实现必须通过 `momozi run --agent mock`

## 验证

```bash
python3 -m momozi run bench/tasks/<id>/<id>.task.yaml --agent mock   # 参考实现必过
```
