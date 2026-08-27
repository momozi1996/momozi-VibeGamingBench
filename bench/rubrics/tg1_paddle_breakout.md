# rubrics: tg1_paddle_breakout

## 评分模型 & Prompt 协议（可复现）

- **打分模型**：通过 `profiles.yaml` 中指定的 adapter 执行，推荐 **claude code 无交互（headless `-p`）** 或 **codex `exec`**；同一 prompt 对同一产物跑 **2 次（位置 A/B 对调）取中位数**以抑制顺序效应。
- **输入材料**：题目需求 spec（该轮 rounds[last].spec）、agent 交付的 `index.html`（截断到 ≤12KB）、下列 4 维锚点表。
- **屏蔽信息**：agent 名称、模型版本、用户提示、以往分数全部 **不进入 prompt**（盲评）。
- **打分范围**：每维 0–5，0 = 不可用、3 = 达标、5 = 优秀（超预期）。
- **P 维度最终映射**：P (0–1) = (completeness + richness + player_exp + visual) / 20。

> 给 agent 看的 prompt 见 `momozi/judge.py` 的 `SCORING_TEMPLATE`；数据生成后每份 run 会以 `scores.P_details` 存档保留 judge 原话。

---

## 维度 1: Completeness 功能完成度（权重 0.30）

问：需求里点名的功能是不是都实现了？

锚点：
- 0：关键功能（球反弹/砖块/计分/暂停）有缺失
- 2：主干功能残缺（例如没有暂停、没有失球处理）
- 3：R1 的全部功能都齐（含暂停与返回主菜单）
- 5：R1 与 R2 的全部增量都齐（砖块 hp 分层、加速道具）

## 维度 2: Richness 内容丰富度（权重 0.25）

问：可玩的内容、状态、细节是不是丰满？

锚点：
- 0：单砖块、单关卡、无音效
- 2：多关卡但没有隐藏要素
- 3：3 种砖块 hp + 道具 + 音效/粒子反馈
- 5：多种道具、连击计分、HUD 丰富、隐藏互动

## 维度 3: Player Exp. 玩家体验（权重 0.25）

问：主循环（开始—操作—反馈—结算）是否让人想玩？

锚点：
- 0：输入无响应或延迟明显
- 2：能玩但手感别扭（球速一致、无立体反馈）
- 3：输入流畅、暂停/重开顺畅、操作反馈清晰
- 5：手感精细（加速度/反弹角、音效、相机震动等惊喜点）

## 维度 4: Visual 视觉表现（权重 0.20）

问：three.js 呈现是否像「3D 游戏」而非「立方体扫把」？

锚点：
- 0：没有 3D 渲染、白屏
- 2：3D 元素在但无光照/无阴影
- 3：光照、视差相机、基本材质
- 5：质感材质、阴影、后处理、色彩搭配出彩

---

judge 输出格式（严格 JSON）：

```json
[{"id":"completeness","score":0-5,"detail":"..."},
 {"id":"richness","score":0-5,"detail":"..."},
 {"id":"player_exp","score":0-5,"detail":"..."},
 {"id":"visual","score":0-5,"detail":"..."}]
```
