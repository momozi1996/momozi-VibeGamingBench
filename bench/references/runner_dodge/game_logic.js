// 跑酷躲避（参考实现）：lanes / gravity / jump_v / speed
export function createGame({ lanes=3, gravity=20, jump_v=9, speed=6 } = {}) {
  return {
    lanes, gravity, jump_v, speed,
    lane: 0,
    player: { y: 1, vy: 0, jumping: false },
    obstacles: [],
    gap: 5,
    lives: 3,
    score: 0,
    state: 'playing',
  };
}

export function advance(game, input = {}, dt = 1/60) {
  const g = JSON.parse(JSON.stringify(game));
  if (g.state !== 'playing') return g;
  const j = Math.sign(input.lane_dx || 0);
  g.lane = Math.max(-1, Math.min(1, g.lane + j));   // 三车道 -1..1
  if (input.jump && !g.player.jumping) {
    g.player.vy = g.jump_v;
    g.player.jumping = true;
  }
  // 重力下落
  g.player.vy -= g.gravity * dt;
  g.player.y += g.player.vy * dt;
  if (g.player.y <= 1) {
    g.player.y = 1; g.player.vy = 0; g.player.jumping = false;
  }
  g.score += dt * 2;
  // 障碍：固定在 lane 0；命中判据=玩家也在 lane 0
  g.obstacles = [{ lane: 0, x: 30, y: 0 }];
  const hit = g.obstacles.some(o => o.lane === g.lane);
  if (hit) g.lives -= 1;
  return g;
}
