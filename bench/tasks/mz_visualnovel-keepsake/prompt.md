# Keepsake

Build **Keepsake**, a quiet memory-reconstruction visual novel about sorting a
late person's belongings, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

Someone has died, and you have been asked to sort through what they left behind.
A faded photograph, a folded letter, a worn ring, a diary with a torn-out
page — each object holds a fragment of a life, and they do not give up their
meaning in order. Keepsake is a **choice-driven visual novel of reconstruction**
where the player examines the keepsakes of a stranger and, piece by piece and
out of sequence, assembles the story of who this person really was — and the
quiet secret time had buried with them.

The fantasy is **piecing together a life from the things it left behind**. The
heart of the loop is **examine, remember, connect, understand** — turning a
keepsake over, hearing the memory it stirs, and fitting it against what you have
already found until a hidden shape emerges. The order the player chooses, and
how they come to read an ambiguous choice the dead made, shape the
understanding they arrive at. It should feel like a slow, tender, melancholy
piece with real emotional weight and more than one way to understand a life, not
a single linear obituary read start to finish.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player is given their
   task — a room, a box, a life's worth of objects to sort — established as a
   quiet illustrated scene with narration that sets the mood and the absence at
   its center.
2. **Examining the Keepsakes** — The player chooses which object to take up,
   in whatever order they like, and each keepsake is examined as an illustrated
   item with the memory or fragment of the past it reveals. The room of
   belongings is something the player works through at their own pace, not a
   fixed slideshow.
3. **Fragments That Connect** — Each examined keepsake adds a remembered
   fragment to what the player knows, and fragments fit against one another:
   a date on a letter explains a photograph, an object's absence answers an
   earlier question. The player feels a life assembling out of order, and what
   they have already found colors how the next piece reads.
4. **A Choice of Understanding** — As the picture comes together the player
   reaches moments of interpretation — how to read an ambiguous decision the
   dead person made, what to believe about a secret, whether to judge or
   forgive. These choices are deliberate and remembered, and what the player has
   uncovered shapes which understandings are even available.
5. **More Than One Way to Remember** — The piece resolves into one of several
   genuinely different closing understandings — a life redeemed, a secret kept
   in kindness, a quiet grief, a truth that recasts everything — each reached
   through which fragments the player found and how they chose to read them,
   and shown as an authored, styled conclusion that names the understanding they
   came to. The player can begin again and arrive somewhere else.

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

# 遗物（Keepsake）

在 `/workspace/game/` 用 Godot 4 开发 **Keepsake**——一款静谧的记忆重构视觉
小说，讲述整理一位逝者遗物的故事。这不是原型，而是一个**完整、可发布的微型
游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

有人去世了，而你被托付去整理他留下的东西。一张褪色的照片、一封折叠的信、一枚
磨损的戒指、一本被撕掉一页的日记——每一件物品都承载着一段人生的碎片，而它们
并不会按顺序交出自己的含义。Keepsake 是一款**选择驱动的重构式视觉小说**，玩家
检视一位陌生人的遗物，一件一件、乱序地拼出这个人究竟是谁——以及时间随他一同
埋葬的那个静默秘密。

游戏的幻想内核是**从一个人留下的东西里拼出他的一生**。循环的核心是
**检视、追忆、串联、理解**——把一件遗物翻过来，听见它勾起的那段记忆，再把它
与你已经找到的东西拼合，直到一个隐藏的形状浮现出来。玩家选择的顺序，以及他们
如何解读逝者做过的某个含义暧昧的选择，塑造了他们最终抵达的理解。它应当让人
感觉像一件缓慢、温柔、忧郁的作品，有真切的情感重量，并且理解一段人生的方式
不止一种，而不是一份从头念到尾的线性讣告。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家被交付了自己的
   任务——一个房间、一只箱子、一整段人生份量的物品要去整理——以一个静谧的插画
   场景配旁白建立起来，奠定基调，以及位于其中心的那份缺席。
2. **检视遗物** —— 玩家可以按自己喜欢的任意顺序选择拿起哪件物品，每件遗物都
   作为一件插画物品被检视，并揭示它所披露的那段记忆或往事碎片。这个满是遗物的
   房间是玩家按自己节奏逐步走完的，而不是一段固定的幻灯片。
3. **彼此串联的碎片** —— 每件被检视的遗物都会给玩家的认知添上一块被追忆起的
   碎片，而碎片之间彼此契合：一封信上的日期解释了一张照片，一件物品的缺席回答了
   先前的一个疑问。玩家会感受到一段人生正在乱序中被组装起来，而他们已经找到的
   东西会渲染下一块碎片的读法。
4. **理解方式的抉择** —— 随着图景逐渐拼合，玩家会来到需要解读的时刻——如何解读
   逝者做过的一个含义暧昧的决定、对一个秘密该信什么、是评判还是原谅。这些选项
   是审慎的、会被记住的，而玩家已揭开的内容会塑造哪些理解方式根本上是否可选。
5. **追忆的方式不止一种** —— 这件作品会收束为数个确实不同的收尾理解之一——一段
   被救赎的人生、一个出于善意被保守的秘密、一份静默的哀伤，或一个改写了一切的
   真相——每一个都通过玩家找到了哪些碎片、以及他们选择如何解读它们来抵达，并以
   精心编排、有设计感的结语呈现，点明他们所抵达的理解。玩家可以重新开始，抵达
   另一处。

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

