# Last Signal

Build **Last Signal**, a post-apocalyptic radio visual novel of scarce
resources and hard choices, as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a
prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

The world has gone quiet, and you keep the night watch over a small radio
station that still has power. Out of the static, survivors call in — hungry,
hunted, frightened, sometimes lying. You answer with the only things you have
left: a thin store of supplies, a failing generator, and your judgment. Last
Signal is a **choice-driven visual novel of triage** where every call asks you
to decide who to help, who to turn away, who to believe — and the resources you
spend and the people you save or abandon decide what the long night makes of
you.

The fantasy is **holding a fragile lifeline together while it runs out**. The
heart of the loop is **listen, weigh, decide, live with it** — taking in a
caller's plea, judging it against what little you can spare, and committing to a
choice that costs something real and is remembered. Generosity may empty your
stores before dawn; caution may save you and damn others. The writing should
make those trade-offs weigh on the player. It should play like a tense,
atmospheric survival drama with real stakes and genuinely different endings, not
a linear script with one outcome.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player takes the night
   watch and is grounded in the station, the dead world outside, and the scarce
   resources they keep, presented as illustrated scenes with narration and a
   sense of place.
2. **Calls Out of the Static** — Survivors reach the player over the radio, each
   a distinct voice with their own situation, plea, and shadow of doubt — a
   family at a roadblock, a stranger who knows too much, a voice that may be
   bait. Calls feel like meeting people, not picking from an identical list.
3. **Decisions That Cost** — For each call the player makes a real choice — send
   supplies, open the door, talk them down, refuse, or probe for the truth — and
   choices visibly spend the player's limited resources (supplies, power, trust,
   or equivalent), so generosity and caution both have a price. The player can
   always see what they have left, and the decision is clearly registered.
4. **A Night That Remembers** — Resources and earlier decisions are carried
   forward and shape what comes later: who calls back, who can still be helped,
   which options remain affordable, and how others come to regard the station.
   Running low changes what the player can do, and a choice made early should
   visibly matter much later in the night.
5. **Many Ways for Dawn to Break** — The night resolves in one of several
   genuinely different endings — a beacon that saved many, a cold survivor who
   outlasted everyone, a station that gave until it had nothing left, or a
   darker truth uncovered — each reachable through how the player spent and
   chose, shown as an authored, styled conclusion that names what the watch
   became. The player can take the watch again to face the night differently.

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

# 最后的信号（Last Signal）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Last Signal**——一款关于资源匮乏与
艰难抉择的后启示录电台视觉小说。这不是原型，而是一个**完整、可发布的微型
游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

世界已经沉寂，而你在一座仍有电力的小型广播电台里值守夜班。从静电噪声中，
幸存者们打来电话——饥饿的、被追猎的、恐惧的，有时是在撒谎的。你只能用手上仅剩
的东西来回应：一份微薄的物资储备、一台快要罢工的发电机，以及你的判断力。
Last Signal 是一款**选择驱动的分诊式视觉小说**，每一通来电都要求你决定帮谁、
拒谁、信谁——而你花掉的资源、你救下或抛弃的人，决定了这漫漫长夜把你变成什么样。

游戏的幻想内核是**在一条脆弱的生命线耗尽之前把它维系住**。循环的核心是
**倾听、权衡、决断、承受**——听完一位来电者的请求，对照你能挤出的那一点东西
去判断，然后敲定一个真有代价、且会被记住的选项。慷慨可能会让你的库存在天亮
之前就见底；谨慎可能救了你自己，却害了别人。文本应当让这些取舍在玩家心里压出
分量。它玩起来应当像一部紧张、氛围浓厚且真有代价的生存剧，拥有确实不同的
结局，而不是一份只有单一结果的线性剧本。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家接下夜班值守，被
   扎根于这座电台、外面那个死去的世界，以及他们守着的匮乏资源之中，以带有旁白
   和地点氛围的插画场景呈现。
2. **来自静电噪声的呼叫** —— 幸存者通过无线电联系上玩家，每一个都是一个独特的
   声音，有自己的处境、请求，以及一层可疑的阴影——路障处的一家人、一个知道得
   太多的陌生人、一个可能是诱饵的声音。这些来电应当让人感觉像在与人相遇，而
   不是从一份千篇一律的清单里挑选。
3. **有代价的决定** —— 对每一通来电，玩家都要做出真实的选项——送出物资、开门
   接纳、劝下对方、拒绝，或试探真相——而选项会明显消耗玩家有限的资源（物资、
   电力、信任或等价物），因此慷慨与谨慎都各有其代价。玩家始终能看到自己还剩
   什么，而决定会被清晰地记录下来。
4. **会记住一切的夜晚** —— 资源和先前的决定会被延续下去，并塑造后续的走向：
   谁会再打回来、谁还救得回来、哪些选项仍然负担得起，以及别人如何看待这座
   电台。库存告急会改变玩家能做的事，而一个很早做出的选项，应当在深夜里明显
   地起作用。
5. **黎明降临的多种方式** —— 这个夜晚会以数个确实不同的结局之一收束——一座
   救下了许多人的灯塔、一个熬过了所有人的冷血幸存者、一座给到一无所有的电台，
   或一个被揭开的更黑暗的真相——每一个都通过玩家如何花费、如何选择来抵达，并以
   精心编排、有设计感的结语呈现，点明这场值守成为了什么。玩家可以再接一次夜班，
   以另一种方式面对这个夜晚。

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

