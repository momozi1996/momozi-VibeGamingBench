# 动物园管理员（Zoo Keeper）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Zoo Keeper**，一款**动物园管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家营建并管理一座动物园，为各种各样的动物建造围栏展区，让游客保持愉快，并追求保育目标。每个动物物种都有栖息地要求——面积、地形类型、温度、同伴——满足这些要求能让动物保持健康并繁育出新的个体。游客支付门票并在礼品店和食品摊消费，但他们是为动物而来：稀有物种和设计精良的围栏展区能招来更大的人群。张力存在于商业压力（游客想看奇观）与动物福利（拥挤的展区让动物应激）之间。整体基调明亮而富有教育意味：郁郁葱葱的栖息地、知识介绍牌，以及看到动物茁壮成长的那份喜悦。

## 玩家体验流程

玩家从标题画面开始一座新的动物园。视图展示一片俯视的园区网格，带有一座入口大门。玩家建造道路、围栏展区、游客便利设施和员工建筑。

围栏展区通过围起一块区域并指定生物群落类型（草原、极地、丛林、水生）来建造。动物从一份目录中获取——每种都有购置成本、栖息地要求和人气评级。把动物放进相符的栖息地能让它保持愉快；不匹配的栖息地会造成应激，并通过一个可见的情绪指示器显示出来。

游客从大门进入，沿道路行走，观赏围栏展区并花钱。游客愉快度取决于动物种类的丰富程度、围栏展区品质、道路布局和便利设施的可用性。愉快的游客会停留更久、花得更多。

当彼此相容的动物共处于一个维护良好的围栏展区时，就会触发繁育。幼崽动物是重要的游客卖点，可以留下，也可以换取保育点数。保育目标（繁育濒危物种、维持遗传多样性）在纯粹的利润之外提供额外的目标。

员工（饲养员、兽医、清洁工）必须招聘并分配岗位。游戏会记录资金、游客数量、动物福利评分和保育进度。一个经过美术处理的结算画面会在每个季度结束时展示动物园统计数据。

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