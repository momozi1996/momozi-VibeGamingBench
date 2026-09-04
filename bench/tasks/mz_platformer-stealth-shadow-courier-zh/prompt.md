# 潜行：暗影信使（Stealth: Shadow Courier）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Shadow Courier**，一款小巧的**俯视视角潜行渗透游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是成为一名孤身信使，靠的不是打斗而是读懂现场——记住巡逻节奏、在层层叠叠的视野锥之间穿针引线，并挑准那个恰到好处的时机溜过一道门或掐掉灯光。有意思的张力在于：每一个目标都会改变玩家的暴露程度——去拿钥匙就意味着穿过一条亮着灯的走廊，去偷文件就意味着在守卫最森严的房间里逗留，而抵达出口又意味着重走一遍巡逻已经变了位的地面。压力来自玩家所能看见的东西（视野锥弧、阴影池、被锁的路线）与他们为了推进而必须冒的风险之间的落差。一步算错，整个计划就崩塌成刺耳的警铃和逐渐收紧的包围网。

## 玩家体验流程

玩家进入一个昏暗、氛围十足的标题画面，它确立了这场秘密行动的调性——游戏名、一道影影绰绰的设施剪影，以及一个开始的入口。

一段简短的任务简报交代了赌注：档案室里存放着一份密封文件，守卫在走廊上巡逻，而信使必须潜入、偷走它，再不被发现地脱身。

操控从一张俯视视角的设施地图开始。信使在房间和走廊之间平顺移动，贴着墙壁和掩体物件走。守卫沿可见的巡逻路线行走，视野锥像探照灯一样在他们前方扫过。玩家读时机、等一个空档，然后溜过去——或者另寻一条绕行的路。

再往深处，一道锁着的门挡住了直通路径。玩家去找一把钥匙或凭证，把它拾起，并看到 HUD 确认已持有。一个电灯开关或配电箱提供另一种力量：拉下它会让一整片区域陷入黑暗，缩小守卫的感知范围，并打开此前完全暴露的阴影路线。

文件就在最危险的那个房间里。偷到它会更新任务状态，并把目标切换为撤离。玩家原路返回或另找一条通往出口的路线，此时他们已经知道巡逻时机已变或警戒等级已升。

被发现会触发升级——先是警告状态，若信使继续逗留则被抓获。带着文件抵达出口会呈现一个经过设计的成功画面；被抓获则呈现失败画面。无论哪种情况，重试和返回标题的操作都让玩家留在循环之中，无需重启应用。

## Vibe Gaming Quality Bar

本题的玩法、逻辑和验收锚点优先于下面的表达规范。不要重写或删减上面的核心
机制；这些要求用于把同一玩法稳定地落成一个可玩的 Vibe Gaming 垂直切片。

- **先玩后美化**：先保证开始、核心输入、状态变化、成功/失败和重玩闭环，再做视觉与动效。
- **技术栈按玩法选最小充分方案**：
  - 2D 规则游戏优先 `HTML5 Canvas 2D + Vanilla JS`；
  - 面板、卡牌、对话和菜单密集时可用 `DOM + CSS + Vanilla JS`；
  - 图标、线稿和几何动画可用 `纯 SVG + CSS 动画 + Vanilla JS`；
  - 连续碰撞、镜头、粒子或街机物理可用 `PhaserJS`；
  - 3D 或空间镜头可用 `Three.js + WebGL`；
  - 只有确实需要 GPU 大规模并行或自定义 GPU 管线时才用原生 `WebGPU`；
  - 可以混合 Canvas、DOM、CSS、SVG，但必须明确每层职责，禁止为了“技术炫技”增加无关复杂度。
- **规则层独立**：`game_logic.js` 保存唯一真相，暴露 `createGame(opts)` 和
  `advance(game, input, dt)`；渲染层只读取状态并呈现，不能偷偷维护第二套规则。
- **每帧可解释**：输入要映射到明确动作，动作要产生可观察状态变化；无效输入、
  边界条件、资源耗尽、受伤、胜利和失败都要有反馈。
- **Vibe 不是装饰**：至少使用两种反馈通道（动画、位移、缩放、粒子、声音、
  HUD 或镜头）表达关键动作；反馈不能遮挡目标或破坏可读性。
- **移动端优先**：关键点击目标至少 44×44 CSS px，支持触摸和鼠标，不能依赖 hover；
  390×844、360×800、430×932 和 1280×800 不得横向滚动或出现控件重叠。
- **确定性与测试**：随机内容使用 seed；至少验证核心规则、胜负条件、重开/恢复、
  输入边界和一个异常状态；不要用截图存在或文字出现冒充功能完成。
- **原创与合规**：使用原创名称、角色、图形、音效和关卡，或明确许可的素材；
  不复制任何原作商标、角色、文本、美术、音乐、关卡数据或代码。

完成后报告：实际文件路径、启动命令、测试命令与结果、关键截图、已知限制、
技术栈取舍和原创资产来源。

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

交互方案（keyboard-first）：本题材以键盘交互为主：提供方向键或 WASD、Space、Enter、Esc 等清晰按键，并在自然需要时加入鼠标。
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
