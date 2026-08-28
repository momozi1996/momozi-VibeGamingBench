# Vessel of Hallownest

Build a **2D atmospheric metroidvania platform-action game** in HTML 4 at
`./`. This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

A silent bug knight descends into a ruined underground kingdom, armed only with
a nail and the will to press deeper. The fantasy is exploration under pressure:
every room might hold a new threat or a shortcut home, and the player is always
weighing aggression against survival. Combat is fast and punishing — each slash
refills the soul that fuels healing, so standing still means dying slowly. The
interesting tension is that the resource loop forces engagement: you heal by
fighting, but fighting risks the health you are trying to recover. Progression
gates the world behind abilities earned in earlier zones, rewarding mastery with
access rather than numbers. The tone is somber, desolate, and beautifully
tragic — cold underground ruins, glowing particles drifting through silence, and
the quiet weight of a kingdom that fell long ago.

## What the Player Experiences

A melancholic title screen greets the player with the game name and a lone
knight silhouette before they choose to begin or continue a saved journey.

The Kingdom Map appears — a network of named stages stretching downward, each
locked until the one before it falls. The player selects the first open stage
and drops in. Inside, the world is a continuous side-scrolling corridor of
connected rooms: platforms jut from cavern walls, thorn pits line the floor, and
infected husks patrol ledges. Movement feels tight and responsive — the knight
accelerates smoothly, jumps with a satisfying arc, clings to walls, and dashes
through gaps that demand precision.

Combat is immediate and visceral. Slashing an enemy staggers it, sprays geo
currency, and fills the soul meter. Taking a hit costs a mask of health and
triggers a brief flash of invincibility. When masks run low the player faces the
core dilemma: hold still to channel soul into healing — vulnerable, exposed — or
press forward and hope the next kill refills enough to survive. Enemies guard
room exits behind soul-barriers that lift only when every husk in the chamber is
dead.

Deeper rooms demand wall-clings and dashes to cross chasms the knight cannot
simply jump. Reaching the far end of a stage triggers a checkpoint that saves
progress and unlocks the next zone on the map. Death is costly — all carried geo
drops at the point of failure and the knight returns to the map to try again.

The final stage is a boss chamber: a large creature with telegraphed attack
patterns that test everything the player has learned. Victory crowns the run;
defeat sends the knight back with nothing but knowledge.

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

# 圣巢容器（Vessel of Hallownest）

在 `./` 用 HTML 4 开发一款 **2D 氛围类银河恶魔城平台动作游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位沉默的虫族骑士深入一座荒废的地下王国，随身只有一把骨钉和一股继续向前的意志。这里的幻想是压力之下的探索：每个房间都可能藏着新的威胁或一条回家的近道，而玩家永远在进攻与生存之间权衡。战斗迅捷且严苛——每一次挥砍都会补充驱动治疗的灵魂，因此站着不动就等于慢慢死去。有意思的张力在于资源循环逼迫你参战：你靠战斗来治疗，但战斗又会危及你正试图恢复的生命。进度把世界锁在前面区域中获得的能力之后，用通行权而不是数值来奖励熟练。整体调性阴郁、荒凉而美得悲怆——寒冷的地下废墟、在寂静中飘散的发光粒子，以及一个早已陨落的王国那份沉默的重量。

## 玩家体验流程

一个忧郁的标题画面以游戏名和一道孤独的骑士剪影迎接玩家，随后他们选择开始新旅程或继续已保存的旅程。

王国地图出现——一张由具名关卡组成、向下延伸的网络，每个关卡都锁着，直到它前面的那个被攻克。玩家选择第一个开放的关卡并落入其中。在里面，世界是一条由相连房间构成的连续横向滚动走廊：平台从洞穴壁上探出，荆棘坑铺在地面，感染的空壳在岩架上巡逻。移动手感紧凑而灵敏——骑士平顺加速，以令人满足的弧线跳跃，能贴附墙面，并能冲刺穿过要求精确的间隙。

战斗是即刻而切身的。挥砍敌人会使其硬直、喷出吉欧货币，并填充灵魂槽。受到打击会损失一个面具的生命，并触发短暂的无敌闪光。当面具剩得不多时，玩家面对核心困境：站着不动把灵魂引导为治疗——脆弱、暴露——还是继续向前，指望下一次击杀能补足到活下来。敌人守着房间出口后方的灵魂屏障，只有当房中每一个空壳都死掉时屏障才会升起。

更深处的房间要求用贴墙和冲刺来跨越骑士无法单靠跳跃通过的深渊。抵达一个关卡的尽头会触发一个保存进度并在地图上解锁下一区域的检查点。死亡代价高昂——所有随身携带的吉欧都会掉在失败地点，骑士则返回地图重新尝试。

最后一个关卡是一间 Boss 房：一头带有预示动作攻击套路的巨大生物，考验玩家学到的一切。胜利为这一轮加冕；失败则让骑士只带着经验退回。

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