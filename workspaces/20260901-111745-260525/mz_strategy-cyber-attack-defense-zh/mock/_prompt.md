# 网络攻击防御战

制作一个完整可玩的 **3D 策略游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款 3D 网络防御动作策略游戏。红色攻击封包沿拓扑飞向中央服务器；玩家拦截威胁、加固节点，并读取可视化预测模型，在不断升级的协同攻击中生存。

## 必须实现的可玩系统

1. **系统 1** - 构建清晰的 3D 拓扑，包含核心服务器、中继节点、路径、正常流量和沿路径移动的多种攻击封包。
2. **系统 2** - 允许点击封包或节点，使用受冷却限制的工具进行拦截、隔离、改道或引爆。
3. **系统 3** - 可视化一个受卡尔曼滤波启发的预测层，估计封包未来路径，并随观测到来更新不确定性。
4. **系统 4** - 运行离散波次，包含诱饵、分裂封包、装甲载荷、失陷节点和最终协同首领攻击。
5. **系统 5** - 加入节点升级、防火墙放置、资源收入、连击得分和服务器生命，在主动与被动防御间形成取舍。
6. **系统 6** - 为每次拦截、漏过、预测更新和节点故障配备独特的 8-bit 合成音效与可见反馈。

## 成长与推进

后续波次扩展拓扑复杂度并解锁专用防御，敌人会适应被过度使用的策略。

## 美术方向

高对比赛博作战空间，包含发光拓扑线、体积封包拖尾、绿色数字雨、红色威胁脉冲和像素音频可视化。

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