# 花园爬行（Garden Crawl）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Garden Crawl**——一款以植物为盟友、以种子
做构筑牌组的花园地牢 Roguelike。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位园丁向下穿行于一座既是地牢也是花园的场所——泥土图块上可以种下种子，它们会
在数个回合内长成盟友、屏障或资源产出者。玩家携带一副种子牌组，在遭遇战之前和
之中把种子打到网格上。向日葵每回合提供能量，荆棘丛伤害相邻的敌人，藤蔓墙阻断
路径，治疗之花则为园丁恢复生命。季节每隔几层轮换一次，改变哪些种子能茁壮生长：
春季提升生长速度，夏季强化攻击型植物，秋季带来额外收获，冬季则让一切变慢。
层与层之间，玩家抓取新种子、把不想要的堆肥掉，并照料一座在多轮之间持续存在的
温室，为将来的每一轮提供开局加成。

## 玩家体验流程

标题画面展示一座在地牢石块上生长起来的花园。开始一轮时，玩家获得一副由 8 张基础
种子组成的初始种子牌组。

每一层都是一场基于网格的遭遇战。园丁站在一侧，敌人从另一侧逼近。在敌人靠到园丁
身前之前，玩家在泥土图块上种下种子。种子会随回合成长：发芽 -> 成熟 -> 生效。
成熟的植物提供各自的效果（伤害、治疗、阻挡、能量产出）。玩家需要管理一项能量
资源，用于种下种子和启动能力。

层与层之间，抓取画面提供三个新种子选项。堆肥选项可以从牌组中移除一张种子。
每 3 层季节变化一次，在视觉上改变环境并调整植物属性。温室作为元层级在多轮之间
持续存在——种在那里的种子提供小幅的开局加成。这一轮在 Boss 层结束，或在园丁
生命值归零时结束。结算画面展示通过的层数、养成的植物数和收集到的种子数。

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