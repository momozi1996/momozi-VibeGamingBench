# Meat Gauntlet

Build **Meat Gauntlet**, a die-and-retry speed platformer with saw blades and
replay ghosts as self-contained HTML page (files: `index.html`, `game_logic.js`). This is not a prototype. It is
a **complete, shippable micro-game** that could sit on an itch.io page or Steam
as a polished vertical slice.

## Core Vision

A tiny square of meat hurls itself through rooms bristling with spinning saw
blades, retracting spikes, and crumbling ledges. Death is instant and restart
is instantaneous — the loop is attempt, die, learn, attempt again until the
room clicks. After clearing a room, a ghost of the successful run replays
alongside the next attempt, turning past mastery into a visible companion. Fifty
compact levels across five worlds escalate from simple jumps to frame-tight
gauntlets that demand wall-slides, mid-air direction changes, and split-second
timing. The game celebrates speed: each level tracks completion time and a
global death counter reminds the player how far they have come.

## What the Player Experiences

A punchy title screen shows the game name, a level-select grid (unlocked
progressively), and a death counter. Selecting a level drops the player in
instantly.

Each level is a single screen. The meat character runs and jumps with tight,
responsive controls. Saw blades spin in fixed or patrolled paths. Spikes
retract and extend on timers. Crumbling platforms vanish after contact. Touching
any hazard kills instantly — the screen flashes, and the player respawns at the
start within a fraction of a second.

On clearing a level, the completion time displays and a ghost recording is
saved. Re-entering the level shows the ghost replaying the best run as a
translucent afterimage. Clearing all levels in a world unlocks the next world
with new hazard types. A results screen per world shows times and death counts.

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

# 肉块试炼场（Meat Gauntlet）

在 `./` 用 HTML 4 开发 **Meat Gauntlet**，一款带锯片和重放幽灵的"死了再来"竞速平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一小块方形的肉把自己抛进遍布旋转锯片、伸缩尖刺和崩塌岩架的房间。死亡是瞬间的，重开也是瞬间的——循环就是尝试、死亡、学习、再尝试，直到这个房间被彻底吃透。清掉一个房间之后，那次成功的幽灵会与下一次尝试并行重放，把过去的熟练变成一个可见的同行者。横跨五个世界的五十个紧凑关卡，从简单的跳跃一路升级到帧级精确的试炼场，要求贴墙下滑、空中变向和瞬间掐时。游戏为速度喝彩：每个关卡都记录完成时间，一个全局死亡计数器提醒玩家他们已经走了多远。

## 玩家体验流程

一个有冲击力的标题画面显示游戏名、一个（逐步解锁的）选关网格，以及一个死亡计数器。选中一个关卡就立刻把玩家投进去。

每个关卡都是单屏。肉块角色以紧凑灵敏的操控奔跑和跳跃。锯片沿固定或巡逻路径旋转。尖刺按计时器缩回和伸出。崩塌平台在接触后消失。碰到任何危险物都会立刻致死——屏幕闪一下，玩家在不到一秒的时间里于起点重生。

清掉一个关卡后会显示完成时间，并保存一份幽灵录像。再次进入该关卡时，会看到幽灵以半透明残影的形式重放最佳的那一轮。清掉一个世界中的全部关卡会解锁下一个世界，并带来新的危险物类型。每个世界都有一个结算画面，显示各关时间和死亡次数。

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