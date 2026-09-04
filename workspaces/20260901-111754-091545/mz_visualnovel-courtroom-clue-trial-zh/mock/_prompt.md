# 法庭线索审判（Courtroom Clue Trial）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Courtroom Clue Trial**——一款小体量的
**法庭推理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨
程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名初级律师，试图在一场戏剧性的审判中揭穿一份虚假的说法。每一句证词
都是一个小谜题：证人说的话听起来合情合理，但玩家卷宗里的某一份证据能证明它是
错的。张力来自于选择何时追问、呈上什么，以及在案子彻底崩盘前法官还能容忍多少
次失误。错误的指控会损耗信誉；失误过多则会以流审告终。游戏的幻想内核是察人
观心、揪出谎言，并用一次时机恰到好处的异议扭转整个法庭。

## 玩家体验流程

玩家开局看到的是一个卷宗风格的标题画面，它奠定了整体基调：法庭徽章、一个案件
编号、一场待审案件的沉重感。开始办案后，会出现一份案情摘要，列明指控、嫌疑人
以及证据卷宗。接着证人登上证人席。他们的证词一句一句滚动播出，玩家可以追问更多
细节，或推进到下一句。在任何时刻，玩家都可以打开证据托盘，查看载有时间戳、
指纹或地点等事实的卡片，并挑一份来对抗当前这句陈述。匹配正确会触发一段异议
演出：证人语塞，证词随之更新，案情发生转折。匹配错误则会招来法官的处罚。第一个
矛盾点被击破之后，会浮现出第二层：一次反驳、一条新线索、一个不太站得住脚的
不在场证明。玩家必须穿越这个更深的谜题才能抵达判决。成功意味着一场有设计感的
胜利，伴随结案的礼乐。失败意味着一个流审画面，并提供重试选项。两种结果都应当
感觉像结局，而不是错误状态。

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