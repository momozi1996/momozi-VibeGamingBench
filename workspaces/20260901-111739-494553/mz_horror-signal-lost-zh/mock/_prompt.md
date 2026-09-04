# 恐怖信号失联（Horror Signal Lost）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖信号失联**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名偏远电台里的无线电操作员，负责对来自船只和哨站的求救信号进行三角
定位，而某种看不见的东西正在干扰这些频率。游戏的幻想核心是孤立与恐惧：独自
待在一间黑屋子里，只有噪点和人声为伴，一点点拼凑出外面正在发生的事，而干扰
却越来越凶猛、越来越针对个人。紧张感来自电池管理——无线电会耗电，而黑暗会
把那个存在引得更近。每完成一次三角定位，就会揭开墙外正在展开的恐怖的一角。

## 玩家体验流程

1. **标题画面** —— 一块黑暗的画面，游戏名像即将断掉的信号一样闪烁，配有噪点
   视觉特效，以及一个做成无线电旋钮样式的开始按钮。
2. **无线电台** —— 单房间视图，展示操作员的桌面：无线电设备、一张插着图钉的
   地图、一个电池量表，以及一扇窗外只有黑暗的窗户。房间由无线电的微光照亮。
3. **信号扫描** —— 玩家调节频率旋钮（水平滑块）来寻找藏在噪点中的求救信号。
   信号锁定时会有音频噼啪声，并出现一段文字记录。每个信号都会给出一组坐标。
4. **三角定位** —— 玩家根据信号坐标在地图上放置图钉。连接三个或更多图钉即可
   揭示信号源位置并推进剧情。随着时间推移，地图上会插满图钉。
5. **干扰实体** —— 干扰会周期性地骤然增强。画面扭曲，无线电发出令人不安的
   声响，玩家必须迅速重新调频以摆脱干扰。失败会导致电池耗损和画面损坏。
6. **电池管理** —— 无线电会消耗电池。量表随时间不断下降。玩家可以降低功率
   （调暗房间、限制扫描范围）来节省电量。电池要靠解开信号谜题才能获得。
   如果电力耗尽，房间会陷入黑暗，那个实体就会靠近。
7. **逐步升级** —— 随着定位出的信号越来越多，干扰变得更严重，信号内容更令人
   不适，窗外也会出现移动的身影。最后一个信号将揭示究竟是什么在猎捕玩家。

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