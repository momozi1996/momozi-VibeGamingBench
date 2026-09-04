# 交通网络（Transit Web）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Transit Web**，一款 2D 交通网络模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是从零开始设计一座城市的交通网络，用彩色线路连接各个站点，并看着
客流像血液穿过血管一样在系统中流动。有趣的张力来自资源稀缺：玩家只有有限的
线路、车厢和隧道，去服务一座不断膨胀的城市。新站点会随时间出现，不同形状代表
不同的乘客目的地类型，而过度拥挤的站点最终会瘫痪，导致游戏结束。每一次线路
铺设都是一种承诺——改线会浪费宝贵的时间，而乘客正在越积越多。方案的优雅程度
很重要：设计良好的网络能从容承接增长，而一团乱麻会在自身的复杂度下崩塌。

## 玩家体验流程

玩家进入游戏时看到一个极简城市地图的标题画面，随后从一张小地图开始，图上有
3 个形状各异的站点（圆形、三角形、方形）。玩家按顺序点击两个或更多站点即可
绘出一条连接它们的线路。微小的乘客图标会出现在站点上，每个的形状都标示其
目的地类型。乘客会登上沿线路行驶的列车，并在形状匹配的站点下车。

随着时间推移，新站点会在地图各处出现。玩家会定期收到资源发放：新线路、额外
车厢（提升线路运力），或隧道（允许跨河）。等候乘客积压过多的站点会闪现警告，
并最终溢出，结束这一轮。玩家可以随时改线，但必须管理好过渡期。不同的地图
布局提供各异的挑战——河流城市、岛链、蔓延的郊区。一轮结束的画面会显示存活
天数、送达的乘客数以及网络效率数据。

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