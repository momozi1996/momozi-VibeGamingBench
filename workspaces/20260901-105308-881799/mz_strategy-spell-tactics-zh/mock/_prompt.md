# 法术战术（Spell Tactics）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Spell Tactics**，一款**基于网格的法师对决战术游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两名法师在一个可破坏的格状竞技场上对峙，一边管理法力与站位，一边从手牌中施放法术。每个法术都有形状——直线、锥形、区域——并会与网格地形互动：火焰烧毁森林，冰霜冻结水域图块，闪电在金属之间连锁。张力是空间性的：完美的法术放在错误的位置就是浪费法力，而对手始终在移动，或为躲闪，或为铺设自己的连击。地形破坏会在战斗中途重塑竞技场，把一场对称的对决变成一道不对称的谜题。基调是奥术而戏剧化的——发光的符文、噼啪作响的能量，以及碎裂成粒子的图块。

## 玩家体验流程

玩家从标题画面在已解锁的卡牌中挑选一套法术牌组，然后进入一场对决。竞技场是一张带有多样地形图块的网格：石地、森林、水域、金属，以及空的深坑。两名法师从相对两侧出发，HP 与法力全满。

回合交替进行。每个回合玩家抽一张法术卡、获得法力，并可以把自己的法师移动最多两格，然后施放一个法术。法术消耗法力并影响网格区域：火球术命中 3x1 的一条直线，冰墙创造出阻挡地形，闪电则在金属图块之间连锁。命中对手造成伤害；命中地形则会将其转化或摧毁。

对手 AI 遵循同样的规则，会战术性地选择法术与位置。随着对决推进，地形破坏会开辟出新的视线，也会封闭掉旧的视线，迫使双方不断调整。

当一名法师的 HP 归零时，对决结束。一个精心设计的结算画面会展示胜者、造成的伤害、施放的法术数量，并提供再战一局或返回菜单的选项。赢下对决会解锁新的法术卡，供后续构筑牌组使用。

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