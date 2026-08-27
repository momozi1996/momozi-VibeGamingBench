# Iron Vanguard

Build **Iron Vanguard**, a 2D top-down grid-based tactical tank defense game in
Godot 4 at `/workspace/game/`. This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A lone armored tank holds the line against relentless waves of automated
warmachines bearing down on a critical command core. The tension lives in
positioning and restraint: movement is grid-locked, only one shell can exist on
screen at a time, and every shot must count because the enemy never stops
advancing. The player is always choosing between pushing forward to intercept a
flanking column and falling back to guard the core from a breakthrough. Terrain
shapes every engagement — brick barricades offer temporary cover until they
crumble, steel walls funnel traffic into kill zones, and mud patches punish
careless repositioning. The risk is always the same: one shell slips past, one
enemy reaches the core, and the defense collapses instantly. The tone is gritty
dieselpunk — rust-iron plating, neon hazard lines, deep shadows, and the
percussive flash of shell impacts.

## What the Player Experiences

A dark industrial title screen sets the mood before the player enters a tactical
map showing available defense zones. Each zone is a distinct battlefield with its
own layout and enemy composition, inviting the player to choose where to make
their stand.

Combat drops the player's tank onto a grid battlefield adjacent to the glowing
command core. The field is a maze of destructible brick walls, impenetrable steel
barriers, and treacherous mud patches. Enemies pour from spawn points at the top
of the screen in waves, each wave more aggressive than the last. Some enemies
rush the core directly, others hunt the player, and specialized carriers glow
with salvageable cargo.

The player steers with grid-locked directional inputs and fires a single shell at
a time — no spray-and-pray, just deliberate aim. Destroying a carrier drops
battlefield salvage: armor repairs, temporary fortifications around the core, or
an EMP pulse that freezes everything on screen. Taking hits degrades the tank's
hull layer by layer; lose all armor and a life is spent.

Victory comes when the last enemy in the wave queue is destroyed, rewarding the
player with accuracy metrics and unlocking the next zone. Defeat is instant if
the core takes a single hit, or gradual if lives run out. Either way the player
returns to the map to regroup and try again.

## Assets

2D assets are mounted read-only at:

- `/workspace/assets/library/` — Kenney CC0 packs (sprites, tiles, UI, fonts).
- `/workspace/assets/library-oga/` — OpenGameArt entries; respect each
  subdir's `LICENSE.txt`.

Browse the library and choose packs.
Copy what you need into your project's `assets/` folder.

## Project layout

```
/workspace/game/
  project.godot
  Main.tscn
  demo_outputs/    ← your input traces (1–10 files)
  scripts/  scenes/  assets/
```

The build must launch cleanly with:

```
godot --headless --path /workspace/game --quit-after 5
```

A reference for Godot CLI flags is at `/workspace/tools/godot_command_line.md`.
**Engine flags like `--headless` and `--quit-after N` must come BEFORE `--`** —
anything after `--` is forwarded to the project as user args and silently
ignored by the engine. Correct shape:
`godot --headless --quit-after 5 --path . -- --scenario near_victory`.

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

Ship **1–10 input-trace files** under `/workspace/game/demo_outputs/`, one per
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
godot --path /workspace/game -- --scenario <id>
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

# 铁血先锋（Iron Vanguard）

在 `/workspace/game/` 用 Godot 4 开发 **Iron Vanguard**，一款 2D 俯视视角、基于网格的战术坦克防守游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一辆孤零零的装甲坦克，独自挡住一波又一波扑向关键指挥核心的自动战争机械。张力就在于站位与克制：移动被锁定在网格上，屏幕上同时只能存在一枚炮弹，而且敌人从不停止推进，所以每一发都必须命中要点。玩家永远在两件事之间抉择：前压去截击一支侧翼纵队，还是回撤守住核心以防被突破。地形塑造着每一场交战——砖砌路障提供临时掩体，直到它们崩解；钢墙把敌人流量引入杀伤区；泥地则惩罚草率的重新占位。风险始终如一：一发炮弹漏过、一个敌人抵达核心，防线就会瞬间崩塌。整体调性是粗砺的柴油朋克——锈铁装甲板、霓虹警示条纹、深重阴影，以及炮弹命中时敲击般的闪光。

## 玩家体验流程

一个暗黑工业风的标题画面奠定气氛，随后玩家进入一张显示可选防守区域的战术地图。每个区域都是一处布局与敌人构成各异的战场，邀请玩家自行选择在何处坚守。

战斗把玩家的坦克投放到网格战场上，紧邻发光的指挥核心。战场是一座由可破坏砖墙、无法穿透的钢制屏障和危险泥地构成的迷宫。敌人成波地从屏幕顶部的出生点涌出，每一波都比上一波更凶悍。有些敌人直冲核心，有些猎杀玩家，而特殊的运输载具则闪着可回收物资的光。

玩家用网格锁定的方向输入操控，并且同时只发射一枚炮弹——没有乱扫乱射，只有刻意瞄准。摧毁一辆运输载具会掉落战场回收物：装甲修复、核心周围的临时防御工事，或是一记冻结全屏一切的 EMP 脉冲。受到打击会一层层削掉坦克的装甲；装甲全失就损失一条命。

当波次队列中的最后一个敌人被摧毁时便取得胜利，玩家会获得命中率数据并解锁下一个区域。若核心受到哪怕一次打击就是立刻失败，若生命耗尽则是渐进的失败。无论哪种情况，玩家都会回到地图重整并再次尝试。

## 资产

2D 资产以只读方式挂载在：

- `/workspace/assets/library/` —— Kenney CC0 资产包（精灵图、图块、UI、字体）。
- `/workspace/assets/library-oga/` —— OpenGameArt 条目；请遵守各子目录下的
  `LICENSE.txt`。

浏览资产库并挑选合适的资产包。
把需要的文件复制到你项目的 `assets/` 目录下。

## 项目结构

```
/workspace/game/
  project.godot
  Main.tscn
  demo_outputs/    ←← 你的输入轨迹（1–10 个文件）
  scripts/  scenes/  assets/
```

构建必须能通过以下命令干净启动：

```
godot --headless --path /workspace/game --quit-after 5
```

Godot 命令行参数的参考文档在 `/workspace/tools/godot_command_line.md`。
**像 `--headless` 和 `--quit-after N` 这类引擎参数必须写在 `--` 之前** ——
`--` 之后的一切都会作为用户参数转发给项目，引擎本身会静默忽略。正确写法：
`godot --headless --quit-after 5 --path . -- --scenario near_victory`。

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

在 `/workspace/game/demo_outputs/` 下提交 **1–10 个输入轨迹文件**，每个演示一份，
命名为 `*.json`。评测器会为每条轨迹启动一个全新的游戏实例，在 1280×720
分辨率下把你的轨迹作为合成的鼠标与键盘输入回放，并录制屏幕。只有按文件名排序的
前 10 条轨迹会被评测；超过 20 秒的录像会从随机的 20 秒窗口中采样。

### 场景（Scenarios）

常规玩法应当从标题画面开始，并演示该任务的核心游戏循环。
演示回放必须是确定性的。对于需要特定状态的演示（某个特定关卡、战斗状态、
升级界面、结算状态或后期配置），请定义具名场景，让你的游戏在以下方式启动时加载它们：

```
godot --path /workspace/game -- --scenario <id>
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