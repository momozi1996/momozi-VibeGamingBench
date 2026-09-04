# 经营：乡村农场（Tycoon: Village Farm）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个 **2D 乡村农场经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家继承了一小块土地，通过日复一日的例行劳作把它变成一座充满生机的农场。这里的幻想是惬意的累积感——每天清晨醒来照料一夜之间长大的作物，卖掉收成换来刚够种下新东西的金币，看着自家庄园慢慢填满色彩与生命。有趣的张力在于每一天都是有限的：体力总在雄心之前耗尽，所以玩家必须选择当下哪些活儿最重要。压力温和但真实——不浇水作物就停滞，透支了明天就得饿着肚子开始。风险从不是灾难性的，只是虚度一天的那份静默代价。经过许多个清晨，农场从裸土变成生机盎然的拼布图景，而这份满足感完完全全是一块图块一块图块挣来的。

## 玩家体验流程

玩家打开已存档的农场或从头开始，看到自己的庄园——一块围起来的可耕土地、一间农舍、一家商店，还有边缘处闪着微光的水面。最初的清晨很简单：耕几格地、撒下种子、浇上水，然后回屋睡觉。每个动作都会在土地上留下可见的痕迹，也消耗掉一天精力中的一小片。

随着金币累积，玩家开始多元化经营——生长期更长但回报更高的新种子类型、带来副业收入的钓鱼点，也许还有一片扩建的田地。每日循环保持不变，但其中的决策变得更有深度：优先种哪些作物，什么时候该收割、什么时候该给下一批浇水，最后一点体力是拿去钓鱼还是留给明天播种。

作物只在夜间生长，所以睡觉就是赋予每一天意义的标点。清晨的揭晓时刻——看到幼苗推进一个阶段、成熟的植株已可采摘——正是把玩家拉进"再来一天"的钩子。进度在就寝时存档，因此回来的玩家醒来面对的是同一座农场、同一段生长季节、同样静静向前的势头。

美术方向是温暖、洒满阳光的卡通田园风——绿色、赭色、柔和的木质——绝不出现裸露的 HTML 引擎 灰。整体基调温和从容，与手速游戏截然相反。

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