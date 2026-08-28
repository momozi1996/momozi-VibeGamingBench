# News Editor

Build **News Editor**, a 2D newspaper management simulation as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The fantasy is running a scrappy newspaper, deciding which stories to chase,
which reporters to assign, and whether to prioritize speed or accuracy in a
media landscape where both reputation and revenue matter. The interesting tension
is the fact-check tradeoff: publishing fast captures readers and ad revenue but
risks printing errors that damage credibility; thorough fact-checking produces
reliable journalism but competitors scoop you and readers drift away. Reporters
have specialties and reliability ratings, stories have complexity and time
sensitivity, and the player must match resources to opportunities while keeping
the lights on.

## What the Player Experiences

The player opens to a newsroom title screen with a printing press motif, then
enters the editor's desk view. The main screen shows today's story leads in an
inbox, the current edition layout, reporter assignments, and financial status.
Story leads arrive throughout the day with topic, complexity, time sensitivity,
and potential impact ratings.

The player assigns reporters to stories, choosing between fast coverage (higher
error risk) and deep investigation (slower but more accurate). Completed stories
are placed in the edition layout — front page, inside, or buried. Publishing
triggers reader response: accurate scoops boost reputation and subscriptions;
errors trigger corrections that cost credibility. Revenue comes from
subscriptions and advertisers (who care about readership numbers). Between
editions the player can hire/fire reporters, invest in fact-checking tools, or
expand coverage areas. The campaign spans 20+ editions with escalating story
complexity, competitor pressure, and financial targets. An edition summary shows
stories published, accuracy rate, readership change, and profit/loss.

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

# 新闻主编（News Editor）

在 `./` 用 HTML 4 开发 **News Editor**，一款 2D 报社经营模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是经营一家草根小报，决定追哪些选题、派哪些记者，以及在一个口碑与
营收都至关重要的媒体环境中是优先求快还是求准。有趣的张力来自事实核查的取舍：
抢先发布能抓住读者与广告收入，却有印出错误、损害公信力的风险；细致的事实核查
能产出可靠的新闻，但竞争对手会抢走独家、读者也会流失。记者各有专长与可靠度
评级，选题各有复杂度与时效性，玩家必须把资源匹配到机会上，同时维持报社运转。

## 玩家体验流程

玩家进入游戏时看到一个以印刷机为主题的编辑部标题画面，随后进入主编办公桌视图。
主画面展示收件箱中今日的选题线索、当期版面布局、记者派工情况和财务状况。选题
线索会在一天中陆续到来，带有主题、复杂度、时效性和潜在影响力评级。

玩家把记者派到各个选题上，在快速报道（错误风险更高）与深度调查（更慢但更准确）
之间做选择。已完成的稿件会被排入当期版面——头版、内页，或压在角落。发布会
触发读者反馈：准确的独家会提升口碑与订阅量；错误会引发更正，从而损耗公信力。
营收来自订阅与广告主（后者在意读者规模）。各期之间玩家可以聘用/解雇记者、
投资事实核查工具，或扩展报道领域。战役横跨 20 期以上，选题复杂度、竞争压力
和财务指标逐步升级。每期总结会显示发布的稿件数、准确率、读者规模变化和盈亏。

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