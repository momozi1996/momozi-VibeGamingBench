# 节奏节拍地牢（Rhythm Beat Dungeon）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个节奏节拍地牢游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一座基于网格的地牢中不断下探，而每一个动作——移动、攻击、闪避——都必须
踩在一条持续播放的节奏音轨的节拍上。脱拍就会踉跄；完美踩拍则让你的攻击造成
额外伤害。敌人会以节奏性的模式预告自己的攻击，玩家必须读懂并加以反制。游戏的
幻想核心是一名战士兼舞者，以音乐般的精准在危险中穿行、收集会改变自身战斗
风格的战利品，并面对攻击模式构成复杂复合节奏的 Boss。

## 玩家体验流程

1. **标题画面** —— 一个有设计感的菜单，游戏名随节拍脉动，配有一个开始按钮，
   以及一片火炬光闪烁的黑暗地牢背景。演出 GameX其灰色。
2. **节拍** —— 一个持续显示的节奏指示器（弹跳图标、脉动边框或节拍器条）标示
   当前节拍。玩家要踩着这个脉动按下移动键或攻击键。完美的时机会闪出金色；
   偏早/偏晚则显示另一种颜色。
3. **网格移动** —— 地牢是基于图块的网格。每一拍玩家可以朝任一正方向移动一格，
   或者原地攻击。脱拍移动会触发踉跄动画并浪费该回合。
4. **敌人** —— 多种敌人类型，各有独特的节奏模式：每 2 拍攻击一次的骷髅、
   在脱拍时移动的史莱姆、每 4 拍传送一次的幽魂。每种敌人都会有视觉上的
   起手预告。
5. **战斗** —— 踩拍攻击造成全额伤害，并伴有令人满足的命中闪光。脱拍攻击造成
   的伤害会降低。敌人会掉落金币，偶尔也掉落装备（改变攻击范围或攻击模式的
   武器）。
6. **战利品与养成** —— 在楼层之间，商店允许玩家用金币购买生命药水、新武器
   （长枪可打到 2 格、匕首每拍攻击两次）或护甲。装备会在视觉上改变玩家精灵图。
7. **Boss 战** —— 每个地牢区段的结尾都有一个 Boss，其攻击构成一套复杂的多拍
   模式。Boss 会以一段独特的视觉序列进行预告，玩家必须记住它并跟着节奏闪避。

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