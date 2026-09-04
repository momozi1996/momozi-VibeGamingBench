# 弧行者（Arcborne）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Arcborne**，一款 2D **钩索摆荡动量平台跳跃游戏**：这是一场计时挑战，玩家要在致命地形之上串联钟摆式摆荡，在完美的瞬间脱手腾空，并在重力占上风之前再次抛出钩索。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

要飞，不要走。玩家扮演一名杂技高手，靠发射钩索、吊在绳上摆荡、并在最高点脱手弹射出一道腾空弧线来跨越深渊——随后再次抛钩，把动量在整条赛道上串联起来。这里的幻想是掌控动量：重力、摆荡弧线和精准掐时的脱手会层层叠加成速度，而笨拙地爬行与流畅串联的完美摆荡之间的差别是可以切身感受到的。一次干净的连续摆荡跑完全程令人畅快无比；一次脱手失误就会把你摔进尖刺。

压力来自时钟。每条赛道都是一场计时挑战，玩家要读地形、挑锚点、决心投入一次摆荡，并判断究竟在哪一帧松手。多种钩索模式带来战术深度——有时你需要纯粹的钟摆动量，有时需要一次直接的拉拽来重新占位——而各个世界本身还会扭曲运动规则，所以在一个生态区中的熟练并不保证在下一个中同样游刃有余。

## 玩家体验流程

1. **标题与入场** —— 玩家进入一个经过设计的标题画面，它确立了杂技般的高速调性。开始一轮游戏后，玩家被投入第一个世界，时钟已经在可见地走动。

2. **摆荡与串联** —— 核心体感是物理性的：朝头顶的锚点发射钩索，感受重力拉出弧线，在钟摆底部积攒速度，然后脱手向前抛射。飞行途中重新抛出的钩索能把一次摆荡接进下一次，全程不落地。玩家还能塑形每一次摆荡——助推、收绳、转向——因此高手的操作看上去流畅迅捷，而新手则手忙脚乱、疲于补救。

3. **多种钩索模式** —— 玩家会发现自己拥有不止一种钩索。摆荡索承载钟摆动量；牵引索则把自己直接拽向锚点，用于贴身攀爬或紧急补救。随着地形提出要求，模式切换会变成本能。

4. **改写规则的世界** —— 旅程带领玩家穿过一个个难度递增、环境各异的世界。每个世界都会引入自己的锚点类型、危险物，以及一种改变摆荡手感的环境修正——弧线中途推挤你的阵风、在地面上拖拽你的传送带、把每次弹射拉长成一段滑翔的低重力。玩家必须针对每套新物理规则调整自己的时机与技巧。

5. **危险与补救** —— 陷坑、尖刺、刀刃和移动危险物会惩罚脱手失误。撞上危险物或坠落会把玩家送回检查点，并给出明确反馈。赛道足够宽容以供学习，但也足够严苛，让一次干净通关显得来之不易。

6. **收束** —— 抵达终点结束本条赛道，并弹出显示用时与奖牌的结算。玩家可以重试以刷新更好的时间，或是推进到下一条赛道。完整的循环——标题、游玩、结算、重试或推进——全程无需重启应用。

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