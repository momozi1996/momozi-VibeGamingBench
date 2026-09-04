# 波次指挥官（Wave Commander）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Wave Commander**，一款 2D 波次防守射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在竞技场中央指挥一座孤立的炮塔或一名可移动的防守者，面对从四面
八方进攻、组织度越来越高的敌人波次死守阵线。有趣的张力来自波次之间的资源
管理：赚到的货币必须在武器升级、防御屏障和消耗性强化道具之间分配，而玩家永远
不够买齐所有东西。敌人编队会越来越复杂——侧翼小队、带盾纵队、快速冲锋兵混编
缓慢的重甲单位——要求玩家每一轮都调整配装与站位。Boss 波次为这种升级过程
划出节点，出现需要持续集火的巨型敌人，而其护卫仍在继续进攻。

## 玩家体验流程

玩家进入游戏时看到一个军事主题的标题画面，选择一个难度，然后部署进第一个
竞技场。玩家角色占据中央，可 360 度瞄准。第 1 波以从单一方向接近的简单敌人
开始。玩家用鼠标瞄准并点击开火，用 WASD 移动以躲避还击。清空一个波次会触发
一个简短的商店阶段，展示可用升级：射速、伤害、散射、护盾修复、可部署地雷，
或一次清屏空袭。

波次在敌人数量、种类和编队复杂度上不断升级。有些波次会同时从多个方向进攻。
每 5 个波次会到来一个 Boss 波次，出现一个带独特攻击阶段的大型敌人，周围环绕
支援单位。竞技场在波次之间也可能变化——出现新掩体、危险区域激活，或战场
缩小。在 20 个波次之后或玩家死亡时，结算画面会显示存活波次数、摧毁的敌人数
以及已购买的升级。

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

交互方案（keyboard-first）：本题材以键盘交互为主：提供方向键或 WASD、Space、Enter、Esc 等清晰按键，并在自然需要时加入鼠标。
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