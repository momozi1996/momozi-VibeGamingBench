# 经营：荒野港湾（Tycoon: Wildhaven）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**多产业边疆经济经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一位边疆老板，要从湖畔荒野中开辟出一座兴旺的哨站。这里的幻想是在一个转动的季节时钟下，同时经营共享同一片土地的多个产业——把其中一个逼得太狠，就会悄悄让其他产业断粮，所以真正的本领在于读懂因果链条，并随着日历推进在各条生产链之间对冲。季节会重塑什么赚钱、什么停滞，天气和野生动物会打乱最周密的计划，而把收益再投资进去会让营地从一间孤零零的棚屋可见地蜕变为一台嗡嗡运转的机器。整体基调温暖却严苛：大自然同样地慷慨与无情，而混日子从来不是一个选项。

## 玩家体验流程

玩家打开已存档的营地或从头开始，看到哨站在眼前铺展开来——森林、开垦地、湖泊，以及一本记着现金与季节的简单账簿。早期的工作是亲力亲为的：砍一棵树、种一垄地、抛一次钓线。每个动作都会可见地改变这片土地，并喂给一条把原始自然变成货物、再变成钱的生产链。

随着收益累积，玩家开始再投资——更好的工具、新的建筑、扩充的产能——哨站在地图上变得更忙碌、更有能力。季节时钟持续转动：温暖的月份适合作物，寒冷的月份冻住湖面，木材需求随之变化，而没有任何单一产业能全年赚钱。玩家学会对冲、囤货和提前规划。

打断毫无预警地到来——风暴压平产出，动物袭击库存——玩家要么适应，要么承受损失。随着时间推移，更深层的游戏显露出来：各产业相互依存，过度开采其中一个会让其他产业退化。均衡的管理会可见地胜过只盯一处的做法。进度会存入存档，因此回来的玩家接手的是同一座哨站、同一个季节、同样的势头。

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