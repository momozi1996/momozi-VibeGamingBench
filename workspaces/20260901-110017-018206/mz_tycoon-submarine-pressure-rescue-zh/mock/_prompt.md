# 潜艇压力救援（Submarine Pressure Rescue）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Submarine Pressure Rescue**，一款小体量的**潜艇损害管制与救援模拟**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家指挥一艘伤痕累累的救援潜艇，正朝着压毁深度下沉。海水从破损的舱室涌入，压力攀升，氧气流失，而电网一次只能供得起有限的系统。每一道命令都是一次取舍：封闭隔壁能减缓进水，却会困住一名船员；把电力改道给抽水泵，就会失去声呐；派工程师去补船体破口，医务室就无人照看。这里的幻想是在不可能的约束下做出绝望而胜任的领导决断——让一艘正在死去的船撑得够久，抵达救援信标并把生还者带回家。

整体基调是紧张的工业求生感：昏暗的船体剖面图、警示灯、蓝色的声呐扫描、阀门图标、船员标记，以及清晰的警报反馈。

## 玩家体验流程

玩家一进入游戏，看到的是一个经过美术处理的潜艇救援标题画面，带有船体剪影和紧急信号。一段任务简报介绍目标、船员名单和初始受损状态。

任务开始后，玩家看到潜艇的舱室布局，附带水位、压力表、氧气和电力路由。早期的损伤还应付得来——一处漏水，一名船员可供派遣。玩家从中学会节奏：辨明威胁、分派船员、盯着维修进度、查看声呐上到信标的距离。

随着任务推进，故障开始连锁。第一个舱室还在抽水，第二个就破损了。电力下降，玩家必须选择哪些系统继续在线。封闭区段里氧气下降。船员被困或受伤。声呐显示信标越来越近，但航线上又出现了新的危险。

到了最后一段路程，一切都在同时崩坏。玩家做出快速而并不完美的判断——牺牲一个舱室来保住其余部分，把最后一点电力储备烧在抽水泵上，指望船体撑得住。抵达信标并稳住船体则显示救援成功。船体崩塌、氧气耗尽或撤离失败则显示落败。两种结局都经过美术处理并可继续操作导航。

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