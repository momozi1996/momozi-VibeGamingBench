# Rhythm DJ Arena

Build a Rhythm DJ Arena as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

Two musical fighters face off on a neon stage, trading rhythmic attacks in a
battle of beats. Each fighter has a note highway; hitting notes charges special
moves that launch across the arena as musical projectiles. The opponent must
dodge or counter with their own charged abilities. The fantasy is a DJ battle
where musical skill translates directly into combat power — perfect combos
unleash devastating bass drops while missed notes leave you vulnerable. Multiple
characters with distinct musical styles and move sets provide variety.

## What the Player Experiences

1. **Title Screen** — A vibrant neon club aesthetic with the game name in
   glowing graffiti-style text, character select and versus mode buttons, and
   animated equalizer bars in the background. No plain HTML grey.
2. **Character Select** — At least 4 playable characters, each with a distinct
   musical theme (electronic, rock, jazz, hip-hop), unique sprite design, and
   different special move sets. Each character's selection shows a preview
   animation and their move list.
3. **Split Highway** — The screen splits: each side has a 3-lane note highway.
   The player hits notes on their side to build a charge meter. The AI opponent
   plays their own highway simultaneously.
4. **Charge and Attack** — When the charge meter fills a threshold, the player
   can spend it to launch a musical attack (bass wave, treble spike, chord
   blast). Attacks travel across the arena toward the opponent. Stronger charges
   (from higher combos) produce more powerful attacks.
5. **Defence and Dodge** — The opponent can dodge attacks by timing a key press
   as the projectile arrives, or absorb hits (losing health). A health bar
   depletes with each successful hit. First to zero loses the round.
6. **Best of Three** — Matches are best-of-3 rounds. Between rounds, a brief
   interlude shows score and lets the tempo increase for the next round.
7. **Arcade Mode** — A ladder of increasingly difficult AI opponents, each with
   faster note patterns and more aggressive attack usage. Defeating all
   opponents shows a character-specific victory screen.

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

# 节奏 DJ 竞技场（Rhythm DJ Arena）

在 `./` 用 HTML 4 开发一个节奏 DJ 竞技场游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两名音乐斗士在霓虹舞台上对峙，用节奏性的攻击展开一场节拍之战。每名斗士都有
一条音符轨道；击中音符可以为特殊技能充能，充满后会化作音乐弹幕横穿竞技场
发射出去。对手必须闪避，或用自己已充能的技能反制。游戏的幻想核心是一场 DJ
对战——音乐技巧直接转化为战斗力：完美连击会释放毁灭性的低音炸弹，而漏掉的
音符则让你门户大开。多名拥有截然不同音乐风格和招式组合的角色带来丰富变化。

## 玩家体验流程

1. **标题画面** —— 鲜艳的霓虹夜店美学，游戏名采用发光的涂鸦风字体，配有
   角色选择和对战模式按钮，背景是动态的均衡器条。演好默认纯灰。
2. **角色选择** —— 至少 4 名可玩角色，各有独特的音乐主题（电子、摇滚、爵士、
   嘻哈）、独特的精灵图设计和不同的特殊招式组合。选中每个角色时会显示一段
   预览动画及其招式列表。
3. **分屏轨道** —— 屏幕一分为二：每一侧都有一条 3 轨的音符轨道。玩家在自己
   那侧击中音符以积攒充能量表。AI 对手同时在自己的轨道上演奏。
4. **充能与攻击** —— 当充能量表达到某个阈值时，玩家可以消耗它发动一次音乐
   攻击（低音波、高音尖刺、和弦冲击）。攻击会横穿竞技场朝对手飞去。充能越强
   （来自更高的连击）产生的攻击就越强力。
5. **防御与闪避** —— 对手可以在弹幕抵达的瞬间按键闪避，或者硬吃伤害（损失
   生命值）。每次成功命中都会削减血条。先归零的一方输掉本回合。
6. **三局两胜** —— 比赛采用 3 局 2 胜制。回合之间有一段简短的间奏，显示得分
   并让下一回合的速度提升。
7. **街机模式** —— 一条难度递增的 AI 对手阶梯，每个对手的音符模式更快、攻击
   使用更具侵略性。击败所有对手会显示该角色专属的胜利画面。

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