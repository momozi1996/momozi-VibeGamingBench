# Submarine Pressure Rescue

Build **Submarine Pressure Rescue**, a compact **submarine damage-control and
rescue simulation** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype.
It is a **complete, shippable micro-game** that could sit on an itch.io page or
Steam as a polished vertical slice.

## Core Vision

The player commands a battered rescue sub sinking toward crush depth. Water
pours through breached compartments, pressure climbs, oxygen bleeds out, and
the power grid can only feed so many systems at once. Every order is a tradeoff:
seal a bulkhead to slow flooding but trap a crewmate, reroute power to pumps
but lose sonar, send the engineer to patch a hull breach while the med bay goes
unattended. The fantasy is desperate, competent leadership under impossible
constraints — keeping a dying vessel alive long enough to reach the rescue
beacon and bring survivors home.

The tone is tense industrial survival: dark hull cross-sections, warning lights,
blue sonar sweeps, valve icons, crew markers, and clear alarm feedback.

## What the Player Experiences

The player opens to a styled submarine rescue title screen with hull silhouette
and emergency signal. A mission briefing introduces the objective, crew roster,
and initial damage state.

Once the mission begins, the player sees the sub's compartment layout with
water levels, pressure gauges, oxygen, and power routing. Early damage is
manageable — a single leak, one crew member to assign. The player learns the
rhythm: identify the threat, assign crew, watch the repair progress, check
the sonar for distance to the beacon.

As the mission continues, failures cascade. A second compartment breaches while
the first is still being pumped. Power drops and the player must choose which
systems stay online. Oxygen falls in sealed sections. Crew members get trapped
or injured. The sonar shows the beacon getting closer, but new hazards appear
on the route.

In the final stretch, everything is failing simultaneously. The player makes
rapid imperfect calls — sacrifice a compartment to save the rest, burn the last
power reserve on pumps, hope the hull holds. Reaching the beacon and
stabilizing the vessel shows rescue success. Hull collapse, oxygen depletion,
or failed evacuation shows defeat. Both outcomes are styled and navigable.

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

# 潜艇压力救援（Submarine Pressure Rescue）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Submarine Pressure Rescue**，一款小体量的**潜艇损害管制与救援模拟**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家指挥一艘伤痕累累的救援潜艇，正朝着压毁深度下沉。海水从破损的舱室涌入，压力攀升，氧气流失，而电网一次只能供得起有限的系统。每一道命令都是一次取舍：封闭隔壁能减缓进水，却会困住一名船员；把电力改道给抽水泵，就会失去声呐；派工程师去补船体破口，医务室就无人照看。这里的幻想是在不可能的约束下做出绝望而胜任的领导决断——让一艘正在死去的船撑得够久，抵达救援信标并把生还者带回家。

整体基调是紧张的工业求生感：昏暗的船体剖面图、警示灯、蓝色的声呐扫描、阀门图标、船员标记，以及清晰的警报反馈。

## 玩家体验流程

玩家一进入游戏，看到的是一个经过美术处理的潜艇救援标题画面，带有船体剪影和紧急信号。一段任务简报介绍目标、船员名单和初始受损状态。

任务开始后，玩家看到潜艇的舱室布局，附带水位、压力表、氧气和电力路由。早期的损伤还应付得来——一处漏水，一名船员可供派遣。玩家从中学会节奏：辨明威胁、分派船员、盯着维修进度、查看声呐上到信标的距离。

随着任务推进，故障开始连锁。第一个舱室还在抽水，第二个就破损了。电力下降，玩家必须选择哪些系统继续在线。封闭区段里氧气下降。船员被困或受伤。声呐显示信标越来越近，但航线上又出现了新的危险。

到了最后一段路程，一切都在同时崩坏。玩家做出快速而并不完美的判断——牺牲一个舱室来保住其余部分，把最后一点电力储备烧在抽水泵上，指望船体撑得住。抵达信标并稳住船体则显示救援成功。船体崩塌、氧气耗尽或撤离失败则显示落败。两种结局都经过美术处理并可继续操作导航。

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

