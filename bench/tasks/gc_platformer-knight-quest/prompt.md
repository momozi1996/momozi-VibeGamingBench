# Knight Quest

Build **Knight Quest**, a retro action platformer with melee combat and
sub-weapons as a self-contained, double-click-to-play HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is a
**complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

An armored knight ventures forth from a peaceful village hub into eight themed
stages — haunted crypt, volcanic forge, frozen peak, sunken temple, sky
fortress, poison swamp, clockwork tower, and shadow throne — each ending in a
boss encounter. The knight wields a primary melee weapon with a satisfying
three-hit combo and collects sub-weapons (throwing axe, boomerang cross, holy
water, dagger) that consume a shared ammo resource. Stages are linear but hide
optional treasure chests behind skill challenges. Between stages the village
hub offers a shop for health upgrades and sub-weapon restocks. The tone is
bright, chunky pixel-art nostalgia with modern responsive controls.

## What the Player Experiences

A title screen shows the game name, the knight's silhouette, and Start/Continue
options. Starting fresh places the player in the village hub — a small
scrolling area with a shop NPC and a stage-select gate showing eight portals
(only the first unlocked initially).

Entering a stage begins a side-scrolling level with platforms, pits, and
enemies. The knight attacks with a melee combo and can use sub-weapons with a
secondary button. Enemies drop gems for the shop and occasional health pickups.
Each stage ends with a boss that has a visible health bar and telegraphed attack
patterns. Defeating the boss unlocks the next stage and returns to the hub.

The shop sells health capacity upgrades, sub-weapon ammo packs, and a damage
boost. Progress is saved between sessions. Completing all eight stages triggers
a victory screen with stats.

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

# 骑士征途（Knight Quest）

在 `/workspace/game/` 用 Godot 4 开发 **Knight Quest**，一款带近战战斗与副武器的复古动作平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名披甲骑士从一个宁静的村庄枢纽出发，前往八个主题关卡——闹鬼地穴、火山锻炉、冰封之巅、沉没神殿、天空堡垒、毒沼、机械钟楼与暗影王座——每个关卡都以一场 Boss 战收尾。骑士手持一把主近战武器，能打出令人满足的三段连击，并会收集消耗共享弹药资源的副武器（投掷斧、回旋十字、圣水、匕首）。关卡是线性的，但会把可选的宝箱藏在技巧挑战之后。关卡之间，村庄枢纽提供一家商店用于血量升级和副武器补货。整体调性是明亮、厚实的像素画怀旧感，配上现代化的灵敏操控。

## 玩家体验流程

标题画面显示游戏名、骑士的剪影，以及开始/继续选项。全新开局会把玩家放在村庄枢纽——一小片可滚动的区域，有一位商店 NPC 和一道显示八个传送门的选关之门（初始只解锁第一个）。

进入一个关卡便开始一段横向滚动的流程，其中有平台、陷坑和敌人。骑士以近战连击攻击，并可用副按键使用副武器。敌人掉落用于商店的宝石和偶尔出现的血量拾取物。每个关卡都以一场 Boss 战结束，Boss 有可见的血条和有预示动作的攻击套路。击败 Boss 会解锁下一个关卡并返回枢纽。

商店出售血量上限升级、副武器弹药包和一项伤害加成。进度在多次会话之间保存。通过全部八个关卡会触发一个带统计数据的胜利画面。

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

