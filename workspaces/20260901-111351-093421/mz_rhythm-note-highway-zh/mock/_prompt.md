# 节奏音符轨道（Rhythm Note Highway）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个节奏音符轨道游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

音符沿着一条多轨道的音符轨道倾泻而下，奔向屏幕底部的判定线。玩家必须在每个
音符越过判定线的一瞬间，精准按下对应轨道的按键。准确度会积累出连击倍率来
放大得分；失误则会中断连击，并消耗一条生命条。游戏的幻想核心是举办一场
演唱会——在流畅的心流状态中打准每一个音符，同时背景舞台灯光会随你的准确度
作出反应。一整套程序化定时的歌曲战役提供了数小时不断升级的挑战。

## 玩家体验流程

1. **标题画面** —— 一片霓虹灯照亮的舞台背景，游戏名采用粗体风格化字体，配有
   一个战役按钮和一个自由演奏按钮。不要出现纯灰。
2. **选曲** —— 一份可滚动的列表，至少 10 首歌曲，标有难度评级（简单/中等/
   困难）、最佳得分和通关评级（S/A/B/C/F）。歌曲会随战役进程依次解锁。
3. **轨道** —— 4 条轨道，颜色编码的音符宝石朝判定条落下。玩家按 D/F/J/K
   （或方向键）来击中音符。判定窗口分为 Perfect、Great、Good、Miss——各有
   截然不同的视觉反馈（爆裂、发光、震动）。
4. **连击系统** —— 连续命中会让连击计数器递增。倍率（x2、x4、x8）会放大得分。
   中断连击会重置计数器，并伴有可见的碎裂特效。
5. **生命条** —— 失误会消耗生命值。生命值归零时歌曲失败，出现显示统计数据的
   游戏结束画面。Perfect 判定会回复少量生命值。
6. **长按音符与滑动音符** —— 有些音符需要按住按键持续其时长（带有一条拖尾）。
   还有些音符会横跨轨道滑动，要求玩家用手指位置跟随。
7. **结算画面** —— 每首歌结束后显示：总得分、最大连击、准确率百分比、评级，
   以及 Perfect/Great/Good/Miss 各判定数量的明细。刷新最高分会触发一段庆祝
   动画。

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