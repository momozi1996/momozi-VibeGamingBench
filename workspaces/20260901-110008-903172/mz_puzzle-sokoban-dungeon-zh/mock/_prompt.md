# 推箱子地牢（Sokoban Dungeon）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Sokoban Dungeon**，一个 2D 回合制推箱子
地牢解谜游戏。玩家在程序化生成的地牢房间中推动箱子，而敌人在每个回合同时行动，
玩家需要收集钥匙和道具来解锁更深的楼层。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款回合制解谜与 Roguelike 的混合作品，玩家每走一步都会触发敌人走一步。
每个地牢房间都是一道空间谜题：箱子必须被推到压力板上才能打开门，但敌人会在网格
上巡逻，并在玩家一移动就朝玩家逼近。张力来自同步回合系统——推一次箱子要花一个
回合，而这期间敌人正在合围，所以玩家必须在不断加剧的威胁下解开空间谜题。钥匙
解锁新房间，道具提供一次性能力（冻结敌人、拉动箱子、传送），程序化的房间布局
保证了变化性。最理想的版本会让人感觉像是把国际象棋和仓库搬运谜题融合在一起，
每一步都有战术上的后果。

## 玩家体验流程

标题画面用石质纹理营造出地牢氛围，并给出清晰的开始入口。玩家进入地牢房间后，
能在网格上看到墙壁、箱子、压力板、锁住的门、钥匙、敌人和出口楼梯。移动是回合制
的：方向键移动一格，同时所有敌人也移动一格。

前期房间教基础的推动：把一个箱子推到压力板上以打开一道门。很快就会出现在移动
时机上与玩家镜像同步的敌人，迫使玩家规划出既能推箱子又能躲开或困住威胁的动作
序列。中期引入多种箱子类型（重箱子需要推两次，冰箱子会一直滑到撞墙为止）、
解锁颜色对应门的钥匙，以及从宝箱里找到的道具。后期房间在程序化编排的布局中把
所有机制结合起来，玩家必须一边解空间谜题，一边管理敌人的位置。

撤销系统让玩家可以回退回合。抵达出口楼梯即前往下一层。被敌人碰到而死亡后可以
重试。战役会生成越来越复杂的楼层，敌人更多、箱子类型更多、空间约束更紧。

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

交互方案（pointer-first）：本题材以鼠标/指针交互为主：支持点击、悬停、拖拽或框选；只有自然需要时再加入键盘快捷键。
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