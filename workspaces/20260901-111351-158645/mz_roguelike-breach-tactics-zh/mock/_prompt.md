# 突破战术（Breach Tactics）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Breach Tactics**——一款在小型网格上进行、
敌人意图完全可见的战术 Roguelike。这不是原型，而是一个**完整、可发布的微型
游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一支由三台机甲组成的小队保卫城市网格，抵御一波又一波异星入侵者。妙处在于：每个
敌人都会在玩家行动之前预告自己的下一步，让每个回合都变成一道关于位移、阻挡与
牺牲的空间谜题。网格很小（8x8），建筑占据着必须保护的格子——若被摧毁的建筑过多，
时间线就宣告失守。战斗之间，玩家赚取反应堆核心，用来升级机甲能力或解锁带被动
特质的新驾驶员。时间线重置机制给玩家每场战斗有限次数的整回合撤销，让灾难性失误
还有挽回余地。四座难度递增的岛屿各自以一场拥有独特网格机制的 Boss 战收尾。

## 玩家体验流程

标题画面展示机甲降落到网格上。岛屿选择地图展示四座岛屿以及分支任务路线。

每场任务把机甲小队放在一片有建筑和不断刷出的敌人的网格上。在玩家移动之前，每个
敌人都会显示自己打算做的事：攻击方向、移动目标或刷出位置。玩家移动每台机甲，
并让每台机甲使用一个能力——推击、射击、护盾、修复或特殊技。所有机甲行动完毕后，
敌人同时执行它们预告过的行动。

保护建筑是首要任务——每栋建筑被毁都会削减一条结构完整度条。完整度耗尽即任务
失败。时间线重置（每场战斗次数有限）可以回退一整个回合。任务之间的升级画面提供
新武器、驾驶员能力和反应堆功率分配。完成一座岛屿即解锁下一座。最终的胜利画面
展示完成的任务数、保住的建筑数和使用过的重置次数。

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