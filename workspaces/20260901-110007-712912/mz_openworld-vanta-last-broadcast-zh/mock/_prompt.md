# 来自万塔的最后广播

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一场横跨小型恒星系的孤寂太空探索战役。玩家驾驶打捞船追踪一座死亡殖民地反复播出的求救信号；风暴、故障系统和互相矛盾的录音让导航逐渐变成生存谜案。

## 必须实现的可玩系统

1. **系统 1** - 在可导航星图中驾驶飞船，支持手动推进、停靠、扫描，并提供至少三个可探索轨道地点。
2. **系统 2** - 调节多频段接收器以分离万塔广播片段，同时处理干扰和伪回波对正确信号的遮蔽。
3. **系统 3** - 在辐射风暴和碎片遭遇中重分配系统，管理船体、电力、燃料与热量。
4. **系统 4** - 从废弃飞船中回收日志和实物证据，再把它们排列到时间线上，从而改变最终信息的含义。
5. **系统 5** - 加入危险与可选救援，在任务进度、船员安全和不断减少的资源之间制造取舍。
6. **系统 6** - 抵达万塔并以多种可玩方式接近信标，不同方案应揭示不同真相与结局。

## 成长与推进

回收部件可提升引擎、扫描精度和电力容量，从而进入更危险的区域并解析更深层信号。

## 美术方向

硬科幻孤寂氛围：黑暗行星剪影、仪表照明船舱、体积信号波、电弧和苍白求救信标。

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