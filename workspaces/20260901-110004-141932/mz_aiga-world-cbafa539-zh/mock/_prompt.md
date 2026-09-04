# 锈落边境

制作一个完整可玩的 **3D 策略游戏**，以
**第三人称** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

一名废土幸存者通过管理资源、缔结联盟、保卫聚落和对抗敌对势力建立领袖声望。

## 世界参数

把它作为原创的 **末日废土** 共享世界改写，范围为 **超大型**，叙事基调为 **响应式**。不得复刻商业角色、名称、设定、标志或受保护的视觉设计。

## 必须实现的可玩系统

1. **系统 1** - 探索《锈落边境》中的至少三个相连城区或领地，每处都有不同机会、危险和归属状态。
2. **系统 2** - 通过谈判、贸易、战术冲突或服务完成差事，并用透明规则获得或失去声望。
3. **系统 3** - 管理至少三个派系，其信任、敌意、联盟和控制权会在玩家选择后持续变化。
4. **系统 4** - 平衡健康、资源、影响力和警觉度，领地事件会在玩家不介入时继续演化。
5. **系统 5** - 在整局中持续保存声望、派系关系、占有或保护地点、消耗资源与未解决后果。
6. **系统 6** - 抵达同时检验领地、派系、资源和声望系统的可玩影响力里程碑，并支持继续游玩或计分结局。

## 推进与持久状态

使用三个阶段组成短流程：先清楚引入中心交互，再与世界压力和有意义选择组合，最后用
综合场景检验掌握程度。重要规则、目标、资源、关系、选择状态、危险、进度和结果必须
显示在稳定 HUD 区域，并在 `game_logic.js` 中有对应状态。各系统必须通过共享状态
互相影响，不能只是彼此割裂的按钮、菜单或视觉演示。

## 美术方向

战术场地便于扫视，单位定位、范围与归属清楚；特效保持克制，信息层级支持连续决策。

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