# 节庆委员会大灾难

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款喜剧风开放村庄管理游戏：玩家要筹办大型节庆，而每位委员会成员都会制造新的危机。玩家在各场地间奔走、安排活动、解决本地事故，并努力保住庆典和社区信任。

## 必须实现的可玩系统

1. **系统 1** - 探索相连村庄，包含至少四个节庆场地、商贩街、仓储区以及布置期间可开启的捷径。
2. **系统 2** - 放置摊位、装饰、舞台、电线和人群护栏，同时满足空间、预算、通行和安全约束。
3. **系统 3** - 建立限时活动日程，并亲自完成游行引导、烹饪、音乐提示或烟花布置等短玩法。
4. **系统 4** - 处理天气、物资丢失、动物逃跑、演员冲突、停电和人群拥堵等动态事件。
5. **系统 5** - 通过可见后果管理委员信任、商贩满意、到场人数、预算和安全，而不是只显示文字报表。
6. **系统 6** - 从开幕到闭幕完整运行最终节庆日，并提供成功、部分失败或喜剧性灾难状态。

## 成长与推进

完成准备工作可解锁更好设备与志愿者能力；未解决事件会延续到最终节庆日并增加复杂度。

## 美术方向

欢快手工低多边形村庄，包含彩旗、多样摊位、表情丰富角色、可读人流和滑稽事件特效。

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