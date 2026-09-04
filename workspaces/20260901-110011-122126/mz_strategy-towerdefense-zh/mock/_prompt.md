# 策略：塔防（Strategy: Tower-Defense）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款 **2D 塔防游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名前线指挥官，盯着一张布满咽喉要地与开阔地带的地图，看着敌潮沿固定通道涌向一个脆弱的终点。手上唯一的工具是少量可部署的防御者和一只不断走动的资源时钟。核心幻想是**在不断升级的压力下解空间谜题**——每一次图块摆放都是一次承诺，每一波敌人都在抬高赌注，而有意思的张力在于：现在花在稳妥选择上的资源，本可以攒下来作为日后绝境中的答案。压力来自解读下一波的构成、决定把稀缺的部署点数（DP）投到哪里，以及判断是要加固正在崩溃的一路，还是赌一个高价单位来翻转整张地图。风险始终存在：一次误读的波次或一次贪心的存钱，就会让防线过薄，敌人在下一次 DP 跳动到来之前就冲了进来。

## 玩家体验流程

1. **标题与战役入口** —— 一个冷峻的工业风标题画面定下基调。玩家从头开始或读取存档，然后进入一张关卡选择地图，其上显示可选任务，每个任务都暗示着前方的敌人构成与难度。

2. **部署阶段** —— 进入关卡后，玩家看到一张格状战场，其中路径、可部署图块与基地终点都有清晰标记。DP 随时间向上跳动。玩家把单位卡从手牌拖到合法图块上；每一次摆放都消耗 DP，并把一名防御者固定到该位置。无效位置或资金不足会被干净地拒绝。

3. **敌袭来临** —— 敌人沿固定路径以离散波次涌来。每一波都比上一波更强或更古怪——更快的斥候、带甲的猛兽、绕过阻挡者的飞行威胁。防御者在射程内自动攻击，阻挡者顶住防线，而玩家看着双方的血条不断下降。死亡会把单位从战场上移除；漏怪则一点点削减基地的生命总量。

4. **升级与应变** —— 后期波次要求的答案，开局阵容单靠自己给不出来。玩家权衡升级、重新调整优先级，并在互相竞争的需求之间摊开有限的 DP。地图变成一道由重叠射程与移动压力点组成的活谜题。

5. **收尾结算** —— 最后一波撞碎在防线上，胜利宣告；或者基地生命归零，失败被确认。通关一个关卡会记录进度并解锁下一关。玩家可以重试、返回关卡选择，或退回标题画面，无需重新启动。

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