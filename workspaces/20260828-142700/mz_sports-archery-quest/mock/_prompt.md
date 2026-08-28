# Sports Archery Quest

Build a **Sports Archery Quest** game as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

The player is an archer on a quest through fantasy lands, using skill-based aiming
to hunt monsters, hit distant targets, and defeat bosses with precision shots.
The fantasy is the perfect shot: accounting for wind and distance, drawing the
bow to full power, and watching the arrow arc across the screen to strike a
weak point. Tension comes from limited arrows, wind that shifts mid-draw, and
monsters that close distance while the player aims. Upgrades improve the bow's
power, arrow types, and the player's draw speed.

## What the Player Experiences

1. **Title Screen** — A forest clearing with an arrow embedded in a target, the
   game name in runic-styled font, and a play button shaped like an arrowhead.
2. **World Map** — A node-based map showing locations: forest, canyon, ruins,
   dragon's peak. Each location has multiple stages. Completing stages unlocks
   the next area.
3. **Aiming Mechanics** — The player draws the bow by holding a button (power
   meter fills), aims with directional input, and releases to fire. Arrow
   trajectory follows a physics arc affected by gravity and wind. A wind
   indicator shows current direction and strength.
4. **Target Stages** — Some stages are pure marksmanship: hit bullseyes at
   increasing distances, shoot moving targets, or thread arrows through narrow
   gaps. Score is based on accuracy and speed.
5. **Monster Hunting** — Monsters approach from the right side. The player must
   hit weak points (glowing spots) to deal maximum damage. Different monsters
   have different weak point locations and movement patterns.
6. **Boss Targets** — Each area ends with a boss: a giant creature with multiple
   weak points that must be hit in sequence. Bosses have attack phases where the
   player must dodge (move vertically) while finding shot windows.
7. **Bow Upgrades** — Earned gold buys upgrades: longer range, faster draw,
   elemental arrows (fire for extra damage, ice to slow, lightning to chain).
   A shop screen shows available upgrades with clear stat comparisons.

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

# 弓箭手远征（Sports Archery Quest）

在 `./` 用 HTML 4 开发一个**弓箭手远征**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名弓箭手，踏上穿越奇幻大陆的旅程，靠技术性的瞄准去猎杀怪物、命中远处
的靶子，并用精准的射击击败 Boss。这里的幻想是那一记完美的箭：算准风力与距离，
将弓拉到满力，然后看着箭矢划过屏幕命中弱点。张力来自有限的箭数、拉弓中途会变向
的风力，以及在玩家瞄准时不断逼近的怪物。升级可以提升弓的力量、箭的种类，以及
玩家的拉弓速度。

## 玩家体验流程

1. **标题画面** —— 一片林间空地，一支箭插在靶子上，游戏名称采用符文风格的字体，
   以及一个箭头形状的开始按钮。
2. **世界地图** —— 一张基于节点的地图，展示各个地点：森林、峡谷、遗迹、龙之峰。
   每个地点包含多个关卡。完成关卡会解锁下一个区域。
3. **瞄准机制** —— 玩家按住按钮来拉弓（力度条填充），用方向输入瞄准，松开射出。
   箭的弹道遵循受重力和风力影响的物理抛物线。一个风力指示器显示当前的风向和
   强度。
4. **靶场关卡** —— 有些关卡是纯粹的射术考验：命中越来越远的靶心、射击移动靶，
   或者让箭穿过狭窄的缝隙。得分基于精度和速度。
5. **怪物狩猎** —— 怪物从右侧逼近。玩家必须击中弱点（发光的斑点）才能造成最大
   伤害。不同的怪物有不同的弱点位置和移动模式。
6. **Boss 靶标** —— 每个区域以一个 Boss 收尾：一头巨大的生物，身上有多个弱点，
   必须按顺序命中。Boss 有攻击阶段，此时玩家必须一边闪避（垂直移动）一边寻找
   出手的窗口。
7. **弓的升级** —— 赚到的金币可以购买升级：更长的射程、更快的拉弓、元素箭
   （火焰造成额外伤害、冰霜减速、闪电连锁）。一个商店画面展示可购买的升级项，
   并附有清晰的属性对比。

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