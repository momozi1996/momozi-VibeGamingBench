# 管道危机（Pipe Crisis）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Pipe Crisis**，一个 2D 管道布线解谜游戏。
玩家在网格上摆放和旋转管道段，在压力累积、系统溢流之前把彩色流体从源头引到
对应颜色的排放口。

这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这是一款建立在流体布线之上、带时间压力的空间解谜游戏。每一关有一个或多个流体源，
在倒计时结束后开始泵送。玩家必须把队列中的管道段铺到网格上，通过旋转和摆放，
为每个源头到其对应排放口构造出连续的通路。张力来自倒计时和多种流体类型：红色
化学品不能与蓝色冷却液混合，绿色酸液会腐蚀普通管道，而交叉的路径需要特殊的接头
配件。最理想的版本会让人感觉像在应对一场手忙脚乱的管道抢险——当流体开始流动、
路径被颜色一路点亮时，此前每一秒的规划都得到了回报。

## 玩家体验流程

标题画面用管道意象和压力表营造出工业氛围。玩家进入以网格为基础的设施界面，
能看到流体源、排放口、障碍物和空白格。管道队列显示接下来会来的配件。倒计时
正一格格逼近流动开始的时刻。

前期关卡教基础布线：用简单的直管和弯管把一个源头连到一个排放口。很快，多个源头
就会要求并行通路，颜色匹配防止交叉污染，障碍物迫使玩家绕出创意路线。中期引入
特殊管道类型：允许两种流体通过而不混合的十字接头、能争取更多时间的储液罐，以及
用于腐蚀性流体的耐酸管道。后期关卡把所有机制结合起来，配上紧张的计时和复杂的
多源布局。

流动开始后，流体会可见地在管道中行进。布线成功会灌满排放口并完成该关卡。死路
造成的溢流或混合违规会触发失败状态。结算画面展示完成时间和效率评级。战役按主题
设施推进，布线要求层层升级。

## HTML 提交格式

用两个文件交付一个可独立运行的浏览器游戏：

- `index.html` - 完整可玩的呈现层。使用 HTML Canvas 2D 或 Three.js/WebGL 完成可玩呈现。
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