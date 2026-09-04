# 开放世界时空穿越（Open-World Time Travel）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界时空穿越游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家发现了一台时空穿越装置，在多个截然不同的时代中探索同一处开放世界地点——
草木繁茂的远古过去、喧闹的工业当下，以及荒凉的高科技未来。在某个时代中的行为
会向后涟漪扩散，改变后续时代的地貌、居民和可通行的路径。这里的幻想是**时间上的
因与果**：玩家读懂世界，在过去做出有意的改动，然后跳向未来见证后果展开。张力
来自蝴蝶效应——一个微小的善举或破坏会跨越数个世纪层层放大——也来自悖论：世界
会抵抗矛盾，玩家必须仔细思考自己改变了什么、又是在何时改变的。游戏应当给人
一种令人脑洞大开、处处相互关联的感觉，就像一个由历史造就的谜题盒。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个"开始旅程"或"开始
   游戏"按钮，以及一幅时间主题背景（彼此交叠、相互渗透的地景、时钟齿轮、极光）。
   不要出现 HTML 引擎 的裸灰色。
2. **三个时代** —— 同一片地理区域被呈现为三个视觉上截然不同的时期：一片带有
   温暖高饱和绿色的远古荒野、一座色调低沉、灰橙交织的工业城景，以及一个冷蓝
   与紫色调的废墟未来。玩家可以在每个时代中自由行走，并认出跨越时间留存下来的
   地标。
3. **时空穿越** —— 玩家启动时空穿越装置在各时代间跳跃。转场会播放一段可见的
   效果，目标时代加载后玩家出现在对应的地图坐标上，从而保持空间上的连续性。
4. **蝴蝶效应** —— 在较早时代中的行为会以可见且对玩法有意义的方式改变后来的
   时代。存在多条因果链：在过去种下某物会改变未来的地貌，摧毁基础设施会重塑
   路线，与 NPC 结交会为其后代留下遗产。
5. **悖论检测** —— 游戏会阻止或惩罚构成悖论的行为。试图摧毁未来的自己所依赖
   之物会触发警告和不稳定状态，直到悖论被消解。
6. **跨时代任务与 NPC** —— 每个时代都有独特的 NPC，他们的任务横跨多个时期。
   完成跨时代目标可解锁新的目的地，或升级时间装置。
7. **时间物品栏** —— 物品具有时代兼容性。有些能经受时空穿越，有些则会腐坏。
   物品栏会告知哪些物品是稳定的、哪些无法在下一次跳跃中存留。

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