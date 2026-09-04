# 长空决斗（Sky Duel）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Sky Duel**，一款 2D 空战游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

这里的幻想是驾驶一架灵巧的战斗机穿越开阔的天空，利用动量与重力在空战缠斗中
机动压制一波波敌机，让搏杀感觉像一场暴烈的舞蹈。有趣的张力来自物理驱动的运动：
飞机具有推力、阻力和重力，所以爬升会流失速度，而俯冲会积累速度。玩家必须管理
能量状态——用高度换速度，或反之——同时对那些利用同一套物理规则的敌人瞄准
射击。通过分数里程碑获得的可定制机体部件让玩家能按自己的风格调校操控性、
火力和生存力。

## 玩家体验流程

玩家进入游戏时看到一个机库标题画面，展示当前的飞机配装，随后升空进行一次出击。
飞机在一片 2D 侧视天空中飞行，边界可环绕或有界。推力通过一个按键施加；飞机用
左/右输入旋转，并始终受重力作用。开火会朝机头朝向发射子弹。敌机以编队入场，
每种都有独特的行为——俯冲轰炸机、盘旋王牌、重型武装飞艇。

摧毁敌人与完成目标可获得分数，在达到阈值时解锁新部件：提升推力的引擎升级、
带来更紧转弯的机翼形状、提供散射或追踪弹的武器吊舱、增加重量的装甲板。出击
之间，玩家在机库中装配部件。Boss 遭遇战会出现带多座炮塔与多攻击阶段的大型
飞行器。战役横跨 6 次以上出击，敌人种类不断增加，并加入风暴与高射炮塔等
环境危险。

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