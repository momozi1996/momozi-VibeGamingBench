# Dungeon Master

Build **Dungeon Master**, a **dungeon management tycoon game** as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

The player is the villain: dig rooms in the earth, fill them with traps and
monsters, and watch greedy heroes stumble in to be defeated. But monsters are
not free — they need gold to recruit, food to keep happy, and rooms that suit
their nature. Heroes arrive in waves of increasing strength, and each one that
escapes spreads word of an easy dungeon, attracting tougher adventurers. The
tension is economic: gold comes from defeated heroes' loot, but spending it all
on offense leaves nothing for creature comforts, and unhappy monsters desert.
The fantasy is running an evil enterprise where the product is doom and the
customers are uninvited.

## What the Player Experiences

From the title screen the player starts a new dungeon. The view shows a
cross-section of earth. The player digs rooms by spending gold, creating a
layout of corridors and chambers. Each room can be designated: treasure rooms
lure heroes deeper, trap rooms damage them, barracks house monsters, and
hatcheries produce food.

Monsters are recruited from a roster — each type has a gold cost, preferred
room type, and combat strength. Placing monsters in rooms they like keeps
morale high; cramming them into unsuitable spaces makes them grumpy and
eventually causes desertion. The creature happiness meter is always visible.

Heroes arrive periodically, entering from the surface and navigating toward
treasure. They fight monsters, trigger traps, and either die (dropping loot)
or escape. Escaped heroes increase the dungeon's fame, attracting stronger
parties next wave. The player must balance dungeon depth, trap density, and
monster strength against the escalating threat.

The game tracks gold, creature count, and waves survived. A styled result
screen shows dungeon statistics when the dungeon heart is destroyed by heroes
or a wave milestone is reached.

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

# 地下城主（Dungeon Master）

在 `/workspace/game/` 用 Godot 4 开发 **Dungeon Master**，一款**地下城管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演反派：在地底挖掘房间，往里填满陷阱和怪物，看着贪婪的英雄们一头闯进来被打败。但怪物不是免费的——招募它们要花金币，让它们开心要喂食物，还得有符合它们天性的房间。英雄会以强度递增的波次到来，而每一个逃脱的英雄都会散播"这地下城很好打"的消息，招来更强悍的冒险者。张力是经济层面的：金币来自被击败英雄的战利品，但全都花在攻势上就没钱照顾怪物的生活，而不开心的怪物会叛逃。这里的幻想是经营一家邪恶企业，产品是毁灭，客户则是不请自来的。

## 玩家体验流程

玩家从标题画面开始一座新的地下城。视图呈现的是一幅大地剖面。玩家花金币挖掘房间，构建出走廊与厅室的布局。每个房间都可以指定用途：宝库诱使英雄深入，陷阱房伤害他们，兵营容纳怪物，孵化场生产食物。

怪物从一份名录中招募——每个种类都有金币成本、偏好的房间类型和战斗强度。把怪物安置在它们喜欢的房间里能保持士气高涨；把它们硬塞进不合适的空间会让它们变得暴躁，最终导致叛逃。生物幸福度计量表始终可见。

英雄会周期性到来，从地表进入并朝宝藏推进。他们会与怪物战斗、触发陷阱，最终要么死亡（掉落战利品），要么逃脱。逃脱的英雄会提升地下城的名声，招来下一波更强的队伍。玩家必须在地下城深度、陷阱密度和怪物强度之间取得平衡，以应对不断升级的威胁。

游戏会记录金币、生物数量和已存活的波次数。当地下城之心被英雄摧毁，或达成某个波次里程碑时，一个经过美术处理的结算画面会展示地下城统计数据。

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

