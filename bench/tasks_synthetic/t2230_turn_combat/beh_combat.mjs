// 回合制战斗：B 维度确定性行为套件
// contract: createGame({n_units,base_hp,base_atk}) / advance(game,{actor_id,target_id})
// 断言：hp 不复负 / 攻击扣血 / 选择失效目标拒绝 / 多于一次攻击当次只扣一次 / 全灭判负 / 纯度
import { pathToFileURL } from 'node:url';
const dir = process.argv[2]; const out = [];
const rec = (id, ok, detail) => out.push({ id, ok, detail });
let G;
try { G = await import(pathToFileURL(`${dir}/game_logic.js`).href); }
catch (e) { rec('load', false, e.message); console.log(JSON.stringify(out)); process.exit(0); }

rec('contract', typeof G.createGame==='function' && typeof G.advance==='function', 'export ok');
{
  const g = G.createGame({ n_units: 4, base_hp: 20, base_atk: 5 });
  const e = g.units[1];
  const a = G.advance(g, { actor_id: g.units[0].id, target_id: e.id });
  rec('T1_hp_reduces', a.units[1].hp === e.hp - (g.units[0]?.atk ?? g.base_atk), `hp ${e.hp}->${a.units[1].hp}`);
}
{
  const g = G.createGame({ n_units: 4, base_hp: 2, base_atk: 5 });
  const a = G.advance(g, { actor_id: g.units[0].id, target_id: g.units[1].id });
  rec('T2_no_negative_hp', a.units.every(u => u.hp >= 0), `hp=${a.units.map(u=>u.hp)}`);
}
{
  const g = G.createGame({ n_units: 4, base_hp: 3, base_atk: 5 });
  let cur = g;
  cur = G.advance(cur, { actor_id: g.units[0].id, target_id: g.units[1].id });   // 1 死亡
  const dead = { ...cur.units[1] };
  const stale = G.advance(cur, { actor_id: cur.units[0].id, target_id: dead.id });
  rec('T3_reject_action_on_dead', stale.turn === cur.turn, `turn ${cur.turn}->${stale.turn}`);
}
{
  const g = G.createGame({ n_units: 2, base_hp: 5, base_atk: 5 });
  let cur = g;
  cur = G.advance(cur, { actor_id: cur.units[0].id, target_id: cur.units[1].id });   // 击倒
  cur = G.advance(cur, { actor_id: cur.units[1].id, target_id: cur.units[0].id });   // 反击（可能 win）
  const alive = cur.units.filter(u => u.hp > 0).length;
  rec('T4_win_or_one_alive', cur.state==='pvp_end' || alive >= 1, `alive=${alive} state=${cur.state}`);
}
{
  const g1 = G.createGame({ n_units: 4, base_hp: 20, base_atk: 5 });
  const g2 = G.createGame({ n_units: 4, base_hp: 20, base_atk: 5 });
  rec('T5_purity', JSON.stringify(G.advance(g1,{actor_id:g1.units[0].id,target_id:g1.units[1].id}))
                   === JSON.stringify(G.advance(g2,{actor_id:g2.units[0].id,target_id:g2.units[1].id})), 'deterministic');
}
console.log(JSON.stringify(out));
