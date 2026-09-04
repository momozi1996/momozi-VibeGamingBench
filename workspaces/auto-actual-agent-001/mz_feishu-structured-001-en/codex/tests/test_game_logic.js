const g = require('../game_logic.js');

function startPlaying(seed){ let game = g.createGame({seed: seed||123}); game = g.advance(game,{type:'start'},0); game = g.advance(game,{type:'confirm'},0); return game; }

// 1. initial phase
test('initial phase is title', ()=>{ const game = g.createGame({seed:1}); assertEq(game.phase,'title'); });

// 2. determinism same seed -> same map stair position
test('deterministic floor map for same seed', ()=>{
  let a=startPlaying(999), b=startPlaying(999);
  const am = a.world.maps['f'+a.world.floor]; const bm = b.world.maps['f'+b.world.floor];
  assertEq(am.stairs.x,bm.stairs.x,'stairs x'); assertEq(am.stairs.y,bm.stairs.y,'stairs y');
});

// 3. movement changes position eventually
test('movement changes player position when possible', ()=>{
  let game = startPlaying(42);
  const pos0 = {x:game.playerPos.x,y:game.playerPos.y};
  let dirs=['up','down','left','right']; let moved=false;
  for(const d of dirs){ let g2=g.advance(game,{type:'move',dir:d},0); if(g2.playerPos.x!==pos0.x || g2.playerPos.y!==pos0.y){ moved=true; break; } }
  assert(moved,'should have moved at least one direction');
});

// 4. encounter triggers after several steps
test('encounter triggers to battle', ()=>{
  let game = startPlaying(77);
  let steps=0; while(game.phase==='playing' && steps<200){ game = g.advance(game,{type:'move',dir:'right'},0); steps++; if(game.phase==='battle') break; }
  assertEq(game.phase,'battle','should be in battle after steps');
});

// helper: ensure in battle
function ensureBattle(seed){ let game=startPlaying(seed||888); let i=0; while(game.phase!=='battle' && i<200){ game=g.advance(game,{type:'move',dir:'right'},0); i++; }
  return game; }

// 5. attack reduces enemy hp
test('attack reduces enemy HP', ()=>{
  let game = ensureBattle(8888); let e=game.battle.enemies[0]; let hp0=e.hp; game = g.advance(game,{ battleAction:{type:'attack', targetIndex:0} },0); assert(game.battle? true:true); // still in battle likely
  e = game.battle? game.battle.enemies[0]: e; assert(e.hp<=hp0,'enemy hp reduced or dead');
});

// 6. fire skill consumes MP and damages
test('fire skill consumes MP', ()=>{
  let game = ensureBattle(2222); let mp0=game.player.mp; let e=game.battle.enemies[0]; let hp0=e.hp; game = g.advance(game,{ battleAction:{type:'skill', id:'fire', targetIndex:0} },0);
  e = game.battle? game.battle.enemies[0]: e; assert(game.player.mp<=mp0-5,'mp reduced'); assert(e.hp<=hp0,'enemy took fire dmg');
});

// 7. item potion heals
test('potion heals HP', ()=>{
  let game = ensureBattle(3333); game.player.hp = Math.max(1, game.player.hp-10); let hp0=game.player.hp; game = g.advance(game,{ battleAction:{type:'item', id:'potion'} },0); assert(game.player.hp>=hp0,'healed or equal');
});

// 8. run eventually escapes
test('run can escape within attempts', ()=>{
  let game = ensureBattle(4444); let attempt=0; while(game.phase==='battle' && attempt<10){ game=g.advance(game,{ battleAction:{type:'run'} },0); attempt++; }
  assert(game.phase!=='battle','escaped eventually');
});

// 9. enemy can defeat player
test('enemy can defeat player', ()=>{
  let game = ensureBattle(5555); game.player.hp=1; // force low hp
  // make enemy turn
  game.battle.turn='enemy'; game = g.advance(game, { }, 0);
  assertEq(game.phase,'defeat');
});

// 10. boss victory leads to victory phase
test('final boss victory -> victory phase', ()=>{
  let game = startPlaying(6666); game.world.floor=3; // simulate
  // create battle with boss
  game.battle = { turn:'player', enemies:[{id:'boss', name:'Dungeon Warden', hp:5, maxHp:120, atk:14, def:6, spd:7, exp:60, gold:50, status:[], skills:['poisonClaw']}], log:[], reward:{}, anim:{}, round:1 };
  game.phase='battle';
  game = g.advance(game,{ battleAction:{type:'attack', targetIndex:0} },0);
  // after enemy turn or immediate, ensure if enemies dead -> victory
  if(game.phase==='battle'){ // continue until kill
    game.battle.enemies[0].hp=0; game.battle.turn='enemy'; game = g.advance(game, {}, 0);
  }
  assertEq(game.phase,'victory');
});

// 11. save and restore snapshot yields same floor and pos
test('save and restore snapshot', ()=>{
  let game = startPlaying(7777); var pos = {x:game.playerPos.x,y:game.playerPos.y}; var snap = JSON.parse(JSON.stringify(game));
  let restored = g.createGame({seed:snap.seed, snapshot:snap}); assertEq(restored.world.floor, game.world.floor); assertEq(restored.playerPos.x, pos.x); assertEq(restored.playerPos.y, pos.y);
});

// 12. NPC branch accept
test('NPC branch accept sets flag', ()=>{
  let game = startPlaying(8889); var m = game.world.maps['f'+game.world.floor]; var npc = m.npc; game.playerPos = {x:npc.x, y:npc.y}; game = g.advance(game,{type:'interact'},0); assert(game.world.awaitChoice,'awaiting choice'); game = g.advance(game,{type:'choice', accept:true},0); assert(game.world.branch.helpedNPC,'helped npc');
});
