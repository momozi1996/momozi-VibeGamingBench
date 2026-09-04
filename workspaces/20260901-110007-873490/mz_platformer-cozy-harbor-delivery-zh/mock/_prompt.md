# 温馨港湾快递（Cozy Harbor Delivery）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Cozy Harbor Delivery**，一款 2D 俯视视角送货路线规划小游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一艘小小的快递船在阳光斑驳的港湾里嗒嗒穿行，在岛屿与浮标之间迂回，把包裹从取货货箱送到码头上等待的客户手中。张力就在于路线规划：多份订单同时倒计时，每一份都有不同的目的地和紧急程度，而港湾的地形恰好错综到玩家无法沿一条直线服务所有人。先抓哪个包裹、让哪位客户失望、以及何时冒险从停泊的船体之间穿一条贴身近道，这就是全部的决策空间。班次之间，玩家把收入重新投入到速度、载货容量或路线提示上，从而塑造下一个班次的手感。整体调性表面温暖悠然，底下却暗含要求——一道被水彩码头和摇曳小船包裹起来的温馨物流谜题。

## 玩家体验流程

一个经过设计的标题画面奠定气氛：游戏名、一幅港湾地图插画，以及一个快递船的身份形象，在玩家按下开始之前迎接他们。

班次从一张俯视港湾地图开始，图上水道、木质码头、岩石岛屿、彩绘浮标和等待中的客户一派生机。玩家平顺地驾船穿行水面，能感觉到它在靠近障碍时减速、在岛缘上弹开。拾取一个货箱会改变船的剪影或 HUD 上的装载信息，确认船上载了什么、要送往何处。

订单在屏幕上层层堆叠——每一份都带有目的地标记和倒计时。有些不慌不忙，有些则闪着紧急提示。玩家串联路线，把包裹投递给对应的客户，看着金币或声望随每次成功送达向上跳动。错过一个计时器，客户就会皱着眉离开。一个日程计时器或班次进度条为本轮倒数，随着未完成订单堆积而不断加压。

班次结束时，结算画面清点送达数、收入和一个表现评级。班次之间的升级或规划画面提供会改变下一轮的选择——更快的引擎、更大的货舱、更好的路线提示。这个循环会诱使玩家再来一班，然后再来一班。

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

交互方案（keyboard-first）：本题材以键盘交互为主：提供方向键或 WASD、Space、Enter、Esc 等清晰按键，并在自然需要时加入鼠标。
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