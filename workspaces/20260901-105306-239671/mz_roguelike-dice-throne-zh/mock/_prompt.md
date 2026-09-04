# 骰子王座（Dice Throne）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dice Throne**——一款带重掷机制、并且装备
会改造骰面的骰子 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位战士以骰子作为战斗系统，在地牢中一路厮杀。每个回合玩家掷出一组骰子，然后
选择保留哪些、重掷哪些（最多两次重掷）。骰面对应能力：剑造成伤害，盾进行格挡，
心恢复生命，骷髅触发特殊攻击。妙处在于：地牢中找到的装备会实际改造骰面——一把
烈焰之剑会把一个剑面替换成造成双倍伤害的火剑面，附魔护甲会给一颗骰子加上一个
盾面。敌人同样掷出可见的骰子，形成一场双方都能看到即将发生什么的透明较量。
把骰面凑成一套互有协同的骰组，就是每一轮之内的元进展。

## 玩家体验流程

标题画面展示翻滚的骰子和发光的骰面图标。开始一轮时，玩家获得 5 颗标准骰子
（每颗的骰面为剑、剑、盾、心、骷髅、空白）。

战斗中，玩家一次掷出所有骰子，配有令人满足的翻滚动画。结果朝上落定。玩家选择
要保留的骰子（它们会锁定在原位），并重掷其余的——每回合最多两次重掷。定案之后，
骰面开始生效：剑对敌人造成伤害，盾减少受到的伤害，心恢复生命，骷髅触发一个特殊
能力。随后敌人掷出自己那批可见的骰子，并以同样方式结算。

遭遇战之间，战利品画面提供能改造骰面的装备——替换、升级或增加骰面。一张地图展示
带有战斗、精英、商店和休息节点的分支路径。商店出售骰面改造和新骰子。这一轮在
一位持有强力定制骰子的 Boss 处终结。死亡时展示抵达的层数、最佳一掷和收集到的装备。

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