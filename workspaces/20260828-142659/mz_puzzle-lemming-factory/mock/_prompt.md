# Lemming Factory

Build **Lemming Factory**, a 2D creature-guiding puzzle game in HTML 4 at
`./`. The player assigns jobs to a stream of marching factory
workers — diggers, builders, blockers, climbers — to guide them safely from
an entrance hatch to an exit door, saving a required quota each level.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a real-time puzzle about indirect control. Creatures march
autonomously in a straight line, turning at walls, falling off ledges, and
walking into hazards unless the player intervenes. The player cannot move
creatures directly but can click on individual workers to assign them a job
from a limited toolbar. Each job transforms the creature's behavior: diggers
carve downward through terrain, builders construct diagonal staircases, blockers
become impassable walls that redirect traffic, and climbers scale vertical
surfaces. The tension comes from limited job supplies, time pressure as
creatures march toward danger, and the spatial reasoning needed to route a
crowd through complex terrain. The best version feels like conducting an
orchestra of tiny workers where every assignment ripples through the crowd's
path.

## What the Player Experiences

A title screen sets the factory tone with marching creature silhouettes and a
clear way to begin. The player enters a level where terrain, hazards (pits,
saws, lava), an entrance hatch, and an exit door are visible. A toolbar shows
available jobs with remaining counts. The hatch opens and creatures begin
marching out at a steady rate.

Early levels teach one job at a time: assign a digger to carve through a floor,
or a builder to bridge a gap. Soon levels require combining jobs — a blocker
redirects traffic while a digger opens an alternate path. Mid-game introduces
climbers for vertical navigation, floaters for safe falls, and bombers for
emergency terrain removal. Each level specifies a save quota; losing too many
creatures to hazards means failure.

The player can adjust release rate and pause to plan. When enough creatures
reach the exit, a results screen shows the save percentage and offers the next
challenge. The campaign has levels grouped into difficulty tiers, each
introducing new terrain types and job combinations.

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
  demo_outputs/    <- your input traces (1-10 files)
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

Ship **1-10 input-trace files** under `./demo_outputs/`, one per
demo, each named `*.json`. The evaluator launches a fresh game per trace,
replays your trace as synthetic mouse and keyboard input at 1280x720, and
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
- `events` — time-ordered inputs. Coordinates are pixels in the 1280x720
  viewport. Supported types:
  - `mouse_click`: `{frame, type, button: "left"|"right", x, y}`
  - `mouse_down` / `mouse_up`: `{frame, type, button: "left"|"right", x, y}` —
    use these for drag interactions: emit `mouse_down` at the start point,
    one or more `mouse_move` events along the way, and `mouse_up` at the end.
    A `mouse_click` is a `mouse_down` + `mouse_up` at the same point in tight
    succession.
  - `mouse_move`: `{frame, type, x, y}`
  - `key_press` / `key_down` / `key_up`: `{frame, type, keycode}` — keycodes:
    `A`-`Z`, `0`-`9`, `ESCAPE`, `ENTER`, `SPACE`, `TAB`, `BACKSPACE`,
    `DELETE`, `SHIFT`, `CTRL`, `ALT`, `UP`, `DOWN`, `LEFT`, `RIGHT`.
  - `wait`: `{frame, type}` — anchor frame, no input.

Replay must be deterministic: same trace, fresh launch, same outcome every time.

---

# 中文版提示词

# 旅鼠工厂（Lemming Factory）

在 `./` 用 HTML 4 开发 **Lemming Factory**，一个 2D 生物引导解谜
游戏。玩家给一队不停行进的工厂工人分配职业——挖掘工、建造工、阻挡工、攀爬工
——引导它们从入口舱门安全走到出口大门，并在每关救下规定的配额。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款关于间接控制的实时解谜游戏。生物会自主地沿直线行进，碰墙转身，从平台
边缘掉落，若玩家不干预就会一头撞进危险中。玩家无法直接移动生物，但可以点击
某个工人，从数量有限的工具栏中给它分配一个职业。每个职业都会改变该生物的行为：
挖掘工向下凿穿地形，建造工搭出斜向阶梯，阻挡工变成不可通行的墙来改变人流走向，
攀爬工则能攀上垂直表面。张力来自职业名额有限、生物不断向危险行进带来的时间压力，
以及把一大群生物疏导穿过复杂地形所需的空间推理。最理想的版本会让人感觉像在
指挥一支小工人组成的交响乐团，每一次分配都会在人群的路线上层层扩散。

## 玩家体验流程

标题画面用行进中的生物剪影营造出工厂氛围，并给出清晰的开始入口。玩家进入关卡后
能看到地形、危险物（深坑、锯片、岩浆）、入口舱门和出口大门。工具栏显示可用职业
及其剩余数量。舱门打开，生物开始以稳定的速率涌出。

前期关卡一次只教一个职业：派一个挖掘工凿穿地板，或派一个建造工架桥跨过缝隙。
很快，关卡就会要求组合使用职业——用阻挡工改变人流方向，同时让挖掘工打开另一条
通路。中期引入用于垂直移动的攀爬工、用于安全降落的漂浮工，以及用于紧急清除地形
的爆破工。每关都规定一个救援配额；被危险物害死的生物太多就算失败。

玩家可以调整放出速率，也可以暂停来做规划。当足够多的生物抵达出口时，结算画面
展示救援百分比，并给出下一个挑战。战役中的关卡按难度层级分组，每一层级都引入
新的地形类型和职业组合。

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
  demo_outputs/    ←<- 你的输入轨迹（1-10 个文件）
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

在 `./demo_outputs/` 下提交 **1-10 个输入轨迹文件**，每个演示一份，
命名为 `*.json`。评测器会为每条轨迹启动一个全新的游戏实例，在 1280x720
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
- `events` —— 按时间排序的输入。坐标是 1280x720 视口内的像素值。
  支持的类型：
  - `mouse_click`：`{frame, type, button: "left"|"right", x, y}`
  - `mouse_down` / `mouse_up`：`{frame, type, button: "left"|"right", x, y}` ——
    用它们实现拖拽交互：在起点发出 `mouse_down`，途中发出一个或多个
    `mouse_move` 事件，在终点发出 `mouse_up`。
    一次 `mouse_click` 等价于在同一点上紧邻连续地发出 `mouse_down` + `mouse_up`。
  - `mouse_move`：`{frame, type, x, y}`
  - `key_press` / `key_down` / `key_up`：`{frame, type, keycode}` —— 可用键码：
    `A`-`Z`、`0`-`9`、`ESCAPE`、`ENTER`、`SPACE`、`TAB`、`BACKSPACE`、
    `DELETE`、`SHIFT`、`CTRL`、`ALT`、`UP`、`DOWN`、`LEFT`、`RIGHT`。
  - `wait`：`{frame, type}` —— 锚定帧，不产生输入。

回放必须是确定性的：同一条轨迹、全新启动，每次都得到相同的结果。