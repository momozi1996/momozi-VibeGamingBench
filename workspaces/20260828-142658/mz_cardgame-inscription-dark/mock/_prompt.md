# Cardgame Inscription Dark

Build a Cardgame Inscription Dark as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A dark and atmospheric card battle game where creatures are summoned by
sacrificing other creatures. The player places cards on a grid battlefield,
but powerful cards demand blood — weaker creatures must be sacrificed to fuel
stronger summons. Each card bears sigils (passive abilities) that create
emergent interactions: a card with "Airborne" flies over blockers; one with
"Bifurcated Strike" hits two lanes. An overworld map connects encounters with
branching paths, and a creeping meta-narrative unfolds through environmental
storytelling. The fantasy is the unsettling thrill of sacrificing your own
creatures for power, wrapped in a cabin-horror atmosphere.

## What the Player Experiences

1. **Title Screen** — A dimly lit wooden table with the game name scratched
   into the surface in rough lettering, a flickering candle, and a "Begin"
   card the player clicks. No plain HTML grey.
2. **The Table** — Battles take place on a 4-lane grid. The player's row faces
   the opponent's row. Cards are played from hand into lanes. Each card has
   attack power, health, a blood cost, and zero or more sigils.
3. **Sacrifice Mechanic** — To play a card costing 2 blood, the player must
   first sacrifice 2 of their own creatures already on the field. Sacrificed
   creatures die with a visual effect. Free cards (0 cost) serve as sacrifice
   fodder. This creates a constant tension between board presence and power.
4. **Sigils** — At least 8 distinct sigils with unique icons: Airborne (attacks
   directly), Bifurcated Strike (hits adjacent lanes too), Mighty Leap (blocks
   Airborne), Stinky (adjacent enemies lose 1 attack), Unkillable (returns to
   hand on death), Fledgling (evolves after 1 turn), Touch of Death (kills
   anything it damages), Many Lives (has 3 extra lives).
5. **Damage Scale** — A balance scale tips as damage is dealt. When one side
   takes 5 more total damage than the other, that side loses. The scale
   visually tips with each hit, creating tension as it approaches the tipping
   point.
6. **Overworld Map** — Between battles, a branching path map shows nodes:
   card battles, totem poles (add a sigil to a card), campfires (merge two
   cards), and traders (buy/sell cards). The player chooses their route.
7. **Atmosphere** — Dark, muted colour palette. Cards look hand-drawn on
   parchment. The opponent is a shadowy figure whose eyes glow. Ambient
   effects (dust motes, candle flicker) reinforce the unsettling mood.

## Assets

2D assets are mounted read-only at:

- `/workspace/assets/library/` — Kenney CC0 packs (sprites, tiles, UI, fonts).
- `/workspace/assets/library-oga/` — OpenGameArt entries; respect each
  subdir's `LICENSE.txt`.

Browse the library and choose packs.
Copy what you need into your project's `assets/` folder.

## Project layout

```
./
  project.html
  Main.tscn
  demo_outputs/    ← your input traces (1–10 files)
  scripts/  scenes/  assets/
```

The build must launch cleanly with:

```
html --headless --path /workspace/game --quit-after 5
```

A reference for HTML CLI flags is at `/workspace/tools/html_command_line.md`.
 —
anything after `--` is forwarded to the project as user args and silently
ignored by the engine. Correct shape:
`html --headless --quit-after 5 --path . -- --scenario near_victory`.

A screenshot helper is available at `/workspace/tools/screenshot.sh`. Use it to actually see what your UI / battlefield /
result screens look like.

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/frame.png --frames 60
```

To screenshot a specific scenario, append `--scenario <id>` after `--`. The
helper consumes only `--out` / `--frames` / `--scene`; remaining args stay in
`OS.get_cmdline_user_args()` for your game code to read. Example:

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/battle_debug.png --frames 120 --scenario battle
```

## Demos

Ship **1–10 input-trace files** under `./demo_outputs/`, one per
demo, each named `*.json`. The evaluator launches a fresh game per trace,
replays your trace as synthetic mouse and keyboard input at 1280×720, and
records the screen. Only the first 10 traces by filename are evaluated;
recordings longer than 20 s are sampled from a random 20 s window.

### Scenarios

Normal play should start from the title screen and demonstrate the task's
core gameplay loop.
Demo playback must be deterministic. For demos that need a specific state
(a specific level, combat state, upgrade screen, result state, or late-game
setup), define named scenarios your game loads when launched with:

