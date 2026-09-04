# 开放世界死灵法师（Open-World Necromancer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界死灵法师（Open-World Necromancer）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名死灵法师，游荡在一个黑暗奇幻世界中，从倒下的敌人身上唤起亡者，
组建一支不断壮大的亡灵军团。这里的幻想是禁忌之力：每一处战场都成为征兵场，
每一座墓地都是金矿。张力来自追猎你的英雄 NPC——圣骑士、女巫猎人和冒险者小队，
它们会随着你的恶名上升而变得更强。你必须征服领地、用亡灵驻军加固据点，并根据
可用的尸体来选择要唤起哪些仆从。

## 玩家体验流程

1. **标题画面** —— 一个黑暗而有氛围的标题，游戏名称以哥特字体呈现，背景是
   雾气弥漫的墓地场景。开始按钮伴着诡异的光脉动。
2. **世界** —— 玩家在一个黑暗的开放世界中自由移动，其中有村庄、墓地、森林和
   废弃要塞。每个区域都有不同的敌人类型和尸体品质。
3. **战斗** —— 敌人（卫兵、民兵、野生动物）一见到你就会攻击。玩家拥有一种
   黑暗魔法攻击，并可以指挥自己的亡灵仆从作战。战斗为实时进行，采用简单的
   点击攻击和技能快捷键。
4. **唤起亡者** —— 敌人倒下后，尸体会留在地上。玩家对尸体引导一个唤起法术，
   将其加入自己的军团。不同的尸体类型产出不同的亡灵：骷髅战士、僵尸蛮兵、
   幽灵弓手。
5. **军团管理** —— 一个仆从面板显示当前军团的构成、生命值和数量。玩家可以
   解散弱小的亡灵，为更强的腾出位置。军团规模上限由玩家的死灵法力等级决定。
6. **领地征服** —— 攻占一座村庄或要塞会把它变成一处黑暗堡垒。驻守的亡灵会
   防卫它。被征服的领地会随时间产出灵魂能量。
7. **英雄猎手** —— 随着恶名增长，英雄 NPC 会生成并追猎玩家。他们很强大，
   拥有独特能力，需要策略才能击败。击败他们可获得精英尸体。

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