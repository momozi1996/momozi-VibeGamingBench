# 攻城工程师（Siege Engineer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Siege Engineer**，一款**基于物理的攻城武器策略游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家搭建并瞄准攻城武器，利用真实的抛射物物理去拆毁城堡工事。每个关卡都会给出一座带有城墙、塔楼与守军的城堡，必须在有限的射击次数内把它化为废墟。玩家选择武器类型，调整角度与力度，然后开火——看着抛射物划过空中的弧线，砸进可破坏的地形。张力在于资源稀缺：弹药有限，每一发都必须算数，而城堡的几何结构本身构成了谜题：该打哪里才能造成最大的结构性崩塌。基调是中世纪工程学：木铁机械、石粉飞扬，以及砖石垮塌时那令人满足的碎裂声。

## 玩家体验流程

玩家从标题画面进入一张由防御日益坚固的城堡组成的战役地图。每个关卡在右侧显示目标城堡，左侧显示玩家的攻城阵位，二者之间是地形。

玩家从可用的武器类型中选择：投石机用于高抛越墙，弩炮用于平直直射，抛石机用于中程轰击。每种武器的抛射物重量、速度与爆炸半径各不相同。玩家通过拖拽界面调整角度与力度来瞄准，并能看到一条弹道预览线。

开火后抛射物按物理规律飞行。命中时，城堡砖块会受到伤害，并可能开裂、崩落或整体倒塌，具体取决于结构支撑——移除一段承重墙会让它上方的一切都塌下来。玩家每关的射击次数有限，必须摧毁足够多的城堡部分以达到破坏阈值。

后期关卡会加入改变抛射物路径的风、抵抗特定武器类型的装甲墙，以及在两次射击之间修补损伤的守军。战役从简单的城墙一路升级到复杂的多塔要塞。

一个精心设计的结算画面会展示破坏百分比、已用射击次数与获得的星数。要拿到三星，必须以最少的射击次数完成高效拆除。

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