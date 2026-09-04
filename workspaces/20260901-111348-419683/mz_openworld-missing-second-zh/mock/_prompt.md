# 消失的一秒

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款紧凑的开放城市调查游戏：一名超级英雄在无法解释的“一秒空白”中失踪。玩家巡查多个相连城区，重建被冻结的事件现场，并判断那场广受赞誉的救援是否其实是一场协同掩盖。

## 必须实现的可玩系统

1. **系统 1** - 探索至少三个相连城区，可在屋顶和街道间自由移动，并通过扫描器定位时间异常现场。
2. **系统 2** - 旋转时间残影、匹配证据位置，在倒计时结束前锁定合理事件顺序，以重建每个“消失的一秒”。
3. **系统 3** - 询问证人；其证词会随信任度和已发现证据变化，再把线索连接到可交互的阴谋板上。
4. **系统 4** - 加入多种异常：错位车辆、重复市民、冻结弹体和被污染的安保无人机等。
5. **系统 5** - 追踪公众信任与机构警觉；指控、泄密和鲁莽扫描会改变 NPC 反应与可用路线。
6. **系统 6** - 以可玩的最终对峙收束，玩家选择并证明多个理论之一，城市结局必须明显不同。

## 成长与推进

解决城区案件可升级扫描范围和时间残影控制，开放受限区域，并解锁越来越复杂的重建。

## 美术方向

雨夜近未来都市，以青色取证投影、琥珀街灯、图像小说阴影和锐利时间裂隙构成视觉语言。

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