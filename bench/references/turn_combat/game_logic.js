// 回合制战斗（参考实现）：n_units / base_hp / base_atk
export function createGame({ n_units=4, base_hp=10, base_atk=3 } = {}) {
  const units = Array.from({ length: n_units }, (_, i) => ({
    id: i, hp: base_hp, max_hp: base_hp, atk: base_atk, alive: true,
  }));
  return { units, base_atk, base_hp, turn: 1, state: 'playing', last_op_rejected: false };
}
export function advance(game, input = {}) {
  const g = JSON.parse(JSON.stringify(game));
  if (g.state !== 'playing') return g;
  const actor = g.units.find(u => u.id === input.actor_id);
  const target = g.units.find(u => u.id === input.target_id);
  if (!actor || !target || !actor.alive || !target.alive || actor.id === target.id) {
    g.last_op_rejected = true;
    return g;
  }
  g.last_op_rejected = false;
  target.hp = Math.max(0, target.hp - actor.atk);
  if (target.hp === 0) target.alive = false;
  const a1 = g.units[0].alive, a2 = g.units.slice(1).every(u => !u.alive);
  if (a1 && a2) g.state = 'pvp_end';
  g.turn += 1;
  return g;
}
