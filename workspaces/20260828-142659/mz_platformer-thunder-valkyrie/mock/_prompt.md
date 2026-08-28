# Thunder Valkyrie

Build **Thunder Valkyrie**, a 2D vertical scrolling bullet-hell shoot-'em-up in
HTML 4 at `./`. This is not a prototype. It is a **complete,
shippable micro-game** that could sit on an itch.io page or Steam as a polished
vertical slice.

## Core Vision

A lone starfighter threads through mathematically dense curtains of enemy fire,
where every pixel of the hitbox matters and every split-second dodge buys another
breath. The tension lives in reading bullet geometry: patterns sweep, spiral, and
converge while the player traces the one safe seam through the chaos. Between
sorties the pilot reinvests plundered gold into hull upgrades, sub-weapons, and
wingman attachments, reshaping how the next wave feels. The tone is bright,
kinetic, and relentless — an arcade reflex challenge wrapped in deep-space neon
and spectacular particle destruction.

## What the Player Experiences

A styled title screen introduces the game with a cosmic backdrop and a clear
path into the hangar.

In the hangar the player reviews their persistent loadout — starfighter level,
shield type, sub-weapon, wingman — and spends gold earned from prior runs to
upgrade slots. Each upgrade visibly changes projectile patterns or survivability
for the next sortie.

From a sector map the player selects a constellation stage. Each stage has a
distinct stellar backdrop and its own enemy composition. Locked stages remain
gated until the previous boss falls.

Once deployed, the screen scrolls vertically over a layered starfield. The
starfighter moves smoothly in response to input, its tiny glowing core hitbox
the only vulnerable point. Primary lasers fire continuously; sub-weapons and
wingmen add flanking fire. Waves of enemy interceptors enter in geometric
formations, releasing scripted bullet configurations that sweep downward. Elite
capital ships drop red power crystals; collecting them triggers a frenzy state
that doubles fire rate and vacuums nearby pickups.

Each stage culminates in a multi-phase boss that locks the scroll and floods the
arena with layered patterns. Taking damage degrades the shield; if it breaks the
run ends with a results overlay showing gold earned and waves survived. Defeating
the boss unlocks the next stage and awards premium components.

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

# 雷霆女武神（Thunder Valkyrie）

在 `./` 用 HTML 4 开发 **Thunder Valkyrie**，一款 2D 纵向卷轴弹幕射击游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一架孤零零的星际战机在数学般密集的敌方火力帷幕中穿行，判定框上的每一个像素都举足轻重，每一次毫秒级的闪避都换来又一口呼吸。张力就在于读懂弹幕几何：弹道会横扫、旋绕、汇聚，而玩家要在混乱之中描出那唯一一道安全的缝隙。出击之间，飞行员把掠夺来的黄金重新投入到船体升级、副武器和僚机挂件上，重塑下一波的手感。整体调性明亮、动感而不留余地——一场包裹在深空霓虹与壮观粒子爆破中的街机反应挑战。

## 玩家体验流程

一个经过设计的标题画面以宇宙背景介绍这款游戏，并给出一条通往机库的清晰路径。

在机库里，玩家查看自己持久保存的配装——星际战机等级、护盾类型、副武器、僚机——并花掉先前几轮赚来的黄金去升级各个槽位。每项升级都会明显改变下一次出击的弹道形态或生存能力。

玩家从一张星区地图上选择一个星座关卡。每个关卡都有独特的星空背景和自己的敌人构成。被锁定的关卡会一直封着，直到前一个 Boss 倒下。

一旦部署，画面便在层叠的星空之上纵向滚动。星际战机随输入平顺移动，其微小的发光核心判定框是唯一的可受伤部位。主激光持续开火；副武器和僚机则补上侧翼火力。一波波敌方截击机以几何编队入场，释放出向下横扫的脚本化弹幕配置。精英主力舰会掉落红色能量水晶；拾取它们会触发一种狂热状态，使射速翻倍并把附近的拾取物吸过来。

每个关卡都以一场多阶段 Boss 战收尾，Boss 会锁住卷轴并用层叠弹幕淹没整个场地。受到伤害会削减护盾；若护盾破碎，这一轮就以一个显示所得黄金和存活波数的结算浮层结束。击败 Boss 会解锁下一个关卡并奖励高级组件。

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