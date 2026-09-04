# 新闻主编（News Editor）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **News Editor**，一款 2D 报社经营模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是经营一家草根小报，决定追哪些选题、派哪些记者，以及在一个口碑与
营收都至关重要的媒体环境中是优先求快还是求准。有趣的张力来自事实核查的取舍：
抢先发布能抓住读者与广告收入，却有印出错误、损害公信力的风险；细致的事实核查
能产出可靠的新闻，但竞争对手会抢走独家、读者也会流失。记者各有专长与可靠度
评级，选题各有复杂度与时效性，玩家必须把资源匹配到机会上，同时维持报社运转。

## 玩家体验流程

玩家进入游戏时看到一个以印刷机为主题的编辑部标题画面，随后进入主编办公桌视图。
主画面展示收件箱中今日的选题线索、当期版面布局、记者派工情况和财务状况。选题
线索会在一天中陆续到来，带有主题、复杂度、时效性和潜在影响力评级。

玩家把记者派到各个选题上，在快速报道（错误风险更高）与深度调查（更慢但更准确）
之间做选择。已完成的稿件会被排入当期版面——头版、内页，或压在角落。发布会
触发读者反馈：准确的独家会提升口碑与订阅量；错误会引发更正，从而损耗公信力。
营收来自订阅与广告主（后者在意读者规模）。各期之间玩家可以聘用/解雇记者、
投资事实核查工具，或扩展报道领域。战役横跨 20 期以上，选题复杂度、竞争压力
和财务指标逐步升级。每期总结会显示发布的稿件数、准确率、读者规模变化和盈亏。

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

交互方案（both）：根据玩法同时支持键盘和指针交互；移动/动作使用键盘，空间选择、菜单和目标操作使用鼠标。
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