# 放置地牢公会（Idle Dungeon Guild）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置地牢公会**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一家冒险者公会，派遣英雄去执行自动化的地牢任务，从中获取战利品和
经验。游戏的幻想核心是当一名公会会长：招募英雄、用捡来的装备武装他们，
看着他们从新手成长为传奇。放置循环会持续把队伍送进地牢；玩家的决策则塑造
队伍配置、装备分配和公会升级。转生会让当前这一代英雄退役，并以继承下来的
公会声望加成开启新的一代。

## 玩家体验流程

1. **标题画面** —— 一个公会大厅内景，配有任务板和英雄剪影，游戏名采用奇幻
   衬线字体，开始按钮做成蜡封信件的样式。
2. **公会大厅** —— 主视图展示公会大厅，包含英雄名册、任务板、装备架和一个
   声望量表。英雄不在执行任务时会在大厅里闲逛。
3. **英雄招募** —— 玩家从一个候选池中招募英雄。每位英雄都有职业（战士、法师、
   盗贼、治疗者）、属性和等级。不同职业的英雄有各自独特的精灵图。
4. **任务派遣** —— 任务板列出可选地牢及其难度、时长和奖励预览。玩家指定一支
   队伍（1-4 名英雄）并派出。一条进度条会显示任务随时间推进的完成度。
5. **自动战斗结果** —— 任务完成时，结算画面会显示获得的战利品、取得的经验，
   以及任何伤情。英雄会自动升级。更好的地牢会产出更稀有的战利品。
6. **装备与战利品** —— 找到的装备（武器、护甲、饰品）可以从装备架分配给英雄。
   更好的装备能提升属性并让英雄挑战更难的地牢。一个对比提示框会显示属性变化。
7. **转生（新一代）** —— 当公会声望达到上限时，玩家可以转生：让所有英雄退役，
   保留装备和公会升级，并以升级更快的新一代重新开始。每一代都能触及更高的
   地牢层级。

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