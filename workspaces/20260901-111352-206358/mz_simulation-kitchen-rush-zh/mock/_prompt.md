# 厨房争分夺秒（Kitchen Rush）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Kitchen Rush**，一款 2D 限时压力烹饪模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在晚餐高峰时段经营一家餐厅厨房，在不同的烹饪工位之间同时应付多张
订单，而计时器在倒数、顾客越来越不耐烦。有趣的张力来自压力下的多任务处理：
每道菜谱都要求在特定工位、按特定顺序完成特定步骤，玩家必须在脑中同时追踪多道
菜。烧糊食物会浪费食材与时间；上错订单会损失口碑。班次之间，玩家会解锁新菜谱、
升级工位并扩建厨房布局，但更大的产能意味着更复杂的订单和更高的顾客期待。

## 玩家体验流程

玩家进入游戏时看到一个餐厅门面的标题画面，随后进入第一个班次。厨房视图展示
按空间排布的各个工位：切菜板、炉灶、油炸锅、烤箱、摆盘区和出餐窗口。订单出现
在顶部，带有菜谱要求与倒计时。玩家点击一个工位进行交互，从储藏室把食材拖到
工位上，并监控烹饪进度。

菜谱一开始很简单——切生菜、摆盘、上菜——但很快就会层层叠加：汉堡需要切配、
炙烤、把配料组装进面包，然后摆盘。多张订单会同时进行。过火会触发冒烟与浪费。
完成订单可按速度赚取金币与小费。班次之间会有一个商店画面，提供工位升级
（更快的炉灶、更大的油炸锅）、新菜谱解锁和厨房扩建。战役推进 10 个以上班次，
订单复杂度、顾客流量与菜谱多样性持续增加。班次总结会显示完成的订单数、失败
的订单数、赚到的小费和星级评价。

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