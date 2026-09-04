# 漂移赛道竞速（Racing Drift Circuit）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个漂移赛道竞速游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款精准操作向的计时赛竞速游戏，掌握漂移就是一切。玩家驾车穿越狭窄的赛道，
在弯道处发起可控的漂移以维持速度。每条赛道都是一道关于走线的谜题——刹车太早
就会白丢几秒；漂移幅度太大就会擦到护栏。你最佳一轮的幽灵车回放会萦绕在每一次
尝试中，逼着你去抠掉那几毫秒。横跨 10 条以上赛道的奖牌系统（金/银/铜）提供了
清晰的进程目标，而在复杂的连续弯道中串出一条完美的漂移链所带来的满足感，
就是核心奖励。

## 玩家体验流程

1. **标题画面** —— 一个动态菜单，游戏名称采用速度感十足的斜体字体，背景是一条
   虚化的赛道，一辆幽灵车正漂移而过，另有"生涯"和"计时赛"按钮。不要出现 HTML 引擎 的
   裸灰色。
2. **赛道选择** —— 一个包含 10 条以上赛道的网格，配有预览缩略图、奖牌状态
   （无/铜/银/金）以及显示出来的最佳成绩。赛道按顺序解锁，需在前一条赛道上
   至少拿到铜牌。
3. **驾驶手感** —— 俯视视角或斜俯视角。车辆平顺地加速，刹车时有可见的减速，
   转向时带有动量。转弯时按住漂移键即可发起漂移：车身横向滑出，身后拖出轮胎
   烟雾粒子。
4. **漂移加速** —— 维持漂移会积攒一条加速槽。在恰当的时机结束漂移会获得一次
   速度爆发，并伴有可见的火焰/尾迹特效。漂移时间越长，加速越强，但也越有可能
   撞墙。
5. **幽灵车回放** —— 玩家最佳单圈的半透明幽灵车会实时地与其并驾齐驱。幽灵车
   清晰可辨（颜色不同、略微透明），能准确显示出时间是在哪里赚到或亏掉的。
6. **奖牌系统** —— 每条赛道都有金/银/铜的时间门槛，在比赛开始前展示。完赛后
   会颁发相应奖牌，并播放一段颁奖台动画。奖牌会记录在赛道选择画面上。
7. **赛道多样性** —— 赛道从简单的椭圆形，到带有发夹弯、连续弯道、高低落差
   （仅视觉效果）和宽窄变化的复杂赛道，各不相同。每条赛道都有独特的视觉主题
   （城市、沙漠、森林、夜晚）。

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