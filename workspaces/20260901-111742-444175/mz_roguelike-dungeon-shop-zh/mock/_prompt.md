# 地牢商店（Dungeon Shop）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dungeon Shop**——一款你要给商品定价并
防范小偷的店主 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家经营一间地牢道具店，往货架上摆放武器、药水和护甲，供冒险者浏览购买。妙处
在于：价格由玩家自己设定，而定价就是核心机制。定得太高，冒险者会空手离开；定得
太低，利润就蒸发了。有些顾客是小偷，会抓起商品夺门而出——玩家必须亲自追上去把
他们扑倒，或者布置陷阱。营业日之间，玩家会深入一座程序化生成的地牢补充货源，
用手头任何没卖掉的库存去打怪。金币用于资助商店升级：展示柜、安保措施和更大的
营业面积。每一轮横跨多个营业日，直到商店要么兴旺到目标金币数，要么破产。

## 玩家体验流程

标题画面展示一间温馨的店内景象，一把剑陈列其中。开始一轮后，商店在第 1 天以
基础的初始库存开门。

在营业阶段，冒险者进店浏览。玩家把商品拖到货架上，并用一个滑块设定价格。冒险者
带有可见的预算指示和偏好。满意的顾客付钱离开；被要价过高的顾客会嗤之以鼻然后
走人。小偷会抓起商品就跑——玩家点击进行追捕，或者启动预先布置好的陷阱。

在地牢阶段，玩家进入一座程序化生成的横版卷轴地牢，进行简单战斗并收集战利品来
充实店里的库存。地牢中表现越好，库存就越好。营业日之间，升级画面提供商店改进
项。这一轮以胜利（达到金币目标）或破产（库存与金币双双耗尽）告终。结算画面展示
存活天数、总利润和抓住的小偷数。

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