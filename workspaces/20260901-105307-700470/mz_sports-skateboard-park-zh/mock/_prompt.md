# 滑板公园（Sports Skateboard Park）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**滑板公园**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在各个公园里滑行，做出特技连击来刷高分，解锁新特技并搭建自定义公园。
这里的幻想是"心流状态"：在一段不间断的连击中把磨轨串进翻板、再串进平衡滑行，
看着分数倍率一路攀升。张力来自落地——一个特技没掐准时机就意味着一次摔车，
连击随之清零。生涯目标推动玩家去精通特定的特技，并在主题公园里达成目标分数。

## 玩家体验流程

1. **标题画面** —— 一个涂鸦风格的标题，游戏名称采用喷漆字体，压在一个半管的
   剪影之上。一个轮子形状的开始按钮。
2. **公园选择** —— 多个布局各异的公园：街式场地（栏杆、台阶、边沿）、垂直坡道
   （半管、碗池），以及一个综合公园（所有元素合而为一）。它们逐步解锁。
3. **滑行** —— 玩家用左/右移动，带有动量物理。速度在下坡时积攒，在上坡时流失。
   滑手拥有流畅的滚动动画，并会对地形做出反应。
4. **特技系统** —— 按键组合触发特技：翻板特技（轻按按键）、磨轨特技（靠近栏杆
   时按下）、抓板特技（在空中按住）。每个特技都有一个名字弹出在屏幕上。特技可以
   串成连击，并带有可见的倍率。
5. **分数倍率** —— 在不触地、不摔车的前提下把特技连起来，倍率就会提升。干净
   落地会把分数入袋；摔车则丢掉当前连击。一个连击计量条显示当前的连接长度和
   潜在得分。
6. **生涯目标** —— 每个公园都有特定挑战："在一次连击中得到 10,000 分"、
   "落成一个 kickflip 接磨轨"、"完成一次全管旋转"。完成目标可解锁新的特技和
   公园。
7. **公园编辑器** —— 玩家可以摆放坡道、栏杆和障碍物来创建自定义公园。摆放的
   元素会吸附到网格上。自定义公园可立即游玩。

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