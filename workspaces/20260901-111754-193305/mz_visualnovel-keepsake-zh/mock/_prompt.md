# 遗物（Keepsake）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Keepsake**——一款静谧的记忆重构视觉
小说，讲述整理一位逝者遗物的故事。这不是原型，而是一个**完整、可发布的微型
游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

有人去世了，而你被托付去整理他留下的东西。一张褪色的照片、一封折叠的信、一枚
磨损的戒指、一本被撕掉一页的日记——每一件物品都承载着一段人生的碎片，而它们
并不会按顺序交出自己的含义。Keepsake 是一款**选择驱动的重构式视觉小说**，玩家
检视一位陌生人的遗物，一件一件、乱序地拼出这个人究竟是谁——以及时间随他一同
埋葬的那个静默秘密。

游戏的幻想内核是**从一个人留下的东西里拼出他的一生**。循环的核心是
**检视、追忆、串联、理解**——把一件遗物翻过来，听见它勾起的那段记忆，再把它
与你已经找到的东西拼合，直到一个隐藏的形状浮现出来。玩家选择的顺序，以及他们
如何解读逝者做过的某个含义暧昧的选择，塑造了他们最终抵达的理解。它应当让人
感觉像一件缓慢、温柔、忧郁的作品，有真切的情感重量，并且理解一段人生的方式
不止一种，而不是一份从头念到尾的线性讣告。

## 玩家体验流程

1. **精心编排的开场** —— 从一个有设计感的标题画面出发，玩家被交付了自己的
   任务——一个房间、一只箱子、一整段人生份量的物品要去整理——以一个静谧的插画
   场景配旁白建立起来，奠定基调，以及位于其中心的那份缺席。
2. **检视遗物** —— 玩家可以按自己喜欢的任意顺序选择拿起哪件物品，每件遗物都
   作为一件插画物品被检视，并揭示它所披露的那段记忆或往事碎片。这个满是遗物的
   房间是玩家按自己节奏逐步走完的，而不是一段固定的幻灯片。
3. **彼此串联的碎片** —— 每件被检视的遗物都会给玩家的认知添上一块被追忆起的
   碎片，而碎片之间彼此契合：一封信上的日期解释了一张照片，一件物品的缺席回答了
   先前的一个疑问。玩家会感受到一段人生正在乱序中被组装起来，而他们已经找到的
   东西会渲染下一块碎片的读法。
4. **理解方式的抉择** —— 随着图景逐渐拼合，玩家会来到需要解读的时刻——如何解读
   逝者做过的一个含义暧昧的决定、对一个秘密该信什么、是评判还是原谅。这些选项
   是审慎的、会被记住的，而玩家已揭开的内容会塑造哪些理解方式根本上是否可选。
5. **追忆的方式不止一种** —— 这件作品会收束为数个确实不同的收尾理解之一——一段
   被救赎的人生、一个出于善意被保守的秘密、一份静默的哀伤，或一个改写了一切的
   真相——每一个都通过玩家找到了哪些碎片、以及他们选择如何解读它们来抵达，并以
   精心编排、有设计感的结语呈现，点明他们所抵达的理解。玩家可以重新开始，抵达
   另一处。

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