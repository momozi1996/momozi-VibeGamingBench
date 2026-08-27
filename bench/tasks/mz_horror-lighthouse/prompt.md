# Horror Lighthouse

Build a **Horror Lighthouse** game as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a lighthouse keeper during an endless storm, maintaining the light
to guide ships safely past the rocks while something in the water tries to lure
them onto the shore. The fantasy is lonely duty against cosmic dread: the beam
is the only thing between sailors and death, but keeping it lit attracts the
attention of what lurks below. Tension comes from fuel management, mechanical
breakdowns, and the creature's escalating attempts to extinguish the light or
drive the keeper mad.

## What the Player Experiences

1. **Title Screen** — A stormy coastal scene with a lighthouse beam sweeping
   through rain, the game name in weathered serif font, and a play button.
2. **The Lighthouse** — A cross-section view showing multiple floors: the lamp
   room at top, living quarters in the middle, fuel storage at the bottom, and
   the dock outside. The player moves between floors.
3. **Light Maintenance** — The lamp burns fuel and occasionally malfunctions. The
   player must refuel from storage below, clean the lens when spray coats it,
   and repair the rotation mechanism when it jams. If the light goes out, ships
   crash.
4. **Ship Guidance** — Ships appear on the dark ocean as distant lights. The
   player must keep the beam rotating to warn them of rocks. Successfully guided
   ships pass safely; crashed ships add wreckage and guilt.
5. **Fuel Management** — Fuel is limited. Supply boats come periodically but the
   storm delays them. The player must ration fuel, choosing between full
   brightness (safe but drains fast) and dim mode (conserves fuel but ships may
   not see it).
6. **The Creature** — Something in the water interferes: tentacles reach for the
   dock, bioluminescent lures mimic ship lights to confuse the keeper, and
   whispers try to convince the player to extinguish the lamp. The player must
   resist and repair damage.
7. **Escalation** — Each night the storm worsens, fuel becomes scarcer, and the
   creature grows bolder. The final night requires the player to keep the light
   burning through a direct assault while guiding the last ship to safety.

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

# 恐怖灯塔（Horror Lighthouse）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖灯塔**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名在无尽风暴中值守的灯塔看守人，必须维持灯光运转，引导船只安全绕过
礁石，而水中的某种东西却试图把它们引向岸边撞毁。游戏的幻想核心是孤独的职守
对抗宇宙级恐惧：光束是水手与死亡之间唯一的屏障，但让它亮着就会引来潜伏在
水下之物的注意。紧张感来自燃料管理、机械故障，以及那个生物一次比一次更凶猛的
企图——熄灭灯光，或者把看守人逼疯。

## 玩家体验流程

1. **标题画面** —— 一幅风暴中的海岸场景，灯塔光束在雨中扫过，游戏名采用饱经
   风霜的衬线字体，还有一个开始按钮。
2. **灯塔** —— 一个剖面视图，展示多个楼层：顶部的灯室、中部的居住舱、底部的
   燃料仓库，以及屋外的码头。玩家可以在楼层间移动。
3. **灯光维护** —— 灯会消耗燃料，并偶尔发生故障。玩家必须从下方的仓库补充
   燃料、在浪花糊住镜片时清洁它、在旋转机构卡死时进行修理。如果灯光熄灭，
   船只就会撞毁。
4. **船只引导** —— 船只会以远处灯火的形式出现在漆黑的海面上。玩家必须保持
   光束旋转以警告它们避开礁石。被成功引导的船只会安全通过；撞毁的船只则留下
   残骸与罪责。
5. **燃料管理** —— 燃料是有限的。补给船会定期前来，但风暴会延误它们。玩家
   必须节约用料，在全亮模式（安全但消耗很快）与昏暗模式（省燃料但船只可能
   看不见）之间做选择。
6. **那个生物** —— 水中的某种东西会前来干扰：触手伸向码头、生物发光的诱饵
   模仿船只灯火来迷惑看守人、低语试图说服玩家熄灭灯火。玩家必须抵抗它并
   修复损坏。
7. **逐步升级** —— 每一夜风暴都会更猛，燃料更加稀缺，那个生物也更加大胆。
   最后一夜要求玩家在一场正面袭击中让灯光持续燃烧，同时把最后一艘船引导至
   安全处。

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

