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