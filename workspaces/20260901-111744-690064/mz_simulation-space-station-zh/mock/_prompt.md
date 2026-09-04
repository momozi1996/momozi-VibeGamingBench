# 太空站（Space Station）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Space Station**，一款 2D 太空站经营模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是指挥一座偏远的太空站，在船员士气、系统维护与资源管理之间取得平衡，
同时从流星雨到海盗突袭的各种随机事件都在试图让一切崩解。有趣的张力来自船员
派工：每名船员都有技能与疲劳度，而每个系统都需要有人值守。在海盗袭击时把工程师
派去操作武器，就意味着没人去修那台漏气的氧气循环机。发电量限制了能同时运行的
系统数量，迫使玩家在保留哪些系统在线上做出艰难抉择。太空站会一个个模块地扩张，
但每个新模块都是又一个会坏掉的系统、又一张要喂的嘴、又一处脆弱点。

## 玩家体验流程

玩家进入游戏时看到一个星空标题画面，上有太空站的剪影，随后进入太空站总览。
视图展示互连模块的剖面：舰桥、生命维持、动力核心、船员舱、货舱和对接口。每个
模块都有电力、结构完整度与人员配置的状态指示。船员头像排列在底部，带有技能
图标与疲劳条。

玩家通过拖动头像把船员派到各模块，通过一个分配面板管理电力分配，并通过选择
对话响应事件。随机事件会定期触发：补给船提出交易、求救信号带来救与不救的
两难、系统故障要求船员立刻响应，而海盗袭击则要求武器有人值守、护盾通电。
事件周期之间，玩家可以用积累的资源建造新模块、研究升级，或让船员休息。游戏
横跨 30 个以上周期，事件严重度逐步升级。如果生命维持失效或全体船员失去行动
能力，则触发游戏结束。胜利要求在太空站保持完好的前提下存活满设定的周期数。

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