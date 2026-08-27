# Racing Terrain Climb

Build a Racing Terrain Climb in Godot 4 at `/workspace/game/`.
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A side-scrolling physics vehicle game where the player drives over rugged
terrain, managing momentum and fuel to reach the farthest distance possible.
The vehicle bounces, tilts, and flips over hills and valleys — too much
throttle on a steep incline flips you backward; too little and you stall on
the slope. Fuel is limited and refilled at checkpoints, creating tension between
speed and conservation. Earned coins buy vehicle upgrades (engine power,
suspension, fuel capacity) and new vehicle types, each with different physics
properties. The fantasy is conquering impossible terrain through smart driving
and incremental improvement.

## What the Player Experiences

1. **Title Screen** — A rugged outdoor scene with the game name in bold blocky
   letters, a vehicle silhouette mid-jump against a sunset sky, and Play/Garage
   buttons. No plain Godot grey.
2. **Stage Select** — Multiple terrain environments (countryside hills, moon
   surface, arctic ice, desert dunes) each with distinct physics properties
   (friction, gravity). Stages unlock by reaching distance milestones.
3. **Driving Physics** — The vehicle has realistic 2D physics: wheels grip
   terrain, the chassis tilts with slope angle, and momentum carries over
   crests. The player controls gas (right) and brake (left), plus tilt
   (up/down) to adjust the vehicle's angle mid-air.
4. **Fuel Management** — A fuel gauge depletes as the player drives. Running
   out stops the vehicle. Fuel canisters appear along the route at intervals.
   The tension between driving fast (burning fuel) and conserving creates
   meaningful decisions.
5. **Coins and Distance** — Coins scatter along the terrain and award currency.
   Distance is tracked as a high score. Each run ends when fuel runs out or
   the vehicle is destroyed (landing on the roof).
6. **Garage/Upgrades** — Between runs, the player spends coins on upgrades:
   engine power, fuel capacity, suspension stiffness, tyre grip. At least 3
   different vehicle types (jeep, motorcycle, monster truck) with visibly
   different sprites and handling characteristics.
7. **Distance Records** — A persistent leaderboard shows best distance per
   stage. Beating a personal record triggers a celebration effect.

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

# 越野爬坡竞速（Racing Terrain Climb）

在 `/workspace/game/` 用 Godot 4 开发一个越野爬坡竞速游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款横向卷轴物理载具游戏，玩家驾车翻越崎岖地形，管理动量与燃油以抵达尽可能远的
距离。载具会在山丘与谷地上弹跳、倾斜、翻滚——在陡坡上油门给太猛会向后翻车；
给太小则会在坡上熄火停住。燃油有限，在检查点补充，从而在速度与节省之间制造出
张力。赚到的金币可以购买载具升级（引擎功率、悬挂、油箱容量）和新的载具类型，
每种都有不同的物理属性。这里的幻想是通过聪明的驾驶和一点点的改良，征服不可能的
地形。

## 玩家体验流程

1. **标题画面** —— 一幕粗粝的户外场景，游戏名称采用粗厚的方块字母，一辆载具的
   剪影在夕阳天空前腾空跃起，另有"开始"/"车库"按钮。不要出现 Godot 的裸灰色。
2. **关卡选择** —— 多种地形环境（乡间丘陵、月球表面、极地冰原、沙漠沙丘），
   每种都有独特的物理属性（摩擦力、重力）。关卡通过达到距离里程碑来解锁。
3. **驾驶物理** —— 载具具有真实的 2D 物理：车轮抓紧地形，底盘随坡度角度倾斜，
   动量会越过坡顶延续下去。玩家控制油门（右方向键）和刹车（左方向键），外加
   倾斜（上/下方向键）以在空中调整载具角度。
4. **燃油管理** —— 油量表随玩家行驶而下降。耗尽后载具会停下。燃油罐会间隔地
   出现在路线沿途。在开快（烧油）与省油之间的张力，造就了有意义的决策。
5. **金币与距离** —— 金币散布在地形沿途，收集可获得货币。距离作为最高分被记录。
   每一轮在燃油耗尽或载具被毁（车顶着地）时结束。
6. **车库/升级** —— 在两轮之间，玩家花金币购买升级：引擎功率、油箱容量、
   悬挂硬度、轮胎抓地力。至少有 3 种不同的载具类型（吉普车、摩托车、
   怪兽卡车），拥有明显不同的精灵图和操控特性。
7. **距离记录** —— 一个持久化的排行榜显示每个关卡的最远距离。打破个人记录会
   触发一段庆祝特效。

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