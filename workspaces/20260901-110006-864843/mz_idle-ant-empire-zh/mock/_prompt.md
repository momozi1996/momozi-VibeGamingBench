# 放置蚂蚁帝国（Idle Ant Empire）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**放置蚂蚁帝国**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家从一只蚁后开始建立一个蚂蚁殖民地，把工蚁分派到各项任务上，解锁新的蚂蚁
类型，并通过转生重置实现指数级增长。游戏的幻想核心是看着一个微小的帝国扩张到
荒谬的规模：从捡食面包屑到收割整座花园，从寥寥几只工蚁到数以百万计。放置循环
持续运转——即使玩家不点击，蚂蚁也在采集资源。紧张感来自资源分配决策，以及
威胁殖民地存亡的季节性挑战。

## 玩家体验流程

1. **标题画面** —— 一幅地下隧道的剖面图，蚂蚁在其中行进，游戏名采用土褐色
   字体，还有一个做成叶片样式的开始按钮。
2. **殖民地视图** —— 一个侧视视角的蚂蚁殖民地，可以看到各个巢室：育婴室、
   食物仓库、蚁后寝宫，以及连接它们的隧道。蚂蚁会明显地在巢室之间搬运资源。
3. **工蚁分派** —— 玩家把蚂蚁分配到各个岗位：采集蚁（收集食物）、建造蚁
   （挖掘新巢室）、兵蚁（防御）和护理蚁（孵卵）。用滑块或按钮来控制分配比例。
   产出速率会实时更新。
4. **资源生产** —— 食物会根据采集蚁数量自动累积。玩家可以点击手动提升采集
   效率。资源用于修建新巢室、孵化蚂蚁和购买升级。
5. **蚂蚁类型** —— 可解锁的蚂蚁类型带有特殊能力：切叶蚁（食物加成）、火蚁
   （防御）、飞蚁（探索）和巨型蚁（10 倍产出）。每种类型都有独特的精灵图。
6. **转生系统** —— 当殖民地规模达到某个阈值时，玩家可以转生：重置殖民地，
   但获得永久倍率（蚁后繁殖力、采集速度、防御强度）。每次转生都会让下一轮
   变得更快。
7. **季节性挑战** —— 周期性事件会威胁殖民地：暴雨淹没隧道（需要建造蚁）、
   捕食者来袭（需要兵蚁）、冬季食物减少（需要存粮）。挺过挑战可获得额外资源。

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