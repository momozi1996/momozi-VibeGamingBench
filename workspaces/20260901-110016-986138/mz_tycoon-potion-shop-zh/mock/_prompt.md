# 魔药店（Potion Shop）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Potion Shop**，一款**炼金药店管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一家奇幻药铺，用采集来的材料调制魔药，卖给患有特定病症的顾客。核心循环由配方驱动：在坩锅前按照已发现的配方组合材料，把成品摆上货架，并设定在利润与顾客满意度之间取得平衡的价格。顾客带着可见的症状上门——咳嗽的骑士、被诅咒的商人、中毒的孩子——并买下与自己需求相符的魔药。张力在于库存管理：稀有材料会用尽，热销魔药卖得比能调制出来的更快，而货架空空的店铺会流失声誉。整体基调是惬意而魔幻的：咕嘟作响的坩锅、发光的药瓶，以及一间堆满趣味细节的店铺。

## 玩家体验流程

玩家从标题画面开始，为这一天开门营业。店铺视图展示货架、一口坩锅、一个材料柜，以及顾客排队的柜台。日循环驱动着节奏：上午调制，下午售卖，晚上补货。

调制在坩锅前进行：玩家从材料柜中选取材料并加以组合。已知配方会显示所需材料；新配方可以通过实验来发现。每瓶魔药都有类型（治疗、解除、增益）和品质等级，取决于材料新鲜度与操作是否正确。

顾客进店时带着以图标显示的可见病症。他们会浏览货架，并按设定的价格买走相符的魔药。满意的顾客会回头并口口相传；不满意的顾客（拿错魔药、太贵、缺货）会留下差评，从而减少客流。

赚来的金币可用于从供应商菜单补充材料、店铺升级（更大的货架、更快的坩锅、材料园圃），以及解锁高级魔药的配方书。游戏会记录金币、声誉和营业天数。一个经过美术处理的结算画面会在每周结束时展示店铺统计数据。

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