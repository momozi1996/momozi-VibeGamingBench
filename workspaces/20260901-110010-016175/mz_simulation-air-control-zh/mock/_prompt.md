# 空中管制（Air Control）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Air Control**，一款 2D 空中交通管制模拟游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是在一块雷达式管制屏幕前把飞机安全引导至它们各自的跑道，在越来越
拥挤的空域中绘制航路，同时避免相撞并应对天气扰动。有趣的张力来自时间压力下的
空间规划：飞机以不同的速度和高度从屏幕边缘进入，每一架都需要抵达某条特定跑道。
玩家绘制航路，飞机会沿之飞行，但不断到来的新飞机会持续迫使玩家重新规划。近距接近
告警会制造出恐慌时刻，此时迅速改航才能避免灾难。天气事件会关闭跑道或形成
禁飞区，要求玩家实时调整精心铺设好的计划。

## 玩家体验流程

玩家进入游戏时看到一个塔台主题的标题画面，从战役列表中选择一座机场，然后进入
雷达视图。屏幕展示一座风格化的俯视机场，含跑道、滑行道及周边空域。飞机出现在
边缘，带有呼号、机型和目标跑道标识。玩家通过点击并拖动航路点，为每一架飞机
绘制一条从当前位置通往其指定跑道的航路。

飞机会按自身速度沿航路飞行。当两架飞机靠得太近时会闪现接近告警。成功着陆可得分；
相撞或飞机未着陆便飞离屏幕会损失生命。关卡之间玩家可以升级：增建跑道、安装
气象雷达、解锁速度控制指令，或扩展空域边界。天气事件——降低能见度的雾、形成
禁飞区的风暴、影响跑道可用性的侧风——会加大压力。战役横跨 3 座机场共 12 个
以上关卡，交通密度与复杂度逐步升级。关卡总结会显示着陆架数、近距接近次数
以及效率评级。

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