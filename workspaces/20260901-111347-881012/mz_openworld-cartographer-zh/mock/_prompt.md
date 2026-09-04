# 开放世界制图师（Open-World Cartographer）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**开放世界制图师（Open-World Cartographer）**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名深入未测绘荒野的制图师，边探索边绘制地图。这里的幻想是发现并掌握
未知：每一步都揭开新的地形，每一个被绘上地图的地标都带来利润与声望。张力来自
危险的地形——悬崖、沼泽、猛兽领地——以及有限的补给。绘制完成的地图可以卖给镇上的
商人，为更深入的远征筹措更好的装备。地图本身就是最主要的 UI 元素，随玩家移动
而逐步填充。

## 玩家体验流程

1. **标题画面** —— 一个羊皮纸风格的标题，游戏名称采用手绘字体，配有墨水瓶与
   羽毛笔的图案，以及一个开始按钮。
2. **荒野** —— 玩家在程序化生成、变化多样的地形中自由移动：森林、山脉、河流、
   洞穴和遗迹。战争迷雾遮蔽未探索的区域。
3. **地图绘制** —— 随着玩家的探索，小地图和全屏地图会逐步填入地形细节。地标
   （遗迹、独特的树木、洞口）可以被标注，以获得额外价值。
4. **危险** —— 敌对的野生动物、险峻的悬崖和流沙威胁着玩家。生命值有限，治疗
   需要返回营地或消耗稀缺的补给。
5. **补给** —— 玩家携带食物、墨水和绳索。食物随时间消耗；标注地标时消耗墨水；
   跨越悬崖需要绳索。补给耗尽会迫使玩家撤退。
6. **出售地图** —— 返回起始小镇后，玩家可以出售绘制完成的地图区块。更大、更
   详尽且带有标注的地图能卖出更高的价格。
7. **装备升级** —— 利润可以购买更好的靴子（移动更快）、罗盘（显示前方地形
   类型）、提灯（用于探索洞穴）和结实的背包（更大的补给容量）。

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