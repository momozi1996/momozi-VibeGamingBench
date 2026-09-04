# 小工厂车间主管（Tiny Factory Foreman）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Tiny Factory Foreman**，一款小体量的 2D 自动化与生产规划游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是经营一座微缩的工厂车间：原材料从一端流入，成品从另一端滚出——前提是玩家把所有环节都正确接通了。有趣的张力是空间性的：传送带只能向前运送，分流器只能分流，而机器只接受特定的输入，所以每一次图块摆放都是一道有时间压力的路径规划谜题。订单会出现在一块看板上，带着倒计时的截止期限，玩家必须决定是为新产品改造生产线，还是从当前布局里再榨出一些产能。风险始终是级联失效——一份材料走错路就卡住一台机器，积压又拖停传送带，接着三笔订单突然同时过期。成长来自赚够钱去解锁更快的传送带、更聪明的分流器，或多输出机器，但每一次升级都是在重塑路径规划难题，而不是简单地解决它。

## 玩家体验流程

玩家一进入游戏，看到的是一个紧凑的车间视图：一侧是几处原材料来源，另一侧是空的订单料箱，两者之间是一片空地网格。一块订单看板显示需要哪些产品、还剩多少时间。最初几分钟是从来源到机器再到料箱铺出一条简单的传送带路径，看着第一只彩色板条箱咔哒咔哒穿过车间。

随着订单变得更复杂，玩家放下分流器来拆分材料流，摆放不同类型的机器把输入转化成中间品或成品，并重新布置传送带以避免冲突。车间填满了动感——小图标沿着传送带滑行，机器在加工时一下一下地脉动，分流器忽左忽右地拨动。设计良好的生产线嗡嗡运转；规划糟糕的生产线则积压堵塞、警告闪烁。

在两轮之间，或者现金允许时，玩家会进入升级画面来提升传送带速度、解锁新的机器配方，或扩充存储容量。这些选择决定了接下来能接哪些订单。最终班次结束，一个结算画面清点已完成的订单、错过的截止期限和赚到的金币，并提供重试或返回标题画面的选项。

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