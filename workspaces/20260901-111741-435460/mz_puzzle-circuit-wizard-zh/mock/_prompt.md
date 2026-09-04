# 电路奇才（Circuit Wizard）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Circuit Wizard**，一个 2D 逻辑电路解谜游戏。
玩家在电路板上摆放并连接逻辑门（AND、OR、NOT、XOR），把信号从输入端布线到输出端，
在整个战役中攻克难度不断攀升的信号布线挑战。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款数字逻辑解谜游戏，玩家用离散元件搭建电路。每一关提供固定的输入信号
（开/关或特定模式），并要求产出指定的输出信号。玩家从工具箱中取出逻辑门放到
网格电路板上，并在它们之间连线，构造出正确的逻辑通路。张力来自空间约束
（电路板空间有限、导线交叉规则）与逻辑复杂度（多位信号、时序、反馈回路）。
最理想的版本会让人感觉自己就是一名手持电烙铁的工程师——每完成一个电路，
都会看到信号从输入到输出层层点亮，带来极强的满足感。

## 玩家体验流程

标题画面以电路元素营造出电子工坊的氛围，并给出清晰的开始入口。玩家进入解谜
电路板界面，能看到输入端子（左侧）、输出端子（右侧）和一片空白的网格工作区。
工具箱列出可用的逻辑门类型及其数量。

前期关卡逐个教会单个逻辑门：把一个输入接过 NOT 门以反转信号，或把两个输入接过
一个 AND 门。很快，关卡就会要求多门串联，玩家必须把复杂的布尔表达式拆解成
物理电路。中期引入 XOR 门、多位总线、信号分路器，以及带来时序约束的延迟元件。
后期关卡呈现取材于现实的挑战：搭建一个加法器、构造一个多路选择器，或用反馈
做出一个锁存器。

玩家按下测试按钮后，信号会可视化地在导线中流动。正确的输出亮起绿色；错误的
输出闪红并显示期望值。完成画面为解题喝彩，并展示逻辑门用量的效率评价。战役
按主题章节推进：基础逻辑、算术电路、存储电路，以及挑战关卡。

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