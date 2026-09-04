# 磁力冲刺（Magnet Dash）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Magnet Dash**，一款带磁力吸引/排斥机制与动量位移的平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一个被磁化的机器人靠吸附向或排斥离每个关卡中散布的金属表面来穿越工业厂房。按住吸引会把机器人拉向最近的金属锚点，并在接近过程中积攒速度。在恰当时机松手就把这股拉力转化为抛射式的动量。排斥会把机器人爆发式地推开，让它横越间隙或沿竖井上冲。吸引与排斥之间的相互作用造就出一套摆荡、弹射般的移动语汇，玩起来像是可控的混乱。三个区域共三十个关卡会引入越来越复杂的磁力谜题，而三场 Boss 战则要求把磁力机制用于进攻——弹开抛射物，或把护盾从敌人身上拉走。

## 玩家体验流程

标题画面显示机器人悬在两块磁铁之间。一个区域选择菜单展示三个区域，每个区域十个关卡，外加每个区域末尾的一场 Boss 战。

进入游玩后，金属表面会以一种醒目的颜色发光。按住吸引键会把机器人拉向最近的金属表面——距离越近，加速越快。松手则把动量转化为自由飞行。在金属表面附近按下排斥会把机器人高速弹开。关卡要求串联这些动作来跨越间隙、攀升竖井，并躲开电场和碾压机之类的危险物。

Boss 战发生在布有金属锚点的竞技场里。Boss 会发射可被磁力弹开的抛射物，或是身上带有能被吸引撕下的金属装甲板。击败 Boss 会解锁下一个区域。完成画面显示时间、收集到的收集品，以及一个基于动量串联的风格评级。

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