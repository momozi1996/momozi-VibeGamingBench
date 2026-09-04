# Roguelike：规则之地（Roguelike: Rulescape）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Rulescape**——一款俯视视角的**规则恐怖
Roguelike 生存游戏**：一个打磨精良的纵向切片，玩家在闹鬼的公共空间中穿行，
破译不稳定的规则，并在这处场所把他吞噬之前逃出去。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片
放到 itch.io 页面或 Steam 上。

## 核心构想

游戏的幻想核心是被困在一处曾经再普通不过的地方——一间医院、一所学校、一座地铁
站——如今却被会变动、会腐坏、会说谎的规则所支配。存活取决于读懂环境、推断哪些
规则是真的，并在时间耗尽之前采取行动。压力来自一张不断推进的时间表，它会改变
什么是安全的；来自行为与当地谜团绑定的异常；也来自这样一种认知——遵守错误的规则
和违反正确的规则一样致命。每处场所在成为一个关卡之前，首先是一个故事：它的房间、
道具、线索和逃脱条件应当感觉像一个彼此相连的谜团，而不是换了贴图的通用地牢。
整体调性是惊悚、血腥、调查向且令人压抑的。

## 玩家体验流程

1. **标题与幸存者选择** —— 玩家来到一个昏暗、有主题感的标题画面，从一小批幸存者中做出选择。每位幸存者带来不同的工具或本能，改变玩家读懂危险以及与场所互动的方式。
2. **进入场所** —— 这一轮把玩家投进一处俯视视角的异常场所——一个有真实感的地方，带有房间、走廊、锁住的门、散落的道具和环境叙事。该场所拥有自己的名称、视觉标识、当地谜团，以及一套玩家可以在游戏世界内查看的张贴规则。
3. **时间表** —— 一个可见的时钟或日程表在探索过程中推进。当它抵达设计好的阈值时，场所的节奏就会改变：新区域解锁、异常改变行为、规则变得更危险，或者一个逃脱窗口打开。
4. **探索与推理** —— 玩家在场所中移动，搜查物品以寻找线索和道具，阅读规则（有些不完整、有误导性或已被腐坏），并拼凑出真正为真的是什么。异常以与场所规则绑定的空间威胁形式出现；玩家的应对方式是逃跑、躲藏、使用道具，或遵守正确的规则——错误的选择会付出生命值、理智值或时间的代价。
5. **结局** —— 胜利来自满足场所的逃脱条件；失败来自一次致命的异常遭遇、一次规则违反，或资源崩溃。结算画面会解释是哪条规则、哪条线索或哪个决定锁定了这一结局。

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