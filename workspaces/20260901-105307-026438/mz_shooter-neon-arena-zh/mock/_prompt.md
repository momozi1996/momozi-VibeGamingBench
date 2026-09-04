# 霓虹竞技场（Neon Arena）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Neon Arena**，一款双摇杆竞技场射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一座封闭的几何竞技场中当那个活到最后的驾驶员，敌意图形一波波
从每一条边界涌入。有趣的张力来自分数倍率：短时间窗口内的每次击杀都会提高倍率，
但只要挨到一次伤害就会把它清零。玩家必须不断向危险中推进以维持连锁，而不是
退守安全区。炸弹提供了一个能清屏的应急按钮，代价是牺牲潜在的倍率成长。多个
布局与危险物摆放各异的竞技场迫使玩家调整移动模式，而不是背下一条安全路线。

## 玩家体验流程

玩家进入游戏时看到一个带霓虹线框美学、不断脉动的标题画面，然后从一个小型
名单中选择一个竞技场。游戏立刻开始：飞船位于屏幕中央，一根摇杆（或 WASD）
负责移动，另一根（或方向键）负责瞄准并持续开火。敌人在竞技场边缘以逐步升级的
波次生成——小型飞镖、会分裂的六边形、追踪型菱形、带护盾的圆环。每次击杀都会
累加到一个可见的倍率计数器上；一根计时条显示倍率还有多久开始衰减。擦弹而不
死亡会积累一项额外的擦弹奖励。

波次之间会有一个简短的升级提示，提供武器改装——更宽的散射、更快的射速、
穿透弹，或多一枚炸弹。竞技场本身也可能变化：墙壁收回、危险区域点燃，或出现
重力井。每隔几个波次会有一个 Boss 图形带着成形的攻击入场。失去所有生命后会
显示一份最终分数细目，含倍率数据、最高连锁，以及该竞技场专属的排行榜名次。

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