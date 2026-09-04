# 动作：虚空收割（Action: Void Harvest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Void Harvest**——一款小巧的 **survivor-like
自动攻击竞技场游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位脆弱的英雄被投入一片不断扩张的敌意虚空，能否存活取决于在虫群缝隙中穿行、
收割它们遗落的能量，并在竞技场把他压垮之前进化出一套奇诡的武器系统。张力来自
升级经济：每一次升级都会重塑这一轮的玩法，但虚空不会等待——敌人每过一秒都变得
更密集、更快、更古怪。玩家永远不会手动开火；站位与升级选择是唯一的操作杠杆。
整体调性应当宇宙感十足且原创——虚空虫、锈蚀炼金、信号照明弹、磁轨爆发、系绳
无人机、碎片地雷——而不是把熟悉的吸血鬼猎人角色表换层皮。

## 玩家体验流程

从一个有设计感的标题画面开始，玩家从一小批原创角色中挑选英雄，每位都有独特的
立绘、初始武器和被动，让这个选择真正像一次策略决策。

竞技场立刻开始：敌人从边缘涌入，英雄的武器自行开火，而玩家用键盘在缝隙中穿行。
被击败的敌人会散落 XP 碎片并被吸向英雄，填满等级槽，随后中断战斗、给出三个升级
选项——一件新武器、一项属性提升，或一次武器进化。每次选择都会带来可见的变化：
更多弹幕、更宽的扇形、绕着英雄旋转的新攻击形态。

时间推动这一轮沿着一条可见的难度阶梯向上。早期的虫群会让位给混合的敌人职能——
冲锋者、远程攻击者、分裂者、持盾者——最终出现精英或类 Boss 的威胁，其机制迫使
玩家重新站位，而不是单纯硬吃伤害。这一轮以胜利或失败收场，在一个有设计感的结算
画面上给出重试与返回标题画面的选项。

全程中，战斗 HUD 让玩家始终掌握状况：HP、XP 条、存活计时器，以及一条展示英雄
已进化成什么样的武器配置栏。

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