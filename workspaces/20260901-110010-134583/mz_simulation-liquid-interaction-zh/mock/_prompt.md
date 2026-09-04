# 抽象流体点击器

制作一个完整可玩的 **3D 模拟游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一个可玩的实时粒子流体实验室，核心是由约一万个粒子组成的球体。玩家通过斥力与引力完成塑形、约束和能量挑战，并理解速度与力场如何改变系统。

## 必须实现的可玩系统

1. **系统 1** - 通过 GPGPU 或等效 GPU 纹理技术模拟约一万个粒子，并提供较低粒子数量的平稳降级方案。
2. **系统 2** - 鼠标移动产生斥力，按下鼠标产生引力；力场半径与强度通过清晰 UI 控制。
3. **系统 3** - 根据速度把粒子颜色从冷色连续映射到暖色，并显示力方向、质心和湍流反馈。
4. **系统 4** - 提供可玩挑战：形成目标轮廓、让流体穿过圆环、约束不稳定核心以及恢复平衡。
5. **系统 5** - 追踪稳定度、逸出粒子、能量消耗、目标精度和耗时，并提供重置与慢动作实验控制。
6. **系统 6** - 在高负载下保持流畅和清晰响应，可自动调整画质但不能改变游戏状态规则。

## 成长与推进

完成实验可解锁多源力场、涡旋、障碍、黏度预设和更高难度目标形状。

## 美术方向

优雅黑色实验室虚空，以发光流体渐变、细网格、玻璃目标体和精确科学 UI 构成。

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