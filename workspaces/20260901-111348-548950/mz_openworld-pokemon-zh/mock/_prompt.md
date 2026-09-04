# 开放世界：WildRealm（Open World: WildRealm）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**生物收集类开放世界 RPG**。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家探索一个生机勃勃的开放世界，在高草丛中偶遇野生生物，与它们展开回合制
战斗——捕捉、培养并壮大一支属于自己的队伍。有趣的张力在于跨遭遇战的资源
管理：每消耗一颗捕捉球、每损失一点 HP、每用掉一次技能冷却，都是一种会一直
延续到玩家找到治疗师之前的投入。随着玩家离小镇越来越远、进入更艰难的地界，
压力不断攀升，而回报则是发现一只稀有生物，或者终于击败道馆馆主、解锁下一个
区域。游戏的感觉应当是**明亮、充满冒险感、令人怀旧**的——可以想象成小体量的
生物驯养结合 *A Short Hike*。

## 玩家体验流程

1. **标题与进入** —— 一个讨人喜欢的标题画面通过游戏名称、一幅风景背景和一个
   清晰的开始按钮来奠定基调。玩家按下开始，抵达一座小镇——一个枢纽，有治疗师、
   一位训练师 NPC，以及一条通往荒野的道路。

2. **开放世界探索** —— 玩家在一张大地图上自由行走，地图至少包含三个视觉上
   截然不同的区域：草原、一座小镇，以及一片位于天然屏障之外的封锁区域。高草丛
   意味着危险：踏入其中有一定概率触发野生生物遭遇战。整个世界一眼就能读懂——
   每个区域都有自己的地形、配色和场景道具。

3. **遭遇与战斗** —— 一个短暂的转场效果把玩家带入回合制战斗场景。玩家可以看到
   双方战斗者，以及 HP 条、等级和技能按钮。攻击会触发可见的动作和 HP 条的
   动画式下降。玩家也可以投出捕捉球（可见的抛物线弧、晃动动画、成功/失败反馈）
   或者逃跑。野生生物的物种和等级各不相同。

4. **成长与进程** —— 击败对手可获得经验；累积足够 XP 后，生物会伴随可见的
   反馈升级。玩家的队伍随时间变强，捕获的生物会加入名册。

5. **NPC 互动** —— 在镇上，一位训练师会向玩家发起一场强制战斗，而治疗师会
   恢复整支队伍。对话显示在一个有设计感的对话面板中。击败道馆馆主会奖励一枚
   徽章，解锁此前被封锁的区域，开放新的疆域供玩家探索。

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