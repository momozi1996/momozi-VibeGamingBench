# 铁路大亨（Railroad Baron）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Railroad Baron**，一款**铁路帝国经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一张城市地图上铺设铁轨、购买列车，并从货运需求中获利。每座城市生产和消耗不同的货物——把一座木材小镇连到一座建筑之城能造出一条赚钱的线路，但前提是轨道足够高效、列车有足够运力。地形决定成本：山地需要昂贵的隧道，河流需要桥梁，平坦的平原便宜但路途更长。一个竞争对手 AI 会营建自己的路网，抢着占下最有利可图的线路。张力在于资本配置：每一英里铁轨都是一笔只有在列车跑起来后才能回本的投资，而在收入流入之前过度建设就意味着破产。整体基调是工业时代的雄心：蒸汽、钢铁，以及连接一片边疆的浪漫。

## 玩家体验流程

玩家从标题画面开始一张新地图。视图展示一张俯视地形图，城市以图标标出各自的货物（木材、谷物、矿石、制成品）。玩家通过点击城市到城市来铺设轨道，成本随所穿越的地形而变化。

一旦两座城市连通，玩家便购买一列火车并把它分配到该线路上。列车沿轨道自动行驶，在一座城市装货，运往另一座城市。收入取决于距离、货物价值和需求——运送城市所需的货物报酬丰厚；运送过剩的货物则报酬微薄。

玩家通过连接更多城市、升级轨道以提速、购买更快的列车，以及研读需求地图来寻找赚钱线路，从而不断扩张。一个竞争对手 AI 会营建自己的路网并争夺同样的需求——如果对方先连通了某条线路，玩家就必须另寻他途。

资金管理至关重要：轨道成本是预付的，购买列车是大笔支出，而收入则随时间涓涓流入。举债能加速成长，但利息会复利累积。游戏在设定的年数之后结束；净资产最高的一方获胜。一个经过美术处理的结算画面会展示路网地图、收入历史和最终排名。

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