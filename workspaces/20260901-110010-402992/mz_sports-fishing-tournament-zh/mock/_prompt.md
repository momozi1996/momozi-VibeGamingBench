# 钓鱼锦标赛（Sports Fishing Tournament）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**钓鱼锦标赛**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家在多个湖泊参加钓鱼锦标赛，挑选装备、读取天气状况、钓上各种鱼种以赢下对阵表。
这里的幻想是竞技钓鱼：知道什么拟饵配什么天况、找到藏着巨物的秘密钓点，并在
锦标赛的压力下把大鱼拉上岸。张力来自计时——锦标赛是限时的，而每一次抛竿都是在
稳妥的渔获与冒险博巨物之间下注。

## 玩家体验流程

1. **标题画面** —— 黎明时分的湖畔场景，游戏名称采用质朴的字形，以及一个做成
   钓具箱卡扣样式的开始按钮。
2. **锦标赛对阵表** —— 玩家可以看到当前的锦标赛对阵表，包含对手、目标鱼种和
   奖金。想要晋级，总重量必须超过对手。
3. **湖泊选择** —— 多个湖泊各具特点：浅水塘（简单，小鱼）、深水水库（中等，
   鱼种多样）、山间溪流（困难，稀有巨物）。每一处都有独特的视觉风格。
4. **装备选择** —— 开钓前，玩家从渔具店中挑选鱼竿、钓线和拟饵。不同的装备适合
   不同的天况与鱼种。更好的装备要花锦标赛奖金来买。
5. **天气系统** —— 锦标赛期间天气会变化：晴天、阴天、雨天。天气会影响鱼的活性
   ——阴天把鱼引到水面，雨天激活底层觅食的鱼，晴天让鱼躲进阴影里。
6. **钓鱼机制** —— 玩家抛竿、等鱼咬钩，然后进行一段需要管理张力的收线小游戏。
   越大的鱼挣扎得越凶。一个渔获画面展示鱼种、重量以及锦标赛排名的更新。
7. **鱼种收集** —— 一本图鉴记录所有钓到的鱼种，并保存最大渔获的记录。稀有鱼种
   只在特定湖泊的特定天况下出现。集齐图鉴可解锁额外的锦标赛。

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