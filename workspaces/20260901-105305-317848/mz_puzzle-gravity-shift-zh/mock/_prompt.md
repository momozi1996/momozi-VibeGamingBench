# 重力翻转（Gravity Shift）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Gravity Shift**，一个 2D 重力旋转解谜
游戏。玩家旋转重力方向，引导一颗球穿过布满障碍的试验室抵达出口，并利用可破坏
地形与连锁反应清出通路。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款建立在方向性重力之上的物理解谜游戏。玩家无法直接移动小球，但可以按
90 度为单位旋转重力（下、左、上、右），让试验室里的一切都朝新方向坠落。张力
来自对重力序列的规划：向右旋转会让球滑撞到墙上，但同时也会把一块巨石砸到可破坏
的平台上，为下一次旋转打开通路。连锁反应会自然涌现——爆炸箱子受撞即引爆，
易碎方块落地一次后碎裂，有重量的物体在落定时会踩下压力开关。最理想的版本会让人
感觉像在编排一台鲁布·戈德堡机械，而重力本身是唯一的工具。

## 玩家体验流程

标题画面用漂浮的几何体和方向箭头营造氛围。玩家进入试验室后，能看到小球、出口
传送门、墙壁、平台、危险物和特殊物件。重力方向指示器显示当前的牵引方向。玩家
按方向键或按钮来旋转重力。

前期试验室教基础旋转：把重力转向右侧，让球滚向出口。很快，障碍就会要求多步序列
——先向下旋转穿过一道缝隙，再向左滑过尖刺。中期引入可破坏地形（第二次受撞才
碎裂的易碎方块、能炸开附近墙壁的爆炸箱子）、可触发开关的有重量物体，以及在坠落
过程中附加横向位移的传送带表面。后期试验室要求精确的旋转序列，每一次重力翻转
都会触发一场重塑关卡地形的连锁反应。

撤销系统让玩家可以回退重力翻转操作。抵达出口传送门即完成该试验室，并弹出庆祝
画面。被危险物害死后可以立即重试。战役按主题世界推进，物理复杂度层层升级。

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