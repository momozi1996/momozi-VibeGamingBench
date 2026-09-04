# 黑色侦探（Detective Noir）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Detective Noir**——一款
**侦探推理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨
程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名私家侦探在一座浸满雨水的城市里办案：勘查犯罪现场、询问嫌疑人，并在一块
推理板上拼凑出谁在何时、为何做了什么。每个案件都是一桩自成一体的谜案，包含
物证、证人陈述，以及一张玩家必须解开的关系网。张力是认知层面的：所有线索都
摆在那里，但要正确地把它们连起来，需要仔细阅读和逻辑排除。错误的指控会白白
消耗信誉，并锁死部分信息。整体调性是经典黑色电影：阴影、风衣、爵士底韵，以及
一群人人都有所隐瞒的道德灰色角色。

## 玩家体验流程

从标题画面开始，玩家在案件板上选择一个案件。每个案件以一个犯罪现场开场——一处
以黑色电影风格呈现的地点，带有可交互热点。点击热点会揭示证据：一片血迹、一封
被撕碎的信、一件放错位置的物品。每一份证据都会连同其细节被加入玩家的笔记本。

随后玩家会走访各个地点，询问嫌疑人和证人。每个角色都有能揭示信息的对话——有些
是真话，有些是误导。玩家可以对某些陈述追问以深入挖掘，有时能解锁新的证据或
矛盾点。

推理板是核心的解谜界面：玩家通过在卡片之间拖出连线，把证据与嫌疑人、时间线和
动机连接起来。当连接足够多时，玩家就可以提出指控——选定何人、何种凶器、何时
作案。正确的指控会以一段戏剧性的揭晓演出破案。错误的指控则要付出信誉点数；
错得太多，案件就会变成悬案。

游戏提供多个难度不同的案件。一个有设计感的结算画面会展示案件结果、找到的证据
以及推理准确率。

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