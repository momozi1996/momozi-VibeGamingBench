# momozi-3A-GamegenBench 设计文档（v0.1）

> 定位：**评测 coding agent「创造类任务」能力的游戏生成 benchmark（生成向）**，核心命题——
> **衡量 agent 能否在多轮迭代中持续构建、修改可玩游戏，并守住已经成立的玩法。**

## 0. 一句话定位

- 工作名：**momozi-3A-GamegenBench**（140 题 · 生产级）
- 给 agent 一段「值得连续迭代的游戏设想」(game arc)，agent 分 3–5 轮生成 Web 3D 游戏；每轮的历史行为 golden suite 必须保持通过，新增玩法必须正确实现；评审按 rubric 出分。

## 1. 为什么存在（对照现有工作找空白）

| Benchmark | 造/玩 | 引擎 | 轮次 | 判分确定性 | 行为回归验证 | 开放度 |
|---|---|---|---|---|---|---|
| GameBench 原型(2606.17861 参考原型) | 造 | Godot，140 任务/15 家族 | 单轮 | 交互 replay + 多模态 judge | ❌ | 开源 demos+代码+数据 |
| Mage (2605.07342) | 造 | Unity(C#)，26 模式 | 单轮 | 四轴（编译/运行/结构/机制） | ❌ | benchmark+replay |
| Orak (2506.03610) | **玩** | 12 款商业游戏 | — | leaderboard+arena | — | CC-BY |
| OmniGameArena (2606.09826) | 玩 | UE5 自建 12 款 | 多轮反思 | 冷启动+IDC 曲线 | — | 待确认 |
| 3DGameAgentBench | 造 | Three.js 单文件 | 多轮 | 人工视频复核 | 概念有、无标准判分 | 数据保密 |
| **momozi-3A-GamegenBench（本设计）** | **造** | Three.js/Web（v1） | **3–5 轮增量** | **确定性 golden suite ≥70% + rubric 补视觉 + 自动行为回归（乘法硬惩罚）** | ✅ 核心卖点 | 计划开源 |

**空白点（差异化）**：
1. **多轮增量 + 行为回归硬约束**：现有生成 BMK 全是「一次造对」；真实开发是长程的。GameBench 参考原型最强 agent 才 41.46%，多轮只会更糟——这正是拉开差距的地方。
2. **逻辑/呈现分层**：Mage 证明直接 NL→代码的机制遵循度会崩（F1≈0.12），加结构化 IR 后 F1→1.00。我们的任务契约天然分层可单测（§2），把这条 insight 做成 BMK 机制。
3. **确定性判分占大头**：现在主要靠多模态 judge（贵、不稳）；我们 ≥70% 给确定性测试，judge 只补视觉与创意。
4. **编译率 ≠ 正确性**：Mage 发现反相关；我们单设「结构空洞」惩罚（呈现维度的 spec check）。

## 2. 核心概念模型：三层产物契约

每道题要求 agent 产出：

| 层 | 内容 | 判分方式 |
|---|---|---|
| **L1 Contract**（逻辑契约） | `game_logic.js`：纯逻辑 `advance(state, action) → state`，无 DOM/无渲染依赖 | 确定性 golden suite，node 秒级，可无限回归 |
| **L2 Presentation**（呈现层） | `index.html`：调用 L1，完成渲染/音效/交互/手感 | rubric judge 盲评 + 硬 spec check |
| **L3 Arc**（出题人资产） | R1..Rk 连续增量 spec + 每轮黄金行为测试点 | 人工维护 |

## 3. 评分体系

```
Total = 0.55·Behavior + 0.25·Presentation + 0.20·Structure

Behavior（确定性行为套件通过率 + 回归惩罚）
  B_score = max(0, pass_rate_k)                      # 末轮关键行为通过率
  B_final = B_score · (1 − 0.20 · regression_rate)   # regression_rate = 前轮通过行为在末轮失败的比例

Presentation（LLM rubric 盲评 0–5，多 judge 取中频）
  P: 视觉质感 / 交互响应 / 手感与反馈 / 创意与说明
  每题 2 锚点（明显好/明显差）先校准，judge 一致率 ≥80% 入库

Structure（确定性 + rubric）
  S: L1/L2 分层合规 / L1 无框架逃逸 / 文件集约数与离线自包含 / 结构空洞惩罚
```

要点：
- **regression 是乘法硬惩罚**——「改着改着玩法没了」被量化成对总分的直接压制（3DGameAgentBench 的痛点）。
- **judge 盲评 + 位置对调**：不看模型名/版本；正序反序各评一次取中频防位置效应。
- duet anchors：2 锚模型（康健/崩溃）做 p∩q≥0.8 签 cmake，不签就 breakdown  arbitration。

## 4. 多轮运行协议（runner 语义）

```
Round 1: prompt = r1_spec
Round k>1: prompt = rk_delta（硬性要求：保持既有行为不破坏；与上一产物 diff 对照）
每轮结束：快照 artifact → 跑 behavior suite 记录逐例 PASS/FAIL → 计算 regression
末轮：追加 rubric（L2）+ structure check
```

- **行为历史**：`runlog.json` 保留每轮每例行为结果，回归矩阵可视化。
- **全灭即终止**：若某轮 golden 全灭，runner 记 0 分并终止——对应真实工程「崩了就崩了」。
- 对抗暴露设计：Rk 常设「诱使模型『优化』老行为」的 delta——例如改物理手感时球速被悄悄改坏、计分边界位移——比纯增量更能压出回归防护能力。这条我们主观定义为 3DGameAgentBench 的辨证代价，这才是直接给 PoC 的。

## 5. 反作弊与泄漏防护

- 离网沙箱：runner 内 `--network none`，禁止引用外链 CDN 之外的资源（白名单 CDN 允许 hash pin）。
- 模板/教程抄袭检查：跨题 embedding 相似度 >0.95 触发人工核查；对已知教程/仓库检索。
- closed/held-out 变体：Family 内同模式换场景+数值，榜单混入 15% held-out（同 OmniGameArena 泛化维度）。
- 锚点防放水：每题附人工过样板 + 模板最小答案各 1 个。
- prompt 注入测试混入：index.html 内审「隐藏约束」类注入，L1 若执行可疑指令即 fail。

## 6. 成本模型

- 模型侧：单任务完整 3–5 轮 ≈15–25 万 tokens；一模型刷 15 题 ≈5M tokens。
- 出题人侧：一题（L1 suite + 4 轮 delta spec）≈6–8 小时（参考 3DGameAgentBench 的 4–5 小时/题）。
- 机器侧：行为 suite 毫秒级；rubric judge 每题 2 次（首+末轮）共 ~2 分钟。
- 发布：v0.1 公开 15 题 → 回访校准 → v1 150 题 + 全开源工具链（open+closed 双数据集，仿 ClawProBench）。

## 7. 开源与数据发布

- 工具链全开源（MIT）；数据集 HuggingFace：`{task.yaml, r1_spec, rk_delta, behavior_suite, rubric, codebook}`。
- **golden suite 公开但 inject_guard 私有**（仿 SWE-Bench 双集思路），防止 models 直接背答案。
- leaderboard 维度：Behavior / Presentation / Change-Robustness（回归子分单列）。

## 8. 路线图

- v0.1：3 示例任务 + harness 单轮/多轮跑通，mock+真实 agent 双通道（本仓库）。
- v0.3：15 题、judge 锚定校准、离网沙箱。
- v1.0：150 题（6 族×25）、公开数据集+leaderboard、多 judge 一致性报告。

## 9. 风险与开放问题

- **judge 稳定性**：rubric 主观维度靠锚点+多 judge；结构维尽量转确定性。
- **基准漂移**：模型刷榜后退 L1 泄漏；closed set + 周期性 refresh。
- **分层契约的元难度**：强制分层可能惩罚「不会分层」的模型——但 Mage 数据表明这正是能力差距显现点，我们以「结构分」透明扣分，不藏。
