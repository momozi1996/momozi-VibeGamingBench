# 六边形征服（Hex Conquest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Hex Conquest**，一款**回合制六边形格征服策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两个阵营为一片笼罩在迷雾中的六边形图块大陆而交战。每回合玩家用占领城市带来的收入招募单位，让军队穿越塑造每一场交战的地形，并一格一格地把迷雾推开。张力活在不完整的信息里：敌人在迷雾背后发展，而每一次推进都有可能撞上一处早有准备的防线。胜利要求在"扩张换收入"与"收缩固防守"之间取得平衡，读懂地图上的咽喉要地，并在对手的经济反超之前发动决定性一击。

## 玩家体验流程

玩家从标题画面挑选一个阵营——每个阵营都有独特的单位阵容与经济加成，会塑造前期策略。地图会在六边形格上生成城市、森林、山脉与平原，迷雾覆盖玩家起始领土之外的一切。

每个回合都有清晰的阶段：从己方城市收取收入、在城市招募单位、让单位跨越六边形格移动、以及攻击相邻的敌人。地形至关重要——森林减缓移动，山脉阻断移动，河流需要额外代价才能渡过。单位分为不同类型：步兵以低成本据守阵地，骑兵快速突击，攻城单位则用于攻破设防城市。

迷雾只在玩家单位周围散开，因此侦察是一项实打实的投入。AI 对手会按自己的策略扩张、建设与进攻。攻下一座城市会把它的收入转给征服者，并把前线向前推进。

当一方控制所有城市或消灭敌方最后一个单位时，游戏结束。一个精心设计的结算画面会展示结果与领土统计数据，并提供再战一局的选项。

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

交互方案（pointer-first）：本题材以鼠标/指针交互为主：支持点击、悬停、拖拽或框选；只有自然需要时再加入键盘快捷键。
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