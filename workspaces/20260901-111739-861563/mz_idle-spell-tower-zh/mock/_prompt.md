# 放置法术塔（Idle Spell Tower）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置法术塔**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家建造一座能被动产生魔力的巫师塔，研究法术，并把施法自动化以获得不断增长的
力量。游戏的幻想核心是奥术积累：看着魔力从一颗水晶流向另一颗、法术自动朝
目标发射，而塔身随着每一轮转生周期越建越高。放置循环持续产生魔力；玩家的
决策则决定研究哪些法术，以及如何在攻击、防御和成长之间分配魔力。转生会让塔
崩塌，并以更好的地基把它重建得更高。

## 玩家体验流程

1. **标题画面** —— 一座高耸的巫师塔矗立在星空下，魔法粒子向上流动，游戏名
   采用奥术手写体，还有一个泛着魔力光芒的开始按钮。
2. **塔视图** —— 一个垂直的塔身剖面图，展示各个楼层。每层都有一项功能：魔力
   生产者、法术实验室、水晶仓库、自动施法器。随着楼层增加，塔会不断长高。
3. **魔力生产** —— 基础魔力会自动跳动增长。每层的魔力生产者都会提升该速率。
   玩家可以点击一颗水晶手动产生一波爆发。一个巨大的魔力计数器占据 UI 的主位。
4. **法术研究** —— 一棵研究树展示可选法术。每个法术都需要花费魔力和时间来
   研究。研究完成的法术可以分配给自动施法器，也可以手动施放以立即生效。
5. **自动施法** —— 自动施法器楼层会在无需玩家输入的情况下，朝目标（逼近塔基的
   怪物）发射法术。每个施法器都有自己的施法速率和法术分配。击败怪物会产出
   魔力水晶。
6. **塔的成长** —— 花费魔力可建造新楼层，每层都有特定功能。更高的楼层能产生
   更多魔力，但成本呈指数上升。塔会在视觉上变得更高。
7. **转生** —— 当塔达到最大高度时，玩家可以让它崩塌（转生）。塔会重置为一层，
   但获得一个永久的高度倍率、更快的魔力生产速度，以及更高层级法术的使用权限。
   每次重建都能更快地达到更高的高度。

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