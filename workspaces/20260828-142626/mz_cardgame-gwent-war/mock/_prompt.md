# Cardgame Gwent War

Build a Cardgame Gwent War as self-contained HTML page (files: `index.html`, `game_logic.js`).
This is not a prototype. It is a **complete, shippable micro-game** that could
sit on an itch.io page or Steam as a polished vertical slice.

## Core Vision

A row-based card battle game where bluffing is as important as card strength.
Each player places unit cards into one of three combat rows (melee, ranged,
siege), and the side with the higher total strength at round's end wins. But
matches are best-of-three — winning a round early by dumping your hand leaves
you empty for the next. The core tension is knowing when to push and when to
pass, baiting the opponent into overcommitting. Multiple faction decks with
unique abilities and a campaign of escalating AI opponents provide depth. The
fantasy is the poker-face moment of passing with a slim lead, daring the
opponent to waste cards chasing it.

## What the Player Experiences

1. **Title Screen** — A medieval war-table aesthetic with the game name in
   iron-forged lettering, faction banners flanking the sides, and Campaign /
   Quick Match / Deck Builder buttons. No plain HTML grey.
2. **Deck Builder** — At least 3 factions (Northern Realms, Monsters, Elves)
   each with 15+ unique cards. The player builds a deck of exactly 25 cards
   from their chosen faction plus neutral cards. Each card shows art, strength
   value, row placement, and any special ability.
3. **The Board** — Three rows per side (melee/ranged/siege) displayed
   horizontally. Cards are played from hand into their designated row. Total
   strength per row and overall total are shown. The opponent's rows mirror
   above.
4. **Turn Structure** — Players alternate playing one card or passing. Once
   both pass, the round ends. The side with higher total strength wins the
   round. Best of 3 rounds wins the match. A round tracker shows current
   standing.
5. **Bluffing and Passing** — The player can pass at any time, locking in their
   current strength. The opponent must then decide whether to keep playing
   cards (wasting resources for future rounds) or also pass. This creates
   rich mind-game dynamics.
6. **Special Abilities** — Cards have abilities: Spy (played on opponent's side
   but draws 2 cards), Medic (resurrects a card from discard), Weather (reduces
   all cards in a row to 1 strength), Commander's Horn (doubles a row's
   strength), Decoy (returns a played card to hand). Each ability has a
   distinct visual effect.
7. **Campaign** — A series of AI opponents with increasing difficulty and
   unique deck strategies. Winning matches earns new cards for the player's
   collection. A world map shows progression through the campaign.

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

# 昆特战争（Cardgame Gwent War）

在 `./` 用 HTML 4 开发一个昆特战争卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款以排为基础的卡牌对战游戏，其中虚张声势与卡牌强度同等重要。双方各自把单位牌
打进三个战斗排之一（近战、远程、攻城），回合结束时总战力更高的一方胜出。但对局
采用三局两胜——过早地倾尽手牌赢下一轮，会让你在下一轮无牌可打。核心张力在于
判断何时该推进、何时该过牌，诱使对手过度投入。多个拥有独特能力的阵营牌组，以及
一条难度层层升级的 AI 对手战役，共同带来深度。这份幻想在于：以微弱优势过牌时那
一刻的扑克脸，赌对手会为追平而白白挥霍手牌。

## 玩家体验流程

1. **标题画面** —— 中世纪战争沙盘美学，游戏名以铁铸字体呈现，两侧列着阵营旗帜，
   并有战役 / 快速对战 / 牌组编辑器按钮。演好默认纯灰。
2. **牌组编辑器** —— 至少 3 个阵营（北方王国、怪物、精灵），每个阵营各有 15 张
   以上独特卡牌。玩家从所选阵营加上中立卡中构建一副恰好 25 张的牌组。每张卡牌
   展示卡面美术、战力数值、所属排位，以及任何特殊能力。
3. **棋盘** —— 每一方三排（近战/远程/攻城），横向排布。卡牌从手牌打进各自指定的
   排。每排战力和总战力都会显示。对手的各排在上方镜像呈现。
4. **回合结构** —— 双方轮流打出一张卡或过牌。一旦双方都过牌，该轮结束。总战力
   更高的一方赢下该轮。三局两胜赢下整场对局。一个轮次追踪器显示当前战况。
5. **虚张声势与过牌** —— 玩家可以随时过牌，锁定自己当前的战力。对手随后必须决定
   是继续打牌（为后续轮次白白消耗资源）还是同样过牌。这造就了丰富的心理博弈。
6. **特殊能力** —— 卡牌拥有各种能力：间谍（打在对手一侧，但抽 2 张牌）、军医
   （从弃牌堆复活一张卡）、天气（把某一排所有卡的战力降为 1）、指挥官号角
   （使某一排战力翻倍）、诱饵（把一张已打出的卡收回手牌）。每种能力都有独特的
   视觉效果。
7. **战役** —— 一系列难度递增、牌组策略各异的 AI 对手。赢下对局会为玩家的收藏
   赢得新卡牌。一张世界地图展示战役进度。

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