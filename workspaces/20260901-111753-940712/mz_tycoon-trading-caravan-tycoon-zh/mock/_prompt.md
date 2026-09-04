# 经营：贸易商队（Tycoon: Trading Caravan）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**路线规划与市场贸易经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一位商队船长，驾着一支小小的商队穿行于一张城镇网络之间，而每座城镇想要的东西和给出的价格都各不相同。这里的幻想是把地图当谜题来读——找出丝绸在哪儿便宜、在哪儿贵如黄金，然后在中间那段路上下注。每条路线都是一场赌博：短路安全但乏味，山口能省下好几天却招来盗匪，而你选的货物可能在抵达之前就变质了。成长会复利累积——更好的货车装得更多，雇来的护卫打开危险的捷径，冷藏箱解锁易腐货物——但风险同样如此，因为更大的一批货意味着出事时更大的损失。压力在于你赶路时市场也在变动，所以昨天板上钉钉的利润会变成明天的累赘。整体基调是羊皮纸与墨水味的商人策略：一个由贸易路线、价格板和精算过的赌注组成的世界。

## 玩家体验流程

玩家打开一张风格化的地图，上面散布着由长度与危险程度各异的道路相连的城镇。一枚商队标记停在当前城镇，一本账簿显示现金、货舱和任何进行中的契约。最初几分钟是扫读价格——这座城镇香料便宜，河对岸那座出价翻倍——然后把货车装满。

选定目的地意味着权衡路线选项：安全的大路在草料和过路费上花得更多，穿过盗匪地盘的捷径则有全部货物尽失的风险。一旦下定决心，商队便开始移动，事件随之展开——一场风暴延误行程，一道关卡索要钱币，路上的一位商人提出一笔额外交易。玩家实时看着货物、金钱和风险此起彼伏。

抵达一座新城镇后，玩家按当地价格出售，查看这里缺什么，再决定是补货还是继续前行。收益资助升级——增加运力的额外车厢、能提前揭示危险的斥候、把易腐货物纳入可交易范围的冷藏设施。每一项升级都会重塑哪些路线和货物才划得来。

随着时间推移，网络逐渐打开：新城镇出现，更高价值的契约变得可接，商队也从孤零零一辆货车成长为一支正经的贸易队伍。当玩家达到某个利润里程碑并看到成功画面，或是债务与失败契约堆积成破产时，这段弧线便告结束。两种结局都无需重启即可继续操作导航。

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