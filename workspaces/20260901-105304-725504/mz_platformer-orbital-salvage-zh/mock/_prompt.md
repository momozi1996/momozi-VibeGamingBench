# 轨道打捞（Orbital Salvage）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Orbital Salvage**，一款小巧的 2D 太空打捞物理游戏：这是一款打磨精良的微型游戏，讲述驾驶一艘小型拖船穿越轨道碎片、用牵引光束扣住残骸，并在燃料耗尽或危险物把载荷撕脱之前把它拖回回收站。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名在碎片带边缘作业的打捞飞行员。拖船不会说停就停——它会漂移、惯性滑行，每次点燃推进器都要与动量搏斗。把牵引光束接到一块残骸上会改变一切：更重的打捞物会把拖船拽偏航线，不稳定的残片有炸裂的危险，而返回空间站的航线要在引力井、漂移的水雷和辐射弧之间穿行。决策空间就在于选择接哪份合约、先抓哪块打捞物、烧燃料时多激进，以及是否为更高报酬冒险走一条穿过危险走廊的近道。轮次之间，玩家把积分重新投入到推力、光束强度或船体装甲上，从而塑造下一份合约的手感。整体调性紧张而工业——一份蓝领的太空工作，而物理才是真正的对手。

## 玩家体验流程

一个经过设计的标题画面奠定气氛：游戏名压在一片星空上，背景有漂移的碎片剪影和一道拖船轮廓，以及一个明确的开始入口。

玩家从一块任务板上挑选合约，板上显示打捞物类型、估算质量、报酬和危险警告。拖船升空进入一片 2D 轨道场域，那里惯性称王——轻点推进会加速，松手让船惯性滑行，而反向制动会飞快烧掉燃料。打捞物漂浮在小行星碎块和危险区之间。玩家机动靠近，发射牵引光束，感受到质量扣上时拖船的一顿。拖一枚沉重的反应堆核心和拖一块轻薄的面板完全不同——船会摇晃、转向半径变大，燃料也烧得更快。

危险物为整条航线打上标点：引力井会弯折飞行路径，水雷一旦擦碰就引爆，辐射弧则在放射前脉动出警告。玩家读场势、规划一条线路并全力投入——或者切断光束、放弃载荷以保住拖船。把打捞物送达空间站会奖励积分并推进合约。结算画面清点收入、燃料消耗和船体损伤，并提供下一份合约或返回标题的选项。

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