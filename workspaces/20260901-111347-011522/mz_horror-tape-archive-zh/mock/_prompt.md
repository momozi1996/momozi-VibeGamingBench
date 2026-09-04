# 恐怖录像档案（Horror Tape Archive）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖录像档案**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家要审查一处设施的监控录像带，来回拖动画面以找出异常并标记时间码。游戏的
幻想核心是取证式的恐惧：明知有什么地方不对劲，却只能盯着平淡无奇的画面，
去抓住某个影子自行移动、或某个身影出现在本不该有人之处的那一瞬。紧张感来自
一条理智值量表——每目睹一次异常它就下降，也来自一个逐渐浮现的认知：录像带
也在反过来看着你。每一次正确标记时间码都会推进调查，但要以精神稳定为代价。

## 玩家体验流程

1. **标题画面** —— 一个 VHS 风格的标题，带有走带扫描线，游戏名采用等宽字体，
   开始按钮做成录像机控制键的样式。
2. **档案室** —— 一张桌子，上面有一台 CRT 显示器、一个录像带架、一块记笔记的
   写字板，以及一个理智值量表。房间只由一盏台灯昏暗地照亮。
3. **录像带选择** —— 玩家从架子上多卷贴有标签的录像带中挑选。每卷带子对应
   一个不同的摄像机位置：走廊、实验室、储藏室、庭院。不同带子的时长和异常
   数量各不相同。
4. **画面审查** —— 显示器播放带颗粒感的监控画面。玩家可以播放、暂停、倒带和
   快进。角落里有一个时间码计数器在走动。画面大多是正常活动，其中藏着细微的
   异常。
5. **异常侦测** —— 当玩家发现有什么不对（影子逆着光移动、某个物体消失、
   背景里出现一个身影）时，就暂停并以当前时间码点击"标记异常"。标记正确可
   获得调查点数；误标则损耗理智值。
6. **理智值量表** —— 观看异常会消耗理智值。低理智会引发视觉损坏：档案室扭曲、
   响起幻听声、画面中出现虚假的异常来欺骗玩家。理智值归零时，本次审查结束。
7. **调查进度** —— 被正确标记的异常会填满一块案情板，把跨录像带的事件串联
   起来。完成串联可解锁新的录像带，并揭开这处设施的秘密。最后一卷带子展示了
   上一任档案员的遭遇。

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