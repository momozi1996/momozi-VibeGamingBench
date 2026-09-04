# 太阳线拉力赛

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一场以路线选择而非单一封闭赛道为核心的太阳系竞速冒险。玩家驾驶模块化赛车穿越轨道门，平衡热量与燃料，遭遇对手，并决定为抵达终点愿意承担多少风险或妥协。

## 必须实现的可玩系统

1. **系统 1** - 在至少三个行星区域驾驶或飞行响应灵敏的 3D 赛车，支持漂移、加速、制动、跳跃和检查点判定。
2. **系统 2** - 在可导航星系图上选择分支路线，在距离、风暴、引力井、通行费和维修机会之间权衡。
3. **系统 3** - 管理燃料、电池、船体和引擎热量；过度加速必须造成可见性能下降甚至故障。
4. **系统 4** - 与拥有可辨识载具和策略的对手竞速，包括尾流、封堵、捷径和机会性救援。
5. **系统 5** - 通过可选事件获取赞助商、升级和路线情报，并形成有意义的机械取舍。
6. **系统 6** - 完成多赛段锦标赛，包含积分榜、赛段结果、对手后果和至少两种最终结局。

## 成长与推进

赛段之间可安装互斥模块，改变操控、效率、耐久、扫描或加速行为。

## 美术方向

明亮复古未来赛车美学，包含饱和行星天空、全息门、热量拖尾、模块化载具和清晰宇宙路线图形。

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