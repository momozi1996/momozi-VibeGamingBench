export function createGame() {
  return { x: 0, state: "playing" };
}

export function advance(game, input = {}, dt = 1 / 60) {
  game.x = Math.max(-500, Math.min(500, game.x + (input.right ? 120 : 0) * dt));
  return game;
}
