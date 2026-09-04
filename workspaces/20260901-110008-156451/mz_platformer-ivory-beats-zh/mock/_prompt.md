# 象牙节拍（Ivory Beats）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ivory Beats**，一款 2D 纵向节奏反应街机游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一道不留余地的暗色方块瀑流沿着极简的单色网格倾泻而下，玩家必须在每一块恰好越过判定线的瞬间将它击碎。这里的张力是纯粹的反应速度与轨道切换节奏的结合：四条轨道意味着每一拍都有四个可能的目标，而一次误击或一次漏击就会立刻结束这一轮。游戏奖励"心流"状态——那种手指快过意识、分数计数器一路模糊上冲的恍神时刻。在两次尝试之间，玩家会在多个各以不同方式扭曲压力的模式中追逐个人最佳：赛跑着清除目标数量、在不断加速的滚动中生存，或是在倒计时内最大化命中数。视觉风格是利落的现代主义极简——一张清爽的黑白网格，每当一块方块碎裂就被霓虹反馈闪光点亮。

## 玩家体验流程

一个干净的标题画面呈现游戏名和一个模式选择菜单，菜单上显示从存档文件读取的个人最佳分数。玩家挑选一个挑战模式，落到一张静止的四轨网格上，一个脉动的提示邀请他们做出第一次敲击。

玩家动手的那一刻，方块开始滚动。暗色方块每行一块地下降，各自落在随机的轨道上，玩家要猛敲轨道键或点击，在最下方的活动方块从底部逃脱之前把它摧毁。每一次成功命中都会以一道霓虹闪光把方块蒸发掉、推动分数上涨，并把下一行拉入位。节奏不断累积——起初缓慢而平易近人，随后加快到手指变成一片虚影。

敲错轨道或让方块逃脱会立刻触发失败：棋盘锁定，出错的方块闪红并伴随屏幕震动，一个结算面板滑到冻结的网格之上。面板显示本轮分数与已保存的最佳分的对比，若被超越就更新纪录，并提供一次即时重试来重置棋盘、无需重新启动。

每个模式都重塑压力的形态：一个模式与时钟赛跑着清除固定数量的方块，另一个每命中若干次就加快滚动直到玩家崩溃，第三个则施加一段紧迫的倒计时、让每一块方块都至关重要。这个循环短促、有冲击力，且耐玩不厌。

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