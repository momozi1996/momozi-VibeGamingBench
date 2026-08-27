// 参考实现（V-gamegen-bench 自测用）：3D 打砖块逻辑层
// 纯函数，不碰 DOM/渲染，可在 node 中直接 import 测试。

export const WALL_X = 9;
export const TOP_WALL = 9;
export const BOTTOM = 10;
export const BALL_R = 0.35;
export const BRICK_W = 2.0;
export const BRICK_H = 0.9;
export const BRICK_ROWS = 3;
export const BRICK_COLS = 6;
export const BASE_SPEED = 6;

export function createGame({ cols = BRICK_COLS, rows = BRICK_ROWS, lives = 3 } = {}) {
  const bricks = [];
  let id = 0;
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      bricks.push({
        id: id++,
        col: c,
        row: r,
        x: (c - (cols - 1) / 2) * (BRICK_W + 0.25),
        y: 7 - r * (BRICK_H + 0.25),
        hp: 1,
        speedMul: 1,
      });
    }
  }
  const ball = {
    x: 0,
    y: -8,
    vx: 2,
    vy: -3,
    speed: BASE_SPEED * 1.1,
  };
  return {
    bricks,
    ball,
    paddle: { x: 0, halfW: 2.5, y: -9 },
    score: 0,
    lives,
    state: 'serve', // serve | playing | paused | win | gameover
    boosts: [],     // {kind, expires}
    ballAlive: true,
  };
}

function normalize(vx, vy, speed) {
  const m = Math.hypot(vx, vy) || 1;
  return { vx: (vx / m) * speed, vy: (vy / m) * speed };
}

export function advance(game, action = {}, dt = 0.016) {
  const g = JSON.parse(JSON.stringify(game));
  if (action.type === 'toggle_pause') {
    g.state = g.state === 'paused' ? (g.ballAlive ? 'playing' : 'serve') : 'paused';
    return g;
  }
  if (g.state === 'paused' || g.state === 'gameover' || g.state === 'win') return g;

  // paddle 移动
  const dx = action.paddleDx || 0;
  g.paddle.x = clamp(g.paddle.x + dx * dt * 10, 0, WALL_X);

  if (g.state === 'serve') {
    if (action.launch) {
      const dir = g.paddle.x >= 0 ? -1 : 1;
      const u = normalize(dir * 1.6, -3.6, g.ball.speed);
      g.ball.vx = u.vx;
      g.ball.vy = u.vy;
      g.state = 'playing';
    }
    return g;
  }

  // playing
  const b = g.ball;
  b.x += b.vx * dt;
  b.y += b.vy * dt;

  // 左右墙
  if (b.x < -WALL_X + BALL_R) { b.x = -WALL_X + BALL_R; b.vx = Math.abs(b.vx); }
  if (b.x > WALL_X - BALL_R)  { b.x = WALL_X - BALL_R;  b.vx = -Math.abs(b.vx); }
  // 顶墙
  if (b.y > TOP_WALL - BALL_R) { b.y = TOP_WALL - BALL_R; b.vy = -Math.abs(b.vy); }

  // paddle
  const p = g.paddle;
  const speed = b.speed || BASE_SPEED;   // 兼容缺 speed 的构造态
  if (b.vy < 0 && b.y - BALL_R <= p.y && b.y > p.y - 1 && Math.abs(b.x - p.x) < p.halfW) {
    const v = normalize(b.vx + (b.x - p.x) * 1.5, Math.abs(b.vy) * 1.02, speed);
    b.vx = v.vx; b.vy = v.vy;   // 反弹永远向上（vy>0）
    b.y = p.y + BALL_R;
  }

  // 掉出底部
  if (b.y < -BOTTOM) {
    g.lives -= 1;
    if (g.lives <= 0) {
      g.lives = 0; g.state = 'gameover';
    } else {
      g.state = 'serve';
      b.x = 0; b.y = -8; b.vx = 2; b.vy = -3;
    }
    return g;
  }

  // 砖块
  for (const br of g.bricks) {
    if (br.hp <= 0) continue;
    const inX = Math.abs(b.x - br.x) <= BRICK_W / 2 + BALL_R;
    const inY = Math.abs(b.y - br.y) <= BRICK_H / 2 + BALL_R;
    if (inX && inY) {
      br.hp -= 1;
      g.score += 10 * (g.speedMulScore || 1);
      // 击穿方向决定反弹轴
      if (Math.abs(b.y - br.y) * BRICK_W > Math.abs(b.x - br.x) * BRICK_H) {
        b.vy = -b.vy;
      } else {
        b.vx = -b.vx;
      }
      if (br.hp <= 0) gameAliveCheck(g);
      break;
    }
  }
  gameAliveCheck(g);
  return g;
}

function gameAliveCheck(g) {
  if (g.bricks.every(b => b.hp <= 0)) g.state = 'win';
}

function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }

// 计分与加速道具（R2 增量）
export function addSpeedBoost(game, seconds = 5) {
  const g = JSON.parse(JSON.stringify(game));
  g.boosts.push({ kind: 'speed', expires: seconds });
  g.ball.speed = BASE_SPEED * 1.5;
  return g;
}
