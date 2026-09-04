# 植物防御（Plant Defense）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Plant Defense**，一款**分路塔防策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一座花园网格横亘在家园与一波波逼近的生物之间。玩家在多路草坪上种下防御者，花费必须主动收集的阳光。每种植物都承担一项战术职责——有的射击，有的阻挡，有的产出经济——而来袭生物的种类会惩罚单一路数的防守。张力在于资源稀缺：阳光来得很慢，植物要消耗真金白银的经济，而一个放错位置的防御者就意味着某一路在援兵长成之前先被攻破。一张冒险地图把关卡串联起来，挑战逐级升级并解锁新植物，让玩家有理由在下一个威胁到来前先掌握好每一件工具。

## 玩家体验流程

玩家从标题画面进入一张呈现关卡路径的冒险地图。选择一个关卡后，会显示即将出现的生物类型，并让玩家从已解锁的阵容中挑选一套植物防御者配置。

关卡在多路网格上进行。阳光会周期性落下，玩家点击收集，积累资源池。植物从工具栏拖到空的网格格子上，每株都要消耗阳光。射手向本路发射弹丸，墙体吸收伤害，产阳光的植物则加速经济。生物成波从右侧边缘进军，各路彼此独立。

生物的多样性迫使玩家随时调整：带甲类型对弱小射击不痛不痒，高速类型能跑过射速慢的植物，飞行类型则绕过地面墙体。后期关卡引入夜间条件，阳光产出下降，迫使玩家依赖替代性的经济植物。

击败所有波次即通关；任何生物到达左侧边缘则失败。胜利会解锁下一个地图节点，有时还会解锁一种新植物。结算画面会展示获得的星数，地图也会有明显更新。

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