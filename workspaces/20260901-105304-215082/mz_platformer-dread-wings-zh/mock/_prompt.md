# 惧翼（Dread Wings）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dread Wings**，一款**单按键无尽飞行游戏**：这是一场暗黑赛博朋克风格的分数追逐，一只脆弱的金属飞鸟在无限延伸的工业危险物走廊中对抗重力。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家用单一输入对抗物理。每一次点击都为对抗无休止的下坠拉力买来一瞬升力，把飞鸟穿过要求精准时机与节奏感的狭窄缝隙。张力来自玩家看到的来势与反射神经能执行的操作之间的落差——每一次成功通过都会抬高赌注，因为分数如今值得保护了。死亡是瞬间的，重试也是瞬间的，而"再来一次就好"的循环就是整个产品。世界是一片暗黑的工业废土：霓虹点亮的管道、烟尘，以及在血色天幕下滚动而过的远方废墟天际线。

## 玩家体验流程

玩家打开游戏，迎面是一个气氛阴郁的标题画面，显示其历史最高分和一个明确的开始入口。开局之后，飞鸟悬停在原地，等待第一次点击。输入到来的那一刻，重力开始生效，走廊开始滚动。每一次点击都触发一股向上的冲量来对抗飞鸟的下坠弧线，形成一条起伏有节奏的飞行轨迹。成对的危险物从右侧滚入，纵向位置随机但缝隙尺寸恒定，要求玩家不断做微调。通过一对危险物会让分数向上跳动。随着时间推移，挑战不断升级——更快的滚动、更紧的余量，或是新的危险物呈现方式，让玩家持续适应。碰到任何表面都会立刻结束这一轮：世界冻结，结算面板揭示最终分数以及是否创造了新纪录，一个按钮就能把玩家送回待命状态，无需重启可执行程序。最高分在多次会话之间持久保存。

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