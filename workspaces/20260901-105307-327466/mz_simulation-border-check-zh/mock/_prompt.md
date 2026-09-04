# 边境查验（Border Check）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Border Check**，一款 2D 证件查验模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一个虚构的威权国家里当一名边境检查站查验员，对照一本不断变化的
规则手册审查旅客的证件，同时努力挣到足够的钱让家人活下去。有趣的张力在于道德
与机械规程的冲突：规则说要拒绝这个人，但对方的故事却令人同情——而每一个错误
决定都会花掉家里买取暖与药品所需的钱。速度很重要，因为每一天都有时间限制、
薪酬按处理人数计算，但赶进度又会造成失误，从而引来传票与罚款。规则每天都变得
更复杂——新的证件类型、新的违禁品检查、新的例外条款——直到玩家要同时处理
五份文件，而一列绝望的面孔正在排队等待。

## 玩家体验流程

玩家进入游戏时看到一个灰暗的标题画面，展示检查站岗亭，随后开始第 1 天。工作
区展示一张桌面，上有查验区、规则手册面板，以及"批准"和"拒绝"两枚印章。旅客
一次一个地走近，把证件递到桌上。玩家拖动这些文件，翻开规则手册核对当前规则，
对比照片与面孔，检查有效期，并交叉核对许可证编号。

每一天都会引入新规则：第 1 天可能只要求姓名匹配，而第 5 天则要求有效的工作
许可、疫苗接种记录以及体重差异核查。一天结束时会显示收入、家庭开支，以及收到
的任何传票。剧情事件会在日与日之间插入——一名守卫提出行贿、一名反抗者请求
帮助、家人病倒。选择会影响叙事走向。游戏横跨 10 天以上，复杂度逐步升级，并
依据累积的选择与财务上的存活情况提供多种结局条件。

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