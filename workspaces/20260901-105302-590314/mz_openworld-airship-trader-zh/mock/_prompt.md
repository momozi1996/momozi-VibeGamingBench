# 开放世界飞艇商人（Open-World Airship Trader）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界飞艇贸易游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶一艘飞艇穿行于漂满浮空岛的天空，每座岛都有自己的经济体系和可供
贸易的货物。这里的幻想是云端之上的自由：在遥远港口之间开辟航线，低买高卖，
用更好的引擎和货舱升级自己的船，并击退潜伏在贸易航道上的天空海盗。张力来自
燃料管理、海盗突袭，以及随你贸易而不断波动的市场价格。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，游戏名称叠在带视差滚动的天空背景上，
   云朵飘动，远处可见岛屿。一个开始按钮启程。
2. **天空地图** —— 玩家驾驶飞艇在一片广阔开放的天空中自由飞行。视野中可见
   多座浮空岛，每座都有独特的轮廓与配色。云层以视差层次飘动。
3. **停靠** —— 接近岛屿时触发停靠提示。停靠后，玩家进入贸易菜单，其中显示
   当地货物、价格以及自己货舱中的物品。
4. **贸易** —— 每座岛都会廉价产出某些货物，同时高价求购另一些货物。玩家买入
   货物，飞往另一座岛，卖出获利。价格随时间波动。
5. **升级** —— 利润用于升级飞艇：更快的引擎、更大的货舱、更好的燃料效率以及
   船体装甲。升级会体现在飞艇精灵图上。
6. **天空海盗** —— 在某些航线上会出现海盗船追击玩家。玩家可以甩掉他们、用
   船载火炮迎战，或者交过路费。战斗为实时进行，采用简单的抛射物射击。
7. **燃料与风险** —— 飞艇在飞行时消耗燃料。燃料耗尽意味着只能无助地随风漂流。
   燃料可以在岛上购买，也可以从漂浮的木箱中找到。

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