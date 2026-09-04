# Roguelike：遗物弹珠台（Roguelike: Relic Pinball）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Relic Pinball**——一款小巧的**弹珠台 /
打砖块 Roguelite**：一个原创、打磨精良的纵向切片，讲述在一座被诅咒的机械台面上
一间一间地推进，击破目标砖阵、触发奥术机构，并收集能在不断升级的一轮之中肉眼
可见地改变弹球行为的遗物。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片
放到 itch.io 页面或 Steam 上。

## 核心构想

玩家正在一间一间地探索一座被诅咒的机械台面。每一间都是一块活生生的弹珠台，
融合了打砖块的结构：目标行、弹垒、开关、通道、闸门、旋转器和特殊砖块共同构成
清晰可读的目标，而弹球始终保持高速与实体感。张力来自挡板时机与遗物协同——每一次
发球都是一场赌博，每一次救球都是一场小小的胜利，而每一次遗物选择都会重塑弹球与
世界互动的方式。弹球可能在接触时分裂、烧穿裂纹砖、朝金属目标弯曲、留下计分回声、
在穿过时给弹垒充能，或在被挡板击中后进入环绕轨道。整体调性是奥术街机机台：
黄铜导轨、玻璃反光、雕纹石砖、发光的遗物图标、明亮的撞击火花，以及干脆利落的
挡板反馈。

## 玩家体验流程

从标题画面开始，玩家看到一幅有设计感的弹珠台意象，其中至少有一件遗物或一种魔法
弹球的身份，暗示着接下来会发生什么。

这一轮把玩家投进一块活的台面。弹球被发射进一片有界的场地，玩家操作左右挡板让它
存活下去，把它穿过弹垒、通道和砖阵。每一次碰撞的感觉都不一样——弹垒把球弹开，
砖块开裂并碎散，开关点亮通道，旋转器为倍率充能，传送门把球扭送到台面另一处。
台面不是被动的背景板；它会回应。

清掉足够多的目标、或触发正确的机构，就会开启一次遗物选择。玩家从若干遗物中挑选
一件，每件都有名称、图标和一条简明规则。所选遗物会立刻改变下一间的玩法——弹球
会分裂、穿透、磁吸，或者拖出火焰尾迹。已激活的遗物栏会持续保留并叠加，因此这
一轮会朝着一套没有两次尝试会相同的奇特配置堆积。

各间越来越难：新的布局、更窄的漏球口、装甲目标、危险弹垒，最终是一块特殊规则
要求远超反应力的 Boss 台面。胜利或失败都落到一个有设计感的结算画面上，让玩家
无需重启应用程序即可再来一次。

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