# Horror Signal Lost

Build a **Horror Signal Lost** game as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is a radio operator in a remote station, triangulating distress signals
from ships and outposts while something unseen jams the frequencies. The fantasy
is isolation and dread: alone in a dark room with only static and voices, piecing
together what is happening outside while the interference grows more aggressive
and personal. Tension comes from battery management — the radio drains power, and
darkness invites the presence closer. Each signal triangulated reveals a piece of
the horror unfolding beyond the walls.

## What the Player Experiences

1. **Title Screen** — A dark screen with the game name flickering like a dying
   signal, static noise visual effects, and a play button styled as a radio dial.
2. **The Radio Station** — A single-room view of the operator's desk: radio
   equipment, a map with pins, a battery gauge, and a window showing darkness
   outside. The room is lit by the radio's glow.
3. **Signal Scanning** — The player tunes a frequency dial (horizontal slider) to
   find distress signals hidden in static. When a signal locks, audio crackles
   and a transcript appears. Each signal gives coordinates.
4. **Triangulation** — The player places pins on the map based on signal
   coordinates. Connecting three or more pins reveals the source location and
   advances the story. The map fills with pins over time.
5. **Jamming Entity** — Periodically, interference spikes. The screen distorts,
   the radio emits unsettling sounds, and the player must quickly retune to
   escape the jamming. Failing causes battery drain and screen corruption.
6. **Battery Management** — The radio consumes battery. A gauge depletes over
   time. The player can reduce power (dimming the room, limiting scan range) to
   conserve. Batteries are found by solving signal puzzles. If power dies, the
   room goes dark and the entity approaches.
7. **Escalation** — As more signals are triangulated, the jamming grows worse,
   signals become more disturbing, and the window shows shapes moving outside.
   The final signal reveals what is hunting the player.

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

# 恐怖信号失联（Horror Signal Lost）

在 `./` 用 HTML 4 开发一个**恐怖信号失联**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名偏远电台里的无线电操作员，负责对来自船只和哨站的求救信号进行三角
定位，而某种看不见的东西正在干扰这些频率。游戏的幻想核心是孤立与恐惧：独自
待在一间黑屋子里，只有噪点和人声为伴，一点点拼凑出外面正在发生的事，而干扰
却越来越凶猛、越来越针对个人。紧张感来自电池管理——无线电会耗电，而黑暗会
把那个存在引得更近。每完成一次三角定位，就会揭开墙外正在展开的恐怖的一角。

## 玩家体验流程

1. **标题画面** —— 一块黑暗的画面，游戏名像即将断掉的信号一样闪烁，配有噪点
   视觉特效，以及一个做成无线电旋钮样式的开始按钮。
2. **无线电台** —— 单房间视图，展示操作员的桌面：无线电设备、一张插着图钉的
   地图、一个电池量表，以及一扇窗外只有黑暗的窗户。房间由无线电的微光照亮。
3. **信号扫描** —— 玩家调节频率旋钮（水平滑块）来寻找藏在噪点中的求救信号。
   信号锁定时会有音频噼啪声，并出现一段文字记录。每个信号都会给出一组坐标。
4. **三角定位** —— 玩家根据信号坐标在地图上放置图钉。连接三个或更多图钉即可
   揭示信号源位置并推进剧情。随着时间推移，地图上会插满图钉。
5. **干扰实体** —— 干扰会周期性地骤然增强。画面扭曲，无线电发出令人不安的
   声响，玩家必须迅速重新调频以摆脱干扰。失败会导致电池耗损和画面损坏。
6. **电池管理** —— 无线电会消耗电池。量表随时间不断下降。玩家可以降低功率
   （调暗房间、限制扫描范围）来节省电量。电池要靠解开信号谜题才能获得。
   如果电力耗尽，房间会陷入黑暗，那个实体就会靠近。
7. **逐步升级** —— 随着定位出的信号越来越多，干扰变得更严重，信号内容更令人
   不适，窗外也会出现移动的身影。最后一个信号将揭示究竟是什么在猎捕玩家。

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