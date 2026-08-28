# Rhythm Garden

Build a Rhythm Garden as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A whimsical garden overworld connects a collection of eight or more timing
minigames, each themed around a different garden activity — watering flowers to
a beat, swatting bugs in rhythm, conducting a bird choir, bouncing seeds into
pots with timed taps. Each minigame teaches a different rhythmic skill (steady
pulse, syncopation, polyrhythm, call-and-response). Mastering individual games
unlocks a final "Remix" stage that weaves all mechanics together into one
climactic performance. The fantasy is a musical gardener tending a world that
blooms in response to rhythmic mastery.

## What the Player Experiences

1. **Title Screen** — A pastel garden scene with the game name in a playful
   hand-drawn font, flowers swaying to a gentle beat, and a "Play" button
   shaped like a watering can. No plain HTML grey.
2. **Garden Hub** — An overworld map showing garden plots, each representing a
   minigame. Completed games bloom with flowers; locked ones show wilted buds.
   The player clicks a plot to enter its minigame.
3. **Minigame Variety** — At least 8 distinct minigames, each with unique
   visuals and a different timing mechanic:
   - Tap to the beat (steady quarter notes)
   - Hold and release (sustained timing)
   - Call and response (echo a pattern)
   - Syncopation (off-beat hits)
   - Polyrhythm (two simultaneous patterns)
   - Speed ramp (accelerating tempo)
   - Pattern memory (repeat increasingly long sequences)
   - Free-form (improvise within a groove)
4. **Scoring** — Each minigame scores accuracy as a star rating (1-3 stars).
   Visual feedback during play shows timing quality with particle bursts for
   perfect hits and wilting effects for misses.
5. **Progression** — Earning stars unlocks later minigames. The garden visibly
   grows and blooms as the player progresses. New flowers, butterflies, and
   decorations appear with each milestone.
6. **Final Remix** — After completing all 8 minigames, a final challenge
   combines mechanics from multiple games into one extended performance. The
   remix transitions between styles every few measures.
7. **Results and Gallery** — A gallery screen shows total stars, best scores per
   minigame, and the fully-bloomed garden as a reward illustration.

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

# 节奏花园（Rhythm Garden）

在 `./` 用 HTML 4 开发一个节奏花园游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一片充满奇趣的花园大地图串联起八个或更多的时机小游戏，每个都以一种不同的
园艺活动为主题——踩着节拍给花浇水、按节奏拍打虫子、指挥一支鸟儿合唱团、
用定时敲击把种子弹进花盆。每个小游戏教会玩家一种不同的节奏技巧（稳定脉动、
切分、复合节奏、一问一答）。逐一精通这些小游戏可解锁一个把所有机制编织在
一起的最终"混音"关卡，成为一场高潮式的演出。游戏的幻想核心是一位音乐园丁，
照料着一个会随着节奏造诣而绽放的世界。

## 玩家体验流程

1. **标题画面** —— 一幅粉彩色调的花园场景，游戏名采用活泼的手绘字体，花朵
   随着轻缓的节拍摇曳，还有一个做成洒水壶形状的"开始"按钮。不要出现 HTML
   默认的纯灰。
2. **花园枢纽** —— 一张大地图，展示一块块园圃，每块代表一个小游戏。已完成的
   游戏会开出花来；未解锁的则显示枯萎的花蕾。玩家点击某块园圃即可进入对应的
   小游戏。
3. **小游戏多样性** —— 至少 8 个截然不同的小游戏，各有独特的视觉表现和不同的
   时机机制：
   - 踩着节拍敲击（稳定的四分音符）
   - 长按与松开（持续时机）
   - 一问一答（复述一段模式）
   - 切分（脱拍击打）
   - 复合节奏（两段同时进行的模式）
   - 速度攀升（速度不断加快）
   - 模式记忆（重复越来越长的序列）
   - 自由发挥（在一段律动中即兴演奏）
4. **计分** —— 每个小游戏以星级（1-3 星）为准确度打分。游戏过程中的视觉反馈
   会体现时机质量：完美命中爆出粒子，失误则出现枯萎效果。
5. **进度推进** —— 赚取星星可解锁后续的小游戏。随着玩家推进，花园会明显地
   生长并绽放。每达成一个里程碑，就会出现新的花朵、蝴蝶和装饰。
6. **最终混音** —— 完成全部 8 个小游戏后，一个最终挑战会把多个游戏的机制
   组合成一场加长演出。这段混音每隔几个小节就在不同风格之间切换。
7. **结算与画廊** —— 一个画廊画面显示星星总数、各小游戏的最佳得分，以及作为
   奖励插画的完全绽放的花园。

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