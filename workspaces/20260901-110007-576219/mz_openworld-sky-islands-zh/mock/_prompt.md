# 开放世界浮空岛（Open-World Sky Islands）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界浮空岛（Open-World Sky Islands）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在悬浮于无尽天空中的浮空岛之间滑翔，探索迷你地牢、收集风之结晶，并击败
Boss 守卫以解锁新的区域。这里的幻想是失重般的自由：从岛缘一跃而下，乘着气流
飞行，在云间发现隐藏的平台。张力来自滑翔机制——空中体力会不断消耗，而坠入
虚空意味着从上一座岛重新开始。风之结晶能延长滑翔距离并解锁强力能力。

## 玩家体验流程

1. **标题画面** —— 一个明亮通透的标题，游戏名称漂浮在云朵和远处的岛屿之间。
   开始按钮做成风之结晶的形状。
2. **岛屿枢纽** —— 玩家从一座中央岛出发，岛上的道路通往各个起飞点。远处的
   岛屿可见，其中一些在解锁前笼罩在薄雾中。
3. **滑翔** —— 玩家从岛缘跳出，使用基于体力的翼翅机制滑翔。气流（以粒子流的
   形式可见）能提升高度。飞行时体力持续消耗；落到任何表面上都会恢复体力。
4. **迷你地牢** —— 每座岛都包含一个小型地牢，内有平台跳跃挑战、敌人，以及一枚
   风之结晶作为奖励。地牢有各具主题的危险机关：火焰喷口、移动平台、尖刺陷阱。
5. **风之结晶** —— 可收集的结晶，既是货币也是能量来源。花费结晶可解锁能力：
   冲刺、二段跳、制造上升气流。结晶计数始终可见。
6. **Boss 守卫** —— 较大的岛上有 Boss 战。每个 Boss 都有玩家必须学习并躲避的
   攻击模式。击败一个 Boss 会解锁通往一片新岛群的通路。
7. **进程** —— 世界被划分为若干岛群。每个岛群都有独特的视觉主题（森林岛、
   结晶岛、火山岛），挑战难度逐级提升。

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