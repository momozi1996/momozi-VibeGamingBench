# 角斗竞技场（Gladiator Arena）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Gladiator Arena**，一款**角斗竞技场管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个奇幻罗马背景下拥有一座角斗竞技场，招募斗士、训练他们、安排比赛，并升级竞技场以吸引更大的观众和更阔绰的赞助商。每名角斗士都有属性、战斗风格和性格——有些是能招来看客的人群宠儿，有些则是能赢却让观众乏味的高效杀手。张力存在于观赏性与存活之间：人群想看鲜血和戏剧性，但死掉的角斗士替换起来很贵。博彩又加了一层风险与回报：玩家可以押注自己的斗士来多赚金币，但冷门翻盘时有发生。整体基调是黄沙与钢铁的恢弘：轰鸣的人群、交击的兵器，以及竞技场地面上的戏剧。

## 玩家体验流程

玩家从标题画面开始一个新的竞技场赛季。主视图展示竞技场建筑群：训练场、营房、竞技场地面和一间管理办公室。时间一天一天推进，走向已排定的比赛之夜。

角斗士从奴隶市场或自由斗士池中招募——每人都有战斗属性（力量、速度、防御）、武器偏好和人群吸引力评级。训练能在数日内提升属性，但要花费食物和教练费用。玩家为他们分配训练方案：力量操练、对练，或是表演技巧练习。

比赛之夜排在日历上。玩家从自己的名单中挑选对阵组合，对手是来访的挑战者或敌对竞技场的斗士。战斗过程中，角斗士依据各自属性与风格自动交战——玩家观看但无法干预。人群的兴奋度会随着戏剧性瞬间（濒死、反败为胜、终结技）而攀升。

收入来自门票销售（取决于观众规模）、赞助合约（取决于竞技场声望）以及博彩赢利。支出包括角斗士的日常开销、训练成本、竞技场维护，以及受伤斗士的医疗费用。

游戏会记录金币、竞技场声望和赛季胜场。一个经过美术处理的结算画面会展示赛季统计数据和冠军角斗士的高光时刻。

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