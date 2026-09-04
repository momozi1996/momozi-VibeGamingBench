# 开放世界赏金猎人（Open-World Bounty）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界赏金猎人游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名独行猎人，游荡在无法无天的边境地带，从一块风化的任务板上揭下契约，
穿越充满敌意的地形追踪危险的目标。这里的幻想是**在不确定中追猎**——每一份
赏金都意味着承诺深入陌生的地界，而有趣的张力在于猎人必须读懂地貌、
管理有限的资源，并决定何时交战、何时撤退。压力来自目标难度的不断攀升、日渐
枯竭的补给，以及"一次失败的狩猎就意味着空手而归"这个认知。风险始终存在：
下一个目标可能比预期更能打，或者猎人在一份轻松的赏金上花得太多，面对真正的
威胁时已一无所剩。

## 玩家体验流程

1. **标题与进入** —— 一个粗砺的西部奇幻风标题画面奠定基调。玩家按下开始，
   抵达一座边境小镇——一个枢纽，有酒馆、任务板，以及若干出售装备或替你包扎
   伤口的 NPC。

2. **接下契约** —— 任务板上展示可接的赏金，每一份都带有目标肖像、难度评级和
   金币报酬。玩家阅读这些卡片，权衡风险与收益，然后确定一个目标。选定的赏金
   成为当前狩猎任务，世界的焦点也随之转向追踪。

3. **狩猎** —— 一个罗盘或方向指示器引导玩家出镇、进入荒野。世界包含多个风格
   各异的区域——林间藏身处、匪帮营地、多岩的峡谷——目标就等在其中某处，或巡逡
   游走，或埋伏待机。旅途本身就是体验的一部分：地形在变化，环境中潜藏威胁，
   而离安全之地越来越远。

4. **对决** —— 找到目标即触发战斗。猎人有多种攻击选择，必须读懂目标的行为
   才能生存下来。目标会带着明显的攻击性反击；双方的血条都在消耗。不同的目标
   要求不同的战术——有的迅捷善避，有的披甲且下手极狠。

5. **领取赏金** —— 成功狩猎后返回小镇会触发结算流程。金币计入钱袋，赏金卡片
   从任务板上被划掉，猎人可以把收入花在更好的装备或更难的契约上。循环重置，
   带来新的目标和更高的赌注。

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