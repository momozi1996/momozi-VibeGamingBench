# 赛博朋克 3D 终端

制作一个完整可玩的 **3D 解谜游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款发生在悬浮赛博朋克终端中的命令驱动 3D 解谜冒险。输入命令会改变周围模拟空间：启动机器、分配能源、移动平台、解码矩阵，并触发强烈空间反馈。

## 必须实现的可玩系统

1. **系统 1** - 实现真正的命令解析器，包含历史、帮助、自动补全或建议、参数、别名和清晰的未知命令处理。
2. **系统 2** - 把命令连接到可见 3D 系统，例如发射火箭、开启区域、旋转代码矩阵、分配能源和移动无人机。
3. **系统 3** - 构建多步骤任务，让玩家检查状态、推断有效命令、组合参数并观察持续后果。
4. **系统 4** - 提供强反馈：成功命令驱动世界动画，发射产生程序化烟雾，无效命令让空间晃动或故障化。
5. **系统 5** - 提供可发现日志、隐藏命令、可选目标、命令文档以及至少三个相连任务章节。
6. **系统 6** - 追踪目标状态、终端权限、错误、已发现命令和完成度，并支持重启与错误输入后的安全恢复。

## 成长与推进

完成任务会提升终端权限，解锁新的命令命名空间，并显露周围 3D 机器的更多部分。

## 美术方向

黑色虚空赛博命令舱，包含玻璃终端平面、洋红/青色矩阵、体积烟雾、自发光机械和受控故障效果。

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