// 行为套件：对 L1 逻辑层做确定性回归断言。
// 用法: node <workspace>/beh_behavior.mjs <workspace_dir>
// stdout: JSON [{id, ok, detail}...]  —— harness 统计通过率与回归。
import { pathToFileURL } from 'node:url';

const artifact = process.argv[2];
if (!artifact) { console.log(JSON.stringify([{ id: 'args', ok: false, detail: 'missing workspace arg' }])); process.exit(1); }

const results = [];
const rec = (id, ok, detail) => results.push({ id, ok, detail });

let G;
try {
  G = await import(pathToFileURL(`${artifact}/game_logic.js`).href);
} catch (e) {
  rec('load_logic', false, `import failed: ${e.message}`);
  console.log(JSON.stringify(results));
  process.exit(0);
}

rec('exports_createGame', typeof G.createGame === 'function', 'createGame');
rec('exports_advance', typeof G.advance === 'function', 'advance');

function freshGame() {
  const g = G.createGame({ cols: 6, rows: 3, lives: 3 });
  g.state = 'playing'; // 直接进入 gameplay（跳过发球态）
  return g;
}

// ---- B0: 发球态不动球 ---------------------------------------------
{
  const g = G.createGame({ cols: 6, rows: 3, lives: 3 });
  const before = JSON.stringify(g.ball);
  const after = G.advance(g, { paddleDx: 0, launch: false }, 1 / 60);
  rec('B0_serve_holds', JSON.stringify(after.ball) === before, 'ball frozen in serve');
}

// ---- B1: 球碰 paddle 反弹（y 从 paddle 上方进入挡板平面，须 vy 变正）----
{
  const g = freshGame();
  const py = g.paddle.y;
  g.ball = { x: g.paddle.x, y: py + G.BALL_R - 1 / 120, vx: 0, vy: -3, r: G.BALL_R }; // 差一拍过拍
  const after = G.advance(g, { paddleDx: 0, launch: false }, 1 / 60);
  rec('B1_paddle_bounce', after.ball.vy > 0 && Math.abs(after.ball.vx) <= 5,
    `vy ${g.ball.vy}->${after.ball.vy}, y ${after.ball.y.toFixed(2)}`);
}

// ---- B2: 侧墙 x 反弹 -------------------------------------------------
{
  const g = freshGame();
  const W = (G.WALL_X || 9) - G.BALL_R;  // -0.35 = 8.65
  g.ball = { x: W + 0.05, y: 0, vx: 3, vy: 0, r: G.BALL_R };   // 向右撞墙，应弹回
  const after = G.advance(g, { paddleDx: 0, launch: false }, 1 / 60);
  rec('B2_wall_bounce', after.ball.vx < 0 && after.ball.x <= W + 0.01,
    `ball in x-range: ${after.ball.x <= W + 0.01}, vx now ${after.ball.vx}`);
}

// ---- B3: 砖块碰撞 → hp-1 & score += 10 &  vy 反向 ------------------
{
  const g = freshGame();
  const br = g.bricks[0];
  g.ball = { x: br.x, y: br.y, vx: 0, vy: 3, r: G.BALL_R };
  const after = G.advance(g, { paddleDx: 0, launch: false }, 1 / 60);
  rec('B3_brick_hit',
    after.score === g.score + 10 && after.ball.vy < 0,
    `score ${g.score}->${after.score}, brick0.hp ${br.hp}->${after.bricks[0].hp}, vy ${after.ball.vy}`);
}

// ---- B4: 球掉出底界 → lives-1 & 不进 win ------------------------------
{
  const g = freshGame();
  g.ball = { x: 0, y: -60, vx: 0, vy: -5, r: G.BALL_R };
  const after = G.advance(g, { paddleDx: 0, launch: false }, 1 / 60);
  rec('B4_ball_lost', after.lives === g.lives - 1 && after.state !== 'win',
    `lives ${g.lives}->${after.lives}, state ${after.state}`);
}

// ---- B5: 动作契约 —— paddleDx 到位 clamp & toggle pause --------------
{
  const g = freshGame();
  const moved = G.advance(g, { paddleDx: 2, launch: false }, 1 / 60);
  rec('B5_paddle_move', Number.isFinite(moved.paddle.x), `paddle.x ${moved.paddle.x.toFixed(2)}`);
  const p1 = G.advance(G.createGame(), { type: 'toggle_pause' }, 1 / 60);
  const p2 = G.advance(p1, { type: 'toggle_pause' }, 1 / 60);
  rec('B5_pause_toggle', p1.state === 'paused' && p2.state !== 'paused',
    `state serve->${p1.state}->${p2.state}`);
}

// ---- B6: 函数纯度：同一输入两调用结果相同 -----------------------------
{
  const g1 = freshGame();
  const g2 = freshGame();
  const a1 = G.advance(g1, { paddleDx: 0.5, launch: false }, 1 / 60);
  const a2 = G.advance(g2, { paddleDx: 0.5, launch: false }, 1 / 60);
  rec('B6_purity', JSON.stringify(a1) === JSON.stringify(a2), 'deterministic');
}

console.log(JSON.stringify(results));
