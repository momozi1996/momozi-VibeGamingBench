# 王国卡牌（Kingdom Cards）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Kingdom Cards**，一款**以卡牌驱动的王国经营策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一个小王国完全通过卡牌来治理。每回合玩家抽一手牌，打出卡牌来兴建建筑、招募士兵、采集资源，或是向敌对领主发动进攻。牌组开局塞满了弱牌；聪明的打法会精简它，用强力升级替换掉废牌。外交牌让玩家可以谈判停战或背叛盟友，为引擎构筑增添一层社交维度。张力在于：每张打出的牌都是一张没留作防守的牌，而敌手不会等你。基调是羊皮纸与墨水的中世纪风：卡牌看起来像王室诏令，王国是一张不断扩张的领地地图，宣战则靠一枚蜡封。

## 玩家体验流程

玩家从标题画面开始一场新战役。王国起初只是地图上的一座城堡，敌对领土清晰可见。每回合玩家从牌组抽五张牌，最多打出三张。建造牌为地图添加建筑（农场产粮、兵营出兵、市场出金）。招募牌增加士兵。进攻牌派遣军队攻打敌手的领土。外交牌开启谈判。

出牌之后，未打出的卡牌可以被销毁以精简牌组，也可以保留到下回合抽牌时使用。新卡牌通过兴建特定建筑或赢下战斗获得——每一次获取都是对牌组的永久改变。

敌手同时进行他们的回合，扩张并发起进攻。地图会随之更新以呈现领土变化。失去所有领土则游戏以失败告终；控制整张地图则获胜。玩家必须在着眼长期发展的经济牌与关乎当下存亡的军事牌之间取得平衡。

一个精心设计的结算画面会展示战役结果与领土变迁历史，并提供开始新游戏的选项。

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