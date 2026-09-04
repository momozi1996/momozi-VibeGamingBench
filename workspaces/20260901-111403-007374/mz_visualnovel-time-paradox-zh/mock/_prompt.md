# 时间悖论（Time Paradox）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Time Paradox**——一款
**时间旅行悖论视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在过去与现在之间往返，在过去做出的对话选项会向前涟漪扩散，改变现在。但
因果律是脆弱的：相互矛盾的改动会制造出悖论，而它们必须在现实崩塌之前被解决。
玩家要同时管理多条时间线，追踪哪些改动彼此兼容、哪些会造成冲突。张力是组合式的：
每一个过去的选项都修好了现在的一个问题，但可能又造出两个新问题。整体调性是科幻
悬疑：时间扭曲特效、分屏时间线视图，以及看着现实自我重写时的那种眩晕感。

## 玩家体验流程

从标题画面开始，玩家进入当下的场景——有什么地方不对（一位朋友失踪了、一栋建筑
被毁了、一条讯息完全说不通）。一台时间装置让玩家可以跳跃到同一地点的过去版本。

在过去，玩家做出改变事件走向的对话选项。回到现在，就能看到后果：在场的角色
不同了、场景中的物品不同了、可用的对话也不同了。一个时间线指示器会显示现实的
当前状态以及任何生效中的悖论。

当两处过去的改动彼此矛盾时（救 A 需要一件已被救 B 消耗掉的物品），悖论就会
发生。悖论量表会随之填充——一旦充满，时间线就会崩塌，游戏结束。玩家必须找到
解法：既满足两边要求、又不产生矛盾的替代路径。

多条时间线分支会在一张时间线地图上以可视化方式被追踪。玩家可以在过去的各个
时刻之间跳跃，以调整选项。真结局要求解决所有悖论，并抵达一条所有当下问题都
被修好的稳定时间线。

一个有设计感的结算画面会展示时间线状态、已解决的悖论数量以及抵达的是哪个结局。

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