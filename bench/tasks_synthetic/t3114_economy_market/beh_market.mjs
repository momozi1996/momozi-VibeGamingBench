// 市场模拟：B 维度确定性行为套件
// contract: createGame({items_n,start_cash}) / advance(game,{op,item,qty})
import { pathToFileURL } from 'node:url';
const dir = process.argv[2]; const out = [];
const rec = (id, ok, detail) => out.push({ id, ok, detail });
let G;
try { G = await import(pathToFileURL(`${dir}/game_logic.js`).href); }
catch (e) { rec('load', false, e.message); console.log(JSON.stringify(out)); process.exit(0); }

rec('contract', typeof G.createGame === 'function' && typeof G.advance === 'function', 'export ok');
const mk = (o) => G.createGame({ items_n: 5, start_cash: 1000, ...(o || {}) });
const play = (s, seq) => seq.reduce((acc, inp) => G.advance(acc, inp), s);

// M1: 现金恒非负
{
  const g = play(mk(), [
    { op: 'buy', item: 0, qty: 3 },
    { op: 'sell', item: 0, qty: 1 },
    { op: 'buy', item: 1, qty: 2 },
  ]);
  rec('M1_cash_nonneg', g.cash >= 0, `cash=${g.cash}`);
}
// M2: 库存恒非负
{
  const g = play(mk(), [
    { op: 'buy', item: 0, qty: 5 },
    { op: 'sell', item: 0, qty: 5 },
  ]);
  rec('M2_stock_nonneg', Array.isArray(g.items) && g.items.every(i => i.qty >= 0),
      `qty=${g.items.map(i => i.qty)}`);
}
// M3: 买入抬价（需求 → 价格单调不减）
{
  const g0 = mk();
  const g = G.advance(g0, { op: 'buy', item: 0, qty: 5 });
  rec('M3_demand_raises_price', g.items[0].price >= g0.items[0].price,
      `${g0.items[0].price} -> ${g.items[0].price}`);
}
// M4: 非法 op 拒绝并留证据
{
  const g = G.advance(mk(), { op: 'steal', item: 0, qty: 1 });
  rec('M4_reject_bad_op', g.last_op_rejected === true, `state=${g.state}`);
}
// M5: 同一序列必同一结果（纯度）
{
  const g1 = play(mk(), [{ op: 'buy', item: 0, qty: 2 }, { op: 'sell', item: 0, qty: 1 }]);
  const g2 = play(mk(), [{ op: 'buy', item: 0, qty: 2 }, { op: 'sell', item: 0, qty: 1 }]);
  rec('M5_purity', JSON.stringify(g1) === JSON.stringify(g2), JSON.stringify(g1) === JSON.stringify(g2) ? 'deterministic' : 'DIFFERS');
}
console.log(JSON.stringify(out));
