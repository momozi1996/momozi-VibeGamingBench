// 市场模拟（参考实现）：items_n / start_cash
export function createGame({ items_n=5, start_cash=1000 } = {}) {
  return {
    cash: start_cash,
    items: Array.from({ length: items_n }, (_, i) => ({ id: i, price: 10 + i * 5, qty: 0 })),
    state: 'ok',
    last_op_rejected: false,
  };
}
export function advance(game, input = {}) {
  const g = JSON.parse(JSON.stringify(game));
  if (g.state === 'halt') return g;
  const item = g.items.find(i => i.id === input.item);
  if (!item || !['buy', 'sell'].includes(input.op) || input.qty <= 0) {
    g.last_op_rejected = true;
    return g;
  }
  const cost = item.price * input.qty;
  if (input.op === 'buy' && g.cash < cost) { g.last_op_rejected = true; return g; }
  if (input.op === 'sell' && item.qty < input.qty) { g.last_op_rejected = true; return g; }
  if (input.op === 'buy') { g.cash -= cost; item.qty += input.qty; item.price += input.qty; }
  else                     { g.cash += cost; item.qty -= input.qty; item.price = Math.max(1, item.price - input.qty); }
  return g;
}
