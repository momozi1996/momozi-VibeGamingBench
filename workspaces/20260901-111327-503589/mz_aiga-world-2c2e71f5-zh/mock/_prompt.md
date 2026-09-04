# 倒置书吏

制作一个完整可玩的 **3D 冒险探索游戏**，以
**第三人称** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

一名宇宙剧本的执行者在倒置世界追捕叛逆武者、收集禁忌真相，并决定是否反抗所谓作者。

## 世界参数

把它作为原创的 **超现实** 共享世界改写，范围为 **中型**，叙事基调为 **超现实**。不得复刻商业角色、名称、设定、标志或受保护的视觉设计。

## 必须实现的可玩系统

1. **系统 1** - 探索《倒置书吏》中的至少三个相连故事地点，支持直接移动、检查地标和解锁路线。
2. **系统 2** - 解决多种空间、顺序或背包谜题，其状态必须存在于规则层。
3. **系统 3** - 与不同角色交谈，选择会改变信任、可用帮助和后续场景目标。
4. **系统 4** - 收集或制作会改变导航、谜题解法或角色结局的重要物品。
5. **系统 5** - 持续保存已发现事实、关系、改变地点和完成的人情，让后续场景承认早期行动。
6. **系统 6** - 以可玩的最终场景收束，把探索、谜题和关系决定组合成明显不同的结果。

## 推进与持久状态

使用三个阶段组成短流程：先清楚引入中心交互，再与世界压力和有意义选择组合，最后用
综合场景检验掌握程度。重要规则、目标、资源、关系、选择状态、危险、进度和结果必须
显示在稳定 HUD 区域，并在 `game_logic.js` 中有对应状态。各系统必须通过共享状态
互相影响，不能只是彼此割裂的按钮、菜单或视觉演示。

## 美术方向

使用可辨识地标、分层路线、环境叙事、有效灯光引导和清晰交互状态。

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