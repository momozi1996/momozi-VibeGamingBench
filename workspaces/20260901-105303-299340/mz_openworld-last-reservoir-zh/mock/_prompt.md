# 最后的水库

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款围绕最后一座可用水库展开的干旱管理探索游戏。玩家往返各聚居地、检查基础设施，再回到议事厅分配水源；气候事件会把政治妥协变成真实的生存问题。

## 必须实现的可玩系统

1. **系统 1** - 探索水库流域及至少四个相连地区，检查水泵、运河、水井、农田和受损净化设备。
2. **系统 2** - 操作带阀门与分配滑块的实体水控台，让水流在 3D 地图中以动画方式重新定向。
3. **系统 3** - 在不断变化的多日预报中平衡库容、污染、压力和各地区需求。
4. **系统 4** - 与多个派系谈判；其需求与信任会根据检查结果、承诺、短缺和历史分配变化。
5. **系统 5** - 通过限时野外任务与紧急改道处理火灾、爆管、沙尘暴和非法取水。
6. **系统 6** - 以议会投票和最终干旱事件结束，其可玩结果同时取决于基础设施与社会合法性。

## 成长与推进

维修和谈判协议会解锁高效基础设施、更准确预报和新分配选项，并永久改变各区韧性。

## 美术方向

日晒褪色的低多边形流域，结合龟裂地面、青绿水流覆盖、风化市政机械、热浪和紧急红光。

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