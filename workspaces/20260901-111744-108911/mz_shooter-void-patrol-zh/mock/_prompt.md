# 虚空巡航（Void Patrol）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Void Patrol**，一款横版卷轴清版射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一架孤身拦截机穿越敌意的深空走廊，在敌方火力的帷幕之间穿梭，
同时把强化道具串成不断升级的武器配装。有趣的张力在于贪婪与安全的抉择：每收集
一个强化道具都会延长当前的武器连锁，但那些光球会漂向危险位置，诱使玩家为了
下一个层级飞进弹幕形态之中。死亡会重置连锁，而生命有限，玩家必须决定何时求稳、
何时为那道毁灭性的满连锁光束而冒险推进。关卡无情地卷动，每一关都以一场多阶段
Boss 战收尾，其弹幕形态要求玩家精通飞船那狭小的判定框与可清屏的炸弹储备。

## 玩家体验流程

玩家进入一个标题画面，飞船的剪影映在卷动的星空之上，随后选择"开始"进入第 1 关。
视口自动向右卷动；敌人编队从边缘以精心编排的波次扫入，抛下弹幕，并不时释放
发光的强化道具光球。玩家可在屏幕边界内自由移动，按住一个按键发射主武器，并能
触发数量有限的炸弹来清除屏幕上的所有弹幕。

在不死亡的情况下连续收集强化道具会让武器沿可见的层级升级——单发、散射、
激光、追踪导弹——每一层都有独特的视觉表现。死亡会把连锁打回基础层级。关卡
之间会有一段简短的过场展示分数与剩余生命。Boss 遭遇战会用一个大型多部件敌人
填满屏幕右侧，随着血量下降，其各段会闪烁并断裂脱落，并在几个不同的攻击阶段
之间循环。五关之后游戏会显示胜利结算；失去所有生命会触发续关画面，续关次数
有限，用尽即为游戏结束。

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