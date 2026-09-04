# 恐怖玩偶屋（Horror Dollhouse）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖玩偶屋**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家探索一座与真实房屋互为镜像的玩偶屋，通过操纵微缩物件来影响原尺寸世界并
逃出去。游戏的幻想核心是诡异的尺度感：在玩偶屋里移动一把小椅子，楼上就传来
一声巨响；打开一扇微缩的门，真实房屋里就会显露出一条隐藏通道。紧张感来自
玩偶屋会回应玩家——玩偶人形会自己移动，没人看着的时候房间会重新排布，微缩
与真实之间的界线逐渐模糊。玩家必须解开跨越两种尺度的谜题，才能找到出路。

## 玩家体验流程

1. **标题画面** —— 一个分屏视图，一边是玩偶屋、一边是它的真实对应物，游戏名
   以稚拙的手写体呈现并往下流淌，还有一个开始按钮。
2. **真实房屋** —— 玩家以侧视视角在一栋黑暗的原尺寸房屋中移动。门被锁住，
   通道被堵塞，而且有什么地方不对劲——房间之间的连接不符合逻辑。
3. **玩偶屋** —— 在阁楼里发现的玩偶屋是真实房屋的微缩复制品。玩家可以放大
   查看并与微小物件交互：搬动家具、开门、拨动开关。
4. **镜像机制** —— 玩偶屋中的动作会影响真实房屋。移动微缩书架会在真实房屋中
   显露出一条通道。点亮一盏小台灯会照亮真实中的黑暗房间。锁上玩偶屋的一扇门
   会把某种东西困在真实房屋里。
5. **谜题推进** —— 每个房间都有一个需要跨两种尺度操作的谜题。玩家要在探索
   真实房屋与调整玩偶屋之间来回切换才能推进。
6. **玩偶屋的回应** —— 随着玩家推进，玩偶屋会自行发生变化：玩偶人形出现在
   玩家刚刚离开的房间里、家具自己移回原位、出现真实房屋中并不存在的新房间。
   调查这些异常会揭开恐怖的真相。
7. **逃脱** —— 最终谜题要求玩家同时操纵两种尺度才能打开前门。结局取决于玩家
   是否调查过那些异常房间，还是对它们视而不见。

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