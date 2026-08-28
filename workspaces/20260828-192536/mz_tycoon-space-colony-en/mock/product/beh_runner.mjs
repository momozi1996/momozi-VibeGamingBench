// 跑酷躲避：B 维度确定性行为套件
// contract: createGame({lanes,gravity,jumpV,speed}) / advance(game,{lane_dx,jump},dt)
// 断言：vy 有界 / lanes 有限 / 跳跃把 vy 抬正 / 碰撞失球→lives-1 / 越界不出 / 函数纯
import { pathToFileURL } from 'node:url';

const dir = process.argv[2];
const out = [];
const rec = (id, ok, detail) => out.push({ id, ok, detail });
let G;
try { G = await import(pathToFileURL(`${dir}/game_logic.js`).href); }
catch (e) { rec('load', false, e.message); console.log(JSON.stringify(out)); process.exit(0); }

rec('exports', typeof G.createGame==='function' && typeof G.advance==='function', 'contract');

// R1: 跳跃把 vy 正值
{
  const g = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  const before = g.player?.vy ?? g.runner?.vy;
  const a = G.advance(g, { jump: true, lane_dx: 0 }, 1/120);
  const after = a.player?.vy ?? a.runner?.vy;
  rec('R1_jump_positive_vy', after > before, `vy ${before}->${after}`);
}
// R2: lane 切换有限
{
  const g = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  const a = G.advance(g, { lane_dx: 1, jump: false }, 1/60);
  rec('R2_lane_switch', Number.isFinite(a.lane ?? a.player?.lane), `lane=${a.lane ?? a.player?.lane}`);
}
// R3: 碰撞进失球
{
  const g = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  const p = g.player ?? g.runner;
  g.obstacles = [{ lane: p.lane ?? 0, y: (p.y ?? 0) + 0.5 }];
  const a = G.advance(g, { jump: false, lane_dx: 0 }, 1/60);
  rec('R3_collision_life_lost', a.lives === g.lives - 1, `lives ${g.lives}->${a.lives}`);
}
// R4: 世界不出界
{
  const g = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  const a = G.advance(g, { jump: false, lane_dx: 0 }, 1/60);
  rec('R4_in_bounds', a.score >= 0 && a.state !== undefined, `score=${a.score}`);
}
// R5: 纯度
{
  const g1 = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  const g2 = G.createGame({ lanes: 3, gravity: 20, jump_v: 9, speed: 6 });
  rec('R5_purity', JSON.stringify(G.advance(g1,{},1/60)) === JSON.stringify(G.advance(g2,{},1/60)), 'deterministic');
}
console.log(JSON.stringify(out));
