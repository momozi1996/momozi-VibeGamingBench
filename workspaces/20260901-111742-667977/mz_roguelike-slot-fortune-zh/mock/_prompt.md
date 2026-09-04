# 老虎机财富（Slot Fortune）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Slot Fortune**——一款符号相互作用、租金
不断攀升的老虎机 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

老虎机每回合转动一次，落定的符号会相互作用来产出金币。转动之间，玩家添加新符号、
移除不想要的，并搭建协同——猫会给相邻的牛奶符号加倍，矿石会喂给相邻的熔炉，
小偷会从邻居那里偷东西。麻烦在于：租金每隔几次转动就要交，而且无情地攀升。玩家
必须搭出一套符号引擎，既能产出足够的金币付租，又能投资于让未来收益复利增长的新
符号。付不出租金，这一轮就结束。这一轮走得越深，可选的符号就越稀有、越强力，
但租金也随之上涨。这是一款伪装成老虎机的构筑牌组类游戏。

## 玩家体验流程

标题画面展示一台风格化的老虎机和发光的符号。开始一轮后，呈现一个 3x5 的老虎机
网格和少量基础符号（金币、樱桃、宝石）。

每回合卷轴转动并落在随机位置上。符号自左至右生效：相邻的相同符号进行支付，特殊
符号则对其邻居触发效果。一个金币计数器统计本回合的收益。转动之后，商店提供三个
可加入卷轴池的新符号，以及一个付费移除一个现有符号的选项。

每 5 次转动就要交租——金额固定，且每个周期递增。若玩家付不出，这一轮结束，计分
画面展示存活的转动次数、金币峰值和最佳符号组合。符号分稀有度层级（普通、稀有、
传说），交互效果依次增强。策略在于精心策划符号池，打造出可靠的高额支付组合。

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