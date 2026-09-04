# 零重力拆解动效

制作一个完整可玩的 **3D 解谜游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款围绕精密无人机或相机爆炸拆解视图构建的 3D 检查维修谜题。玩家拆解设备、查看带标签零件、诊断故障，并按正确顺序恢复装配。

## 必须实现的可玩系统

1. **系统 1** - 通过滑块和鼠标滚轮平滑控制爆炸拆解程度，不同零件组应具有不同弹性与阻尼响应。
2. **系统 2** - 支持环绕、缩放、悬停高亮、隔离和固定的 3D 标签；标签应始终可读并正确指向移动零件。
3. **系统 3** - 设计检查谜题，让玩家通过视觉线索、诊断读数和功能说明识别故障零件。
4. **系统 4** - 要求遵循正确拆装顺序，包含工具选择、依赖检查、吸附预览和无效操作反馈。
5. **系统 5** - 提供多个设备模块或故障场景，涉及光学、电源、控制板、电机、散热和结构零件。
6. **系统 6** - 通过可玩的系统测试验证维修，并根据诊断与装配准确度显示性能差异。

## 成长与推进

新的维修工作加入更密集装配、更隐蔽故障、校准步骤和可选效率挑战。

## 美术方向

高端工业可视化，以拉丝金属、透明塑料、橡胶、玻璃光学件、棚拍灯光、清晰轮廓和克制技术标签呈现。

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