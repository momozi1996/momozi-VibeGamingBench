# 弓箭手远征（Sports Archery Quest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**弓箭手远征**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名弓箭手，踏上穿越奇幻大陆的旅程，靠技术性的瞄准去猎杀怪物、命中远处
的靶子，并用精准的射击击败 Boss。这里的幻想是那一记完美的箭：算准风力与距离，
将弓拉到满力，然后看着箭矢划过屏幕命中弱点。张力来自有限的箭数、拉弓中途会变向
的风力，以及在玩家瞄准时不断逼近的怪物。升级可以提升弓的力量、箭的种类，以及
玩家的拉弓速度。

## 玩家体验流程

1. **标题画面** —— 一片林间空地，一支箭插在靶子上，游戏名称采用符文风格的字体，
   以及一个箭头形状的开始按钮。
2. **世界地图** —— 一张基于节点的地图，展示各个地点：森林、峡谷、遗迹、龙之峰。
   每个地点包含多个关卡。完成关卡会解锁下一个区域。
3. **瞄准机制** —— 玩家按住按钮来拉弓（力度条填充），用方向输入瞄准，松开射出。
   箭的弹道遵循受重力和风力影响的物理抛物线。一个风力指示器显示当前的风向和
   强度。
4. **靶场关卡** —— 有些关卡是纯粹的射术考验：命中越来越远的靶心、射击移动靶，
   或者让箭穿过狭窄的缝隙。得分基于精度和速度。
5. **怪物狩猎** —— 怪物从右侧逼近。玩家必须击中弱点（发光的斑点）才能造成最大
   伤害。不同的怪物有不同的弱点位置和移动模式。
6. **Boss 靶标** —— 每个区域以一个 Boss 收尾：一头巨大的生物，身上有多个弱点，
   必须按顺序命中。Boss 有攻击阶段，此时玩家必须一边闪避（垂直移动）一边寻找
   出手的窗口。
7. **弓的升级** —— 赚到的金币可以购买升级：更长的射程、更快的拉弓、元素箭
   （火焰造成额外伤害、冰霜减速、闪电连锁）。一个商店画面展示可购买的升级项，
   并附有清晰的属性对比。

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