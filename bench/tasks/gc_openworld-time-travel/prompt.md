# Open-World Time Travel

Build a **2D open-world time-travel game** in Godot 4 at `/workspace/game/`.
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player discovers a time-travel device and explores the same open-world
location across multiple distinct eras — a lush ancient past, a bustling
industrial present, and a desolate high-tech future. Actions in one era ripple
forward and alter the landscape, inhabitants, and available paths in later eras.
The fantasy is **temporal cause and effect**: the player reads the world, makes
deliberate changes in the past, then jumps forward to witness consequences
unfold. Tension comes from the butterfly effect — a small act of kindness or
destruction cascades across centuries — and from paradox: the world resists
contradictions, and the player must think carefully about what they change and
when. The game should feel mind-bending and interconnected, like a puzzle box
made of history.

## What the Player Experiences

1. **Title Screen** — A styled opening with the game name, a "Begin Journey"
   or "Play" button, and a temporal backdrop (overlapping landscapes bleeding
   into each other, clock gears, aurora). No naked Godot grey.
2. **Three Eras** — The same geographical region rendered in three visually
   distinct time periods: an ancient wilderness with warm saturated greens, an
   industrial cityscape with muted greys and oranges, and a ruined future with
   cold blues and purples. The player walks freely in each era and recognises
   landmarks that persist across time.
3. **Time Travel** — The player activates a time-travel device to jump between
   eras. The transition plays a visible effect and the destination era loads
   with the player at the corresponding map coordinates, preserving spatial
   continuity.
4. **Butterfly Effect** — Actions in an earlier era alter later eras in visible,
   gameplay-meaningful ways. Multiple causal chains exist: planting something in
   the past changes the landscape in the future, destroying infrastructure
   reshapes routes, befriending NPCs leaves legacies for their descendants.
5. **Paradox Detection** — The game prevents or punishes paradoxical actions.
   Attempting to destroy something your future self depends on triggers warnings
   and instability until the paradox is resolved.
6. **Cross-Era Quests and NPCs** — Each era has unique NPCs whose quests span
   multiple time periods. Completing cross-era objectives unlocks new
   destinations or upgrades the time device.
7. **Temporal Inventory** — Items have era compatibility. Some survive time
   travel while others decay. The inventory communicates which items are stable
   and which will not survive the next jump.

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

# 开放世界时空穿越（Open-World Time Travel）

在 `/workspace/game/` 用 Godot 4 开发一个**2D 开放世界时空穿越游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家发现了一台时空穿越装置，在多个截然不同的时代中探索同一处开放世界地点——
草木繁茂的远古过去、喧闹的工业当下，以及荒凉的高科技未来。在某个时代中的行为
会向后涟漪扩散，改变后续时代的地貌、居民和可通行的路径。这里的幻想是**时间上的
因与果**：玩家读懂世界，在过去做出有意的改动，然后跳向未来见证后果展开。张力
来自蝴蝶效应——一个微小的善举或破坏会跨越数个世纪层层放大——也来自悖论：世界
会抵抗矛盾，玩家必须仔细思考自己改变了什么、又是在何时改变的。游戏应当给人
一种令人脑洞大开、处处相互关联的感觉，就像一个由历史造就的谜题盒。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个"开始旅程"或"开始
   游戏"按钮，以及一幅时间主题背景（彼此交叠、相互渗透的地景、时钟齿轮、极光）。
   不要出现 Godot 的裸灰色。
2. **三个时代** —— 同一片地理区域被呈现为三个视觉上截然不同的时期：一片带有
   温暖高饱和绿色的远古荒野、一座色调低沉、灰橙交织的工业城景，以及一个冷蓝
   与紫色调的废墟未来。玩家可以在每个时代中自由行走，并认出跨越时间留存下来的
   地标。
3. **时空穿越** —— 玩家启动时空穿越装置在各时代间跳跃。转场会播放一段可见的
   效果，目标时代加载后玩家出现在对应的地图坐标上，从而保持空间上的连续性。
4. **蝴蝶效应** —— 在较早时代中的行为会以可见且对玩法有意义的方式改变后来的
   时代。存在多条因果链：在过去种下某物会改变未来的地貌，摧毁基础设施会重塑
   路线，与 NPC 结交会为其后代留下遗产。
5. **悖论检测** —— 游戏会阻止或惩罚构成悖论的行为。试图摧毁未来的自己所依赖
   之物会触发警告和不稳定状态，直到悖论被消解。
6. **跨时代任务与 NPC** —— 每个时代都有独特的 NPC，他们的任务横跨多个时期。
   完成跨时代目标可解锁新的目的地，或升级时间装置。
7. **时间物品栏** —— 物品具有时代兼容性。有些能经受时空穿越，有些则会腐坏。
   物品栏会告知哪些物品是稳定的、哪些无法在下一次跳跃中存留。

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