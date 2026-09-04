# 信号铁路调度员（Signal Rail Dispatcher）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Signal Rail Dispatcher**，一款小而精的 2D 铁路信号与路线管理游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一间狭小信号楼里的独任调度员，看着彩色列车在示意图板上缓缓爬行，做出会在时间上一路涟漪扩散的瞬时排线决定。每一次道岔扳动都锁定一条路径；每一个红灯都以准点率为代价换来思考的余地。核心幻想是**在不断累积的压力下静默地掌控全局**——时刻表起初温和，随后把互相冲突的班次层层堆叠，直到图板变成一张险象环生的网，玩家必须提前想好几步才能让一切保持流动。最理想的版本感觉像一道控制室谜题：一次错误的切换就会连锁成延误，而一个干净利落的班次则来之不易。

## 玩家体验流程

1. **班次开始** —— 一个精心设计的标题画面定下铁路控制室的基调。玩家开始一个班次，看到一张紧凑的轨道示意图，其中车站、侧线、信号机与可切换的道岔像示意地图一样铺陈开来。
2. **读懂图板** —— 列车在入口点出现并沿轨道缓行。每列车都有可见的身份标识——颜色、班次类型、目的地——而时刻表或 HUD 会告诉玩家它需要去哪里、何时抵达。信号机亮红或亮绿；道岔显示当前扳向哪一侧。
3. **排线决策** —— 玩家点击信号机来扣停或放行列车，并扳动道岔以改变路径。被放行的列车会沿着已设定的路线行驶，直到遇上下一个红灯或抵达目的地。挑战在于排序：两列车无法安全共用同一区段，放行一列就意味着另一列必须等待。
4. **难度升级** —— 班次逐渐吃紧。更多列车到达，特快班次要求优先权，延误层层累积，被占用的区段迫使玩家创造性地改线。冲突警告或占用指示灯会在碰撞即将发生时提醒玩家。
5. **收尾结算** —— 班次以一个结算画面结束，报告准点率、避免或造成的事故，以及整体表现。玩家可以重试或返回标题画面，无需重启应用程序。

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