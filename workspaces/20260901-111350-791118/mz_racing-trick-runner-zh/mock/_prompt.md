# 特技滑降跑者（Racing Trick Runner）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个特技滑降跑者游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款无尽下坡跑酷游戏，玩家在程序化变化的地形中劈波前行，借着坡道腾空做出空中
特技，以提升速度和分数。坡道永无尽头——挑战在于你能在摔车前跑多远。天气会从
晴朗转为暴风雪，白天循环到夜晚，地形也变得更陡、更险恶。特技是生存的关键：
它们会补满一条加速槽，让你能强行冲过平坦路段。可解锁的角色拥有不同的特技风格
与视觉花样，提供了长线目标。

## 玩家体验流程

1. **标题画面** —— 一幅雪山远景，游戏名称采用带霜感的风格化字体，一位剪影
   车手正在做后空翻，另有"开始"/"收藏"按钮。不要出现 HTML 引擎 的裸灰色。
2. **一轮滑降** —— 横向卷轴的无尽下坡。角色自动向坡下移动；玩家控制起跳时机、
   特技执行和落地角度。地形随视差山脉背景一同滚动。
3. **特技系统** —— 在空中时，玩家用方向键输入特技指令（翻转、旋转、抓板）。
   每个特技都有分值和时间代价。在特技后干净落地会奖励分数并补充加速。落地
   糟糕（角度不对）会导致一次踉跄，损失速度。
4. **加速机制** —— 加速槽由成功的特技填充。启动加速会大幅提升速度，并带有
   可见的尾迹特效。加速对于通过平坦路段和缺口至关重要。
5. **天气与昼夜** —— 一轮之中天况会变化：晴空转为浓雾（能见度降低），再转为
   降雪（地形滑溜），再转为暴风雪（两者兼有）。白天渐变为夜晚，能见度降低。
   每种天况对玩法和视觉的影响都各有区别。
6. **障碍与地形** —— 岩石、树木和冰裂缝会作为障碍出现。地形在平滑坡面、
   雪包坡、悬崖落差和坡道序列之间变化。撞上障碍物则本轮结束。
7. **角色收集** —— 至少 5 个可解锁角色，通过达成距离里程碑或分数目标获得。
   每个角色都有独特的精灵图、特技动画风格，以及一项特殊能力（跳得更高、
   加速更久、多一点生命值）。

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

交互方案（keyboard-first）：本题材以键盘交互为主：提供方向键或 WASD、Space、Enter、Esc 等清晰按键，并在自然需要时加入鼠标。
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