```
html --path /workspace/game -- --scenario <id>
```

When `--scenario <id>` is present the game must skip menus, set up the named
state deterministically (seed any RNG), and begin accepting input immediately.

### Trace file format

```json
{
  "scenario": "title_flow",
  "duration_frames": 360,
  "events": [
    {"frame": 30,  "type": "mouse_click", "button": "left", "x": 300, "y": 360},
    {"frame": 90,  "type": "key_press",   "keycode": "1"},
    {"frame": 180, "type": "key_press",   "keycode": "SPACE"},
    {"frame": 300, "type": "wait"}
  ]
}
```

- `scenario` — optional; omit for a normal game launch from the title screen.
- `duration_frames` — total frames to record at 30 fps; cap at **600 (20 s)**.
- `events` — time-ordered inputs. Coordinates are pixels in the 1280×720
  viewport. Supported types:
  - `mouse_click`: `{frame, type, button: "left"|"right", x, y}`
  - `mouse_down` / `mouse_up`: `{frame, type, button: "left"|"right", x, y}` —
    use these for drag interactions: emit `mouse_down` at the start point,
    one or more `mouse_move` events along the way, and `mouse_up` at the end.
    A `mouse_click` is a `mouse_down` + `mouse_up` at the same point in tight
    succession.
  - `mouse_move`: `{frame, type, x, y}`
  - `key_press` / `key_down` / `key_up`: `{frame, type, keycode}` — keycodes:
    `A`–`Z`, `0`–`9`, `ESCAPE`, `ENTER`, `SPACE`, `TAB`, `BACKSPACE`,
    `DELETE`, `SHIFT`, `CTRL`, `ALT`, `UP`, `DOWN`, `LEFT`, `RIGHT`.
  - `wait`: `{frame, type}` — anchor frame, no input.

Replay must be deterministic: same trace, fresh launch, same outcome every time.

---

# 中文版提示词

# 黑暗铭刻（Cardgame Inscription Dark）

在 `./` 用 HTML 4 开发一个黑暗铭刻卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款黑暗且氛围浓厚的卡牌对战游戏，召唤生物需要献祭其他生物。玩家把卡牌放到网格
战场上，但强力卡牌索求鲜血——必须献祭较弱的生物来为更强的召唤供能。每张卡都刻有
印记（被动能力），它们会催生出涌现式的互动：带"飞行"的卡越过阻挡者；带"分叉打击"
的卡同时命中两条通道。一张大地图以分支路径串联起各场遭遇，一段悄然渗出的元叙事
则通过环境叙事层层展开。这份幻想在于：在木屋恐怖的氛围包裹下，为力量而献祭自己
生物时那种令人不安的快感。

## 玩家体验流程

1. **标题画面** —— 一张光线昏暗的木桌，游戏名以粗糙的字体刻在桌面上，一支摇曳的
   蜡烛，以及一张供玩家点击的"开始"卡牌。演好默认纯灰。
2. **牌桌** —— 战斗在 4 条通道的网格上展开。玩家的一排面对对手的一排。卡牌从手牌
   打进各条通道。每张卡都有攻击力、生命值、鲜血消耗，以及零个或多个印记。
3. **献祭机制** —— 要打出一张消耗 2 点鲜血的卡，玩家必须先献祭场上自己已有的
   2 个生物。被献祭的生物会伴随视觉效果死去。免费卡牌（0 消耗）可充当献祭素材。
   这在场面控制与力量之间制造出持续的张力。
4. **印记** —— 至少 8 种各具独特图标的印记：飞行（直接攻击）、分叉打击（同时命中
   相邻通道）、强力跃击（可阻挡飞行）、恶臭（相邻敌人攻击力 -1）、不灭（死亡时
   回到手牌）、雏鸟（1 回合后进化）、死亡之触（杀死任何被它伤害的目标）、九命
   （额外拥有 3 条命）。
5. **伤害天平** —— 一座天平会随伤害的造成而倾斜。当一方承受的总伤害比另一方多出
   5 点时，该方落败。天平每次受击都会在视觉上倾斜，随着逼近临界点而制造张力。
6. **大地图** —— 战斗之间会出现一张分支路径地图，上面有各类节点：卡牌对战、图腾柱
   （为一张卡添加印记）、营火（合并两张卡）、商人（买卖卡牌）。玩家自行选择路线。
