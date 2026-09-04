# 热线劫案（Hotline Heist）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Hotline Heist**，一款俯视视角的快节奏动作射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是踹门冲进满是武装守卫的房间，凭精准的瞄准和残酷的效率在几秒内清空
整个楼层。有趣的张力来自脆弱性：玩家和敌人都是一击致命，这让每一次进门都成为
一道致命谜题，犹豫就等于死亡。连击计分奖励速度——不停顿地连续击杀会提升分数
倍率，鼓励不顾一切的进攻，与一击即死的赌注形成平衡。散落在各楼层的多样武器
迫使玩家临场应变：霰弹枪能清掉一堆敌人但会惊动下一个房间，而消音手枪能保住
突袭优势却要求精度。

## 玩家体验流程

玩家看到一个风格化的标题画面，从战役列表中选择一个楼层，然后在建筑入口外生成。
镜头从上方展示完整的楼层平面图——房间、走廊、门以及敌人巡逻路线部分可见。玩家
用 WASD 移动，用鼠标瞄准，点击攻击。门可以被踹开以震晕门后的敌人。

每个楼层都是一道自成一体的谜题，由 4-8 个房间通过门与走廊相连。守卫沿固定路线
巡逻；有些站着不动，有些来回踱步。武器散落在地上——棒球棍、手枪、霰弹枪、
冲锋枪、飞刀——每种弹药有限或只能用一次。清空一个楼层上的所有敌人会触发计分
画面，显示用时、连击链与武器多样性奖励。死亡会立刻重开该楼层。战役提供 8 个
以上楼层，守卫密度逐步升级，并加入新的敌人类型（重甲兵、猎犬、枪手）以及更
逼仄的布局。

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