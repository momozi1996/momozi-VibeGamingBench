# 恐怖灯塔（Horror Lighthouse）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个**恐怖灯塔**游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家是一名在无尽风暴中值守的灯塔看守人，必须维持灯光运转，引导船只安全绕过
礁石，而水中的某种东西却试图把它们引向岸边撞毁。游戏的幻想核心是孤独的职守
对抗宇宙级恐惧：光束是水手与死亡之间唯一的屏障，但让它亮着就会引来潜伏在
水下之物的注意。紧张感来自燃料管理、机械故障，以及那个生物一次比一次更凶猛的
企图——熄灭灯光，或者把看守人逼疯。

## 玩家体验流程

1. **标题画面** —— 一幅风暴中的海岸场景，灯塔光束在雨中扫过，游戏名采用饱经
   风霜的衬线字体，还有一个开始按钮。
2. **灯塔** —— 一个剖面视图，展示多个楼层：顶部的灯室、中部的居住舱、底部的
   燃料仓库，以及屋外的码头。玩家可以在楼层间移动。
3. **灯光维护** —— 灯会消耗燃料，并偶尔发生故障。玩家必须从下方的仓库补充
   燃料、在浪花糊住镜片时清洁它、在旋转机构卡死时进行修理。如果灯光熄灭，
   船只就会撞毁。
4. **船只引导** —— 船只会以远处灯火的形式出现在漆黑的海面上。玩家必须保持
   光束旋转以警告它们避开礁石。被成功引导的船只会安全通过；撞毁的船只则留下
   残骸与罪责。
5. **燃料管理** —— 燃料是有限的。补给船会定期前来，但风暴会延误它们。玩家
   必须节约用料，在全亮模式（安全但消耗很快）与昏暗模式（省燃料但船只可能
   看不见）之间做选择。
6. **那个生物** —— 水中的某种东西会前来干扰：触手伸向码头、生物发光的诱饵
   模仿船只灯火来迷惑看守人、低语试图说服玩家熄灭灯火。玩家必须抵抗它并
   修复损坏。
7. **逐步升级** —— 每一夜风暴都会更猛，燃料更加稀缺，那个生物也更加大胆。
   最后一夜要求玩家在一场正面袭击中让灯光持续燃烧，同时把最后一艘船引导至
   安全处。

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