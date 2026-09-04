# 恐怖第 13 层（Horror Floor 13）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖第 13 层**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一栋被诅咒大楼里的电梯操作员，每一层楼都是一场自成一体的噩梦。游戏的
幻想核心是被困在职守之中：乘客提出楼层要求，玩家必须把他们送到——但每去过
一层，现实就会被进一步扭曲。紧张感来自互相冲突的乘客要求（有些楼层很危险，
有些乘客并非表面所见），以及电梯本身——随着诅咒加深，它会不断故障。这栋楼
有十三层，而第 13 层永远不该被造访。

## 玩家体验流程

1. **标题画面** —— 一块阴暗的装饰艺术风电梯面板，上面标着楼层数字，游戏名以
   黄铜字体呈现，开始按钮的样式则是关门按钮。
2. **电梯** —— 主视图是电梯内部：一块楼层选择面板、一个显示当前楼层的指示器、
   会开合的门，以及一扇可以看到井道的小窗。
3. **乘客** —— NPC 会走进来并提出楼层要求。每位乘客都有独特的外形和举止。
   有些是正常人；有些则令人不安（眼睛数量不对、精灵图闪烁、说话倒着来）。
   玩家必须选择是否照他们的要求执行。
4. **楼层造访** —— 当电梯门在某一层打开时，玩家会看到一段场景速写：无限延伸的
   酒店走廊、所有人都被冻住的办公室、没有地板的舞厅。每一层都是一个独特的
   恐怖场景，并附带一小段互动内容。
5. **故障** —— 电梯会越来越不听话：停到错误的楼层、灯光闪烁、按钮重新排列、
   指示器疯狂旋转。玩家必须随之应变并维持控制。
6. **乘客带来的后果** —— 把乘客送到错误楼层或拒绝他们的要求都有后果：大楼变得
   更加充满敌意，出现新的不可能存在的楼层，电梯也向第 13 层不断下降。
7. **第 13 层** —— 最后一层。抵达那里将触发高潮。玩家如何对待乘客决定了结局。
   游戏根据玩家做出的选择设有多个结局。

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