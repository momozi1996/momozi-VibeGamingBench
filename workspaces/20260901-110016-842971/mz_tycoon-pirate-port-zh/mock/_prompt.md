# 海盗港（Pirate Port）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Pirate Port**，一款**海盗巢穴管理经营**游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在一座热带岛屿上营建一处隐秘的海盗港，用酒馆和码头吸引船队，派他们出海掠夺战利品，并在恶名太盛时抵御皇家海军。经济在三种货币之间循环：掠夺得来的金币资助建筑，声望吸引更好的船队，恶名则招来海军的注意。张力在于最赚钱的行动同时也让恶名涨得最快，迫使玩家在进攻性与防御准备之间求平衡。整体基调是加勒比式的冒险豪情：棕榈树、摇摇晃晃的码头、朗姆酒桶和炮火硝烟。

## 玩家体验流程

玩家从标题画面开始经营一座新的港口。视图展示一座沿海岛屿，附带用于建造的网格。玩家建造码头来停泊船只、酒馆来吸引海盗船队、仓库来存放战利品，以及防御设施（城墙、火炮、瞭望塔）来击退海军的进袭。

海盗船队会依据港口的声望前来。每支船队都有船型、战斗强度和维持成本。玩家从一张贸易航线地图上选定目标，派出船队去掠夺——目标越富庶，产出的金币越多，但恶名也涨得越高。掠夺过程自动推演，并给出一份结果摘要。

金币资助扩张：更好的码头能吸引更大的船，升级过的酒馆让船队保持愉快，而一座船坞则允许修理和升级船只。船队士气取决于酒馆品质、掠夺成果和报酬。

当恶名达到阈值时，海军会来进攻。海军进袭是塔防式的遭遇战，港口的火炮和城墙必须顶住来袭的战舰。挺过一次进袭会让恶名略微下降；失败则意味着损失建筑和船队。

游戏会记录金币、舰队规模和已完成的掠夺次数。当港口陷落或达成某个繁荣里程碑时，一个经过美术处理的结算画面会展示港口统计数据。

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