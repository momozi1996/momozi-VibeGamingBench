# Strategy: Tower-Defense

Build a **2D Tower-Defense Game** as self-contained HTML page (files: `index.html`, `game_logic.js`). This is not
a prototype. It is a **complete, shippable micro-game** that could sit on an
itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a field commander staring down a map of chokepoints and open
ground, watching a tide of hostiles pour along fixed corridors toward a
vulnerable endpoint. The only tool is a handful of deployable defenders and a
ticking resource clock. The fantasy is **spatial puzzle-solving under escalating
pressure** -- every tile placement is a commitment, every wave ratchets the
stakes, and the interesting tension is that resources spent now on a safe pick
could have been saved for a desperate answer later. The pressure comes from
reading the next wave's composition, choosing where to invest scarce Deployment
Points, and deciding whether to shore up a crumbling lane or gamble on a
high-cost unit that might turn the whole map. The risk is always that one
misread wave or one greedy save leaves the line too thin and enemies pour
through before the next DP tick arrives.

## What the Player Experiences

1. **Title and Campaign Entry** -- A cold, industrial title screen sets the tone.
   The player starts fresh or loads a save, then enters a stage-select map
   showing available missions, each hinting at the enemy composition and
   difficulty ahead.

2. **Deployment Phase** -- Inside a stage the player sees a grid battlefield with
   clearly marked paths, deployable tiles, and a base endpoint. DP ticks upward
   over time. The player drags unit cards from a hand onto legal tiles; each
   placement costs DP and commits a defender to that position. Invalid spots or
   insufficient funds refuse cleanly.

3. **The Assault** -- Enemies surge along the fixed path in discrete waves. Each
   wave is stronger or stranger than the last -- faster scouts, armored brutes,
   flying threats that bypass blockers. Defenders auto-attack within range,
   blockers hold the line, and the player watches HP bars tick down on both
   sides. Deaths remove units from the field; leaks chip away at the base's
   life total.

4. **Escalation and Adaptation** -- Later waves demand answers the opening
   roster cannot provide alone. The player weighs upgrades, repositions
   priorities, and stretches DP across competing needs. The map becomes a living
   puzzle of overlapping ranges and shifting pressure points.

5. **Resolution** -- The final wave breaks against the defense and victory is
   declared, or the base's life hits zero and defeat is acknowledged. Clearing
   a stage marks progress and unlocks the next. The player can retry, return to
   stage select, or quit to title without relaunching.

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

# 策略：塔防（Strategy: Tower-Defense）

在 `./` 用 HTML 4 开发一款 **2D 塔防游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名前线指挥官，盯着一张布满咽喉要地与开阔地带的地图，看着敌潮沿固定通道涌向一个脆弱的终点。手上唯一的工具是少量可部署的防御者和一只不断走动的资源时钟。核心幻想是**在不断升级的压力下解空间谜题**——每一次图块摆放都是一次承诺，每一波敌人都在抬高赌注，而有意思的张力在于：现在花在稳妥选择上的资源，本可以攒下来作为日后绝境中的答案。压力来自解读下一波的构成、决定把稀缺的部署点数（DP）投到哪里，以及判断是要加固正在崩溃的一路，还是赌一个高价单位来翻转整张地图。风险始终存在：一次误读的波次或一次贪心的存钱，就会让防线过薄，敌人在下一次 DP 跳动到来之前就冲了进来。

## 玩家体验流程

1. **标题与战役入口** —— 一个冷峻的工业风标题画面定下基调。玩家从头开始或读取存档，然后进入一张关卡选择地图，其上显示可选任务，每个任务都暗示着前方的敌人构成与难度。

2. **部署阶段** —— 进入关卡后，玩家看到一张格状战场，其中路径、可部署图块与基地终点都有清晰标记。DP 随时间向上跳动。玩家把单位卡从手牌拖到合法图块上；每一次摆放都消耗 DP，并把一名防御者固定到该位置。无效位置或资金不足会被干净地拒绝。

3. **敌袭来临** —— 敌人沿固定路径以离散波次涌来。每一波都比上一波更强或更古怪——更快的斥候、带甲的猛兽、绕过阻挡者的飞行威胁。防御者在射程内自动攻击，阻挡者顶住防线，而玩家看着双方的血条不断下降。死亡会把单位从战场上移除；漏怪则一点点削减基地的生命总量。

4. **升级与应变** —— 后期波次要求的答案，开局阵容单靠自己给不出来。玩家权衡升级、重新调整优先级，并在互相竞争的需求之间摊开有限的 DP。地图变成一道由重叠射程与移动压力点组成的活谜题。

5. **收尾结算** —— 最后一波撞碎在防线上，胜利宣告；或者基地生命归零，失败被确认。通关一个关卡会记录进度并解锁下一关。玩家可以重试、返回关卡选择，或退回标题画面，无需重新启动。

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