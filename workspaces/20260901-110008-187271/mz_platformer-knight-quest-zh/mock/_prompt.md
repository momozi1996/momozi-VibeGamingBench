# 骑士征途（Knight Quest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Knight Quest**，一款带近战战斗与副武器的复古动作平台跳跃游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一名披甲骑士从一个宁静的村庄枢纽出发，前往八个主题关卡——闹鬼地穴、火山锻炉、冰封之巅、沉没神殿、天空堡垒、毒沼、机械钟楼与暗影王座——每个关卡都以一场 Boss 战收尾。骑士手持一把主近战武器，能打出令人满足的三段连击，并会收集消耗共享弹药资源的副武器（投掷斧、回旋十字、圣水、匕首）。关卡是线性的，但会把可选的宝箱藏在技巧挑战之后。关卡之间，村庄枢纽提供一家商店用于血量升级和副武器补货。整体调性是明亮、厚实的像素画怀旧感，配上现代化的灵敏操控。

## 玩家体验流程

标题画面显示游戏名、骑士的剪影，以及开始/继续选项。全新开局会把玩家放在村庄枢纽——一小片可滚动的区域，有一位商店 NPC 和一道显示八个传送门的选关之门（初始只解锁第一个）。

进入一个关卡便开始一段横向滚动的流程，其中有平台、陷坑和敌人。骑士以近战连击攻击，并可用副按键使用副武器。敌人掉落用于商店的宝石和偶尔出现的血量拾取物。每个关卡都以一场 Boss 战结束，Boss 有可见的血条和有预示动作的攻击套路。击败 Boss 会解锁下一个关卡并返回枢纽。

商店出售血量上限升级、副武器弹药包和一项伤害加成。进度在多次会话之间保存。通过全部八个关卡会触发一个带统计数据的胜利画面。

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