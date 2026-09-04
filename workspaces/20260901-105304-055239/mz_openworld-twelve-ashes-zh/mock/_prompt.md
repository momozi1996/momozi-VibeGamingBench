# 十二灰烬之冠

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一场横跨十二个破碎国度的紧凑奇幻战役，这些国度共同构成一张可探索战略地图。玩家通过外交、野外战斗和危险联盟收集王冠碎片，而灰烬风暴会逐步抹去未受保护的领土。

## 必须实现的可玩系统

1. **系统 1** - 穿越包含十二个可辨识国度或国度节点的世界地图；每处都有聚落、统治者、地方冲突和旅行危险。
2. **系统 2** - 通过声望、承诺、贡品、证据和派系关系解决谈判，而不是只提供一次对话选择。
3. **系统 3** - 进行实时战术遭遇，包含移动、攻击、闪避、同伴指令以及清晰的胜利或撤退条件。
4. **系统 4** - 收集能力与代价各异的王冠碎片，它们会改变旅行、外交、战斗或抗灰烬能力。
5. **系统 5** - 模拟推进中的灰烬前线，改变路线、摧毁资源，并迫使玩家决定访问国度的顺序。
6. **系统 6** - 以议会集结或征服序列收束；其玩法结构和结局取决于幸存国度与联盟。

## 成长与推进

碎片、同伴和国度条约构成灵活流派，而永久失去国度确保战役决策不能全部逆转。

## 美术方向

被赋予 3D 生命的风格化暗黑奇幻地图，十二种强烈地域色彩、灰烬天空、纹章 UI 和魔法王冠效果。

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