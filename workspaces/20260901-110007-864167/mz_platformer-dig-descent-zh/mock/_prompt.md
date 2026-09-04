# 掘地下潜（Dig Descent）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dig Descent**，一款带向下射击与连击计分的垂直下潜平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名潜行者无止境地向下坠入程序化拼接出的竖井，朝脚下开火来摧毁方块、减缓下落，并把击杀串成不断攀升的连击。枪既是攻击手段也是移动工具——向下射击会带来向上的后坐力，为绕开危险物争取到宝贵的几毫秒。从被摧毁的方块中收集到的宝石，可以用在一轮之中途经的商店里，那里备有武器升级和血量补充。玩家下潜得越深，屏幕滚动越快，危险物也越密集。死亡会把一切重置回地表，除了技术之外什么都带不走。

## 玩家体验流程

标题画面显示游戏名、最高分和一个开始按钮。按下开始立刻进入下潜。

玩家角色持续下落。按下开火键向下射击，摧毁软质方块并把角色略微向上顶起。敌人在竖井中横向游走——击中它们会增加连击计数，从而提升宝石价值。落在平台上会重置连击，但也提供一个安全的喘息瞬间。碰到尖刺、敌人或屏幕顶部会损失血量。

每隔几个深度层会出现一个商店平台，提供三项可购买的升级：武器散射、射速、血量补充或护盾。玩家花掉收集到的宝石后继续向下。程序化生成确保没有两轮是完全一样的。血量归零时，游戏结束画面显示抵达深度、收集的宝石数、最高连击，以及一个重试按钮。

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