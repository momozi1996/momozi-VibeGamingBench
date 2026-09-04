# 花园生态守护者（Garden Ecosystem Keeper）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Garden Ecosystem Keeper**，一款小体量的**生态园艺管理**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家照料一座小小的修复型花园，其中每一块图块都是一张活网络的一部分。植物争夺水分与光照，传粉者沿着花期走廊移动，害虫钻单一栽培的空子，而天气会在一夜之间改变整个平衡。核心张力是稀缺条件下的看护经营：每回合行动次数有限、水量有限、季节难以预料，还有会惩罚蛮力种植的生物多样性目标。兴旺的花园是玩家谱写出来的，而不是点几下就点出来的。

整体基调温和却有系统感——可读的花床、种子包、传粉者轨迹、害虫警告、随季节变化的色调，以及清晰的生物多样性计量表。花园应当显得鲜活且经过设计，而不是一片彩色方块的原始网格。

## 玩家体验流程

玩家一进入游戏，看到的是一处花园修复场景，并选择一块要照料的园地。第一次种植很简单：几种种子、湿润的土壤、平静的天气。植物在一回合回合中可见地生长，玩家学会浇水、等待、收获的节奏。

很快，生态系统开始显露自己的意志。传粉者造访了某一处花床，却无视了另一处。单一栽培的那一行附近出现了害虫聚集。伴生种植的线索逐渐浮现——番茄旁的香草能驱除蚜虫，野花能把蜜蜂引向果树。玩家开始谱写花床，而不只是把它们填满。

天气与季节抬高了赌注。一场干旱迫使玩家分诊：最后那点水给哪些花床？一次早霜威胁着没有防护的幼苗。多雨的季节淹没低洼图块，却让池塘栖息地繁荣起来。玩家每一回合都在调整自己的计划，在短期存活与长期生物多样性目标之间寻求平衡。

到了后期，花园成为一张交互密织的网。玩家要管理传粉者走廊、害虫屏障、湿度区域和季节轮作。当修复目标达成——某个目标生物多样性分数、一场花期庆典，或是一条完整的栖息地链条——结算画面会反映花园的健康状况与构成。失败时则展示是什么崩溃了、为什么崩溃，邀请玩家下次换一种策略。

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