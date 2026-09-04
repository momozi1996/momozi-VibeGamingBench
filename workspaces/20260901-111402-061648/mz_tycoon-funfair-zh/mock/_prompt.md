# 经营：游乐场（Tycoon: Funfair）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**基于网格的主题公园管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是把一片荒地变成人人爱去、热闹沸腾的游乐园。玩家一半是建筑师，一半是会计师：每一条铺下的道路、每一处摆好的设施，都在塑造活生生的人群如何走动、消费和感受。有趣的张力在于成长会自我喂养——满意的人群带来现金去建更多游乐设施，而更多设施又吸引更大的人群——但雪球也会朝反方向滚。疏忽道路、抬价太狠，或者让队伍无限膨胀，公园空得会比填满时更快。压力来自在雄心与人群耐心之间求平衡：扩张太快就破产，太慢则游客厌倦。风险始终在于某一个糟糕决定——一条死路、一次涨价、一处缺失的便利设施——会在数字反映出来之前悄悄毒害满意度。

## 玩家体验流程

玩家从一块空地、一座大门和一小笔现金开始。最初几分钟是从入口向外铺出一条主干道路，并放下第一个游乐设施——看着最初的三两个游客涓涓流入并花钱，就是那个钩子。从那里开始，剧情弧线是有机的增长：收入资助新的游乐设施和摊位，人群膨胀起来，网格逐渐填满色彩与动感。

玩家最留意的其实是人群本身——沿着道路流动的小小访客、聚集在热门设施旁的人潮、朝食品摊漂移的身影。一座建得好的公园处处涌动着动感；一座规划糟糕的公园则有冷清的角落和瓶颈。满意度读数和现金计数器一眼就能讲清故事，但真正的反馈是视觉的：兴旺的公园看上去就是忙碌而鲜活的。

定价是那根即便在成熟公园里也能让局面保持有趣的杠杆。收费更高，每位游客的价值更大，但来的人更少、走得更早。降价则人群涌入闸门，但利润变薄。玩家总在调这个旋钮，同时还要做布局决策——下一个设施放哪儿，是否把现有设施升级成招牌项目，何时再加一个食品摊来让公园远端的游客也满意。

随着时间推移，那块空地从裸露的网格蜕变为一片铺展开来、熙熙攘攘的游乐场。进度会跨存档留存，因此玩家回来时还是同一座公园，从上次离开的地方接着玩。整体基调明亮、欢快、色彩浓郁——一场洒满阳光的嘉年华，满是旋转的游乐设施和糖果般的颜色。

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