# 辩论社（Debate Club）

用单文件 HTML 双击即开方式交付两个文件（`index.html`、`game_logic.js`） 开发 **Debate Club**——一款
**辩论与矛盾点视觉小说**。这不是原型，而是一个**完整、可发布的微型游戏**——
其打磨程度应当足以作为纵向切片放到 itch.io 页面或 Steam 上。

## 核心构想

玩家扮演一名学生调查者，必须在正式辩论中把证据射向自相矛盾的陈述，以此揭穿
谎言。嫌疑人会在结构化的论辩中提出主张，玩家必须判断哪一句陈述与收集到的证据
相矛盾，然后在恰当的时机呈上正确的证明。张力来自时机与精准：陈述会滚动而过，
提出异议的窗口很短，而错误的异议会损伤玩家的声望分。多名嫌疑人、多轮辩论层层
推进，最终指向真正的凶手。整体调性是学术惊悚：校园长廊、正式讲台、锋利的对白，
以及当场抓住某人说谎时的那股快感。

## 玩家体验流程

从标题画面开始，玩家进入调查阶段。他们探索各个地点（教室、图书馆、庭院），
点击热点来收集证据卡——每张卡都有一条事实、一个来源和一个关联性标签。收集证据
就是为辩论所做的准备。

辩论阶段是核心玩法。嫌疑人轮流发表陈述，以滚动的文字面板呈现。玩家聆听（阅读）
并留意矛盾点——即与已收集证据冲突的陈述。一旦发现，玩家就选中对应的证据卡，
把它作为一枚"真相子弹"射向那句矛盾的陈述。

命中正确会触发一段戏剧性的击破演出：陈述碎裂，嫌疑人语塞，新的信息随之揭晓。
命中错误则要付出声望点数——损失过多，这场辩论就输了。击破一个矛盾点之后，
辩论会推进到一个主张更难对付的新阶段。

跨越不同嫌疑人的多轮辩论逐步构建起整个案件。最后一轮要求玩家从累积的证据中
指认凶手。一个有设计感的结算画面会展示判决、声望分和证据准确率。

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