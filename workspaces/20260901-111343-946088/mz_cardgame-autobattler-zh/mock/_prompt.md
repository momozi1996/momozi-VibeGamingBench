# 卡牌自动战斗（Cardgame Autobattler）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个卡牌自动战斗游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款"抽选后观战"的自动战斗游戏：玩家每一轮从共享商店招募生物，把它们布置在棋盘
上，然后看它们自动对抗敌方队伍。策略完全存在于抽选阶段：买哪些生物、何时升级
以获得更强的单位、以及如何在部族标签之间构建协同。同一部族的生物会互相增益——
攒够足够多的野兽就能获得攻击力加成；用亡灵填满一排，它们就能复活一次。8 人淘汰
赛制（对 AI 模拟）会随着场上人数收窄而制造出层层升级的压力。这份幻想在于：从
随机的供给中拼出一支梦之队，然后看着你的协同引擎摧枯拉朽地击溃对手。

## 玩家体验流程

1. **标题画面** —— 一间酒馆内景，游戏名写在吧台上方的木制招牌上，生物剪影坐在
   桌旁，还有一个做成酒馆门样式的"寻找对战"按钮。演出 GameX其灰色。
2. **商店阶段** —— 每一轮，商店展示 3-5 个随机生物供购买。玩家花金币买下生物，
   把它们放到备战席或直接放上棋盘（槽位有限）。出售生物会返还部分金币。一个
   计时器倒数至战斗阶段。
3. **棋盘布置** —— 玩家的棋盘分为前排和后排。站位很关键：前排生物会先被攻击；
   拥有远程攻击的后排生物能更久地保持安全。采用拖放摆放。
4. **自动战斗** —— 计时器归零时，玩家的棋盘会自动与对手的棋盘交战。生物按顺序
   攻击，以最近的敌人为目标。能力会根据条件触发（攻击时、死亡时、战斗开始时）。
   战斗过程伴有攻击动画和不断消减的血条。
5. **部族协同** —— 至少 5 个部族（野兽、亡灵、机械、巨龙、元素）。凑齐某部族
   2/4/6 个会激活层层升级的加成，并在协同追踪面板中展示。协同是最主要的策略轴。
6. **经济** —— 金币收入每轮递增。连胜和连败都会给予额外金币。存下的金币会产生
   利息（每存 10 金币得 1 金币）。升级需要花金币，但会提升商店品质和棋盘容量。
7. **淘汰** —— 玩家从一份生命值池开始。输掉一轮会按存活敌方生物数量按比例扣除
   生命值。最后存活的玩家获胜。排名画面展示最终名次。

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