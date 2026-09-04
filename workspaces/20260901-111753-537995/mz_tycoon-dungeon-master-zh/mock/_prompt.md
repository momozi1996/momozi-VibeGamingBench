# 地下城主（Dungeon Master）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Dungeon Master**，一款**地下城管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演反派：在地底挖掘房间，往里填满陷阱和怪物，看着贪婪的英雄们一头闯进来被打败。但怪物不是免费的——招募它们要花金币，让它们开心要喂食物，还得有符合它们天性的房间。英雄会以强度递增的波次到来，而每一个逃脱的英雄都会散播"这地下城很好打"的消息，招来更强悍的冒险者。张力是经济层面的：金币来自被击败英雄的战利品，但全都花在攻势上就没钱照顾怪物的生活，而不开心的怪物会叛逃。这里的幻想是经营一家邪恶企业，产品是毁灭，客户则是不请自来的。

## 玩家体验流程

玩家从标题画面开始一座新的地下城。视图呈现的是一幅大地剖面。玩家花金币挖掘房间，构建出走廊与厅室的布局。每个房间都可以指定用途：宝库诱使英雄深入，陷阱房伤害他们，兵营容纳怪物，孵化场生产食物。

怪物从一份名录中招募——每个种类都有金币成本、偏好的房间类型和战斗强度。把怪物安置在它们喜欢的房间里能保持士气高涨；把它们硬塞进不合适的空间会让它们变得暴躁，最终导致叛逃。生物幸福度计量表始终可见。

英雄会周期性到来，从地表进入并朝宝藏推进。他们会与怪物战斗、触发陷阱，最终要么死亡（掉落战利品），要么逃脱。逃脱的英雄会提升地下城的名声，招来下一波更强的队伍。玩家必须在地下城深度、陷阱密度和怪物强度之间取得平衡，以应对不断升级的威胁。

游戏会记录金币、生物数量和已存活的波次数。当地下城之心被英雄摧毁，或达成某个波次里程碑时，一个经过美术处理的结算画面会展示地下城统计数据。

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