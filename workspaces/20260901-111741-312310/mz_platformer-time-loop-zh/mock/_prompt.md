# 时间循环（Time Loop）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Time Loop**，一款 30 秒时间循环平台跳跃游戏，过去自己的重放会帮助解开谜题。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

每个关卡都是一段 30 秒的循环。计时器归零时，时间倒回，玩家重新开始——但上一次循环的幽灵会同时重放，并与世界发生交互。幽灵可以按住开关、引开敌人，或站在压力板上，而当前的玩家则去处理别的目标。多重循环层层叠加：第 1 次循环的幽灵按住一道门，第 2 次循环的幽灵站在一个平台上搭出一座桥，而在第 3 次循环中玩家终于借助两个幽灵的贡献抵达出口。谜题在于时间上的协调——规划每一个循环中的自己需要在何时做什么，好让所有版本跨越时间通力合作。四个章节共二十四个关卡，从单幽灵谜题一路升级到四重循环的编排。

## 玩家体验流程

标题画面显示交叠的时钟指针和幽灵剪影。一个章节菜单展示四个章节，每个章节六个关卡。

进入关卡会启动一段 30 秒倒计时。玩家奔跑、跳跃，并与开关和物件交互。计时器归零时，屏幕闪光并倒回——玩家在出生点重新开始，但一个半透明的幽灵会精确重放他们在上一次循环中所做的一切。幽灵在物理上与世界交互：它会按下按钮、按住门，并挡住激光。

玩家最多可以叠加四重循环。顶部的一条时间轴显示所有活动幽灵及其在这 30 秒窗口中的当前位置。在所有必需的开关都被按住（由幽灵或玩家）的情况下抵达出口水晶即完成关卡。一个重置按钮会清除所有幽灵以重新开始。关卡完成时显示所用的循环数以及在最后一次循环中抵达出口的时间。

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