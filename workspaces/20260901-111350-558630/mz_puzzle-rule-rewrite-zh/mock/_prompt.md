# 规则改写（Rule Rewrite）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Rule Rewrite**，一个 2D 基于网格的
文字方块解谜游戏。玩家在图块网格上推动词块，拼成句子来改写这一关的规则，
从而改变物体的作用和世界的运行方式。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款空间逻辑解谜游戏，而关卡本身就是由语言构成的。名词、动词和属性以可推动
的方块形式存在，与它们所描述的物体处在同一张网格上。拼出 "WALL IS STOP" 这样的
句子会让墙壁变得坚实；把某个词推开、打断这个句子，墙壁就变得可以穿过。玩家角色
本身也不是固定的——"YOU" 是一个属性，可以被重新指派给任何名词。张力来自规则的
递归特性：每一步移动都可能重新定义什么是危险、什么是目标，甚至玩家究竟在操控
什么。最理想的版本会让人感觉像是一道包裹在文字游戏里的逻辑谜题，每一关都在教你
熟悉的英文单词之间一种新的相互作用。

## 玩家体验流程

标题画面用风格化的词块意象介绍这款游戏，并给出清晰的开始入口。玩家进入一张网格，
其中物体（墙、旗、骷髅、钥匙）与词块（名词如 WALL、FLAG；动词如 IS、HAS；
属性如 STOP、WIN、PUSH、DEFEAT、YOU）共存。用方向键移动会一格一格地推动词块
和物体。

前期关卡教基础操作：把 "FLAG IS WIN" 推到一起，让旗子成为目标，然后走进去。很快，
玩家就会发现自己可以打散规则、重新指派属性，甚至改变自己操控的是哪个物体。中期
关卡引入条件链、同时生效的多条规则句，以及会在规则变化时发生形变的物体。后期
关卡要求提前规划好几步，因为打破一条规则去组成另一条会在整个棋盘上引发级联的
状态变化。

撤销系统让玩家可以自由回退。关卡完成时会用一个风格化画面来庆祝，并推进到下一道
谜题。战役共有 20 个以上关卡，复杂度层层升级，并被分组为若干世界，每个世界都
引入一个新的单词或机制。

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