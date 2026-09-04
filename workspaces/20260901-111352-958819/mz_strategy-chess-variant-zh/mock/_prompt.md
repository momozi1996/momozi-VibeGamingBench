# 变体国际象棋（Chess Variant）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Chess Variant**，一款**带冷却与地形机制的战术国际象棋游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

经典的国际象棋棋子获得了带冷却计时的特殊能力，而棋盘本身也变成了地形——有的格子治疗，有的造成伤害，有的阻挡移动。其结果是一款既奖励国际象棋直觉、又要求全新战术思维的游戏：当主教每四回合就能传送一次时，骑士的双叉攻击就没那么要紧了；而控制住治疗泉眼所在的格子，可能左右整个残局。战役模式会逐关解锁新棋子与新能力，在把各项机制组合成复杂谜题之前先逐一教会玩家。基调是中世纪奇幻：石制棋盘、发光符文，以及仿佛被附魔战士般的棋子。

## 玩家体验流程

玩家从标题画面进入一张包含顺序关卡的战役地图。每个关卡都是一道国际象棋谜题或一场遭遇战，发生在带有特定地形格与棋子阵容的主题棋盘上。前期关卡一次只教一项机制——一个带冲刺能力的棋子、一个阻挡的格子、一段必须留意的冷却。

游玩时，棋盘会在特定格子上显示地形覆盖层：绿色代表治疗，红色代表伤害，灰色代表不可通行。棋子按标准国际象棋规则移动，但每个棋子还各有一项独特能力（冲锋、护盾、传送、范围攻击），以一个带冷却计数的按钮呈现。使用能力会消耗该回合并开始冷却。

AI 对手使用同样的规则与能力。吃掉敌方国王即胜利；自己的国王被吃则失败。战役通过引入具备新能力的新棋子类型以及更复杂的地形布局来逐步升级难度。完成一关会解锁下一关，有时还会为玩家在后续关卡中的阵容添加一个新棋子。

一个精心设计的结算画面会展示胜利或失败，并提供重试或继续前进的选项。

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