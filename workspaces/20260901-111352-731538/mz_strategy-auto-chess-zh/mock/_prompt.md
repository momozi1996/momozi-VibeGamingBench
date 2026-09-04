# 自走棋（Auto Chess）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Auto Chess**，一款**自动战斗抽卡与站位策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

八名玩家进入一场由战场自行厮杀的锦标赛。回合之间，玩家从共享商店中抽选单位，把它们摆在格状棋盘上，然后看它们自动对阵对手的阵型。策略完全在于抽选与站位：买哪些单位、何时升级以获得更多棋盘格位、如何编排前排坦克与后排输出、以及要追求哪些协同特质。金币管理是这一切的心跳——刷新商店要花金币，攒金币能吃利息，而在错误的时机破产就意味着你的军队比所有人都弱。淘汰赛不断削减参赛者，直到只剩一名玩家。

## 玩家体验流程

玩家一开始看到的是大厅画面，上面有八个头像（一名人类、七名 AI）。每一回合以准备阶段开始：商店提供五个随机单位，玩家用金币购买，把单位拖到格状棋盘上，并编排阵型。将同一单位的三个副本合并可以把它升级到更强的星级，并伴有可见的形态变化。

单位归属于不同职业与种族，当场上同一特质的单位数量足够时便会授予协同加成——协同追踪器会显示已激活与即将激活的加成。玩家必须在专注的协同体系与抓取单体强力单位之间做出取舍。

计时器归零时，战斗阶段开始。单位自动攻击、施放技能、相继倒下，直到一方被全歼。落败的玩家会根据存活的敌方单位数量损失生命值。回合之间，玩家可以看到全部八名参赛者及其生命值的积分榜。

经济奖励耐心：未花完的金币每回合都会产生利息，但战力落后就意味着承受重创。张力始终存在于"现在花钱求生存"与"攒钱以求后期爆发"之间。

当玩家被淘汰或成为最后的幸存者时，游戏结束。一个精心设计的结算画面会展示最终排名与关键数据。

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