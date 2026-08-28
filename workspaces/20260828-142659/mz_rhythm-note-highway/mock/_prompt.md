# Rhythm Note Highway

Build a Rhythm Note Highway as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Notes cascade down a multi-lane highway toward a judgement line at the bottom
of the screen. The player must press the matching lane key precisely as each
note crosses the line. Accuracy builds a combo multiplier that amplifies the
score; misses break the streak and drain a life bar. The fantasy is performing
a concert — nailing every note in a flow state while the background stage
lights react to your accuracy. A full campaign of procedurally-timed songs
provides hours of escalating challenge.

## What the Player Experiences

1. **Title Screen** — A neon-lit stage backdrop with the game name in a bold
   stylized font, a campaign button, and a free-play button. No plain grey.
2. **Song Select** — A scrollable list of at least 10 songs with difficulty
   ratings (Easy/Medium/Hard), best scores, and completion grades (S/A/B/C/F).
   Songs unlock sequentially through the campaign.
3. **The Highway** — 4 lanes with colour-coded note gems falling toward a
   judgement bar. The player presses D/F/J/K (or arrow keys) to hit notes.
   Timing windows: Perfect, Great, Good, Miss — each with distinct visual
   feedback (burst, glow, shake).
4. **Combo System** — A combo counter increments on consecutive hits. The
   multiplier (x2, x4, x8) scales score. Breaking combo resets the counter
   with a visible shatter effect.
5. **Life Bar** — Misses drain health. If health hits zero, the song fails
   with a game-over screen showing stats. Perfects restore a small amount.
6. **Hold Notes and Slides** — Some notes require holding the key for their
   duration (a trailing tail). Others slide across lanes, requiring the player
   to follow with their finger position.
7. **Results Screen** — After each song: total score, max combo, accuracy
   percentage, grade, and a breakdown of Perfect/Great/Good/Miss counts.
   New high scores trigger a celebration animation.

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

# 节奏音符轨道（Rhythm Note Highway）

在 `./` 用 HTML 4 开发一个节奏音符轨道游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

音符沿着一条多轨道的音符轨道倾泻而下，奔向屏幕底部的判定线。玩家必须在每个
音符越过判定线的一瞬间，精准按下对应轨道的按键。准确度会积累出连击倍率来
放大得分；失误则会中断连击，并消耗一条生命条。游戏的幻想核心是举办一场
演唱会——在流畅的心流状态中打准每一个音符，同时背景舞台灯光会随你的准确度
作出反应。一整套程序化定时的歌曲战役提供了数小时不断升级的挑战。

## 玩家体验流程

1. **标题画面** —— 一片霓虹灯照亮的舞台背景，游戏名采用粗体风格化字体，配有
   一个战役按钮和一个自由演奏按钮。不要出现纯灰。
2. **选曲** —— 一份可滚动的列表，至少 10 首歌曲，标有难度评级（简单/中等/
   困难）、最佳得分和通关评级（S/A/B/C/F）。歌曲会随战役进程依次解锁。
3. **轨道** —— 4 条轨道，颜色编码的音符宝石朝判定条落下。玩家按 D/F/J/K
   （或方向键）来击中音符。判定窗口分为 Perfect、Great、Good、Miss——各有
   截然不同的视觉反馈（爆裂、发光、震动）。
4. **连击系统** —— 连续命中会让连击计数器递增。倍率（x2、x4、x8）会放大得分。
   中断连击会重置计数器，并伴有可见的碎裂特效。
5. **生命条** —— 失误会消耗生命值。生命值归零时歌曲失败，出现显示统计数据的
   游戏结束画面。Perfect 判定会回复少量生命值。
6. **长按音符与滑动音符** —— 有些音符需要按住按键持续其时长（带有一条拖尾）。
   还有些音符会横跨轨道滑动，要求玩家用手指位置跟随。
7. **结算画面** —— 每首歌结束后显示：总得分、最大连击、准确率百分比、评级，
   以及 Perfect/Great/Good/Miss 各判定数量的明细。刷新最高分会触发一段庆祝
   动画。

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