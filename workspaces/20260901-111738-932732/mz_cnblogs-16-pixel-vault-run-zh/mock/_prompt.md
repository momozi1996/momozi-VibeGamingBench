# 像素秘境疾行

制作一个完整可玩的 **2D 平台跳跃游戏**，以
**横向卷轴视角** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

一款精确像素平台游戏，组合二段跳、冲刺、检查点、隐藏房间、收集物和紧凑多阶段路线。

## 必须实现的可玩系统

1. **系统 1** - 奔跑与跳跃支持土狼时间、输入缓冲、可变跳高和稳定碰撞。
2. **系统 2** - 使用二段跳与冲刺，并提供清楚充能、空中控制和危险互动。
3. **系统 3** - 激活检查点、快速重生并追踪收集物，不能丢失合法进度。
4. **系统 4** - 通过可发现触发器隐藏可选房间，并完成多段升级平台挑战。
5. **系统 5** - 提供至少三种功能不同的内容变化，实质改变时机、路线、资源使用或风险，不能只更换标签和颜色。
6. **系统 6** - 使用三阶段短流程：教学核心交互、在压力下组合系统，并以完整胜利、失败或计分完成闭环收束。

## 推进与持久状态

使用三个阶段组成短流程：先清楚引入中心交互，再与世界压力和有意义选择组合，最后用
综合场景检验掌握程度。重要规则、目标、资源、关系、选择状态、危险、进度和结果必须
显示在稳定 HUD 区域，并在 `game_logic.js` 中有对应状态。各系统必须通过共享状态
互相影响，不能只是彼此割裂的按钮、菜单或视觉演示。

## 美术方向

玩家、危险与落脚面轮廓清楚，景深层级稳定，并通过运动轨迹、挤压拉伸与冲击反馈增强手感。

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