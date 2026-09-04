# 机甲出击（Mech Sortie）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Mech Sortie**，一款俯视视角的机甲射击游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一台重武装步行机甲穿越敌方领地，并在任务之间定制它的武器挂点
以应对前方的威胁。有趣的张力来自配装规划：机甲的挂点槽位有限（手臂、肩部、
背部），而每件武器都有重量、弹药和射程上的取舍。导弹巢在远距离上具有压制力，
却让机甲在近身时不堪一击；双联速射炮能撕碎近处目标但会过热。任务会从被摧毁的
敌人身上产出残骸物资，用于资助新武器与底盘升级，形成一个令人满足的循环——
部署、摧毁、回收残骸、定制、再部署。

## 玩家体验流程

玩家进入游戏时看到一个机库画面，展示他们的机甲及标注好的各个挂点。可用武器
列在军械库面板中；把一件武器拖到某个挂点即可装备，同时显示重量与能量约束。
从战役地图上选择一个任务后，机甲便被部署进一张俯视视角的战场。

机甲用 WASD 移动（比步兵更慢，且带惯性），躯干可通过鼠标瞄准独立旋转，并用
鼠标按键与数字键发射已装备的武器。任务带有目标：歼灭所有敌人、防守某一据点、
护送车队，或清除某个目标。敌人种类包括步兵、轻型载具、敌对机甲和炮塔工事。
摧毁敌人会掉落残骸箱，接触即可拾取。任务完成后会展示一份任务报告，含获得的
残骸物资、受到的伤害以及命中率数据。战役横跨 8 个以上任务，难度逐步升级，并
以一场最终 Boss 机甲遭遇战收尾。

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