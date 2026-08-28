// Sports Fishing Tournament — pure logic layer.
// No DOM, no THREE. createGame(opts) -> state, advance(game, input, dt) -> state.
// input = { down:{key:bool}, pressed:{key:bool} }; dt in seconds.
(function (global) {
  'use strict';

  // ---- seeded RNG (mulberry32) so runs are deterministic & testable ----
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // ---- static data ----
  var LAKES = {
    pond: { name: 'Mossback Pond', depth: 'shallow', difficulty: 1, tint: 0x6fae5e, time: 90,
      species: ['bluegill', 'bass', 'catfish'] },
    reservoir: { name: 'Stillwater Reservoir', depth: 'deep', difficulty: 2, tint: 0x4f7fb0, time: 100,
      species: ['walleye', 'trout', 'pike', 'bass'] },
    stream: { name: 'Ridgeline Stream', depth: 'cold', difficulty: 3, tint: 0x8fd3d0, time: 110,
      species: ['trout', 'salmon', 'pike', 'golden'] }
  };

  // species: min/max lbs, base value, preferred weather, rarity(0..1), trophy flag
  var SPECIES = {
    bluegill: { name: 'Bluegill', min: 0.3, max: 1.2, val: 6, weather: 'sunny', rarity: 0.0 },
    bass:     { name: 'Largemouth Bass', min: 1.0, max: 7.0, val: 14, weather: 'overcast', rarity: 0.15 },
    catfish:  { name: 'Channel Catfish', min: 2.0, max: 14.0, val: 12, weather: 'rainy', rarity: 0.1 },
    walleye:  { name: 'Walleye', min: 1.5, max: 8.0, val: 16, weather: 'overcast', rarity: 0.2 },
    trout:    { name: 'Rainbow Trout', min: 0.8, max: 5.0, val: 18, weather: 'rainy', rarity: 0.15 },
    pike:     { name: 'Northern Pike', min: 3.0, max: 18.0, val: 26, weather: 'overcast', rarity: 0.5 },
    salmon:   { name: 'Chinook Salmon', min: 6.0, max: 30.0, val: 40, weather: 'rainy', rarity: 0.7 },
    golden:   { name: 'Golden Dorado', min: 8.0, max: 40.0, val: 90, weather: 'rainy', rarity: 0.95 }
  };

  var WEATHERS = ['sunny', 'overcast', 'rainy'];
  var WEATHER_FX = { sunny: 0.7, overcast: 1.25, rainy: 1.4 }; // bite-rate multiplier
  var WEATHER_SHADE = { sunny: 'shade', overcast: 'surface', rainy: 'bottom' };

  // gear tiers: [rod, line, lure] each 0..3
  var RODS = [
    { name: 'Bamboo Rod', power: 1, cost: 0 },
    { name: 'Graphite Rod', power: 2, cost: 150 },
    { name: 'Carbon Pro', power: 3, cost: 400 }
  ];
  var LINES = [
    { name: 'Mono 8lb', strength: 1, cost: 0 },
    { name: 'Braid 15lb', strength: 2, cost: 120 },
    { name: 'Fluoro 30lb', strength: 3, cost: 320 }
  ];
  var LURES = [
    { name: 'Worm', match: 'bluegill', draw: 1, cost: 0 },
    { name: 'Crankbait', match: 'bass', draw: 2, cost: 100 },
    { name: 'Spinner', match: 'trout', draw: 2, cost: 100 },
    { name: 'Jig', match: 'catfish', draw: 2, cost: 130 },
    { name: 'Minnow', match: 'walleye', draw: 3, cost: 260 },
    { name: 'Spoon', match: 'pike', draw: 4, cost: 400 }
  ];

  // tournaments: a bracket is 3 rounds; each round has an opponent weight to beat.
  function makeBracket(seed) {
    var r = mulberry32(seed);
    var lakes = ['pond', 'reservoir', 'stream'];
    var targets = ['bluegill', 'bass', 'trout'];
    var rounds = [];
    var opps = ['Rusty Reel', 'Old Man Pike', 'The Legend'];
    for (var i = 0; i < 3; i++) {
      rounds.push({
        lake: lakes[Math.min(i, 2)],
        target: targets[i],
        opponent: opps[i],
        oppWeight: Math.round((12 + i * 14 + r() * 6) * 10) / 10,
        prize: [200, 500, 1200][i],
        beaten: false
      });
    }
    return rounds;
  }

  function weatherFor(round, elapsed) {
    // weather rotates every ~30s within a round
    return WEATHERS[Math.floor(elapsed / 30) % 3];
  }

  function createGame(opts) {
    opts = opts || {};
    var seed = opts.seed != null ? opts.seed : 1234567;
    var g = {
      screen: 'TITLE',
      seed: seed,
      rng: mulberry32(seed),
      money: opts.money != null ? opts.money : 300,
      round: 0,                // bracket round index 0..2
      bracket: makeBracket(seed),
      lake: null,
      gear: { rod: 0, line: 0, lure: 0 },
      ownedLures: [0],          // indices into LURES owned
      shopCursor: 0,            // 0=rod,1=line,2+=lures
      lakeCursor: 0,
      menuCursor: 0,
      // fishing session
      weather: 'sunny',
      elapsed: 0,               // round timer
      timeLeft: 0,
      totalWeight: 0,
      lastCatch: null,
      // fish sub-state
      phase: 'IDLE',            // IDLE,CAST,WAIT,HOOK,REEL,DONE
      phaseT: 0,
      biteT: 0,
      fish: null,
      tension: 0,
      distance: 0,             // 0..1 distance reeled in (1 = landed)
      logbook: {},             // species -> {count, best}
      logUnlocked: false,
      message: '',
      flash: 0
    };
    return g;
  }

  function resetRound(g) {
    var rd = g.bracket[g.round];
    g.lake = rd.lake;
    g.elapsed = 0;
    g.timeLeft = LAKES[g.lake].time;
    g.totalWeight = 0;
    g.lastCatch = null;
    g.phase = 'IDLE'; g.phaseT = 0; g.biteT = 0; g.fish = null;
    g.tension = 0; g.distance = 0;
    g.weather = 'sunny';
  }

  // ---- helpers ----
  function gearPower(g) {
    return RODS[g.gear.rod].power;
  }
  function gearStrength(g) {
    return LINES[g.gear.line].strength;
  }
  function lureMatchBonus(lureIdx, sp) {
    var l = LURES[lureIdx];
    return l.match === sp ? 1.5 : 1.0;
  }

  // roll a fish for the current lake/weather/gear
  function rollFish(g) {
    var r = g.rng;
    var lake = LAKES[g.lake];
    // weather skews which species bite
    var pool = lake.species.slice();
    var weights = pool.map(function (s) {
      var sp = SPECIES[s];
      var w = 1 - sp.rarity * 0.8;
      if (sp.weather === g.weather) w *= 2.2;     // weather match
      else if (sp.weather === WEATHER_SHADE[g.weather]) w *= 0.6;
      return w;
    });
    var total = weights.reduce(function (a, b) { return a + b; }, 0);
    var pick = r() * total, acc = 0, idx = 0;
    for (var i = 0; i < pool.length; i++) { acc += weights[i]; if (pick <= acc) { idx = i; break; } }
    var key = pool[idx], sp = SPECIES[key];
    var power = gearPower(g), draw = LURES[g.gear.lure].draw;
    var sizeBias = (power + draw) / 6;            // better gear -> bigger fish
    var w = sp.min + r() * (sp.max - sp.min);
    w *= 0.6 + sizeBias * 0.8;
    w = Math.round(w * 10) / 10;
    return { key: key, name: sp.name, weight: w, value: Math.round(sp.val * w),
      fight: sp.max, trophy: w >= sp.max * 0.9 };
  }

  function recordCatch(g, fish) {
    var e = g.logbook[fish.key] || { count: 0, best: 0, name: fish.name };
    e.count++; e.best = Math.max(e.best, fish.weight); e.name = fish.name;
    g.logbook[fish.key] = e;
    if (Object.keys(g.logbook).length >= 6) g.logUnlocked = true;
  }

  // ---- gear shop transactions ----
  function buyOrUpgrade(g) {
    // cycle shopCursor: 0 rod, 1 line, 2..(2+L-1) lures
    if (g.shopCursor === 0) {
      if (g.gear.rod < RODS.length - 1 && g.money >= RODS[g.gear.rod + 1].cost) {
        g.money -= RODS[g.gear.rod + 1].cost; g.gear.rod++;
      }
    } else if (g.shopCursor === 1) {
      if (g.gear.line < LINES.length - 1 && g.money >= LINES[g.gear.line + 1].cost) {
        g.money -= LINES[g.gear.line + 1].cost; g.gear.line++;
      }
    } else {
      var li = g.shopCursor - 2;
      if (li < LURES.length && g.ownedLures.indexOf(li) < 0 && g.money >= LURES[li].cost) {
        g.money -= LURES[li].cost; g.ownedLures.push(li); g.gear.lure = li;
      }
    }
  }

  function endRound(g, won) {
    var rd = g.bracket[g.round];
    if (won) { rd.beaten = true; g.money += rd.prize; g.message = 'Round won! +$' + rd.prize; }
    else { g.message = 'Round lost.'; }
    if (g.round >= g.bracket.length - 1 || !won) {
      g.screen = won ? 'OVER' : 'OVER';
      g.overWon = won;
    } else {
      g.round++; g.screen = 'BRACKET';
    }
  }

  // ---- main advance ----
  function advance(g, input, dt) {
    var P = input.pressed || {};
    if (g.flash > 0) g.flash = Math.max(0, g.flash - dt);

    switch (g.screen) {
      case 'TITLE':
        if (P.enter || P.space) g.screen = 'BRACKET';
        break;

      case 'BRACKET':
        if (P.enter || P.space) g.screen = 'LAKE';
        if (P.l) g.screen = 'LOG';
        break;

      case 'LAKE':
        if (P.w || P.up) g.lakeCursor = (g.lakeCursor + 2) % 3;
        if (P.s || P.down) g.lakeCursor = (g.lakeCursor + 1) % 3;
        if (P.enter || P.space) {
          g.lake = ['pond', 'reservoir', 'stream'][g.lakeCursor];
          g.shopCursor = 0; g.screen = 'GEAR';
        }
        break;

      case 'GEAR':
        // shop rows: [0]rod [1]line [2..2+L-1]lures [last] START.
        var n = 2 + LURES.length + 1;
        if (P.w || P.up) g.shopCursor = (g.shopCursor + n - 1) % n;
        if (P.s || P.down) g.shopCursor = (g.shopCursor + 1) % n;
        if (g.shopCursor >= 2 && g.shopCursor < 2 + LURES.length) {
          if (P.a || P.left) { var oi = g.ownedLures.indexOf(g.gear.lure);
            g.gear.lure = g.ownedLures[(oi + g.ownedLures.length - 1) % g.ownedLures.length]; }
          if (P.d || P.right) { var oi2 = g.ownedLures.indexOf(g.gear.lure);
            g.gear.lure = g.ownedLures[(oi2 + 1) % g.ownedLures.length]; }
        }
        if (P.enter || P.space) {
          if (g.shopCursor === n - 1) { resetRound(g); g.screen = 'FISH'; } // START row
          else buyOrUpgrade(g);
        }
        if (P.escape) g.screen = 'LAKE';
        break;

      case 'FISH':
        updateFishing(g, input, dt);
        if (P.escape) { g.screen = 'BRACKET'; }
        break;

      case 'CATCH':
        if (P.enter || P.space) {
          var rd = g.bracket[g.round];
          if (g.elapsed >= g.timeLeft) { endRound(g, g.totalWeight > rd.oppWeight); }
          else { g.phase = 'IDLE'; g.screen = 'FISH'; }
        }
        break;

      case 'LOG':
        if (P.escape || P.enter) g.screen = 'BRACKET';
        break;

      case 'OVER':
        if (P.enter || P.space) {
          var ng = createGame({ seed: g.seed + 7, money: g.money });
          Object.assign(ng, { logbook: g.logbook, money: g.money, logUnlocked: g.logUnlocked });
          Object.keys(ng).forEach(function (k) { g[k] = ng[k]; });
        }
        break;
    }
    return g;
  }

  function updateFishing(g, input, dt) {
    var P = input.pressed || {};
    g.elapsed += dt;
    var lakeT = LAKES[g.lake].time;
    g.timeLeft = Math.max(0, lakeT - g.elapsed);
    g.weather = weatherFor(g.round, g.elapsed);
    g.phaseT += dt;

    if (g.phase === 'IDLE') {
      g.tension = 0; g.distance = 0;
      if (P.space) { g.phase = 'CAST'; g.phaseT = 0; g.message = 'Casting...'; }
    } else if (g.phase === 'CAST') {
      if (g.phaseT > 0.6) { g.phase = 'WAIT'; g.phaseT = 0; g.biteT = 0; g.message = 'Waiting for a bite...'; }
    } else if (g.phase === 'WAIT') {
      g.biteT += dt;
      var rate = WEATHER_FX[g.weather] * (0.5 + LURES[g.gear.lure].draw * 0.2);
      if (g.biteT > 2.5 - Math.min(1.8, rate * 0.5) && g.rng() < rate * dt * 0.9) {
        g.phase = 'HOOK'; g.phaseT = 0; g.fish = rollFish(g); g.message = 'BITE! Set the hook!';
        g.flash = 0.3;
      }
    } else if (g.phase === 'HOOK') {
      if (g.phaseT > 1.6) { g.phase = 'WAIT'; g.phaseT = 0; g.message = 'Got away...'; g.fish = null; }
      else if (P.space) { g.phase = 'REEL'; g.phaseT = 0; g.tension = 0.2; g.distance = 0;
        g.message = 'Reel it in!'; }
    } else if (g.phase === 'REEL') {
      var f = g.fish, power = gearPower(g), str = gearStrength(g);
      var fight = (f.fight / 40);                 // 0..1 fightiness
      // fish fights: tension rises faster for big fish, eased by rod power
      var pull = fight * dt * (1.6 - power * 0.25);
      if (P.space) {                              // reeling: gains distance, raises tension
        g.distance += dt * (0.18 + power * 0.05) * (1 - g.tension * 0.5);
        g.tension += pull * 1.1 + dt * 0.25;
      } else {                                    // slack: tension falls, fish regains
        g.tension -= dt * 0.7;
        g.distance -= dt * 0.12 * fight;
      }
      g.tension = Math.max(0, Math.min(1, g.tension));
      g.distance = Math.max(0, Math.min(1, g.distance));
      // line snap if tension over line strength
      var limit = 0.45 + str * 0.2;
      if (g.tension > limit) {
        g.message = 'Line snapped!'; g.phase = 'DONE'; g.phaseT = 0; g.fish = null;
      } else if (g.distance >= 1) {
        recordCatch(g, g.fish); g.totalWeight = Math.round((g.totalWeight + g.fish.weight) * 10) / 10;
        g.lastCatch = g.fish; g.message = 'Landed ' + g.fish.name + '!';
        g.phase = 'DONE'; g.phaseT = 0;
      }
    } else if (g.phase === 'DONE') {
      if (g.phaseT > 1.1) { g.screen = 'CATCH'; g.phase = 'IDLE'; }
    }

    if (g.timeLeft <= 0 && g.phase !== 'REEL' && g.screen === 'FISH') {
      endRound(g, g.totalWeight > g.bracket[g.round].oppWeight);
    }
  }

  // ---- render descriptor (plain data the HTML draws) ----
  function renderState(g) {
    var rd = g.bracket[g.round];
    return {
      screen: g.screen,
      message: g.message,
      flash: g.flash,
      round: g.round,
      totalRounds: g.bracket.length,
      lake: g.lake ? LAKES[g.lake] : null,
      lakeKey: g.lake,
      weather: g.weather,
      timeLeft: g.timeLeft,
      totalWeight: g.totalWeight,
      opponent: rd ? { name: rd.opponent, weight: rd.oppWeight, prize: rd.prize, target: rd.target } : null,
      gear: { rod: RODS[g.gear.rod], line: LINES[g.gear.line], lure: LURES[g.gear.lure], money: g.money },
      ownedLures: g.ownedLures.slice(),
      shopCursor: g.shopCursor,
      lakeCursor: g.lakeCursor,
      phase: g.phase,
      tension: g.tension,
      distance: g.distance,
      fish: g.fish,
      lastCatch: g.lastCatch,
      logbook: g.logbook,
      logUnlocked: g.logUnlocked,
      logTotal: Object.keys(g.logbook).length,
      speciesTotal: Object.keys(SPECIES).length,
      overWon: g.overWon,
      bracket: g.bracket.map(function (r) {
        return { lake: r.lake, opponent: r.opponent, weight: r.oppWeight, prize: r.prize, beaten: r.beaten };
      })
    };
  }

  global.FishingGame = {
    createGame: createGame,
    advance: advance,
    renderState: renderState,
    SPECIES: SPECIES,
    LAKES: LAKES,
    LURES: LURES,
    RODS: RODS,
    LINES: LINES
  };
})(typeof window !== 'undefined' ? window : this);
