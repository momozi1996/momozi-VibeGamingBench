# 开放世界竞速（Open-World Racing）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**2D 开放世界竞速游戏**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶载具穿越一张包含多个生态区的大型开放世界地图，发现散布各处的赛道并
在上面竞速。每条赛道都有独特的布局、地形类型和待打破的计时赛记录。张力来自
动量管理——刹车太晚会冲出路面，在正确的时机漂移则会奖励一次速度提升，而每个
生态区都要求不同的驾驶风格。美术风格应当给人**快速、鲜艳、街机感**的观感——
可以想象成小体量的 *Burnout* 结合 *A Short Hike*。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的开场，包含游戏名称、一个开始按钮，以及一幅
   富有动感的竞速背景（速度线、汽车剪影、日落公路）。不要出现 HTML 引擎 的裸灰色。
2. **世界** —— 玩家出生在一张开放世界地图上，其中至少有三个视觉上截然不同的
   生态区：海岸公路、沙漠峡谷和山间隘口。载具可以朝任意方向自由行驶，随意探索。
3. **散布的赛道** —— 每个生态区至少包含一条赛道，由可见的起终点线和检查点门
   标示。赛道拥有与其地形相适应的不同布局：长直道、密集的连续弯，或者带落差的
   发夹弯。
4. **载具物理** —— 载具的加速、刹车和转向都带有可见的动量。绕弯漂移会产生一条
   刹车痕轨迹，并在松开时给予短暂的速度提升。载具精灵图在转向时会明显倾斜。
5. **计时与记录** —— 玩家越过起点线时圈速计时开始，到达终点线时停止。HUD 显示
   当前圈速、最佳圈速，以及一个奖牌等级（依据用时评定金/银/铜）。
6. **赛道解锁** —— 在一条赛道上取得铜牌或更好的成绩会解锁下一条赛道，并伴有
   可见的解锁动画。玩家通过赢取奖牌在世界中推进。
7. **速度反馈** —— HUD 上始终显示一个速度表。高速时，屏幕边缘会呈现细微的
   动态模糊或速度线效果。

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