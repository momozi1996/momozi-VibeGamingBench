# Pactbound

Build **Pactbound**, a summoner pact-choice visual novel, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a summoner walking a road lined with spirits and monsters, and each one
offers the same dangerous bargain: a pact. Bind it and gain its power, but carry
its price and its loyalties; refuse it and stay clean but weaker; deceive it and
risk what comes due later. Pactbound is a **choice-driven visual novel** where
the player meets a procession of would-be familiars and decides which to bind,
and the **collection of pacts they carry becomes who they are** — shaping which
factions trust them, which paths open, and how the journey ends.

The fantasy is **defining yourself by the bargains you make**. The heart of the
loop is **meet, weigh, bind or break** — encountering a spirit with its own
nature and cost, judging what a pact with it would make of you, and committing
to a bargain the story remembers. A summoner bound to gentle hearth-spirits
walks a different road than one who collected demons, and the writing should make
those allegiances felt. It should play like an atmospheric journey with real
stakes and genuinely different endings, not a linear tour with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player sets out as a
   summoner and is introduced to the road ahead and the bargain at the heart of
   the world, presented as illustrated scenes with characters and narration.
2. **Spirits with Their Own Nature** — Along the way the player meets a variety
   of would-be familiars — a loyal hearth-spirit, a proud beast, a whispering
   demon, and others — each with its own voice, temperament, the power it
   offers, and the price it asks. Encounters feel like meeting distinct
   characters, not picking from an identical list.
3. **Bind, Refuse, or Deceive** — At each spirit the player makes a real choice:
   seal a pact and take on its power and its loyalties, refuse and stay
   unbound, or strike a false bargain with consequences down the line. The
   decision is deliberate and clearly registered, and the player can see what
   they have bound to themselves.
4. **Pacts That Define You** — The pacts the player carries are **remembered and
   accumulate into an identity**: which factions and spirits trust or revile the
   player, which options and dialogue open up, and which later encounters and
   endings become reachable all depend on the company they keep. A choice made
   early should visibly shape a scene much later.
5. **A Journey That Ends Many Ways** — The road resolves in one of several
   genuinely different endings — crowned among monsters, a champion of the
   unbound, a betrayer alone, or a peacemaker between worlds — each reachable
   through the pacts and choices the player made, and shown as an authored,
   styled conclusion that names what they became. The player can set out again
   to bind a different fate.

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

# 契约缚身（Pactbound）

在 `/workspace/game/` 用 Godot 4 开发 **Pactbound**——一款召唤师契约抉择视觉
小说。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

你是一名召唤师，走在一条两侧遍布精灵与怪物的路上，而它们每一个都提出同样一桩
危险的交易：契约。缔结它，你便获得它的力量，但也要背上它的代价与它的效忠；
拒绝它，你保持清白但更加弱小；欺骗它，你则要为日后到期的账单承担风险。
Pactbound 是一款**选择驱动的视觉小说**，玩家会遇见一队接一队渴望成为眷属的
存在，并决定缚结哪些，而**他们所背负的这一整套契约就成了他们是谁**——它塑造了
哪些阵营信任他们、哪些道路会开启，以及这场旅程如何终结。

游戏的幻想内核是**以你所做的交易来定义你自己**。循环的核心是
**相遇、权衡、缚结或断绝**——遇见一个有自己本性与代价的精灵，判断与它缔约会把
你变成什么样，然后敲定一桩故事会记住的交易。缚结于温和的炉灶之灵的召唤师，与
一个收集恶魔的召唤师走的是完全不同的路，而文本应当让这些效忠关系被真切感受到。
它玩起来应当像一场氛围浓厚且真有代价的旅程，拥有确实不同的结局，而不是一趟
只有单一路径的线性观光。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家以召唤师的身份启程，
   被介绍前方的道路以及这个世界核心的那桩交易，以带有角色与旁白的插画场景呈现。
2. **各有本性的精灵** —— 沿途玩家会遇见形形色色渴望成为眷属的存在——一个忠诚的
   炉灶之灵、一头骄傲的野兽、一个低语的恶魔，还有其他——每一个都有自己的声音、
   性情、它提供的力量，以及它索取的代价。这些遭遇应当让人感觉像在与各具特色的
   角色相遇，而不是从一份千篇一律的清单里挑选。
3. **缚结、拒绝，或欺骗** —— 面对每一个精灵，玩家都要做出真实的选项：封定契约
   并承受它的力量与它的效忠、拒绝并保持未缚状态，或者达成一桩虚假的交易而留下
   日后的后果。决定是审慎的、会被清晰记录的，而玩家可以看到自己都把什么缚结到了
   身上。
4. **定义你的契约** —— 玩家所背负的契约会被**记住并累积成一种身份**：哪些阵营
   与精灵信任或厌恶玩家、哪些选项与对话会开放、哪些后续遭遇与结局变得可以抵达，
   全都取决于他们所结交的伙伴。一个很早做出的选项，应当明显地塑造一个很晚出现
   的场景。
5. **有多种终结方式的旅程** —— 这条路会以数个确实不同的结局之一收束——在群魔之中
   加冕、成为未缚者的守护者、成为一个孤身的背叛者，或成为世界之间的调停者——
   每一个都通过玩家缔结的契约与做出的选择来抵达，并以精心编排、有设计感的结语
   呈现，点明他们成为了什么。玩家可以再次启程，去缚结另一种命运。

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

