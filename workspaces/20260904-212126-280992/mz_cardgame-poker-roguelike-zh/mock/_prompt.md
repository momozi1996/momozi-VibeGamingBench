# 扑克 Roguelike（Cardgame Poker Roguelike）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`）：开发一个扑克 Roguelike 卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款建立在扑克牌型判定之上的 Roguelike 计分游戏。玩家被发到牌，必须组成牌型
（对子、顺子、同花）来得分，以达成不断攀升的底注目标。妙处在于：可收集的小丑牌
会以极其疯狂的方式改写计分规则——有的会让所有红桃的数值变成三倍，有的会让每一个
对子都算作葫芦。轮次之间，商店出售新的小丑牌、卡牌强化和消耗品。这份幻想在于：
发现荒诞离奇的计分组合，把区区一对 2 变成百万分的一手牌。达不到底注，这一轮就
结束了。

## 玩家体验流程

1. **标题画面** —— 赌场黑色电影风格，游戏名以烫金浮雕字体呈现在绿色台面呢上，
   背景中有洗牌动画，以及新的一轮 / 统计按钮。演出 GameX其灰色。
2. **手牌** —— 玩家从一副标准牌组中拿到 8 张牌。他们最多选出 5 张组成一个扑克
   牌型并提交计分。剩下的牌可以弃掉并重抽（每轮弃牌次数有限）。
3. **计分** —— 每种牌型都有基础筹码值和倍率（例如：对子 = 10 筹码 x2，同花 =
   35 筹码 x4）。小丑牌和强化会修改这些数值。分数会随着各个修正项依次生效而
   逐步累加显示，营造出戏剧性的张力。
4. **底注** —— 每一轮都有一个目标分数（底注）。小盲注、大盲注和 Boss 盲注依次
   攀升。玩家每轮有多手牌来达成目标。达不到底注，这一轮就结束。
5. **小丑牌** —— 最多 5 个小丑牌槽位。每张小丑牌都有独特的破坏规则效果，配有
   插画和说明文字。小丑牌可从商店购买，或从 Boss 盲注中获得。小丑牌之间的协同
   会造就指数级的计分潜力。
6. **商店** —— 轮次之间，把赚到的钱花在新的小丑牌、卡牌强化（箔面、全息、多彩
   ——各自带有计分加成）、券票（永久升级）或补充包（新的扑克牌）上。
7. **Boss 盲注** —— 带有减益条件的特殊底注（例如："所有梅花均为背面朝下"、
   "本轮不能弃牌"、"打出的第一手牌被减益"）。玩家必须针对该 Boss 条件调整策略。

## Vibe Gaming Quality Bar

本题的玩法、逻辑和验收锚点优先于下面的表达规范。不要重写或删减上面的核心
机制；这些要求用于把同一玩法稳定地落成一个可玩的 Vibe Gaming 垂直切片。

- **先玩后美化**：先保证开始、核心输入、状态变化、成功/失败和重玩闭环，再做视觉与动效。
- **技术栈按玩法选最小充分方案**：
  - 2D 规则游戏优先 `HTML5 Canvas 2D + Vanilla JS`；
  - 面板、卡牌、对话和菜单密集时可用 `DOM + CSS + Vanilla JS`；
  - 图标、线稿和几何动画可用 `纯 SVG + CSS 动画 + Vanilla JS`；
  - 连续碰撞、镜头、粒子或街机物理可用 `PhaserJS`；
  - 3D 或空间镜头可用 `Three.js + WebGL`；
  - 只有确实需要 GPU 大规模并行或自定义 GPU 管线时才用原生 `WebGPU`；
  - 可以混合 Canvas、DOM、CSS、SVG，但必须明确每层职责，禁止为了“技术炫技”增加无关复杂度。
- **规则层独立**：`game_logic.js` 保存唯一真相，暴露 `createGame(opts)` 和
  `advance(game, input, dt)`；渲染层只读取状态并呈现，不能偷偷维护第二套规则。
- **每帧可解释**：输入要映射到明确动作，动作要产生可观察状态变化；无效输入、
  边界条件、资源耗尽、受伤、胜利和失败都要有反馈。
- **Vibe 不是装饰**：至少使用两种反馈通道（动画、位移、缩放、粒子、声音、
  HUD 或镜头）表达关键动作；反馈不能遮挡目标或破坏可读性。
- **移动端优先**：关键点击目标至少 44×44 CSS px，支持触摸和鼠标，不能依赖 hover；
  390×844、360×800、430×932 和 1280×800 不得横向滚动或出现控件重叠。
- **确定性与测试**：随机内容使用 seed；至少验证核心规则、胜负条件、重开/恢复、
  输入边界和一个异常状态；不要用截图存在或文字出现冒充功能完成。
- **原创与合规**：使用原创名称、角色、图形、音效和关卡，或明确许可的素材；
  不复制任何原作商标、角色、文本、美术、音乐、关卡数据或代码。

完成后报告：实际文件路径、启动命令、测试命令与结果、关键截图、已知限制、
技术栈取舍和原创资产来源。

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