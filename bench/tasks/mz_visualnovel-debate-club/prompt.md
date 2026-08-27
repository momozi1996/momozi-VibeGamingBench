# Debate Club

Build **Debate Club**, a **debate and contradiction visual novel** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is a student investigator who must expose lies in formal debates by
firing evidence at contradictory statements. Suspects make claims during
structured arguments, and the player must identify which statement contradicts
collected evidence, then present the right proof at the right moment. The
tension is timing and precision: statements scroll past, the window to object
is brief, and wrong objections damage the player's reputation score. Multiple
suspects across multiple debate rounds build toward identifying the true
culprit. The tone is academic-thriller: school halls, formal podiums, sharp
dialogue, and the rush of catching someone in a lie.

## What the Player Experiences

From the title screen the player enters an investigation phase. They explore
locations (classroom, library, courtyard) clicking hotspots to gather evidence
cards — each card has a fact, a source, and a relevance tag. Evidence
collection is the preparation for the debate.

The debate phase is the core gameplay. Suspects take turns making statements
displayed as scrolling text panels. The player listens (reads) and watches for
contradictions — a statement that conflicts with collected evidence. When they
spot one, they select the matching evidence card and fire it as a "truth
bullet" at the contradicting statement.

A correct hit triggers a dramatic break sequence: the statement shatters, the
suspect falters, and new information is revealed. An incorrect hit costs
reputation points — lose too many and the debate is lost. After breaking a
contradiction, the debate advances to a new phase with harder claims.

Multiple debate rounds across different suspects build the case. The final
round requires the player to identify the culprit from the accumulated
evidence. A styled result screen shows the verdict, reputation score, and
evidence accuracy.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server.** It must render within 3 seconds on a normal laptop.
- `game_logic.js` — pure logic layer (`createGame(opts)` / `advance(game, input, dt)`),
  imported by `index.html`. Same pattern as `bench/references/tg1/game_logic.js`.

Constraints:
- All assets procedural (colors, cubes, spheres); no external images/audio fetched at runtime.
- Keyboard-only input handled via `keydown`/`keyup`. WASD + space + enter + ESC.
- `index.html` must not `fetch()` / `XMLHttpRequest` any URL; only CDN allowed is three.js.
- Size budget: `game_logic.js` ≤ 220 lines, `index.html` ≤ 120 KB.

Judge reads `index.html` (headless Chromium screenshot) + `game_logic.js`; there is no
CLI invocation, no download, no runtime dependency.

# 中文版提示词

# 辩论社（Debate Club）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Debate Club**——一款
**辩论与矛盾点视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名学生调查者，必须在正式辩论中把证据射向自相矛盾的陈述，以此揭穿
谎言。嫌疑人会在结构化的论辩中提出主张，玩家必须判断哪一句陈述与收集到的证据
相矛盾，然后在恰当的时机呈上正确的证明。张力来自时机与精准：陈述会滚动而过，
提出异议的窗口很短，而错误的异议会损伤玩家的声望分。多名嫌疑人、多轮辩论层层
推进，最终指向真正的凶手。整体调性是学术惊悚：校园长廊、正式讲台、锋利的对白，
以及当场抓住某人说谎时的那股快感。

## 玩家体验流程

从标题画面开始，玩家进入调查阶段。他们探索各个地点（教室、图书馆、庭院），
点击热点来收集证据卡——每张卡都有一条事实、一个来源和一个关联性标签。收集证据
就是为辩论所做的准备。

辩论阶段是核心玩法。嫌疑人轮流发表陈述，以滚动的文字面板呈现。玩家聆听（阅读）
并留意矛盾点——即与已收集证据冲突的陈述。一旦发现，玩家就选中对应的证据卡，
把它作为一枚"真相子弹"射向那句矛盾的陈述。

命中正确会触发一段戏剧性的击破演出：陈述碎裂，嫌疑人语塞，新的信息随之揭晓。
命中错误则要付出声望点数——损失过多，这场辩论就输了。击破一个矛盾点之后，
辩论会推进到一个主张更难对付的新阶段。

跨越不同嫌疑人的多轮辩论逐步构建起整个案件。最后一轮要求玩家从累积的证据中
指认凶手。一个有设计感的结算画面会展示判决、声望分和证据准确率。

## 提交格式（HTML）

交付物 **两个文件**：

- `index.html` —— 双击即开的单文件页面, 走 CDN 引入 `three.js`
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  **不允许** `npm install` / 构建工具 / Python 服务器。普通笔记本 3 秒内必须渲染出来。
- `game_logic.js` —— 纯逻辑层 `createGame(opts)` / `advance(game, input, dt)`,
  由 `index.html` import。规范参考 `bench/references/tg1/game_logic.js`。

约束：
- 全部资产程序化生成(颜色、立方体、球体), 不运行时外取图像/音频。
- 键盘输入 `WASD + 空格 + Enter + ESC`。
- `index.html` 不发生运行时 `fetch/XHR`; 除 three.js 外不引入别的 CDN。
- 体量：`game_logic.js ≤ 220 行`, `index.html ≤ 120 KB`。