7. **氛围** —— 黑暗、低饱和的配色。卡牌看起来像手绘在羊皮纸上。对手是一个双眼
   发光的黑影身形。环境效果（浮尘、烛火闪动）进一步强化这种令人不安的情绪。

## 资产

2D 资产以只读方式挂载在：

- `/workspace/assets/library/` —— Kenney CC0 资产包（精灵图、图块、UI、字体）。
- `/workspace/assets/library-oga/` —— OpenGameArt 条目；请遵守各子目录下的
  `LICENSE.txt`。

浏览资产库并挑选合适的资产包。
把需要的文件复制到你项目的 `assets/` 目录下。

## 项目结构

```
./
  project.html
  Main.tscn
  demo_outputs/    ←← 你的输入轨迹（1–10 个文件）
  scripts/  scenes/  assets/
```

构建必须能通过以下命令干净启动：

```
html --headless --path /workspace/game --quit-after 5
```

HTML 命令行参数的参考文档在 `/workspace/tools/html_command_line.md`。
**像 `--headless` 和 `--quit-after N` 这类引擎参数必须写在 `--` 之前** ——
`--` 之后的一切都会作为用户参数转发给项目，引擎本身会静默忽略。正确写法：
`html --headless --quit-after 5 --path . -- --scenario near_victory`。

`/workspace/tools/screenshot.sh` 提供了截图辅助工具。用它来实际查看你的
UI / battlefield / result 画面长什么样。

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/frame.png --frames 60
```

要给特定场景截图，在 `--` 之后追加 `--scenario <id>`。该工具只消费
`--out` / `--frames` / `--scene`；其余参数会留在
`OS.get_cmdline_user_args()` 里供你的游戏代码读取。示例：

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/battle_debug.png --frames 120 --scenario battle
```

## 演示

在 `./demo_outputs/` 下提交 **1–10 个输入轨迹文件**，每个演示一份，
命名为 `*.json`。评测器会为每条轨迹启动一个全新的游戏实例，在 1280×720
分辨率下把你的轨迹作为合成的鼠标与键盘输入回放，并录制屏幕。只有按文件名排序的
前 10 条轨迹会被评测；超过 20 秒的录像会从随机的 20 秒窗口中采样。

### 场景（Scenarios）

常规玩法应当从标题画面开始，并演示该任务的核心游戏循环。
演示回放必须是确定性的。对于需要特定状态的演示（某个特定关卡、战斗状态、
升级界面、结算状态或后期配置），请定义具名场景，让你的游戏在以下方式启动时加载它们：

```
html --path /workspace/game -- --scenario <id>
```

当 `--scenario <id>` 存在时，游戏必须跳过菜单，确定性地建立该具名状态
（为任何随机数发生器设定种子），并立即开始接受输入。

### 轨迹文件格式

```json
{
  "scenario": "title_flow",
  "duration_frames": 360,
  "events": [
    {"frame": 30,  "type": "mouse_click", "button": "left", "x": 300, "y": 360},
    {"frame": 90,  "type": "key_press",   "keycode": "1"},
    {"frame": 180, "type": "key_press",   "keycode": "SPACE"},
    {"frame": 300, "type": "wait"}
  ]
}
```

- `scenario` —— 可选；从标题画面常规启动游戏时省略此字段。
- `duration_frames` —— 以 30 fps 录制的总帧数；上限为 **600（20 秒）**。
- `events` —— 按时间排序的输入。坐标是 1280×720 视口内的像素值。
  支持的类型：
  - `mouse_click`：`{frame, type, button: "left"|"right", x, y}`
  - `mouse_down` / `mouse_up`：`{frame, type, button: "left"|"right", x, y}` ——
    用它们实现拖拽交互：在起点发出 `mouse_down`，途中发出一个或多个
    `mouse_move` 事件，在终点发出 `mouse_up`。
    一次 `mouse_click` 等价于在同一点上紧邻连续地发出 `mouse_down` + `mouse_up`。
  - `mouse_move`：`{frame, type, x, y}`
  - `key_press` / `key_down` / `key_up`：`{frame, type, keycode}` —— 可用键码：
    `A`–`Z`、`0`–`9`、`ESCAPE`、`ENTER`、`SPACE`、`TAB`、`BACKSPACE`、
    `DELETE`、`SHIFT`、`CTRL`、`ALT`、`UP`、`DOWN`、`LEFT`、`RIGHT`。
  - `wait`：`{frame, type}` —— 锚定帧，不产生输入。

回放必须是确定性的：同一条轨迹、全新启动，每次都得到相同的结果。