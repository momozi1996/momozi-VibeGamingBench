# 盗贼小丑扑克（Rogue Joker Poker）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Rogue Joker Poker**，一款小而精的**扑克牌型 Roguelite 刷分游戏**。玩家用扑克牌型、稀奇古怪的小丑牌与商店升级搭建出一台计分引擎，在一轮高风险的游戏中击破不断升级的盲注目标。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家坐在一张超现实的绒布赌桌前，仅凭扑克牌型和一支不断扩充的古怪小丑牌阵容，去击破一连串水涨船高的分数目标。每一轮都是一次清晰可读的战术选择：留哪些牌、弃哪些牌、何时用掉一次出牌机会而不是继续钓一手更好的组合，以及当前的小丑牌阵容如何扭曲同花、顺子、对子或高牌打法的价值。压力来自每轮有限的出牌与弃牌次数、不断升级的盲注目标，以及扭曲计分算法的 Boss 规则。基调是**利落、诡奇、赌场街机风、渴求分数**：绒布赌桌、霓虹筹码、动态卡牌、古怪的小丑肖像、紧凑的提示框，以及清晰的计分算式，应当让这款游戏显得是被设计出来的，而不是用默认控件拼凑出来的。

不要克隆任何具名商业游戏的确切 UI、美术、文案、卡牌名称或图标体系。请使用原创的术语、小丑牌、规则、配色与画面构图，同时保留"扑克计分加 Roguelite 修正"这一大类的类型幻想。

## 玩家体验流程

一轮游戏以一个精心设计的标题画面开场，定下赌场街机的情绪，并邀请玩家开始。开始之后，玩家会面对一连串分数目标不断攀升的盲注。每一轮会发一手卡牌，显示点数、花色与选中状态。玩家研究手牌，选出卡牌组成一个扑克组合，然后要么打出去计分，要么弃掉不想要的牌以抽取替补——两种做法都会烧掉有限的资源。

当一手牌被打出时，计分的瞬间会可见地展开：先识别扑克牌型，计算基础筹码与倍率，然后每张激活的小丑牌依次生效，肉眼可见地改变算式。分数会朝盲注目标动画攀升。玩家像看一台机器那样观察小丑牌行列，逐渐学会哪些组合会触发哪些加成。

盲注之间，一家商店会提供新的小丑牌、牌组改造与升级。购买会为后续轮次重塑计分引擎。一轮游戏会经由小盲、大盲与 Boss 盲逐级升级。Boss 轮会引入迫使玩家重新思考牌型评估的特殊规则：某个花色被禁用、弃牌需要额外代价、手牌上限被压缩，或某张小丑牌被反转。

击破最终目标即胜利。在某个盲注之下用尽出牌次数则为失败。无论哪种结局，一个精心设计的结算画面都会提供重试或返回标题画面的选项。

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