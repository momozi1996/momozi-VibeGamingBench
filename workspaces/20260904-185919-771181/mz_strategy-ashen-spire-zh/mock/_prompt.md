# 策略：灰烬尖塔（Strategy: Ashen Spire）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Ashen Spire**，一款小而精的**黑暗奇幻 Roguelike 构筑牌组类卡牌战斗游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

核心幻想是仅凭一副单薄的牌组和沿途搜刮到的东西，一层一层地攀爬一座受诅咒的高塔。每场战斗都是一道小型战术谜题：能量稀缺，敌人会预告自己的下一步行动，而每张打出的牌都会重塑这一轮余下部分的胜算。有意思的张力在于：牌组既是你的武器，也是你的负累——加入强力卡牌会稀释稳定性，而保持精简则意味着面对不断升级的威胁时手段太少。压力来自解读敌人意图、在进攻与防守之间分配能量，以及赌哪张奖励卡牌会在三场战斗之后开花结果。风险始终存在：一次贪心的选牌，或一次误读的意图，就可能让你手里没有格挡、离死亡只差一击。

## 玩家体验流程

玩家进入一个黑暗而富有氛围感的标题画面，为这场阴森的登塔之旅定下基调。开始一轮后，会展现一张分叉的路线图——节点织成的网络向上延伸，通向最终对决，其间的分岔迫使玩家选择要面对哪些危险、要避开哪些危险。

进入战斗节点后，玩家被投入一场回合制卡牌对决。抽出一手少量卡牌，能量回满，敌人则显示它下一回合打算做什么。玩家消耗能量打牌——削减敌人血量的打击牌、抬起护盾的防御牌，以及各种更奇特的战术效果：中毒、燃烧、额外抽牌，或是扭曲规则。当手牌用尽或玩家觉得满意时，结束回合让敌人行动，随后抽出新的一手牌，循环继续。

赢下一场战斗后，会提供若干新卡牌供玩家编入牌组，每张都有自己的特性与费用。地图随之更新，玩家挑选下一个节点，牌组则随着每一层变得更丰富也更危险。不同遭遇会出现不同的像素怪物，剪影与行为各具特色，因此没有两次攀爬的感受是相同的。

一轮的结局在塔顶揭晓：击败 Boss，一个精心设计的胜利画面为这次攀登喝彩；或者在途中任何地方血量归零，失败画面记录下你走到了多远。无论哪种结局，玩家都可以重试或返回标题画面，无需重启应用程序。

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