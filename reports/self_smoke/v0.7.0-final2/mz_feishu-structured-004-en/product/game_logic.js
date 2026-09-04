(function (root) {
  function createGame(opts) {
    opts = opts || {};
    return {
      phase: "title",
      score: 0,
      goal: 5,
      lives: 3,
      elapsed: 0,
      seed: Number(opts.seed || 20260904),
      actions: 0,
      lastAction: ""
    };
  }
  function advance(game, input, dt) {
    input = input || {};
    dt = Math.max(0, Math.min(0.25, Number(dt) || 0));
    if (input.action === "restart") return Object.assign(game, createGame({ seed: game.seed }));
    if (input.action === "start" && (game.phase === "title" || game.phase === "win" || game.phase === "lose")) {
      game.phase = "playing"; game.elapsed = 0; game.actions = 0; game.score = 0; game.lives = 3; return game;
    }
    if (input.action === "pause" && (game.phase === "playing" || game.phase === "paused")) {
      game.phase = game.phase === "playing" ? "paused" : "playing"; return game;
    }
    if (game.phase !== "playing") return game;
    game.elapsed += dt;
    if (input.action && ["pointer","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"," ","w","a","s","d"].includes(input.action)) {
      game.actions += 1; game.score = Math.min(game.goal, game.actions); game.lastAction = input.action;
    }
    if (game.actions >= game.goal) game.phase = "win";
    else if (game.elapsed > 45) { game.lives = 0; game.phase = "lose"; }
    return game;
  }
  var api = { createGame: createGame, advance: advance };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== "undefined" ? window : globalThis));
