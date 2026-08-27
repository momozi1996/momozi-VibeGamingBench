# Grim Fable

Build **Grim Fable**, a branching dark-fairytale visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You step into fairy tales you think you already know — but the woods are darker
than you remember, the kind are not always good, and the wicked may have their
reasons. Grim Fable is a **choice-driven visual novel** where the player relives
familiar storybook tales as their protagonist, yet the choices on offer were
never in the original telling. What looks like a bedtime story hides an uneasy
truth, and the player's decisions decide which version of that truth comes to
pass.

The fantasy is **rewriting a story you assume you know**. The game should turn
the player's own expectations into the trap: a beloved tale opens the familiar
way, then forks toward outcomes the fairy tale never allowed. The heart of the
loop is **read, examine, weigh, decide** — taking in a richly written scene,
looking closely at what the illustration is hiding, sizing up who and what to
trust, and committing to a choice that the story remembers and pays off later.
It should feel like turning the pages of a haunted picture book where text,
portraits, backdrops, and choice menus all belong to the same authored world.
This is a polished, atmospheric storybook with real stakes and genuinely
different endings, not a linear text dump with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player begins the tale and
   is eased into a familiar fairy-tale premise, presented as an illustrated
   storybook scene with characters, narration, and a clear sense of who they
   are and where they stand.
2. **Reading & Examining the Scene** — The story unfolds through paced dialogue
   and narration over illustrated backdrops, but the scene is not just read — it
   invites investigation. Props, details of the setting, and the characters
   present can hide narration, clues, or secrets the player would otherwise
   miss, so the comforting tale's darker underside is something the player
   uncovers, not just something told to them.
3. **Clues That Add Up** — What the player examines and learns is **gathered and
   remembered**: a blood-flecked knife noticed on a table, a confession teased
   out of a character, a detail that contradicts the storybook version. These
   discoveries accumulate into the player's understanding and unlock or color
   the choices and revelations that follow, rewarding a curious player who looks
   closely over one who rushes ahead.
4. **Meaningful Choices** — At key moments the player is offered choices that
   the original story never gave them — whom to trust, what to reveal, which
   path to take through the wood. Choices are deliberate decisions with stakes,
   not cosmetic flavor; what the player has uncovered shapes which options are
   available and what they mean, and the game makes clear that a decision has
   been made and registered.
5. **Consequences That Stick** — Earlier choices are remembered and shape what
   comes later: which characters confide in the player, what truths surface,
   and which doors close. The player should feel the story bending around their
   decisions rather than running on rails, and recurring tales or returning
   characters should reflect what the player did before.
6. **Divergent Endings** — The tale resolves in one of several genuinely
   different endings — a subversion of the happy ending, a grim reckoning, a
   hidden truth uncovered, or a quiet escape — each reachable through different
   choices and clearly tied to how the player played. The ending is an authored,
   styled conclusion that names what the player's path brought about, and the
   player can begin again to seek a different one.

## HTML Submission Format

You must deliver **two files**:

- `index.html` — one self-contained page, uses `three.js` from CDN
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  opens by double-clicking in any modern browser. **No build step, no `npm install`,
  no Python server, no Godot.** It must render within 3 seconds on a normal laptop.
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

# 暗黑寓言（Grim Fable）

在 `/workspace/game/` 用 Godot 4 开发 **Grim Fable**——一款分支叙事的黑暗童话
视觉小说。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以
作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

你踏入了那些你以为自己早已熟知的童话——但林子比你记忆中更幽暗，善良的人并不
总是好人，而邪恶者或许自有其理由。Grim Fable 是一款**选择驱动的视觉小说**，
玩家以主角的身份重历那些耳熟能详的故事书篇章，但摆在面前的选项从来不曾出现在
原本的讲述里。看似睡前故事的东西藏着一个令人不安的真相，而玩家的决定决定了
那个真相的哪个版本会成真。

游戏的幻想内核是**重写一个你自以为知道的故事**。游戏应当把玩家自身的预期变成
陷阱：一个深受喜爱的故事以熟悉的方式开场，随后岔向童话从不允许的结果。循环的
核心是**阅读、检视、权衡、决断**——沉浸进一个文笔丰盈的场景，仔细看清插画在
隐藏什么，估量该信谁、该信什么，然后敲定一个故事会记住并在后续给出回报的选项。
它应当让人感觉像在翻动一本闹鬼的图画书，其中文本、立绘、背景与选项菜单都属于
同一个精心编排的世界。这是一本打磨精良、氛围浓厚且真有代价的故事书，拥有确实
不同的结局，而不是一份只有单一路径的线性文本倾泻。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家开启这个故事，被
   缓缓引入一个熟悉的童话前提，以带有角色、旁白的插画故事书场景呈现，并清晰
   交代他们是谁、身处何地。
2. **阅读与检视场景** —— 故事通过节奏得当的对话与旁白在插画背景上展开，但场景
   不只是被阅读——它邀请你去调查。道具、场景中的细节以及在场的角色，都可能藏着
   玩家原本会错过的旁白、线索或秘密，因此那个温馨故事的阴暗面是玩家自己揭开的，
   而不只是被告知的。
3. **逐渐拼合的线索** —— 玩家检视到、了解到的东西会被**收集并记住**：桌上那把
   注意到的带血斑的刀、从某个角色口中套出的一句自白、一个与故事书版本相矛盾的
   细节。这些发现会累积成玩家的认知，并解锁或渲染其后的选项与揭晓，从而奖励
   那些仔细观察的好奇玩家，而不是一路猛冲的玩家。
4. **有意义的选项** —— 在关键时刻，玩家会得到原本故事从未给过他们的选项——信任
   谁、揭露什么、走林中的哪条路。选项是有代价的审慎决定，而不是装点门面的风味
   文本；玩家已揭开的内容会塑造哪些选项可用、以及它们意味着什么，而游戏会明确
   表示一个决定已经做出并被记录。
5. **会留下痕迹的后果** —— 早先的选项会被记住，并塑造后续的走向：哪些角色会向
   玩家吐露心事、哪些真相会浮出水面、哪些门会关上。玩家应当感觉故事在围着他们
   的决定弯折，而不是在轨道上照跑，而反复出现的故事或回归的角色也应当反映出
   玩家先前做过的事。
6. **分岔的结局** —— 故事会以数个确实不同的结局之一收束——对幸福结局的颠覆、
   一场冷酷的清算、一个被揭开的隐秘真相，或一次静默的逃离——每一个都通过不同的
   选项抵达，并与玩家的玩法明确挂钩。结局是一段精心编排、有设计感的结语，点明
   玩家所走的路带来了什么，而玩家可以重新开始，去寻找另一个结局。

## 提交格式（HTML）

交付物 **两个文件**：

- `index.html` —— 双击即开的单文件页面, 走 CDN 引入 `three.js`
  (`<script type="module">import * as THREE from 'https://unpkg.com/three@0.169.0/build/three.module.js'</script>`),
  **不允许** `npm install` / 构建工具 / Python 服务器 / Godot。普通笔记本 3 秒内必须渲染出来。
- `game_logic.js` —— 纯逻辑层 `createGame(opts)` / `advance(game, input, dt)`,
  由 `index.html` import。规范参考 `bench/references/tg1/game_logic.js`。

约束：
- 全部资产程序化生成(颜色、立方体、球体), 不运行时外取图像/音频。
- 键盘输入 `WASD + 空格 + Enter + ESC`。
- `index.html` 不发生运行时 `fetch/XHR`; 除 three.js 外不引入别的 CDN。
- 体量：`game_logic.js ≤ 220 行`, `index.html ≤ 120 KB`。

