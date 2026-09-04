# 开放世界生存（Open-World Survival）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界生存游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一片荒野中孤身醒来，必须采集资源、制作工具、搭建庇护所，并活过夜晚。
这里的幻想是**压力之下的自力更生**——每一个决定都很重要，因为白昼有限、饥饿
不止，而世界在天黑之后变得充满敌意。有趣的张力在于优先级的取舍：是现在就找
食物还是为以后做工具，是探索还是加固，是冒险还是求稳。气温下降，视野收窄，
生存取决于准备。美术风格应当给人**质朴、粗糙、有沉浸感**的观感——可以想象成
小体量的 *Don't Starve* 结合 *A Short Hike*。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮，以及一幅
   荒野背景（森林、营地或山景）。不要出现 HTML 引擎 的裸灰色。

2. **荒野** —— 玩家出生在一张开放世界地图上，其中有多个视觉上截然不同的生态区：
   青草平原、茂密森林，以及多岩地形或水域。玩家可以在一片广阔的可探索空间中
   沿 8 个方向自由移动。

3. **资源采集** —— 地图上散布着可交互的资源：可获取木材的树、可获取石料的
   岩石露头，以及可获取食物的浆果丛。玩家靠近资源并交互即可采集，并伴有可见的
   反馈（动画、粒子效果，或资源本身消失）。

4. **生存数值** —— 状态条始终可见（饥饿、口渴或体温）。它们随时间下降。当某条
   状态条降到临界水平时，玩家会承受后果：移动变慢、屏幕暗角、生命值流失，
   或其他可见的惩罚。

5. **制作** —— 一个制作面板显示可用的配方，它们会消耗采集到的材料。配方产出
   有用的物品：取暖用的营火、提供保护的庇护所、加快采集的斧头。玩家能看到
   哪些可以造、哪些资源还不够。

6. **建造与放置** —— 制作出的建筑可以作为持久对象放置到世界中。营火提供温暖
   和光亮。庇护所可恢复生命值或阻挡环境伤害。放置时有清晰的视觉指示。

7. **昼夜循环** —— 时间自动流逝。白天明亮而安全。夜晚使地图变暗、视野收窄，
   并加快生存数值的消耗。夜间待在营火附近可以扩大玩家的安全半径。活过一个
   完整的昼夜循环是最低的成功条件。

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