# 间谍主控（Spy Handler）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Spy Handler**——一款
**间谍行动管理视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名主控官，在指挥席上调度外勤特工、接收讯息、做出实时决策，并同时
管理多项行动。信息是不可靠的——特工可能已被渗透，情报可能是被人塞进来的，而
时间压力逼着你在还没完全弄清之前就做决定。玩家阅读传入的电讯、从有限的选项中
挑选回应，并承受那些在各项行动之间连锁扩散的后果。张力在于高压下的信息管理：
线头太多、时间不够，还有那个挥之不去的问题——该信谁。整体调性是冷战间谍：加密
电文、档案卷宗、地图上的红色图钉，以及数条人命悬于一条回复之上的重量。

## 玩家体验流程

从标题画面开始，玩家进入行动室——一张办公桌，上面有一台讯息终端、一幅标示特工
位置的地图，以及若干档案卷宗。时间以实时方式推进（可加速），外勤特工的讯息陆续
传来。

每条讯息都呈现一个处境：某位特工报告发现目标、请求撤离、警告有人跟踪，或询问
指令。玩家阅读讯息，并从两到四个选项中选出一个回应。回应各有后果：派出支援要
消耗资源，命令特工继续行动会危及他的安全，而等待可能导致窗口关闭。

多项行动同时进行。在处理一名特工的危机时，另一名特工的讯息又到了。玩家必须做
分诊——有些状况十万火急，有些可以等。优先级系统能帮上忙，但并不能消除压力。

信息的可靠性是核心挑战。有些讯息含有来自已被渗透特工的虚假情报。玩家必须交叉
比对各方报告、查看特工的信任评级，有时还得牺牲一项行动来保护整个网络。信任评级
会根据特工情报是否被证实准确而更新。

行动以成功或失败告终。一个有设计感的结算画面会展示任务结果、特工状态（安全、
被捕、被收买）以及总体收集到的情报。

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