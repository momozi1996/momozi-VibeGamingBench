# 蚁群帝国（Ant Colony）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ant Colony**，一款**俯视视角的蚁群经营策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家从高空俯瞰指挥一整个蚁群，指派工蚁挖掘隧道、采集食物、照料幼虫、抵御入侵者。蚁群是一个活的有机体：蚂蚁需要分配职责，隧道需要规划以保证流转效率，而食物储备决定了能养活多少张嘴。张力来自互相竞争的优先级——每一只在挖土的蚂蚁就是一只没在觅食的蚂蚁，每一条延伸出去的隧道都是一条新的防线。季节会改变地表：夏季食物充沛但捕食者也多；冬季则切断补给线，迫使蚁群靠存粮度日。核心幻想是成为蜂巢式群体的隐形大脑，把成千上万个微小决策编排成一个繁盛的地下文明。

## 玩家体验流程

玩家从标题画面开始一个新蚁群。视图呈现一幅大地剖面，上方是地表，下方是土壤。蚁后位于起始巢室中，玩家指挥最初的工蚁向外挖掘。

挖掘会形成隧道与巢室。玩家为巢室指定用途：育婴室让虫卵孵化更快，粮仓防止食物腐坏，兵营训练兵蚁。通过把蚂蚁拖到任务区域来分配职责——觅食蚁前往地表，挖掘蚁延伸隧道，护理蚁照料幼虫，兵蚁巡守出入口。

食物以零散资源的形式出现在地表。觅食蚁沿隧道路线把食物搬回——路径越短越宽，运送就越快。蚁后产卵孵化出新蚂蚁，蚁群随之壮大，但每只蚂蚁每天都要消耗食物。食物收入跟不上却过度扩张，蚁群就会饿死。

威胁会周期性到来：敌对昆虫从隧道入口入侵，雨水淹没浅层隧道，冬季冻结地表食物。玩家必须在扩张与防御之间取得平衡，并规划隧道深度以抵抗洪水。

游戏会记录蚁群人口与存活天数。当蚁后死亡或达成某个生存里程碑时，一个精心设计的结算画面会展示蚁群统计数据。

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