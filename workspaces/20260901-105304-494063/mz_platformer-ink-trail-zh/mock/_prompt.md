# 墨痕（Ink Trail）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ink Trail**，一款玩家留下的轨迹会在延迟之后凝固成实体平台的平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一只墨灵在空荡的虚空中疾行，身后留下一道湿墨轨迹，短暂延迟之后凝固成可行走的平台。墨灵的墨量有限——一旦储墨见底，就再也留不下轨迹，直到抵达一处墨井补充。核心谜题是：在空无一物的空间里规划一条路径，使你留下的轨迹恰好构成你抵达出口所需的平台。有时你必须折返回来，踩在自己的轨迹上。有时你必须在跳跃途中画出一座桥，并在它凝固的瞬间落在上面。墨井分布稀疏，逼迫玩家高效规划路线。横跨六个世界的三十六个关卡会陆续引入吹散湿墨的风、溶解轨迹的橡皮、只在匹配表面附近才凝固的彩色墨水，以及数秒后消退的限时墨水。

## 玩家体验流程

标题画面显示墨水滴落汇成游戏名。一个世界选择网格展示六个世界，每个世界六个关卡。

玩家正常移动和跳跃。移动时，墨水以一条可见的湿线拖在角色身后。经过 1 秒延迟后，湿墨硬化成实体平台，并伴有令人满足的视觉弹跳。一个墨量条显示剩余存量——见底时，移动便不再留下轨迹。散布在关卡中的墨井可以补满墨量条。

前期关卡教授基础的轨迹平台跳跃：从空中跑过去再折返踩上自己已凝固的轨迹，从而跨越一道间隙。后期关卡增加复杂度：风会在湿墨硬化前把它横向推移，橡皮会删掉轨迹的一段，限时墨水会在数秒后消退、要求速度。每个关卡都有基于用墨效率的三星评级。关卡完成画面显示用墨量、时间和获得的星数。

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