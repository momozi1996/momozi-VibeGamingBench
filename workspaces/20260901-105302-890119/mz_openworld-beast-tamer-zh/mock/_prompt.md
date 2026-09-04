# 开放世界驯兽师（Open-World Beast Tamer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界驯兽师（Open-World Beast Tamer）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在多样的生态区中漫游——丛林、苔原、沙漠、沼泽——寻找并驯服拥有独特能力的
野生生物。这里的幻想是与强大的野兽建立羁绊，并用它们的技能解决环境谜题、抵达
新的区域。张力来自驯服过程本身：每种生物都需要不同的方式（潜行、诱饵、节奏），
而失败的尝试会惊走野兽。被驯服的生物会在使用中进化，获得新的形态和能力。

## 玩家体验流程

1. **标题画面** —— 一个色彩鲜明的标题，展示游戏名称以及各生态区中的生物剪影。
   一个开始按钮启动冒险。
2. **生态区探索** —— 玩家在彼此连通的生态区中自由行走，每个区域都有独特的地形、
   配色和环境生物。生态区的边界在视觉上清晰可辨。
3. **生物发现** —— 野生生物在各个生态区中游荡，行为模式可见。图鉴中的剪影
   暗示着尚未发现的物种。每种生物都有独特的精灵图和待机动画。
4. **驯服** —— 接近生物会触发驯服小游戏：玩家必须完成某种模式（掌握点击时机、
   提供正确的诱饵，或不惊动对方地潜行靠近）。成功后该生物加入队伍。
5. **生物能力** —— 每只驯服的生物都有一项独特能力：火焰吐息能融化冰障，钻地者
   能挖穿松软地面，飞行者能载着玩家越过沟壑。玩家切换当前生物来解决谜题。
6. **环境谜题** —— 被堵住的道路需要特定的生物能力。冰封的河流需要火焰，深渊
   需要飞行，封闭的洞穴需要蛮力。
7. **进化** —— 在解谜和探索中使用生物会填充一条经验量表。填满后，该生物进化为
   更强的形态，拥有增强的能力和新的精灵图。

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