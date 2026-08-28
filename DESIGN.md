# momozi-VibeGamingBench 设计文档（v0.4.0）

## 1. 定位

本 benchmark 评测 coding agent 将游戏设计需求转化为完整、可玩的浏览器游戏的能力。
题目强调互相连接的玩法系统、明确的胜负或完成闭环、可读反馈和成品级呈现，而不是静态
场景、交互演示或只有菜单的原型。

当前题池：

- 491 个游戏概念。
- 每个概念拆成英文和中文两个独立样本，共 982 题。
- 21 个标准化游戏 `family`。
- 低、中、高三个实现难度等级。

## 2. 单题结构

每个任务目录严格包含四个文件：

| 文件 | 作用 |
|---|---|
| `*.task.yaml` | ID、语言、类型、难度、提示词、产物合同和评分维度 |
| `prompt.md` | 直接提供给生成 agent 的单语提示词 |
| `rubric.original.json` | 具体玩法、深度、体验与美术锚点 |
| `rubric.mapping.json` | 细粒度锚点到四个评分维度的映射 |

`prompt.md` 必须与 YAML 中 `rounds[0].spec` 完全一致。中英文变体共享
`base_task_id`、`family`、`difficulty` 和 rubric 结构。

## 3. 产物合同

agent 在工作区的 `product/` 中交付：

| 文件 | 合同 |
|---|---|
| `index.html` | 双击可运行的完整浏览器游戏；包含 Canvas 2D 或 WebGL/Three.js 呈现 |
| `game_logic.js` | 确定性规则层；导出 `createGame(opts)` 和 `advance(game, input, dt)` |

任务禁止构建步骤、本地服务器和运行时下载图片、模型、视频或音频。允许按题面约定加载
固定版本的 Three.js。完整玩法、HUD 和主要反馈应在 1280x720 下可读。

## 4. 自动评测流程

1. 选择题目，可按 task、语言、类型、难度、offset 和 limit 过滤。
2. runner 创建隔离工作区并写入当前单语提示词。
3. `profiles.yaml` adapter 或外部 harness 生成 `index.html` 与 `game_logic.js`。
4. collector 兼容产物写入 `product/` 或工作区根目录的 harness。
5. BUILD gate 检查必需文件、Canvas/WebGL 信号和外部资源限制。
6. CONTRACT 通过 Node.js 导入规则层并检查两个导出和基本状态推进。
7. BUILD 与 CONTRACT 允许时，DeepSeek judge 读取需求、代码和详细 rubric 锚点。
8. 每题结果写入 `runs/auto/<run-id>/`，随后更新 JSON 与 Markdown 排行榜。

用户必须显式指定 `--all`、`--task` 或筛选条件，避免误触发 982 题的真实生成和评分成本。
`--resume` 只复用指定 run ID 下已经存在的每题结果。

## 5. 评分协议

四个维度均为 0-5：

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

- `BUILD`：静态硬门控，值为 0 或 1。
- `CONTRACT`：通用行为合同的通过率，值为 0-1。
- `overall_score`：正式总分，值为 0-100。

BUILD 失败或规则层完全不可导入时，跳过付费 LLM judge 并直接记 0 分。部分合同失败会按
通过率降低总分，避免一个只满足文件名的项目获得完整主观评分。

## 6. Judge 约束

自动 judge 默认模型为 `deepseek-v4-flash`，可通过 `.env` 或 `--judge-model` 覆盖。
API 调用采用 OpenAI 兼容的 `/chat/completions` JSON 接口，不增加厂商 SDK 依赖。

评分提示词要求：

- agent 和被测模型身份不可见。
- 0、1、2、3、4、5 每档都有明确语义。
- 只能按 `index.html` 与 `game_logic.js` 的可验证代码证据评分。
- 不得依据变量名、菜单标签、注释、计划或 TODO 推断功能存在。
- 每个维度必须返回理由、代码证据和关键缺失项。
- 返回结构经过本地严格校验，维度缺失、越界或非 JSON 均视为 judge 基础设施错误。

HTTP 429 与 5xx 会指数退避重试。judge 错误的结果不会进入正式排行榜，可用原 run ID
修复后断点续跑。

## 7. 排行榜

正式 leaderboard 只聚合 `evaluation_protocol == "auto-v1"` 且
`leaderboard_eligible == true` 的每题结果。mock judge、协议夹具和 judge 基础设施错误
不会进入榜单。

每个模型展示：

- 总分均值。
- 四个维度的 0-5 均分。
- BUILD 通过率。
- CONTRACT 平均通过率。
- 已完成题目数和结果数。

排序依次使用总分、未乘门控的 rubric 分和 CONTRACT 均值。

## 8. 难度语义

难度表示在浏览器垂直切片中实现题面要求的工程复杂度，不表示游戏类型价值，也不表示
模型预期得分。确定性分类器使用以下信号：

- 游戏类型的基础复杂度。
- 2D/3D 范围。
- 明确要求的系统数量。
- 物理、AI、寻路、模拟、经济、持久状态、联网、程序生成和高级渲染信号。

分数不高于 4 为 `low`，5-7 为 `medium`，8 以上为 `high`。分类规则集中在
`scripts/task_metadata.py`，生成器和统计门禁共用同一实现。

## 9. 数据门禁

`scripts/generate_task_distribution.py --check` 验证：

- 491 个完整中英文概念对。
- 982 个任务目录，每目录严格四个文件。
- ID、目录、语言后缀与 `base_task_id` 一致。
- 提示词和 YAML R1 完全一致。
- 双语变体的类型和难度一致。
- 静态产物合同是 `index.html + game_logic.js`。
- rubric 权重合计为 1，所有映射锚点真实存在。
- 声明的行为检查脚本存在。
- `bench/TASK_DISTRIBUTION.md` 与当前题池完全一致。

`scripts/validate_pool.py --only-mz` 进一步运行 982 题的 mock runner/build gate
兼容性门禁，并更新 `bench/POOL_AUDIT.md`。

## 10. 当前边界

- 当前题池是单轮生成任务；旧式多轮 runner 保留兼容，但不作为正式自动榜单协议。
- BUILD 和 CONTRACT 是确定性合同检查，不等同于完整浏览器玩法、性能或视觉回归测试。
- visual 维度由代码证据判断；严肃发布前仍应做浏览器截图抽样和多 judge 校准。
- 不同模型的排行榜对比应使用相同题目集合、相同 judge 模型与相同协议版本。
