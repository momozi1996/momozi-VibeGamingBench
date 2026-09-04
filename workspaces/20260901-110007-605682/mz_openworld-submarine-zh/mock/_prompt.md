# 开放世界潜艇（Open-World Submarine）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界潜艇（Open-World Submarine）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家驾驶一艘潜艇穿行于浩瀚的深海，用声呐在黑暗中导航，发现沉船残骸、水下洞穴
和奇异的生物。这里的幻想是深渊的刺激：下潜到光线消失、压力递增的极深处，找到
无人抵达过的宝藏。张力来自氧气管理、船体耐压极限，以及声呐上浮现的未知轮廓。
打捞到的宝藏可用于资助升级，让潜艇能下潜得更深。

## 玩家体验流程

1. **标题画面** —— 一个黑暗的海洋主题标题，游戏名称以发光的生物荧光字体呈现，
   气泡上升，并配有一个开始按钮。
2. **海洋** —— 玩家在一片大型 2D 海洋剖面中自由驾驶潜艇。深度向下递增，可见的
   压力分区通过颜色从浅蓝渐变为深海军蓝再到黑色来标示。
3. **声呐** —— 视野受限。玩家发出声呐脉冲，在一定半径内显现地形、残骸和生物。
   声呐脉冲以不断扩散的圆环形式可见。被动声呐把移动的接触目标显示为光点。
4. **探索** —— 沉船、水下洞穴和珊瑚群散布在海洋中。玩家与残骸对接以打捞货物，
   进入洞穴寻找稀有矿物，并拍摄生物以领取研究悬赏。
5. **氧气** —— 一条持续消耗的氧气量表迫使玩家定期上浮，或者在洞穴中寻找气室。
   氧气耗尽会导致昏迷并被强制上浮，同时损失货物。
6. **深度压力** —— 下潜超过潜艇的额定深度会造成船体压力。船体完整度量表随之
   下降；一旦归零，潜艇便会被压毁。升级可提高额定深度。
7. **升级** —— 打捞所得可用于购置更好的船体装甲板（下潜更深）、更大的氧气罐、
   更远的声呐范围、货舱扩容，以及一盏在不用声呐时也能保证视野的探照灯。

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