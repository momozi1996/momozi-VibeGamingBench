# Circuit Wizard

Build **Circuit Wizard**, a 2D logic-circuit puzzle game in Godot 4 at
`/workspace/game/`. The player places and connects logic gates (AND, OR, NOT,
XOR) on a board to route signals from inputs to outputs, solving increasingly
complex signal-routing challenges across a campaign.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The game is a digital logic puzzle where the player builds circuits from
discrete components. Each level provides fixed input signals (on/off or
patterned) and requires specific output signals. The player places gates from
a toolbox onto a grid board and draws wires between them to create the correct
logic path. The tension comes from spatial constraints (limited board space,
wire crossing rules) and logical complexity (multi-bit signals, timing
sequences, feedback loops). The best version feels like being an engineer
with a soldering iron, where each completed circuit produces a satisfying
cascade of signals lighting up from input to output.

## What the Player Experiences

A title screen sets the electronic workshop tone with circuit imagery and a
clear way to begin. The player enters a puzzle board where input terminals
(left side), output terminals (right side), and an empty grid workspace are
visible. A toolbox shows available gate types with quantities.

Early levels teach individual gates: connect an input through a NOT gate to
invert the signal, or wire two inputs through an AND gate. Soon levels require
multi-gate chains where the player must decompose a complex boolean expression
into a physical circuit. Mid-game introduces XOR gates, multi-bit buses,
signal splitters, and delay elements that add timing constraints. Late levels
present real-world-inspired challenges: build an adder, construct a
multiplexer, or create a latch with feedback.

Signals flow visually through wires when the player activates the test button.
Correct outputs light up green; incorrect ones flash red with the expected
value shown. A completion screen celebrates the solve and shows gate count
efficiency. The campaign progresses through themed chapters: basic logic,
arithmetic circuits, memory circuits, and challenge rounds.

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
  demo_outputs/    <- your input traces (1-10 files)
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

Ship **1-10 input-trace files** under `/workspace/game/demo_outputs/`, one per
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

# 电路奇才（Circuit Wizard）

在 `/workspace/game/` 用 Godot 4 开发 **Circuit Wizard**，一个 2D 逻辑电路解谜游戏。
玩家在电路板上摆放并连接逻辑门（AND、OR、NOT、XOR），把信号从输入端布线到输出端，
在整个战役中攻克难度不断攀升的信号布线挑战。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款数字逻辑解谜游戏，玩家用离散元件搭建电路。每一关提供固定的输入信号
（开/关或特定模式），并要求产出指定的输出信号。玩家从工具箱中取出逻辑门放到
网格电路板上，并在它们之间连线，构造出正确的逻辑通路。张力来自空间约束
（电路板空间有限、导线交叉规则）与逻辑复杂度（多位信号、时序、反馈回路）。
最理想的版本会让人感觉自己就是一名手持电烙铁的工程师——每完成一个电路，
都会看到信号从输入到输出层层点亮，带来极强的满足感。

## 玩家体验流程

标题画面以电路元素营造出电子工坊的氛围，并给出清晰的开始入口。玩家进入解谜
电路板界面，能看到输入端子（左侧）、输出端子（右侧）和一片空白的网格工作区。
工具箱列出可用的逻辑门类型及其数量。

前期关卡逐个教会单个逻辑门：把一个输入接过 NOT 门以反转信号，或把两个输入接过
一个 AND 门。很快，关卡就会要求多门串联，玩家必须把复杂的布尔表达式拆解成
物理电路。中期引入 XOR 门、多位总线、信号分路器，以及带来时序约束的延迟元件。
后期关卡呈现取材于现实的挑战：搭建一个加法器、构造一个多路选择器，或用反馈
做出一个锁存器。

玩家按下测试按钮后，信号会可视化地在导线中流动。正确的输出亮起绿色；错误的
输出闪红并显示期望值。完成画面为解题喝彩，并展示逻辑门用量的效率评价。战役
按主题章节推进：基础逻辑、算术电路、存储电路，以及挑战关卡。

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
  demo_outputs/    ←<- 你的输入轨迹（1-10 个文件）
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

在 `/workspace/game/demo_outputs/` 下提交 **1-10 个输入轨迹文件**，每个演示一份，
命名为 `*.json`。评测器会为每条轨迹启动一个全新的游戏实例，在 1280x720
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