# 壁舞者（Wall Dancer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Wall Dancer**，一款带贴墙攀爬与冲刺机制的精确操作平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名灵巧的攀登者一屏一屏地向上穿越水晶洞窟，贴附墙面、用一次定向冲刺弹射出去，并穿过要求像素级精确时机的尖刺走廊。游戏围绕两个动词构建：贴附与冲刺。贴附在墙上让玩家缓慢下滑，同时扫视房间寻找下一处安全表面。冲刺消耗单次充能，充能会在着地或抓墙时重置，由此形成一种"投入—恢复—再投入"的节奏，让每个房间都像一道靠肌肉记忆解开的小谜题。五个章节陆续引入新的危险物——气流、崩塌的墙、移动的尖刺、重力翻转和限时门——每一样都在不改变核心双动词语汇的前提下叠加复杂度。

## 玩家体验流程

标题画面呈现游戏名和一个章节选择选项（通关前锁定）。按下开始把玩家投入第 1 章第 1 房。

每个房间正好占满一屏。玩家角色接触即贴附到墙上，缓慢向下滑动。贴附时按跳跃会从墙面弹开。在空中按冲刺会让角色朝瞄准的方向高速射出，并消耗掉冲刺充能。落到地面或抓住另一面墙会恢复充能。尖刺、陷坑和移动危险物会立刻致死，玩家会在房间入口重生，没有加载画面。

清掉一个房间后，摄像机滚动到下一个。每个章节包含 8-12 个房间，以一个综合了本章全部危险物的最终房间收尾。完成一个章节会返回枢纽，并解锁下一章。每个章节的死亡计数器和最佳时间记录鼓励玩家为求精通而反复重玩。

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