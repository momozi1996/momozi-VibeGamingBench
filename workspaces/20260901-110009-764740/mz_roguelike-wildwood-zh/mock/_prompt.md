# Roguelike：荒林（Roguelike: Wildwood）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款**带回合制战斗的节点地图森林探索
Roguelike**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当
足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

游戏的幻想核心是读懂一片危险的森林。小径上的每一个岔口都是一场在信息不完整的
情况下押下的赌注：树干上的爪痕、林冠上方盘绕的烟、灌木丛中一闪的金属光。玩家
之所以继续深入，不是因为路是安全的，而是因为那些线索让风险显得可以估量。当野兽
出现时，战斗是审慎且讲究位置的——一小套技能被花在各自惩罚不同失误的生物身上。
生命值从不会免费回满，所以三片林间空地之前挨的每一道擦伤，到最终之门时依然要紧。
死亡对这一轮是永久的，但对玩家不是：存入的金币和数量渐减的入场券，让每次远征
都有分量，同时又不让失败变成死路。整体调性是压低声息、时刻警觉的——斑驳的光影、
远处的嚎叫、以及靠多熬过一个节点换来的营火噼啪声。

## 玩家体验流程

玩家从一处小径起点营地开始，这里会在多次游玩之间记住他——入场券、金币，以及他
挣得的所有持久优势都在这里一目了然。进入森林要花掉一张入场券，所以出发这个决定
本身就已带有筹码。

一旦进入，这一轮就以一张不断向林中深处延伸的小径节点分支地图展开。节点不会被
完全揭示；地图只提供局部证据——足迹、烟、微光、被扰动的灌木——让玩家在当前的生命值、
金币和深度之间权衡风险。选定一个节点会剥去它的神秘：那可能是一头野兽、一只箱子、
一处营火、一名商人、一个陷阱，也可能是更糟的东西。

战斗是回合制且以技能驱动的。英雄拥有若干各不相同、需要消耗一种资源的能力，而不同
的野兽要求不同的应对——迅捷的狼、披甲的熊、含毒的蛇。中毒或流血这类持续状态会在
多个回合内逐步发作，奖励那些读懂威胁并提前规划的玩家。

战斗之间，玩家收集遗物和装备，它们会重塑英雄的战斗方式，而不只是回满生命值。
一轮之内的成长是可触摸的：新的按钮、新的选项、应对森林下一次抛来之物的新方式。

一轮的结局是胜利——抵达林之心并战胜它的守卫者——或是死亡，死亡会把玩家送回营地，
少了一张入场券，但存入的金币更丰厚。进展在多次游玩之间持续保留，因此退出再回来
时，接手的还是同一份积蓄和同一条缓慢累积力量的道路。

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

交互方案（both）：根据玩法同时支持键盘和指针交互；移动/动作使用键盘，空间选择、菜单和目标操作使用鼠标。
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