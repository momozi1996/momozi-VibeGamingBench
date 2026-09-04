# 城市电力平衡师

制作一个完整可玩的 **3D 模拟游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款实时 3D 城市电网调度模拟。玩家在用电、储能和车网互动模式之间切换建筑，同时应对可再生能源与需求波动，在不切断关键服务的前提下阻止级联过载。

## 必须实现的可玩系统

1. **系统 1** - 渲染低多边形城市，包含动态风机、光伏场、变电站、充电枢纽、储能建筑和可见输电线路。
2. **系统 2** - 允许点击建筑切换运行模式，并通过拖动或选择变电站在不同电网区域间重新分配容量。
3. **系统 3** - 实时模拟发电、需求、储能电量、线路容量、频率稳定和过载传播。
4. **系统 4** - 用动画显示能量流向；过载建筑在故障前应从正常蓝色变为闪烁红色警告。
5. **系统 5** - 提供平稳天气、晚间峰值、可再生能源骤降、热浪和关键服务优先级等多种场景。
6. **系统 6** - 按可靠性、绿电利用、成本、未满足需求和恢复时间评分，并提供成功与级联停电失败状态。

## 成长与推进

战役场景会解锁电池、需求响应工具、更强线路和预测辅助，提供新策略而非单纯数值升级。

## 美术方向

清晰低多边形基础设施微缩景观，包含多样绿地、温暖城市窗光、青色能源流和明确黄/红故障状态。

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