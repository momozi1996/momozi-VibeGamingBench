# 极简 3D 节奏大师

制作一个完整可玩的 **3D 节奏动作游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款发生在无限自发光隧道中的极简 3D 节奏游戏。几何目标随节拍抵达；准确按键会把它们击碎成物理碎片，而隧道、材质和镜头会响应合成音频。

## 必须实现的可玩系统

1. **系统 1** - 在多条轨道生成几何节拍目标，并依据确定性谱面对按键进行 Perfect、Good 和 Miss 判定。
2. **系统 2** - 使用 Web Audio API 合成与分析器，让自发光材质、隧道分段和镜头冲击响应当前频段。
3. **系统 3** - 成功击中时把目标打碎成具有速度感的物理碎片；漏过时目标穿过玩家并造成独特隧道扭曲。
4. **系统 4** - 实现连击、倍率、得分、生命、歌曲进度、暂停、重试以及带判定统计的结算画面。
5. **系统 5** - 提供至少三张谱面或难度模式，节奏、速度、轨道组合和视觉身份均有区别。
6. **系统 6** - 在辉光、镜头运动、碎片和音频响应特效下仍保持判定清晰，并提供降低晃动与闪烁的辅助设置。

## 成长与推进

通关谱面可解锁更密集节奏、长按目标、交替打击方向和装饰性隧道主题，同时不破坏确定性节拍。

## 美术方向

克制的霓虹隧道，以黑色负空间、强轨道色、自发光几何体、频率响应表面和清晰冲击文字呈现。

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