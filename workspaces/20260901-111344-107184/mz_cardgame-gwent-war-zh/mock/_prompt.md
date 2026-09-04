# 昆特战争（Cardgame Gwent War）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个昆特战争卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款以排为基础的卡牌对战游戏，其中虚张声势与卡牌强度同等重要。双方各自把单位牌
打进三个战斗排之一（近战、远程、攻城），回合结束时总战力更高的一方胜出。但对局
采用三局两胜——过早地倾尽手牌赢下一轮，会让你在下一轮无牌可打。核心张力在于
判断何时该推进、何时该过牌，诱使对手过度投入。多个拥有独特能力的阵营牌组，以及
一条难度层层升级的 AI 对手战役，共同带来深度。这份幻想在于：以微弱优势过牌时那
一刻的扑克脸，赌对手会为追平而白白挥霍手牌。

## 玩家体验流程

1. **标题画面** —— 中世纪战争沙盘美学，游戏名以铁铸字体呈现，两侧列着阵营旗帜，
   并有战役 / 快速对战 / 牌组编辑器按钮。演出 GameX其灰色。
2. **牌组编辑器** —— 至少 3 个阵营（北方王国、怪物、精灵），每个阵营各有 15 张
   以上独特卡牌。玩家从所选阵营加上中立卡中构建一副恰好 25 张的牌组。每张卡牌
   展示卡面美术、战力数值、所属排位，以及任何特殊能力。
3. **棋盘** —— 每一方三排（近战/远程/攻城），横向排布。卡牌从手牌打进各自指定的
   排。每排战力和总战力都会显示。对手的各排在上方镜像呈现。
4. **回合结构** —— 双方轮流打出一张卡或过牌。一旦双方都过牌，该轮结束。总战力
   更高的一方赢下该轮。三局两胜赢下整场对局。一个轮次追踪器显示当前战况。
5. **虚张声势与过牌** —— 玩家可以随时过牌，锁定自己当前的战力。对手随后必须决定
   是继续打牌（为后续轮次白白消耗资源）还是同样过牌。这造就了丰富的心理博弈。
6. **特殊能力** —— 卡牌拥有各种能力：间谍（打在对手一侧，但抽 2 张牌）、军医
   （从弃牌堆复活一张卡）、天气（把某一排所有卡的战力降为 1）、指挥官号角
   （使某一排战力翻倍）、诱饵（把一张已打出的卡收回手牌）。每种能力都有独特的
   视觉效果。
7. **战役** —— 一系列难度递增、牌组策略各异的 AI 对手。赢下对局会为玩家的收藏
   赢得新卡牌。一张世界地图展示战役进度。

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