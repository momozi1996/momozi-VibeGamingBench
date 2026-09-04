# 雷霆女武神（Thunder Valkyrie）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Thunder Valkyrie**，一款 2D 纵向卷轴弹幕射击游戏。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一架孤零零的星际战机在数学般密集的敌方火力帷幕中穿行，判定框上的每一个像素都举足轻重，每一次毫秒级的闪避都换来又一口呼吸。张力就在于读懂弹幕几何：弹道会横扫、旋绕、汇聚，而玩家要在混乱之中描出那唯一一道安全的缝隙。出击之间，飞行员把掠夺来的黄金重新投入到船体升级、副武器和僚机挂件上，重塑下一波的手感。整体调性明亮、动感而不留余地——一场包裹在深空霓虹与壮观粒子爆破中的街机反应挑战。

## 玩家体验流程

一个经过设计的标题画面以宇宙背景介绍这款游戏，并给出一条通往机库的清晰路径。

在机库里，玩家查看自己持久保存的配装——星际战机等级、护盾类型、副武器、僚机——并花掉先前几轮赚来的黄金去升级各个槽位。每项升级都会明显改变下一次出击的弹道形态或生存能力。

玩家从一张星区地图上选择一个星座关卡。每个关卡都有独特的星空背景和自己的敌人构成。被锁定的关卡会一直封着，直到前一个 Boss 倒下。

一旦部署，画面便在层叠的星空之上纵向滚动。星际战机随输入平顺移动，其微小的发光核心判定框是唯一的可受伤部位。主激光持续开火；副武器和僚机则补上侧翼火力。一波波敌方截击机以几何编队入场，释放出向下横扫的脚本化弹幕配置。精英主力舰会掉落红色能量水晶；拾取它们会触发一种狂热状态，使射速翻倍并把附近的拾取物吸过来。

每个关卡都以一场多阶段 Boss 战收尾，Boss 会锁住卷轴并用层叠弹幕淹没整个场地。受到伤害会削减护盾；若护盾破碎，这一轮就以一个显示所得黄金和存活波数的结算浮层结束。击败 Boss 会解锁下一个关卡并奖励高级组件。

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

交互方案（keyboard-first）：本题材以键盘交互为主：提供方向键或 WASD、Space、Enter、Esc 等清晰按键，并在自然需要时加入鼠标。
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