# 火箭摩托越野赛（Racing Rocket Trials）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个火箭摩托越野赛游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款基于物理的摩托车障碍赛游戏，精准的油门控制与身体重心倾斜就是一切。车手要在
20 个以上手工设计的关卡中，穿越越来越荒诞的坡道、回环、跷跷板和爆炸油桶。摔车
场面十分壮观——车手在撞击瞬间变为布娃娃，在赛道上翻滚，呈现出一幕黑色幽默。
挑战是外科手术级别的：轻踩油门爬上一面近乎垂直的墙、向后倾身跨过一道缺口，
或是从摆动的危险物之间穿针引线。检查点很宽容，但计时器毫不留情——奖牌奖励的是
速度和零失误的一轮。

## 玩家体验流程

1. **标题画面** —— 一片粗粝的工业背景，游戏名称采用镂空模板风格的粗体字体，
   一辆摩托车剪影正在翘前轮，另有"开始"/"关卡选择"按钮。不要出现 HTML 引擎 的
   裸灰色。
2. **关卡选择** —— 一个包含 20 个以上关卡的网格，按 4 个难度档位组织
   （简单/中等/困难/极限）。每关都显示奖牌状态、最佳成绩和一张小预览图。
   关卡在各档位内按顺序解锁。
3. **摩托车物理** —— 摩托车具有真实的 2D 物理：两个带悬挂的车轮，以及一个会
   倾斜的车手身体。油门（右方向键）驱动后轮加速；刹车（左方向键）使其减速。
   上/下方向键让车手前倾/后倾，从而移动重心。
4. **障碍多样性** —— 关卡中会出现坡道、回环、跷跷板、摆动的钟摆、爆炸油桶、
   崩塌平台、移动平台和陡坡。每种障碍类型都有独特的视觉设计和物理交互。
5. **布娃娃摔车** —— 当车手的身体以不良角度撞上障碍物或地面时，他会变成布娃娃
   飞离摩托车。摔车过程通过物理驱动的肢体运动演出。一个"失误"计数器会加一，
   玩家在上一个检查点重生。
6. **检查点** —— 布置在每个关卡各处的旗帜或标记。抵达其中一个即保存进度。
   计时器持续运行。失误越少、用时越短，就能获得越好的奖牌。
7. **奖牌与星级系统** —— 每关根据完成时间颁发金/银/铜奖牌。零失误完成则额外
   获得一颗"完美"星。奖牌与星星的总数会解锁后续的难度档位。

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