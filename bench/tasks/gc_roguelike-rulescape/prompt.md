# Roguelike: Rulescape

Build **Rulescape**, a top-down **rules-horror roguelike survival game** in
Godot 4 at `/workspace/game/`: a polished vertical slice where the player
navigates haunted public spaces, deciphers unstable rules, and escapes before
the site consumes them.

This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is being trapped inside a place that was once ordinary -- a
hospital, a school, a subway station -- now governed by rules that shift,
corrupt, and lie. Survival depends on reading the environment, deducing which
rules are real, and acting before time runs out. The pressure comes from an
advancing timetable that changes what is safe, anomalies whose behavior is
tied to the local mystery, and the knowledge that obeying the wrong rule is as
deadly as breaking the right one. Each site is a story before it is a level:
its rooms, props, clues, and escape condition should feel like one connected
mystery, not a generic dungeon with swapped textures. The tone is frightening,
bloody, investigative, and oppressive.

## What the Player Experiences

1. **Title and Survivor Choice** -- The player arrives at a dark, themed title screen and selects a survivor from a small roster. Each survivor brings a different tool or instinct that changes how the player reads danger and interacts with the site.
2. **Entering the Site** -- The run drops the player into a top-down anomaly site -- a real-feeling place with rooms, corridors, locked doors, scattered props, and environmental storytelling. The site has its own name, visual identity, local mystery, and set of posted rules that the player can inspect in-world.
3. **The Timetable** -- A visible clock or schedule advances during exploration. When it reaches authored thresholds the site's rhythm changes: new areas unlock, anomalies shift behavior, rules become more dangerous, or an escape window opens.
4. **Exploration and Deduction** -- The player moves through the site, searches objects for clues and items, reads rules (some incomplete, misleading, or corrupted), and pieces together what is actually true. Anomalies appear as spatial threats tied to the site's rules; the player responds by fleeing, hiding, using items, or obeying the correct rule -- wrong choices cost health, sanity, or time.
5. **Resolution** -- Victory comes from satisfying the site's escape condition; defeat comes from a fatal anomaly encounter, rule violation, or resource collapse. The result screen explains what rule, clue, or decision sealed the outcome.

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

# Roguelike：规则之地（Roguelike: Rulescape）

在 `/workspace/game/` 用 Godot 4 开发 **Rulescape**——一款俯视视角的**规则恐怖
Roguelike 生存游戏**：一个打磨精良的纵向切片，玩家在闹鬼的公共空间中穿行，
破译不稳定的规则，并在这处场所把他吞噬之前逃出去。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片
放到 itch.io 页面或 Steam 上。

## 核心构想

游戏的幻想核心是被困在一处曾经再普通不过的地方——一间医院、一所学校、一座地铁
站——如今却被会变动、会腐坏、会说谎的规则所支配。存活取决于读懂环境、推断哪些
规则是真的，并在时间耗尽之前采取行动。压力来自一张不断推进的时间表，它会改变
什么是安全的；来自行为与当地谜团绑定的异常；也来自这样一种认知——遵守错误的规则
和违反正确的规则一样致命。每处场所在成为一个关卡之前，首先是一个故事：它的房间、
道具、线索和逃脱条件应当感觉像一个彼此相连的谜团，而不是换了贴图的通用地牢。
整体调性是惊悚、血腥、调查向且令人压抑的。

## 玩家体验流程

1. **标题与幸存者选择** —— 玩家来到一个昏暗、有主题感的标题画面，从一小批幸存者中做出选择。每位幸存者带来不同的工具或本能，改变玩家读懂危险以及与场所互动的方式。
2. **进入场所** —— 这一轮把玩家投进一处俯视视角的异常场所——一个有真实感的地方，带有房间、走廊、锁住的门、散落的道具和环境叙事。该场所拥有自己的名称、视觉标识、当地谜团，以及一套玩家可以在游戏世界内查看的张贴规则。
3. **时间表** —— 一个可见的时钟或日程表在探索过程中推进。当它抵达设计好的阈值时，场所的节奏就会改变：新区域解锁、异常改变行为、规则变得更危险，或者一个逃脱窗口打开。
4. **探索与推理** —— 玩家在场所中移动，搜查物品以寻找线索和道具，阅读规则（有些不完整、有误导性或已被腐坏），并拼凑出真正为真的是什么。异常以与场所规则绑定的空间威胁形式出现；玩家的应对方式是逃跑、躲藏、使用道具，或遵守正确的规则——错误的选择会付出生命值、理智值或时间的代价。
5. **结局** —— 胜利来自满足场所的逃脱条件；失败来自一次致命的异常遭遇、一次规则违反，或资源崩溃。结算画面会解释是哪条规则、哪条线索或哪个决定锁定了这一结局。

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