# 洞穴深渊（Spelunk Depths）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Spelunk Depths**——一款带物理物件和店主的
程序化平台跳跃 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位探险家向下穿越程序化生成的洞穴层，利用绳索、炸弹以及手边任何物件来通过陷阱、
击败生物、收集宝藏。世界里的每一个物件都有物理——罐子可以砸向敌人，支撑被破坏后
岩石会滚落，爆炸会在可破坏地形中连锁传播。店主在某些层出售道具，但如果玩家偷东西
就会转为敌对。在任意一层逗留过久会激活幽灵计时器，产生一个无敌的追猎者，迫使玩家
持续向前推进。满足特定条件后会解锁捷径，让老练的玩家跳过前面的层。死亡是永久的，
会把玩家送回地表，除了经验之外一无所有。

## 玩家体验流程

标题画面展示带深度标记的洞穴入口。开始一轮时，探险家出现在第 1 层，携带基础装备：
4 条绳索和 4 枚炸弹。

每一层都是一个程序化生成的平台跳跃关卡，底部有一个出口。探险家奔跑、跳跃、用鞭子
抽打敌人、向上抛出绳索造出可攀爬的绳线，并放置炸弹炸穿地形。罐子、木箱和骷髅可以
被捡起投掷。陷阱包括弓箭陷阱、尖刺坑和压碎方块。敌人以简单 AI 巡逻。

商店每隔几层出现一次，摆出待售道具——购买需要从宝石和箱子中收集来的金币。偷窃会
在这一轮的余下时间里触发店主的敌意。在一层停留 3 分钟后，一个幽灵会刷出并不停
追赶玩家。每 5 层环境主题变换一次。死亡时展示抵达深度、收集金币和击败敌人数的总结。

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