# 每条路都在午夜前回返

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款超现实公路循环探索游戏。无论选择哪条路线，玩家都会在午夜前回到同一家汽车旅馆；地标会逐渐腐化，而记忆会跨循环保留。玩家必须绘制矛盾并打破空间拓扑。

## 必须实现的可玩系统

1. **系统 1** - 驾驶并步行探索相连公路网，包含至少四个独特地标、分支路口和可进入建筑。
2. **系统 2** - 呈现清晰的白昼至午夜循环；道路连接会变化，但选定证据、地图标注和玩家知识会保留。
3. **系统 3** - 允许玩家放置地图标记，并比较路程、路牌、阴影和地标状态，以找出不可能的连接。
4. **系统 4** - 加入不断变化的搭车者、电台广播、天气和路边危险，在后续循环中揭示不同线索。
5. **系统 5** - 追踪车况、燃料、疲劳和扭曲度；午夜临近时，控制与景观会随之改变。
6. **系统 6** - 提供多种打破拓扑的方案，要求玩家在最终午夜重置前执行已学会的路线序列。

## 成长与推进

每验证一个空间矛盾都会解锁新地图工具与记忆锚点，使更多状态跨循环保留并暴露更深路线。

## 美术方向

梦境般的夜间公路美学，包含湿润柏油、钠灯、模拟仪表辉光、不可能折叠地平线和逐步升级的空间扭曲。

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