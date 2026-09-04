# 旅鼠工厂（Lemming Factory）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Lemming Factory**，一个 2D 生物引导解谜
游戏。玩家给一队不停行进的工厂工人分配职业——挖掘工、建造工、阻挡工、攀爬工
——引导它们从入口舱门安全走到出口大门，并在每关救下规定的配额。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款关于间接控制的实时解谜游戏。生物会自主地沿直线行进，碰墙转身，从平台
边缘掉落，若玩家不干预就会一头撞进危险中。玩家无法直接移动生物，但可以点击
某个工人，从数量有限的工具栏中给它分配一个职业。每个职业都会改变该生物的行为：
挖掘工向下凿穿地形，建造工搭出斜向阶梯，阻挡工变成不可通行的墙来改变人流走向，
攀爬工则能攀上垂直表面。张力来自职业名额有限、生物不断向危险行进带来的时间压力，
以及把一大群生物疏导穿过复杂地形所需的空间推理。最理想的版本会让人感觉像在
指挥一支小工人组成的交响乐团，每一次分配都会在人群的路线上层层扩散。

## 玩家体验流程

标题画面用行进中的生物剪影营造出工厂氛围，并给出清晰的开始入口。玩家进入关卡后
能看到地形、危险物（深坑、锯片、岩浆）、入口舱门和出口大门。工具栏显示可用职业
及其剩余数量。舱门打开，生物开始以稳定的速率涌出。

前期关卡一次只教一个职业：派一个挖掘工凿穿地板，或派一个建造工架桥跨过缝隙。
很快，关卡就会要求组合使用职业——用阻挡工改变人流方向，同时让挖掘工打开另一条
通路。中期引入用于垂直移动的攀爬工、用于安全降落的漂浮工，以及用于紧急清除地形
的爆破工。每关都规定一个救援配额；被危险物害死的生物太多就算失败。

玩家可以调整放出速率，也可以暂停来做规划。当足够多的生物抵达出口时，结算画面
展示救援百分比，并给出下一个挑战。战役中的关卡按难度层级分组，每一层级都引入
新的地形类型和职业组合。

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