# Pactbound

Build **Pactbound**, a summoner pact-choice visual novel, in Godot 4 at
`/workspace/game/`. This is not a prototype. It is a **complete, shippable
micro-game** that could sit on an itch.io page or Steam as a polished vertical
slice.

## Core Vision

You are a summoner walking a road lined with spirits and monsters, and each one
offers the same dangerous bargain: a pact. Bind it and gain its power, but carry
its price and its loyalties; refuse it and stay clean but weaker; deceive it and
risk what comes due later. Pactbound is a **choice-driven visual novel** where
the player meets a procession of would-be familiars and decides which to bind,
and the **collection of pacts they carry becomes who they are** — shaping which
factions trust them, which paths open, and how the journey ends.

The fantasy is **defining yourself by the bargains you make**. The heart of the
loop is **meet, weigh, bind or break** — encountering a spirit with its own
nature and cost, judging what a pact with it would make of you, and committing
to a bargain the story remembers. A summoner bound to gentle hearth-spirits
walks a different road than one who collected demons, and the writing should make
those allegiances felt. It should play like an atmospheric journey with real
stakes and genuinely different endings, not a linear tour with a single path.

## What the Player Experiences

1. **An Authored Opening** — From a styled title the player sets out as a
   summoner and is introduced to the road ahead and the bargain at the heart of
   the world, presented as illustrated scenes with characters and narration.
2. **Spirits with Their Own Nature** — Along the way the player meets a variety
   of would-be familiars — a loyal hearth-spirit, a proud beast, a whispering
   demon, and others — each with its own voice, temperament, the power it
   offers, and the price it asks. Encounters feel like meeting distinct
   characters, not picking from an identical list.
3. **Bind, Refuse, or Deceive** — At each spirit the player makes a real choice:
   seal a pact and take on its power and its loyalties, refuse and stay
   unbound, or strike a false bargain with consequences down the line. The
   decision is deliberate and clearly registered, and the player can see what
   they have bound to themselves.
4. **Pacts That Define You** — The pacts the player carries are **remembered and
   accumulate into an identity**: which factions and spirits trust or revile the
   player, which options and dialogue open up, and which later encounters and
   endings become reachable all depend on the company they keep. A choice made
   early should visibly shape a scene much later.
5. **A Journey That Ends Many Ways** — The road resolves in one of several
   genuinely different endings — crowned among monsters, a champion of the
   unbound, a betrayer alone, or a peacemaker between worlds — each reachable
   through the pacts and choices the player made, and shown as an authored,
   styled conclusion that names what they became. The player can set out again
   to bind a different fate.

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
`godot --headless --quit-after 5 --path . -- --scenario ending_monarch`.

A screenshot helper is available at `/workspace/tools/screenshot.sh`. Use it to
actually see what your title / encounter / choice / ending screens look like.

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/frame.png --frames 60
```

To screenshot a specific scenario, append `--scenario <id>` after `--`. The
helper consumes only `--out` / `--frames` / `--scene`; remaining args stay in
`OS.get_cmdline_user_args()` for your game code to read. Example:

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/pact_debug.png --frames 120 --scenario ending_monarch
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
(a particular spirit encounter, a pact roster state, a pact-gated choice, or
one of the journey endings), define named scenarios your game loads when
launched with:

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

# 契约缚身（Pactbound）

在 `/workspace/game/` 用 Godot 4 开发 **Pactbound**——一款召唤师契约抉择视觉
小说。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

你是一名召唤师，走在一条两侧遍布精灵与怪物的路上，而它们每一个都提出同样一桩
危险的交易：契约。缔结它，你便获得它的力量，但也要背上它的代价与它的效忠；
拒绝它，你保持清白但更加弱小；欺骗它，你则要为日后到期的账单承担风险。
Pactbound 是一款**选择驱动的视觉小说**，玩家会遇见一队接一队渴望成为眷属的
存在，并决定缚结哪些，而**他们所背负的这一整套契约就成了他们是谁**——它塑造了
哪些阵营信任他们、哪些道路会开启，以及这场旅程如何终结。

游戏的幻想内核是**以你所做的交易来定义你自己**。循环的核心是
**相遇、权衡、缚结或断绝**——遇见一个有自己本性与代价的精灵，判断与它缔约会把
你变成什么样，然后敲定一桩故事会记住的交易。缚结于温和的炉灶之灵的召唤师，与
一个收集恶魔的召唤师走的是完全不同的路，而文本应当让这些效忠关系被真切感受到。
它玩起来应当像一场氛围浓厚且真有代价的旅程，拥有确实不同的结局，而不是一趟
只有单一路径的线性观光。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家以召唤师的身份启程，
   被介绍前方的道路以及这个世界核心的那桩交易，以带有角色与旁白的插画场景呈现。
2. **各有本性的精灵** —— 沿途玩家会遇见形形色色渴望成为眷属的存在——一个忠诚的
   炉灶之灵、一头骄傲的野兽、一个低语的恶魔，还有其他——每一个都有自己的声音、
   性情、它提供的力量，以及它索取的代价。这些遭遇应当让人感觉像在与各具特色的
   角色相遇，而不是从一份千篇一律的清单里挑选。
3. **缚结、拒绝，或欺骗** —— 面对每一个精灵，玩家都要做出真实的选项：封定契约
   并承受它的力量与它的效忠、拒绝并保持未缚状态，或者达成一桩虚假的交易而留下
   日后的后果。决定是审慎的、会被清晰记录的，而玩家可以看到自己都把什么缚结到了
   身上。
4. **定义你的契约** —— 玩家所背负的契约会被**记住并累积成一种身份**：哪些阵营
   与精灵信任或厌恶玩家、哪些选项与对话会开放、哪些后续遭遇与结局变得可以抵达，
   全都取决于他们所结交的伙伴。一个很早做出的选项，应当明显地塑造一个很晚出现
   的场景。
5. **有多种终结方式的旅程** —— 这条路会以数个确实不同的结局之一收束——在群魔之中
   加冕、成为未缚者的守护者、成为一个孤身的背叛者，或成为世界之间的调停者——
   每一个都通过玩家缔结的契约与做出的选择来抵达，并以精心编排、有设计感的结语
   呈现，点明他们成为了什么。玩家可以再次启程，去缚结另一种命运。

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
`godot --headless --quit-after 5 --path . -- --scenario ending_monarch`。

`/workspace/tools/screenshot.sh` 提供了截图辅助工具。用它来实际查看你的
title / encounter / choice / ending 画面长什么样。

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/frame.png --frames 60
```

要给特定场景截图，在 `--` 之后追加 `--scenario <id>`。该工具只消费
`--out` / `--frames` / `--scene`；其余参数会留在
`OS.get_cmdline_user_args()` 里供你的游戏代码读取。示例：

```
/workspace/tools/screenshot.sh --path /workspace/game \
      -- --out /workspace/pact_debug.png --frames 120 --scenario ending_monarch
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