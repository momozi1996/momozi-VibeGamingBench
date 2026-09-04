# 越野爬坡竞速（Racing Terrain Climb）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个越野爬坡竞速游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一款横向卷轴物理载具游戏，玩家驾车翻越崎岖地形，管理动量与燃油以抵达尽可能远的
距离。载具会在山丘与谷地上弹跳、倾斜、翻滚——在陡坡上油门给太猛会向后翻车；
给太小则会在坡上熄火停住。燃油有限，在检查点补充，从而在速度与节省之间制造出
张力。赚到的金币可以购买载具升级（引擎功率、悬挂、油箱容量）和新的载具类型，
每种都有不同的物理属性。这里的幻想是通过聪明的驾驶和一点点的改良，征服不可能的
地形。

## 玩家体验流程

1. **标题画面** —— 一幕粗粝的户外场景，游戏名称采用粗厚的方块字母，一辆载具的
   剪影在夕阳天空前腾空跃起，另有"开始"/"车库"按钮。不要出现 HTML 引擎 的裸灰色。
2. **关卡选择** —— 多种地形环境（乡间丘陵、月球表面、极地冰原、沙漠沙丘），
   每种都有独特的物理属性（摩擦力、重力）。关卡通过达到距离里程碑来解锁。
3. **驾驶物理** —— 载具具有真实的 2D 物理：车轮抓紧地形，底盘随坡度角度倾斜，
   动量会越过坡顶延续下去。玩家控制油门（右方向键）和刹车（左方向键），外加
   倾斜（上/下方向键）以在空中调整载具角度。
4. **燃油管理** —— 油量表随玩家行驶而下降。耗尽后载具会停下。燃油罐会间隔地
   出现在路线沿途。在开快（烧油）与省油之间的张力，造就了有意义的决策。
5. **金币与距离** —— 金币散布在地形沿途，收集可获得货币。距离作为最高分被记录。
   每一轮在燃油耗尽或载具被毁（车顶着地）时结束。
6. **车库/升级** —— 在两轮之间，玩家花金币购买升级：引擎功率、油箱容量、
   悬挂硬度、轮胎抓地力。至少有 3 种不同的载具类型（吉普车、摩托车、
   怪兽卡车），拥有明显不同的精灵图和操控特性。
7. **距离记录** —— 一个持久化的排行榜显示每个关卡的最远距离。打破个人记录会
   触发一段庆祝特效。

## Vibe Gaming Quality Bar

本题的玩法、逻辑和验收锚点优先于下面的表达规范。不要重写或删减上面的核心
机制；这些要求用于把同一玩法稳定地落成一个可玩的 Vibe Gaming 垂直切片。

- **先玩后美化**：先保证开始、核心输入、状态变化、成功/失败和重玩闭环，再做视觉与动效。
- **技术栈按玩法选最小充分方案**：
  - 2D 规则游戏优先 `HTML5 Canvas 2D + Vanilla JS`；
  - 面板、卡牌、对话和菜单密集时可用 `DOM + CSS + Vanilla JS`；
  - 图标、线稿和几何动画可用 `纯 SVG + CSS 动画 + Vanilla JS`；
  - 连续碰撞、镜头、粒子或街机物理可用 `PhaserJS`；
  - 3D 或空间镜头可用 `Three.js + WebGL`；
  - 只有确实需要 GPU 大规模并行或自定义 GPU 管线时才用原生 `WebGPU`；
  - 可以混合 Canvas、DOM、CSS、SVG，但必须明确每层职责，禁止为了“技术炫技”增加无关复杂度。
- **规则层独立**：`game_logic.js` 保存唯一真相，暴露 `createGame(opts)` 和
  `advance(game, input, dt)`；渲染层只读取状态并呈现，不能偷偷维护第二套规则。
- **每帧可解释**：输入要映射到明确动作，动作要产生可观察状态变化；无效输入、
  边界条件、资源耗尽、受伤、胜利和失败都要有反馈。
- **Vibe 不是装饰**：至少使用两种反馈通道（动画、位移、缩放、粒子、声音、
  HUD 或镜头）表达关键动作；反馈不能遮挡目标或破坏可读性。
- **移动端优先**：关键点击目标至少 44×44 CSS px，支持触摸和鼠标，不能依赖 hover；
  390×844、360×800、430×932 和 1280×800 不得横向滚动或出现控件重叠。
- **确定性与测试**：随机内容使用 seed；至少验证核心规则、胜负条件、重开/恢复、
  输入边界和一个异常状态；不要用截图存在或文字出现冒充功能完成。
- **原创与合规**：使用原创名称、角色、图形、音效和关卡，或明确许可的素材；
  不复制任何原作商标、角色、文本、美术、音乐、关卡数据或代码。

完成后报告：实际文件路径、启动命令、测试命令与结果、关键截图、已知限制、
技术栈取舍和原创资产来源。

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