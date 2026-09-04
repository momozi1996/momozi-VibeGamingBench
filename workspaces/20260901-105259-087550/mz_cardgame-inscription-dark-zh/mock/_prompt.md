# 黑暗铭刻（Cardgame Inscription Dark）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个黑暗铭刻卡牌游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款黑暗且氛围浓厚的卡牌对战游戏，召唤生物需要献祭其他生物。玩家把卡牌放到网格
战场上，但强力卡牌索求鲜血——必须献祭较弱的生物来为更强的召唤供能。每张卡都刻有
印记（被动能力），它们会催生出涌现式的互动：带"飞行"的卡越过阻挡者；带"分叉打击"
的卡同时命中两条通道。一张大地图以分支路径串联起各场遭遇，一段悄然渗出的元叙事
则通过环境叙事层层展开。这份幻想在于：在木屋恐怖的氛围包裹下，为力量而献祭自己
生物时那种令人不安的快感。

## 玩家体验流程

1. **标题画面** —— 一张光线昏暗的木桌，游戏名以粗糙的字体刻在桌面上，一支摇曳的
   蜡烛，以及一张供玩家点击的"开始"卡牌。演出 GameX其灰色。
2. **牌桌** —— 战斗在 4 条通道的网格上展开。玩家的一排面对对手的一排。卡牌从手牌
   打进各条通道。每张卡都有攻击力、生命值、鲜血消耗，以及零个或多个印记。
3. **献祭机制** —— 要打出一张消耗 2 点鲜血的卡，玩家必须先献祭场上自己已有的
   2 个生物。被献祭的生物会伴随视觉效果死去。免费卡牌（0 消耗）可充当献祭素材。
   这在场面控制与力量之间制造出持续的张力。
4. **印记** —— 至少 8 种各具独特图标的印记：飞行（直接攻击）、分叉打击（同时命中
   相邻通道）、强力跃击（可阻挡飞行）、恶臭（相邻敌人攻击力 -1）、不灭（死亡时
   回到手牌）、雏鸟（1 回合后进化）、死亡之触（杀死任何被它伤害的目标）、九命
   （额外拥有 3 条命）。
5. **伤害天平** —— 一座天平会随伤害的造成而倾斜。当一方承受的总伤害比另一方多出
   5 点时，该方落败。天平每次受击都会在视觉上倾斜，随着逼近临界点而制造张力。
6. **大地图** —— 战斗之间会出现一张分支路径地图，上面有各类节点：卡牌对战、图腾柱
   （为一张卡添加印记）、营火（合并两张卡）、商人（买卖卡牌）。玩家自行选择路线。
7. **氛围** —— 黑暗、低饱和的配色。卡牌看起来像手绘在羊皮纸上。对手是一个双眼
   发光的黑影身形。环境效果（浮尘、烛火闪动）进一步强化这种令人不安的情绪。

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