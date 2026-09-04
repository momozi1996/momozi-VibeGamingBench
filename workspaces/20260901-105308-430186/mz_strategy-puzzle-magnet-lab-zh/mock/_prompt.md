# 解谜：磁力实验室（Puzzle Magnet Lab）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Puzzle Magnet Lab**，一款基于 2D 网格的磁力解谜小游戏。玩家通过操纵极性来推拉磁性物体穿过一座实验室，解开空间谜题，把一枚能量核心引导到出口。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款回合制空间逻辑解谜游戏，建立在一条核心规则之上：异极相吸，同极相斥。每个关卡都是一个由磁体、金属箱、闸门与危险物构成的封闭系统，玩家必须在落子之前推演连锁反应。张力来自不可逆性与层层递进的后果：翻转一个极性开关或许解开了一道闸门，却同时把一个箱子撞进了危险物。最理想的版本感觉像一个被干净实验室美学包裹起来的微型物理沙盒，每道谜题都在教你熟悉的磁力规则之间的一种新互动。

## 玩家体验流程

标题画面用磁力意象定下实验室基调，并提供清晰的开始方式。玩家进入一间基于网格的解谜室，其中墙体、地板图块、磁性箱子、极性指示器、开关、闸门与出口都一眼可辨。移动是审慎的，一次一格，而网格强制严格的空间推理。

前期谜题教授基础：把一个同极箱子推开，或把一块异极方块拉到压力板上以打开闸门。随着玩家推进，关卡会把各种机制叠加起来。极性反转开关会反转玩家的磁场，把一道斥力难题变成一次引力机会。危险图块惩罚草率的移动。多步序列要求玩家提前规划好几步，其中前期的一次推动为后期跨房间的一次拉拽做好铺垫。

撤销或重置选项让挫败感保持在可控范围内。当核心到达出口时，一个完成画面为这次解题喝彩，并提供下一项挑战。失败状态清晰且可恢复。整体弧线从简单的单箱房间推进到需要动用推、拉、反转与排序全套工具的复杂多闸门密室。

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