# 3D 塔防微缩模型

制作一个完整可玩的 **3D 策略游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款发生在微缩岛屿上的明亮体素塔防游戏。玩家放置并升级防御塔，敌人使用 A* 绕过地形与合法障碍，让建造行为与路径形状形成战术关系。

## 必须实现的可玩系统

1. **系统 1** - 允许在体素网格上通过鼠标放置防御塔，包含幽灵预览、范围提示、费用检查、烟雾粒子和落地弹跳。
2. **系统 2** - 敌人使用 A* 从出生点前往基地，放置后重新计算合法路线，并拒绝完全堵死道路的建造。
3. **系统 3** - 实现至少三种防御塔，具有不同索敌、激光或弹体行为、伤害定位、冷却和升级分支。
4. **系统 4** - 运行多波敌人，包含多种敌人类型、属性升级、奖励、基地生命、胜负、暂停和速度控制。
5. **系统 5** - 加入可破坏或变化地形、分支道路，以及影响射程、速度或伤害的战术地块。
6. **系统 6** - 制作具有体积感的命中与死亡爆炸、清晰生命反馈、经济 UI 和完整结算/重试流程。

## 成长与推进

新岛屿加入路线限制、防御塔联动、敌人抗性以及短战役中的永久解锁选择。

## 美术方向

精致马卡龙体素微缩岛，包含繁茂地形、玩具感塔与敌人、清晰激光、块状烟雾和彩色体积爆炸。

## HTML 提交格式

用两个文件交付一个可独立运行的浏览器游戏：

- `index.html` - 完整可玩的呈现层。使用 Three.js 和 WebGL 完成可玩呈现。
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