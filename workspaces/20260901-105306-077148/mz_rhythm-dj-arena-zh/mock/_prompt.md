# 节奏 DJ 竞技场（Rhythm DJ Arena）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一个节奏 DJ 竞技场游戏。
这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为
纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

两名音乐斗士在霓虹舞台上对峙，用节奏性的攻击展开一场节拍之战。每名斗士都有
一条音符轨道；击中音符可以为特殊技能充能，充满后会化作音乐弹幕横穿竞技场
发射出去。对手必须闪避，或用自己已充能的技能反制。游戏的幻想核心是一场 DJ
对战——音乐技巧直接转化为战斗力：完美连击会释放毁灭性的低音炸弹，而漏掉的
音符则让你门户大开。多名拥有截然不同音乐风格和招式组合的角色带来丰富变化。

## 玩家体验流程

1. **标题画面** —— 鲜艳的霓虹夜店美学，游戏名采用发光的涂鸦风字体，配有
   角色选择和对战模式按钮，背景是动态的均衡器条。演出 GameX其灰色。
2. **角色选择** —— 至少 4 名可玩角色，各有独特的音乐主题（电子、摇滚、爵士、
   嘻哈）、独特的精灵图设计和不同的特殊招式组合。选中每个角色时会显示一段
   预览动画及其招式列表。
3. **分屏轨道** —— 屏幕一分为二：每一侧都有一条 3 轨的音符轨道。玩家在自己
   那侧击中音符以积攒充能量表。AI 对手同时在自己的轨道上演奏。
4. **充能与攻击** —— 当充能量表达到某个阈值时，玩家可以消耗它发动一次音乐
   攻击（低音波、高音尖刺、和弦冲击）。攻击会横穿竞技场朝对手飞去。充能越强
   （来自更高的连击）产生的攻击就越强力。
5. **防御与闪避** —— 对手可以在弹幕抵达的瞬间按键闪避，或者硬吃伤害（损失
   生命值）。每次成功命中都会削减血条。先归零的一方输掉本回合。
6. **三局两胜** —— 比赛采用 3 局 2 胜制。回合之间有一段简短的间奏，显示得分
   并让下一回合的速度提升。
7. **街机模式** —— 一条难度递增的 AI 对手阶梯，每个对手的音符模式更快、攻击
   使用更具侵略性。击败所有对手会显示该角色专属的胜利画面。

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