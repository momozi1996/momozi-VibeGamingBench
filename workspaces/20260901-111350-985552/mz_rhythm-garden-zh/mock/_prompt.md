# 节奏花园（Rhythm Garden）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个节奏花园游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一片充满奇趣的花园大地图串联起八个或更多的时机小游戏，每个都以一种不同的
园艺活动为主题——踩着节拍给花浇水、按节奏拍打虫子、指挥一支鸟儿合唱团、
用定时敲击把种子弹进花盆。每个小游戏教会玩家一种不同的节奏技巧（稳定脉动、
切分、复合节奏、一问一答）。逐一精通这些小游戏可解锁一个把所有机制编织在
一起的最终"混音"关卡，成为一场高潮式的演出。游戏的幻想核心是一位音乐园丁，
照料着一个会随着节奏造诣而绽放的世界。

## 玩家体验流程

1. **标题画面** —— 一幅粉彩色调的花园场景，游戏名采用活泼的手绘字体，花朵
   随着轻缓的节拍摇曳，还有一个做成洒水壶形状的"开始"按钮。不要出现 HTML 引擎
   默认的纯灰。
2. **花园枢纽** —— 一张大地图，展示一块块园圃，每块代表一个小游戏。已完成的
   游戏会开出花来；未解锁的则显示枯萎的花蕾。玩家点击某块园圃即可进入对应的
   小游戏。
3. **小游戏多样性** —— 至少 8 个截然不同的小游戏，各有独特的视觉表现和不同的
   时机机制：
   - 踩着节拍敲击（稳定的四分音符）
   - 长按与松开（持续时机）
   - 一问一答（复述一段模式）
   - 切分（脱拍击打）
   - 复合节奏（两段同时进行的模式）
   - 速度攀升（速度不断加快）
   - 模式记忆（重复越来越长的序列）
   - 自由发挥（在一段律动中即兴演奏）
4. **计分** —— 每个小游戏以星级（1-3 星）为准确度打分。游戏过程中的视觉反馈
   会体现时机质量：完美命中爆出粒子，失误则出现枯萎效果。
5. **进度推进** —— 赚取星星可解锁后续的小游戏。随着玩家推进，花园会明显地
   生长并绽放。每达成一个里程碑，就会出现新的花朵、蝴蝶和装饰。
6. **最终混音** —— 完成全部 8 个小游戏后，一个最终挑战会把多个游戏的机制
   组合成一场加长演出。这段混音每隔几个小节就在不同风格之间切换。
7. **结算与画廊** —— 一个画廊画面显示星星总数、各小游戏的最佳得分，以及作为
   奖励插画的完全绽放的花园。

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