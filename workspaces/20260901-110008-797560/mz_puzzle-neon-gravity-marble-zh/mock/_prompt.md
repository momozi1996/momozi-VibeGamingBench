# 霓虹重力球

制作一个完整可玩的 **3D 解谜游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款通过键盘倾斜或设备方向控制的触感型 3D 霓虹弹珠迷宫。真实重力、碰撞、移动几何体和动量就是谜题本身；玩家需要学习压弯、制动和重定向，穿越越来越危险的透明赛道。

## 必须实现的可玩系统

1. **系统 1** - 使用 Cannon.js 模拟弹珠，包含重力、滚动加速度、弹性、摩擦、坡道、护轨和可信碰撞。
2. **系统 2** - 支持方向键倾斜与设备方向控制，并提供校准、灵敏度设置和始终可用的桌面替代方案。
3. **系统 3** - 用镜头冲击、火花、声音和受支持设备上的 Vibration API 表现碰撞，同时保持操控清晰。
4. **系统 4** - 提供至少三条赛道，包含检查点、移动平台、发射板、窄轨、危险、收集物和终点门。
5. **系统 5** - 追踪时间、坠落次数、检查点进度、最佳成绩和可选收集物；离开赛道后应快速恢复。
6. **系统 6** - 使用随速度变化的拖尾或后处理表现运动模糊与高速危险感。

## 成长与推进

后续赛道加入更强重力、旋转框架、极性区域和风险收益分支，同时保持确定性重置。

## 美术方向

黑暗合成波虚空，以半透明自发光赛道、对比危险色、发光粒子、光泽弹珠和克制辉光呈现。

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