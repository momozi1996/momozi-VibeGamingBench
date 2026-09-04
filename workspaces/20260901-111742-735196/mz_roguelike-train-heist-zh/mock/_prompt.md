# 列车劫案（Train Heist）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Train Heist**——一款逐节车厢展开遭遇的
程序化列车车厢 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名匪徒登上一列程序化生成的列车的尾车，必须一节一节向前打，在列车到站之前抵达
车头。每节车厢都是一场自成一体的遭遇：载着可供抢劫的平民的客车厢、有武装守卫的
警卫车厢、有待撬保险柜的货运车厢、以掩体为核心展开枪战的餐车，或者有定时锁金库的
邮政车厢。匪徒携带的弹药和生命值都有限，一路向前推进就是在消耗这两样。前面车厢
的战利品，可以在列车中段出现的黑市车厢里用于采购。一个回合计数器代表到站的距离
——若它在抵达车头之前归零，这次劫案就失败了。每一轮都会生成一列车厢序列和长度
各不相同的新列车。

## 玩家体验流程

标题画面展示夕阳映衬下的蒸汽列车剪影。开始一轮后，展示整列列车的侧视图，车厢
类型部分可见（有些隐藏）。

玩家进入尾车，遭遇第一节车厢的挑战。战斗是回合制并带有掩体机制——匪徒和敌人各自
在家具后面占据位置并交火。弹药有限，必须从倒下的守卫身上搜刮。客车厢提供抢劫
选择：恫吓以快速拿钱，或者仔细搜查以获得更好的战利品，但要承担惊动前方守卫的风险。

一条进度条显示在列车上的位置和剩余回合数。黑市车厢提供医疗包、弹药、特殊武器和
伪装。抵达车头会触发一场对抗列车长的 Boss 战。胜利展示总战利品、清空的车厢数和
剩余回合数。失败（生命值归零或时间耗尽）则展示匪徒在这列车上走到了多远。

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