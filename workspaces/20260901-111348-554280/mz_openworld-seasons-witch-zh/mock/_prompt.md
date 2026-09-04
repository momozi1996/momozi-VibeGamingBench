# 开放世界四季女巫（Open-World Seasons Witch）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界四季女巫（Open-World Seasons Witch）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名掌控着一座小山谷四季的女巫，在春、夏、秋、冬之间切换以解决问题、
帮助村民。这里的幻想是元素掌控：冻结河流以便渡过，让花朵绽放以吸引蜜蜂产蜜，
融化积雪以显露埋藏的物品，或者让挡路的藤蔓枯萎。张力来自村民的委托——它们需要
特定的季节组合，以及只在某些季节生长的药剂材料。每个季节都会在视觉和机制上
彻底改变整个世界。

## 玩家体验流程

1. **标题画面** —— 一个四格标题，分别展示同一座山谷在四个季节中的样貌，游戏
   名称使用流畅的手写体。开始按钮四周环绕着季节图标。
2. **山谷** —— 玩家在一座山谷中自由移动，其中有村庄、森林、湖泊、山路和农田。
   整个世界的外观会随当前季节而变化。
3. **季节切换** —— 玩家可以施放季节法术来改变世界。一个环形菜单显示四个季节；
   选中其中一个会触发一段视觉转场，改变地形、水体、植被和天空的颜色。
4. **世界反应** —— 每个季节都有机制上的效果：冬天冻结水面并显露冰洞；春天使
   植物生长并让河流充盈；夏天使沼泽干涸并让果实成熟；秋天落叶，显露隐藏的
   小径，并削弱木质结构。
5. **村民任务** —— 村中的 NPC 会请求需要操控季节才能完成的帮助：一位农夫的
   作物需要先下雨（春）再有阳光（夏）；一位建造者需要冻结的湖面（冬）来运送
   石料；一位治疗师需要秋天的蘑菇。
6. **药剂调制** —— 在不同季节采集的材料可以在女巫的小屋里调配成药剂。药剂
   赋予各种能力：速度提升、屏障护盾、生物魅惑。一本配方书记录已发现的组合。
7. **进程** —— 完成任务可获得声望并解锁山谷的新区域。帮助足够多的村民后，
   山间隘口会开启，露出一个需要精通全部四个季节才能应对的最终挑战。

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