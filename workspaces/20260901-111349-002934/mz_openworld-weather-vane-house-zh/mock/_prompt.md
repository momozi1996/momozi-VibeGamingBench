# 风向标宅邸的冬季条款

制作一个完整可玩的 **3D 开放世界冒险游戏**，交付为经过打磨的浏览器纵向切片。

## 核心构想

一场发生在庞大家族宅邸内外的冬季生存谜案。遗嘱宣读后，继承人被异常严寒困住；玩家必须探索宅邸、管理热量、观察家族日程，并找出究竟哪条遗嘱条款在控制天气。

## 必须实现的可玩系统

1. **系统 1** - 探索多层宅邸、温室、冰封庭院、佣人地道和风向标塔，并解锁捷径。
2. **系统 2** - 在燃料有限的情况下操作锅炉、通风口、壁炉、百叶窗和电路，管理各房间温度。
3. **系统 3** - 观察并询问家族成员；每发现一条条款，其日程、联盟和通行权限都会变化。
4. **系统 4** - 利用肖像、钥匙、法律文件、机械锁和环境温度状态解决继承谜题。
5. **系统 5** - 应对不断升级的严寒影响，如冻结门、脆裂地板、停电和外出时的暴风雪暴露。
6. **系统 6** - 抵达风向标机构，执行、重新解释或摧毁最终条款，形成不同家族结局。

## 成长与推进

找回条款并恢复供暖区可延长安全探索时间、揭示隐藏侧翼，并增加家族谈判筹码。

## 美术方向

冰雪哥特宅邸，以温暖烛光室内、蔓延冰蓝、黄铜供暖机械、彩窗和风驱雪效构成对比。

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