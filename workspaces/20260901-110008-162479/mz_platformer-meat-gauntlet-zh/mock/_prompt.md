# 肉块试炼场（Meat Gauntlet）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Meat Gauntlet**，一款带锯片和重放幽灵的"死了再来"竞速平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一小块方形的肉把自己抛进遍布旋转锯片、伸缩尖刺和崩塌岩架的房间。死亡是瞬间的，重开也是瞬间的——循环就是尝试、死亡、学习、再尝试，直到这个房间被彻底吃透。清掉一个房间之后，那次成功的幽灵会与下一次尝试并行重放，把过去的熟练变成一个可见的同行者。横跨五个世界的五十个紧凑关卡，从简单的跳跃一路升级到帧级精确的试炼场，要求贴墙下滑、空中变向和瞬间掐时。游戏为速度喝彩：每个关卡都记录完成时间，一个全局死亡计数器提醒玩家他们已经走了多远。

## 玩家体验流程

一个有冲击力的标题画面显示游戏名、一个（逐步解锁的）选关网格，以及一个死亡计数器。选中一个关卡就立刻把玩家投进去。

每个关卡都是单屏。肉块角色以紧凑灵敏的操控奔跑和跳跃。锯片沿固定或巡逻路径旋转。尖刺按计时器缩回和伸出。崩塌平台在接触后消失。碰到任何危险物都会立刻致死——屏幕闪一下，玩家在不到一秒的时间里于起点重生。

清掉一个关卡后会显示完成时间，并保存一份幽灵录像。再次进入该关卡时，会看到幽灵以半透明残影的形式重放最佳的那一轮。清掉一个世界中的全部关卡会解锁下一个世界，并带来新的危险物类型。每个世界都有一个结算画面，显示各关时间和死亡次数。

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