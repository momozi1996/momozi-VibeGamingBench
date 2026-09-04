# 视觉错觉解谜

制作一个完整可玩的 **3D 解谜游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款围绕不可能建筑展开的正交投影 3D 解谜游戏。玩家旋转雕塑般的建筑，直到分离道路在屏幕上重合，为小角色创造临时可通行连接。

## 必须实现的可玩系统

1. **系统 1** - 使用吸附角度与自由拖动控制绕 3D 建筑旋转正交相机，同时保持稳定构图与正确深度排序。
2. **系统 2** - 检测路径端点的屏幕空间对齐，只有几何与遮挡条件有效时才允许通行。
3. **系统 3** - 允许点击可达节点，让角色沿连接路线移动；无效移动必须给出清晰反馈。
4. **系统 4** - 提供至少六个逐步升级的谜题，使用旋转塔、可移动桥、电梯、开关、遮挡物和多步对齐。
5. **系统 5** - 加入撤销、重开、相机复位、选中节点高亮、可选提示以及确定性谜题状态。
6. **系统 6** - 通过携带或激活目标物完成关卡，再解锁贯穿整座建筑的选关路径。

## 成长与推进

新章节加入分层对齐规则、移动部件、分裂角色和同时满足的路径条件，并通过视觉方式教学。

## 美术方向

宁静建筑微缩景观，使用干净石材、宝石点缀、柔和阴影、不可能剪影和极简插画 UI。

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