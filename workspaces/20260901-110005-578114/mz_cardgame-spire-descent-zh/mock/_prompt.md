# 尖塔沉降（Cardgame Spire Descent）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个尖塔沉降卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款构筑牌组类 Roguelike：玩家一层一层地攀登尖塔，用一副通过抽选决策不断成长和
演化的牌组与敌人作战。每场战斗都是一道战术谜题：打出攻击牌造成伤害，技能牌获得
格挡，能力牌带来持续增益——全部受制于每回合的能量预算。战斗之间，玩家从奖励选择
中抽选新卡、光顾商店，并收集能扭曲规则的遗物。三个各具特色的角色职业，拥有不同
的初始牌组和卡池，确保了重玩价值。这份幻想在于：打造出一套能把最终 Boss 玩成
儿戏的破坏级连击引擎——前提是你能活得够久，把它拼齐。

## 玩家体验流程

1. **标题画面** —— 风暴天空映衬下一座黑暗塔楼的剪影，游戏名以华丽的奇幻字体呈现，
   并有新的一轮 / 继续按钮。演出 GameX其灰色。
2. **职业选择** —— 三个角色职业（战士、盗贼、法师），各有独特的立绘、初始牌组
   描述和标志性机制（战士：力量叠加；盗贼：飞刀生成；法师：法球引导）。
3. **地图导航** —— 一张展示当前章节的分支路径地图。节点代表战斗遭遇、精英战、
   商店、休息点和事件。玩家在权衡风险与收益中选择自己穿越该章节的路线。
4. **卡牌战斗** —— 回合制战斗。玩家每回合抽 5 张牌，拥有 3 点能量可供消耗，通过
   打出卡牌来攻击或防御。敌人会显示其意图（攻击数值、增益、减益），便于玩家规划。
   生命值在战斗之间延续。
5. **卡牌奖励** —— 战斗结束后，从 3 张牌中选 1 张加入牌组。卡牌分稀有度（普通、
   罕见、稀有），边框颜色各不相同。玩家也可以跳过奖励，让牌组保持精简。
6. **遗物** —— 修改规则的被动物品（例如："每回合获得 1 点能量"、"第 1 回合额外
   抽 2 张牌"）。遗物显示在屏幕顶部的一条栏中，带有提示说明。精英敌人必定掉落
   一件遗物。
7. **三个章节** —— 一轮游戏横跨 3 个章节，每个章节末尾都有一个 Boss。Boss 拥有
   独特机制和多阶段模式。击败最终 Boss 即赢下这一轮，并弹出展示统计数据的胜利
   画面。

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