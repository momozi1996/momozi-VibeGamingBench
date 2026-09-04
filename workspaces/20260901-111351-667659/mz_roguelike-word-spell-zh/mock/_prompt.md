# 咒文拼词（Word Spell）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Word Spell**——一款带字母图块和遭遇战的
拼词施法 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度
应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位巫师靠着用字母图块拼出的法术在地牢中一路厮杀。每回合玩家手中有一把字母图块，
必须拼出一个单词——单词越长伤害越高，而特定的字母组合会触发元素效果（含 "fire"
的单词造成燃烧伤害，"ice" 冰冻，"heal" 恢复生命）。遭遇战之间，玩家收集新的字母
图块、升级已有的（一个金色 "E" 计分翻倍），并从自己的池子里移除弱字母。敌人拥有
可见的生命值，并以倒计时预告攻击。张力在于压力之下的词汇量：在敌人出手之前，从
一手随机字母中找出最长、协同最强的单词。

## 玩家体验流程

标题画面展示排列成法术效果的字母图块。开始一轮时，玩家获得一个由 20 个常见字母
图块组成的初始池。

战斗中，从池里抽出 7 个图块。玩家把图块拖到拼写栏上组成单词，然后施放。有效单词
造成与长度成正比的伤害（3 个字母 = 弱，7 个字母 = 毁灭性）。特殊字母组合会触发以
元素图标显示的额外效果。无效单词会失效并浪费该回合。施放之后敌人发动攻击（伤害
以倒计时数字提前显示）。

遭遇战之间，奖励画面提供新图块（包括带额外效果的稀有辅音和元音）、图块升级或图块
移除。一张地图展示带战斗节点、休息节点（治疗）和商店节点（买卖图块）的分支路径。
这一轮在一位生命值极高、需要多个强力单词才能击败的 Boss 处终结。死亡时展示基于
抵达层数和施放过的最长单词计算的分数。

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