# 策略：兽群冲突（Strategy: Beast Clash）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款**单路实时动物战争策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两个动物王国在一条争夺激烈的单路上碰撞。玩家指挥其中一方，花费食物派遣生物向敌方巢穴进军，对手也在做同样的事。每一次击杀都会喂养成长，成长解锁进化，而进化把涓涓细流般的小动物变成顶级掠食者的滔天巨浪。张力活在经济里：食物稀缺，生物要消耗真实资源，在错误的时机做出错误的花费就会把这条路让给敌人。基调活泼却凶悍——一片阳光普照的草原与丛林边境，战争从窜来窜去的小动物一路升级为高大到震屏的巨兽。

## 玩家体验流程

玩家从标题画面挑选一个王国——每一个都像一个真正的阵营，拥有自己的动物、身份认同与作战气质，因此这个选择是一次策略决定，而不是换个皮肤。

战斗在两座巢穴之间的横向卷轴路线上展开。食物随时间逐渐积累，玩家花费食物把生物从自家巢穴派出。每个生物都会自行向敌方进军，与遇到的一切交战，把前线来回推移。玩家从不直接操控某个生物；策略在于何时花费、派哪种生物、何时投资采集者以获取更多食物，以及何时攒资源用于进化。

生物有各自鲜明的定位——顶住前线的坚实阻挡者、从后方施加惩罚的远程打击者，以及维持经济运转的采集者。最强的军队靠的是配合：阻挡者承受伤害，远程巨兽安全输出，采集者则维持压制力。敌人也会派出自己的组合，并随时间变得更加危险，所以一成不变的方案必输。

随着一场场小规模交锋获胜，成长进度条会逐渐填满。达到阈值后，王国将进化到新的纪元，解锁更大更凶猛的生物，并让巢穴的外观明显升级。后期纪元的巨兽显然远胜开局纪元的小动物，而且是拓展战术，而不是简单地取代此前的一切。

在整场战斗中，玩家都能一眼读懂战况——食物、进化进度，以及双方巢穴的血量。摧毁敌方巢穴即胜利；自家巢穴陷落则失败。每种结局都落到一个精心设计的结算画面上，让结果一目了然，并让玩家无需重启应用程序就能再战一场。

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