# 密室逃脱（Escape Room）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Escape Room**——一款
**叙事型密室逃脱视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一间锁死的房间中醒来，完全不记得自己是怎么来的。每个房间都是一个自成
一体的谜题盒：检视物品、组合道具、破译密码，并找到出口。但这同时也是一段叙事
——在逃脱过程中做出的选项会让故事分支，揭示出关于玩家为何被困的不同真相。多个
房间串联成一个更大的谜团，而要抵达真结局，就必须解开所有房间并做出特定的叙事
选项。张力是双重的：解谜带来的智性满足，叠加上发现真相时的叙事恐惧。整体调性
是氛围悬疑：昏暗的灯光、晦涩的字条，以及被禁闭时那种滴答逼近的压迫感。

## 玩家体验流程

从标题画面开始，玩家进入第一个房间。画面呈现一幅第一人称视角风格的房间插图，
带有可交互热点——抽屉、画作、锁具、散落的物件。点击热点会检视它们，有时会把
道具加入道具栏。

道具可以互相组合（钥匙 + 锁、密码本 + 加密信息），也可以用在热点上。每个房间
都有一串门槛式的谜题：解开一个，就会揭示下一个。谜题类型包括图案匹配、密码
破译、隐藏物品寻找和逻辑推演。

在解谜段落之间，会出现影响故事分支的叙事时刻，提供对话选项。玩家可能会找到一张
揭示某个角色动机的字条，而他们的回应决定了他们相信哪个版本的事件——从而影响
接下来解锁哪些房间、抵达哪个结局。

多个房间构成一条序列，一个比一个更难。真结局要求玩家完成所有房间并做出特定的
推理选项。其他结局同样有效，但并不完整——玩家会知道自己漏掉了什么。

一个有设计感的结算画面会展示逃脱用时、解开的谜题数量以及抵达的是哪个结局，
并附上一条关于未走之路的提示。

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