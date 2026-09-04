# 尖塔牌组远征

制作一个完整可玩的 **2D 策略游戏**，以
**俯视角** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

围绕带能量的回合制卡牌战斗、多个角色职业、遗物收集系统、程序化三幕地图构建原创且连贯的玩法闭环。各系统必须通过共享状态互相影响，不能只是彼此
割裂的按钮、菜单或视觉演示。

## 必须实现的可玩系统

1. **核心机制 A - 带能量的回合制卡牌战斗**：让玩家能够直接操控或进行策略决策；状态变化必须
   确定，反馈清晰，并能观察到成功与失败后果。
2. **核心机制 B - 多个角色职业**：与第一项机制连接，使玩家决策能够改变时机、位置、
   资源、风险或可用选项。
3. **核心机制 C - 遗物收集系统**：实现从输入到结果的完整流程，包括无效操作、边界
   条件以及恢复或重置行为。
4. **核心机制 D - 程序化三幕地图**：必须实质改变策略、成长或重玩结果，不能只是标签
   或装饰状态。
5. **支撑系统**：从以下机制签名中至少实现四项，并接入核心循环：资源与行动经济；单位、卡牌或建筑克制；地图控制与视野；对手 AI 决策；升级或科技路线；明确的范围和预览；多阶段局势升级；完整胜负条件。
6. **内容广度与结果**：至少加入三种单位、卡牌、建筑或政策定位，一个会响应玩家的对抗系统、资源取舍、逐步升级的局势，以及完整胜负闭环。

## 成长与状态

使用三个阶段组成短流程：先清楚引入核心交互，再在更高压力下组合支撑系统，最后用综合
场景检验掌握程度。重要规则、资源、目标、选择状态、进度、危险与结果必须显示在稳定的
HUD 区域，并在 `game_logic.js` 中有对应状态。

## 美术方向

战术场地应便于扫视，单位定位、范围和归属清楚；特效保持克制，信息层级支持玩家连续决策。

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