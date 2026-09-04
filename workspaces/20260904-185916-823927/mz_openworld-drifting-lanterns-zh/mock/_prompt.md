# 漂流群岛的灯塔守护者

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一款穿越与修复游戏：漂浮群岛上的引航灯正逐一熄灭。玩家驾驶小型滑翔器往返移动陆块，重新点亮导航网络，并在危险天气中维系孤立社区之间的联系。

## 必须实现的可玩系统

1. **系统 1** - 在至少五座漂流岛屿之间滑翔、攀爬和停靠；岛屿相对位置与可达路线会随时间变化。
2. **系统 2** - 通过镜片、燃料、校准和限时点火序列等实体机制修复并重燃灯塔。
3. **系统 3** - 利用已点亮的网络导航：活跃光束会揭示安全风道、隐藏岛屿和紧急路线。
4. **系统 4** - 通过探索、配送任务和环境穿越挑战收集燃料与维修材料。
5. **系统 5** - 使用转向、临时护盾、信号弹和快速维修，保护灯塔免受风暴与空中生物侵袭。
6. **系统 6** - 恢复贯穿群岛的完整航线，并完成最终风暴穿越；结果应体现哪些社区得到了连接。

## 成长与推进

升级滑翔翼、燃料箱、镜片和气象仪器可扩大航程，并进入更高、更快移动的岛屿。

## 美术方向

充满希望的天空奇幻风，包含绘画般云层、温暖灯火金、冷色风暴、微缩岛屿生态和优雅风流可视化。

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