# 策略：遭遇战（Strategy: Skirmish）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款**黑暗奇幻战术遭遇战**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家指挥一支人数处于劣势的小队，穿越一场场绝境般的格状战斗，其中每一次移动都是一次不可撤回的承诺，每一次损失在这场战斗中都是永久的。核心幻想是**阴郁的战术求生**——寥寥数名专才对抗如潮的敌人，站位就是性命，而一次误判就会让你损失一个战斗中无法补充的单位。基调糅合了小规模版的 *Into the Breach* 与 *Darkest Dungeon*：受限的配色、高对比度、紧张的决策。最理想的版本让玩家感觉自己像一位被逼到墙角的将军，找到了那唯一一串把不可能的胜算扭转为险胜的行动序列。

## 玩家体验流程

一个氛围阴郁的标题画面立刻定下黑暗奇幻的基调。玩家开始游戏，收到一份简短的战术简报——小队的目标、前方的威胁、事关的利害——然后网格才出现。

战斗是回合制且审慎的。玩家选中一个单位，看到它有限的移动范围在网格上亮起，然后把它落定到某个位置。敌人可见、具有攻击性且数量众多——小队总是寡不敌众。玩家用完自己的行动后，一个"结束回合"指令把控制权交给敌方，敌方会带着明确意图推进：包抄、拉近距离、进入射程就攻击。随后控制权交回，循环重复。

战斗致命且清晰可读。攻击需要贴身或有明确的射程指示，会削减持续记录的 HP，并可致死。死亡单位从棋盘上消失，不再阻挡也不再构成威胁。玩家的队员都是专才——移动范围、攻击方式、HP 上限或能力各不相同——因此决定谁去哪里、谁打什么，就是核心的决策空间。

战场本身也增添了战术层次：地形障碍把移动收束进特定通道，危险区域惩罚草率的站位，或者目标设定带来超出单纯歼灭之外的时间压力。多种战斗布局让体验不会在打完一场后就被解穿。

歼灭所有敌人即胜利；失去整支小队则失败。任一结局都会落到一个精心设计的结算画面上，展示发生了什么，而玩家可以重试或返回标题画面，无需重新启动。整条弧线——标题、简报、战斗、结算——流畅地衔接为一段连续的、经过编排的体验。

## Vibe Gaming Quality Bar

本题的玩法、逻辑和验收锚点优先于下面的表达规范。不要重写或删减上面的核心
机制；这些要求用于把同一玩法稳定地落成一个可玩的 Vibe Gaming 垂直切片。

- **先玩后美化**：先保证开始、核心输入、状态变化、成功/失败和重玩闭环，再做视觉与动效。
- **技术栈按玩法选最小充分方案**：
  - 2D 规则游戏优先 `HTML5 Canvas 2D + Vanilla JS`；
  - 面板、卡牌、对话和菜单密集时可用 `DOM + CSS + Vanilla JS`；
  - 图标、线稿和几何动画可用 `纯 SVG + CSS 动画 + Vanilla JS`；
  - 连续碰撞、镜头、粒子或街机物理可用 `PhaserJS`；
  - 3D 或空间镜头可用 `Three.js + WebGL`；
  - 只有确实需要 GPU 大规模并行或自定义 GPU 管线时才用原生 `WebGPU`；
  - 可以混合 Canvas、DOM、CSS、SVG，但必须明确每层职责，禁止为了“技术炫技”增加无关复杂度。
- **规则层独立**：`game_logic.js` 保存唯一真相，暴露 `createGame(opts)` 和
  `advance(game, input, dt)`；渲染层只读取状态并呈现，不能偷偷维护第二套规则。
- **每帧可解释**：输入要映射到明确动作，动作要产生可观察状态变化；无效输入、
  边界条件、资源耗尽、受伤、胜利和失败都要有反馈。
- **Vibe 不是装饰**：至少使用两种反馈通道（动画、位移、缩放、粒子、声音、
  HUD 或镜头）表达关键动作；反馈不能遮挡目标或破坏可读性。
- **移动端优先**：关键点击目标至少 44×44 CSS px，支持触摸和鼠标，不能依赖 hover；
  390×844、360×800、430×932 和 1280×800 不得横向滚动或出现控件重叠。
- **确定性与测试**：随机内容使用 seed；至少验证核心规则、胜负条件、重开/恢复、
  输入边界和一个异常状态；不要用截图存在或文字出现冒充功能完成。
- **原创与合规**：使用原创名称、角色、图形、音效和关卡，或明确许可的素材；
  不复制任何原作商标、角色、文本、美术、音乐、关卡数据或代码。

完成后报告：实际文件路径、启动命令、测试命令与结果、关键截图、已知限制、
技术栈取舍和原创资产来源。

## HTML 提交格式

用两个文件交付一个可独立运行的浏览器游戏：

- `index.html` - 完整可玩的呈现层。使用 HTML Canvas 2D 或 Three.js/WebGL 完成可玩呈现。
- `game_logic.js` - 确定性的状态与规则层，使用经典脚本格式并暴露
  `createGame(opts)` 和 `advance(game, input, dt)`；可选暴露
  `render(gameState, renderCtx)`。

页面无需构建步骤或本地服务器即可打开，普通笔记本应在三秒内完成首屏渲染。
资源必须在运行时自包含生成，不得请求网络：可以使用程序化几何体、Canvas2D
绘制并编码为 `data:` URI 的纹理、离屏 Canvas 粒子精灵、Web Audio API 合成音效、
着色器、后处理和 CSS。不得嵌入或运行时获取外部图片、模型、视频或音频文件。
Three.js 可以从固定版本的官方 CDN 加载；如使用后处理，只能加载同一 Three.js
版本下固定的 `examples/jsm/postprocessing/*` 模块。

交互方案（pointer-first）：本题材以鼠标/指针交互为主：支持点击、悬停、拖拽或框选；只有自然需要时再加入键盘快捷键。
完整游戏区和 HUD 在 1280x720 下应清晰可读。需要有明确的开始流程、简短游戏内
引导、暂停与重开控制、完整胜负/计分结果闭环，以及每项关键操作的可见反馈。

`index.html` 不得使用 `fetch()` 或 `XMLHttpRequest` 请求外部 URL；只允许上述
固定版本 Three.js CDN。`index.html` ≤ 400 KB；`game_logic.js` 行数限制仅作
建议，不作为 BUILD 失败条件。

### 逻辑与渲染脚手架

```html
<script src="./game_logic.js"></script>
<script>
  const { createGame, advance, render } = window.GameLogic;
  const game = createGame({});
  // 主循环调用 advance；render(game, { THREE, scene, ... }) 可选。
</script>
```

```javascript
(function (root) {
  function createGame(opts) { return { phase: "title", score: 0 }; }
  function advance(game, input, dt) { return game; }
  function render(gameState, renderCtx) { /* optional visual hook */ }
  const api = { createGame, advance, render };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` 必须是纯函数，不访问 DOM 或 Three.js 对象；可选的 `render()` 由
主循环调用并负责把状态映射到场景、材质、粒子和后处理。