# 圣巢容器（Vessel of Hallownest）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发一款 **2D 氛围类银河恶魔城平台动作游戏**。这不是原型，而是一个**完整、可发布的微型游戏**——其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

一位沉默的虫族骑士深入一座荒废的地下王国，随身只有一把骨钉和一股继续向前的意志。这里的幻想是压力之下的探索：每个房间都可能藏着新的威胁或一条回家的近道，而玩家永远在进攻与生存之间权衡。战斗迅捷且严苛——每一次挥砍都会补充驱动治疗的灵魂，因此站着不动就等于慢慢死去。有意思的张力在于资源循环逼迫你参战：你靠战斗来治疗，但战斗又会危及你正试图恢复的生命。进度把世界锁在前面区域中获得的能力之后，用通行权而不是数值来奖励熟练。整体调性阴郁、荒凉而美得悲怆——寒冷的地下废墟、在寂静中飘散的发光粒子，以及一个早已陨落的王国那份沉默的重量。

## 玩家体验流程

一个忧郁的标题画面以游戏名和一道孤独的骑士剪影迎接玩家，随后他们选择开始新旅程或继续已保存的旅程。

王国地图出现——一张由具名关卡组成、向下延伸的网络，每个关卡都锁着，直到它前面的那个被攻克。玩家选择第一个开放的关卡并落入其中。在里面，世界是一条由相连房间构成的连续横向滚动走廊：平台从洞穴壁上探出，荆棘坑铺在地面，感染的空壳在岩架上巡逻。移动手感紧凑而灵敏——骑士平顺加速，以令人满足的弧线跳跃，能贴附墙面，并能冲刺穿过要求精确的间隙。

战斗是即刻而切身的。挥砍敌人会使其硬直、喷出吉欧货币，并填充灵魂槽。受到打击会损失一个面具的生命，并触发短暂的无敌闪光。当面具剩得不多时，玩家面对核心困境：站着不动把灵魂引导为治疗——脆弱、暴露——还是继续向前，指望下一次击杀能补足到活下来。敌人守着房间出口后方的灵魂屏障，只有当房中每一个空壳都死掉时屏障才会升起。

更深处的房间要求用贴墙和冲刺来跨越骑士无法单靠跳跃通过的深渊。抵达一个关卡的尽头会触发一个保存进度并在地图上解锁下一区域的检查点。死亡代价高昂——所有随身携带的吉欧都会掉在失败地点，骑士则返回地图重新尝试。

最后一个关卡是一间 Boss 房：一头带有预示动作攻击套路的巨大生物，考验玩家学到的一切。胜利为这一轮加冕；失败则让骑士只带着经验退回。

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