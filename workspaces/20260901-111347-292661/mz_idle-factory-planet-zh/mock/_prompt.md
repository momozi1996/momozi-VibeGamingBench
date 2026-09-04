# 放置工厂星球（Idle Factory Planet）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置工厂星球**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在星球表面放置能自动生产资源的机器，把生产线串联起来，研究各种升级，
直到这颗星球被开采枯竭——然后转生到一颗新星球，带着更好的科技重新开始。
游戏的幻想核心是工业级的规模感：看着传送带把矿石送往冶炼厂、再送往加工厂，
产出数字指数级攀升，星球表面被一张精密的工厂网络逐渐填满。放置循环让生产
持续进行；玩家则优化布局并解锁新的机器类型。

## 玩家体验流程

1. **标题画面** —— 一颗被密布传送带的小型工厂覆盖的行星，游戏名采用工业模板
   字体，还有一个齿轮形状的开始按钮。
2. **星球表面** —— 一个代表星球表面的俯视网格。玩家在图块上放置机器。传送带
   在视觉上把机器连接起来，展示资源在它们之间流动。
3. **机器放置** —— 机器包括：采矿机（开采原矿）、冶炼厂（矿石转金属）、
   加工厂（金属转零件）和售卖站（零件转信用点）。每台机器在有供料时都会自动
   生产。玩家从一个面板中把机器拖到网格上。
4. **生产链** —— 机器必须按顺序连接。前一台的产出通过传送带送入下一台的输入。
   更长的生产链能产出更值钱的货物。一个生产速率显示会给出吞吐量。
5. **研究** —— 信用点用于资助研究，从而解锁更好的机器：更快的采矿机、多输入
   加工厂和存储缓冲区。一棵科技树展示可用的升级及其成本与效果。
6. **星球枯竭** —— 星球的资源是有限的。一个枯竭量表显示剩余矿石。资源变稀薄
   时，采矿机会变慢。资源枯竭后，玩家必须转生。
7. **转生（新星球）** —— 转生会前往一颗资源更丰富的新星球。玩家保留研究进度，
   并获得一个永久的生产倍率。每颗新星球起步更快、上限更高。

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