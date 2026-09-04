# 开放世界钓鱼（Open-World Fishing）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界钓鱼游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个宁静的开放世界中探索，其间点缀着湖泊、河流和海岸，抛出鱼线钓起
各种鱼类。这里的幻想是耐心得到回报：读懂水面、掌握抛竿时机、与咬钩的鱼周旋，
最终把一条稀有渔获记入图鉴。张力来自收线小游戏——拉得太猛线会断，太松鱼会跑。
天气和时间会改变上钩的鱼种，促使玩家在新的条件下重访熟悉的钓点。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮和一片
   宁静的水面背景。不要出现 HTML 引擎 的裸灰色。
2. **世界** —— 玩家在开放的地貌中自由行走，其中有几处视觉上截然不同的水域——
   一片平静的湖泊、一条带水流效果的湍急河流，以及一段深海岸线。每处水域的
   外观和感觉都不同，栖息的鱼类也各不相同。
3. **抛竿** —— 玩家蓄力一条抛竿力量条，松开后甩出鱼线。距离取决于时机。鱼线
   落水时带有水花效果。
4. **咬钩与收线** —— 浮标漂在水面上。鱼咬钩时，玩家通过一次限时按键把它钩住，
   然后通过收线和放线来控制线的张力。一条张力条显示受力程度——张力过大鱼线
   就会断。
5. **鱼类多样性** —— 多种截然不同的鱼种，外观、体型和栖息地各异。钓上一条鱼
   会显示它的名称、尺寸和风味文本。稀有鱼类有独特的视觉亮点。
6. **钓鱼图鉴** —— 一本图鉴记录已钓到的鱼种，未钓到的以剪影显示，并附带一个
   完成度百分比。
7. **天气与时间** —— 天气变化会影响出现哪些鱼。昼夜循环改变光照和水的颜色，
   有些鱼种只在特定条件下才会咬钩。

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