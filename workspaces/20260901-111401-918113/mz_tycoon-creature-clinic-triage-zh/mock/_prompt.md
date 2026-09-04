# 生物诊所分诊（Creature Clinic Triage）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Creature Clinic Triage**，一款小体量的**生物护理诊所模拟**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一个繁忙的班次里经营一家小小的奇幻兽医诊所。生物到诊的速度快于能被治疗的速度，每只身上都带着可见的病症，暗示它们需要什么。核心张力在于高压下的分诊：先接诊哪位病患，把它送去哪里，还在排队等候的那些又会怎样？判断正确、调度得当，诊所就能运转顺畅、积累声望；判断失误、延误或错配，则要付出健康与信任的代价。

整体基调温暖却讲究实务。诊所大厅应当显得生机勃勃：排队的生物、忙碌的工位，以及事情做对或做错时清晰的反馈。避免电子表格式的美学；要让它像一间真正运作中的奇幻医务室。

## 玩家体验流程

玩家一进入游戏，看到的是有主题感的诊所门厅，随后开始一个班次。病患陆续进门，每一只都是有明显症状和紧急程度指示的独特生物。最早到诊的都很直白——一种明确的病症，一个显而易见的去处。玩家从中学会节奏：查看、决断、分流。

随着班次推进，队伍越排越长。新的生物种类出现，带着陌生或复合的症状。工位被占满，或者物资见底。此时玩家必须权衡取舍：先稳住危重病例，还是先清掉简单的以腾出接诊能力？分流错误会浪费时间并让病患恶化。忽视紧急程度则会让病情持续劣化。

到了班次后期，压力达到顶点——急诊、复合病例、资源短缺。玩家要在接诊能力与紧急程度之间来回权衡，快速做出并不完美的决定。班次结束时，一份结算总览反映玩家的管理成效：治愈的生物、失去的生物、赢得的声望，以及是否解锁了更难的班次或升级。

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