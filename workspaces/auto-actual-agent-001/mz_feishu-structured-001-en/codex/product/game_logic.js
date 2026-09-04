(function (root) {
  // Deterministic RNG (Mulberry32)
  function makeRNG(seed) {
    var s = seed >>> 0;
    return function() {
      s |= 0; s = s + 0x6D2B79F5 | 0;
      var t = Math.imul(s ^ s >>> 15, 1 | s);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }
  function rngInt(rng, a, b){ return Math.floor(rng()*(b-a+1))+a; }
  function rngChoice(rng, arr){ return arr[rngInt(rng,0,arr.length-1)]; }

  function clone(obj){ return JSON.parse(JSON.stringify(obj)); }

  function newPlayer(){
    return {
      name: 'Wanderer', lvl: 1, exp: 0, nextExp: 20,
      hp: 40, maxHp: 40, mp: 12, maxMp: 12,
      atk: 8, def: 4, spd: 6,
      status: [], // {id:'poison', turns:3}
      equipment: { weapon: {name:'Rusty Dagger', atk:2}, armor: {name:'Cloth', def:1} },
      inventory: [ {id:'potion', name:'Potion', qty:2}, {id:'ether', name:'Ether', qty:1} ],
      gold: 0
    };
  }

  function enemyTemplates(floor){
    if(floor===3){ return [
      {id:'boss', name:'Dungeon Warden', hp: 120, atk: 14, def: 6, spd:7, exp: 60, gold: 50, skills:['poisonClaw']}
    ]; }
    var pool = [
      {id:'slime', name:'Moss Slime', hp: 22, atk:6, def:2, spd:4, exp:10, gold:6, skills:[]},
      {id:'bat', name:'Cave Bat', hp: 16, atk:5, def:1, spd:8, exp:9, gold:5, skills:['poisonClaw']},
      {id:'skeleton', name:'Bones', hp: 28, atk:7, def:3, spd:5, exp:12, gold:8, skills:[]}
    ];
    if(floor>=2){ pool.push({id:'mage', name:'Feral Mage', hp:26, atk:9, def:2, spd:6, exp:15, gold:12, skills:['poisonClaw']}); }
    return pool;
  }

  function makeEnemyFromTemplate(t){
    return { id:t.id, name:t.name, hp:t.hp, maxHp:t.hp, atk:t.atk, def:t.def, spd:t.spd, exp:t.exp, gold:t.gold, status:[], skills:t.skills.slice() };
  }

  function newGameWorld(rng){
    return { floor:1, maxFloor:3, maps: {}, branch:{ helpedNPC:false, talkedNPC:false },
      stats: { enemiesDefeated:0, chestsOpened:0, steps:0, time:0 },
      encounterSteps: 0, encounterThreshold: rngInt(rng,6,12),
      message:'' };
  }

  function makeMap(rng, w, h){
    // 0 wall, 1 floor, 2 stairs, 3 npc, 4 chest
    var tiles = new Array(h); for(var y=0;y<h;y++){ tiles[y]=new Array(w).fill(0); }
    // Drunkard walk carve
    var x=Math.floor(w/2), y=Math.floor(h/2); tiles[y][x]=1; var floors=1; var target=Math.floor(w*h*0.35);
    var dirs=[[1,0],[-1,0],[0,1],[0,-1]];
    while(floors<target){ var d=rngInt(rng,0,3); x=Math.max(1,Math.min(w-2,x+dirs[d][0])); y=Math.max(1,Math.min(h-2,y+dirs[d][1])); if(tiles[y][x]===0){ tiles[y][x]=1; floors++; } }
    // place stairs, npc, chests on floor tiles
    var floorCells=[]; for(var yy=1;yy<h-1;yy++){ for(var xx=1;xx<w-1;xx++){ if(tiles[yy][xx]===1) floorCells.push([xx,yy]); }}
    var stairs = floorCells[rngInt(rng,0,floorCells.length-1)]; tiles[stairs[1]][stairs[0]] = 2;
    var npc = floorCells[rngInt(rng,0,floorCells.length-1)]; tiles[npc[1]][npc[0]] = 3;
    var chestCount = rngInt(rng,3,6);
    for(var i=0;i<chestCount;i++){ var c = floorCells[rngInt(rng,0,floorCells.length-1)]; if(tiles[c[1]][c[0]]===1) tiles[c[1]][c[0]]=4; }
    // find spawn near center
    var spawn=[Math.floor(w/2),Math.floor(h/2)]; var best=9999; for(var i2=0;i2<floorCells.length;i2++){ var c=floorCells[i2]; var d2=Math.abs(c[0]-spawn[0])+Math.abs(c[1]-spawn[1]); if(d2<best){best=d2; spawn=c;}}
    return { w:w,h:h,tiles:tiles, spawn:{x:spawn[0],y:spawn[1]}, stairs:{x:stairs[0],y:stairs[1]}, npc:{x:npc[0],y:npc[1]}, explored:{} };
  }

  function getMap(game){
    var key = 'f'+game.world.floor; var m = game.world.maps[key]; if(!m){ m = makeMap(game.rng, 32, 24); game.world.maps[key]=m; }
    return m;
  }

  function canWalk(m,x,y){ if(x<0||y<0||x>=m.w||y>=m.h) return false; return m.tiles[y][x]!==0; }

  function levelUpIfNeeded(p){ while(p.exp>=p.nextExp){ p.exp-=p.nextExp; p.lvl++; p.nextExp = Math.floor(p.nextExp*1.5); p.maxHp+=6; p.hp=p.maxHp; p.maxMp+=3; p.mp=p.maxMp; p.atk+=2; p.def+=1; } }

  function scoreFrom(game){ var w=game.world; return w.stats.enemiesDefeated*10 + w.stats.chestsOpened*5 + (w.branch.helpedNPC?20:0) + (w.floorCleared? w.floorCleared*15:0); }

  function createGame(opts){
    opts = opts || {};
    var seed = (opts.seed===undefined? (Date.now()>>>0) : (opts.seed>>>0));
    var rng = makeRNG(seed);
    var player = newPlayer();
    var world = newGameWorld(rng);
    var game = { seed:seed, rng:rng, phase:'title', player:player, world:world, ui:{}, score:0, floating:[], battle:null, saved:false };
    if(opts.snapshot){
      game = opts.snapshot; game.rng = makeRNG(game.seed);
      if(game.rngTick){ for(var i=0;i<game.rngTick;i++){ game.rng(); } }
    }
    return game;
  }

  function pushFloating(game, text, kind){ game.floating.push({text:text, kind:kind||'note', t:0}); }

  function tryEncounter(game){
    var w = game.world; w.encounterSteps++; w.stats.steps++;
    var chance = 0.04 + (w.encounterSteps*0.01);
    if(w.encounterSteps >= w.encounterThreshold || game.rng()<chance){
      w.encounterSteps = 0; w.encounterThreshold = rngInt(game.rng,6,12);
      startBattle(game);
    }
  }

  function startBattle(game){
    var floor = game.world.floor;
    var tps = enemyTemplates(floor);
    var count = (floor===3?1:rngInt(game.rng,1,2));
    var enemies=[];
    if(floor===3 && !game.world.bossSpawned){ enemies=[ makeEnemyFromTemplate(tps[0]) ]; game.world.bossSpawned=true; }
    else{ for(var i=0;i<count;i++){ enemies.push(makeEnemyFromTemplate(rngChoice(game.rng,tps))); } }
    game.battle = { turn:'player', enemies:enemies, log:[], reward:{exp:0,gold:0}, anim:{}, round:1 };
    game.phase = 'battle';
    pushFloating(game, 'Encounter!', 'event');
  }

  function takeDamage(target, dmg){ var real = Math.max(1, dmg); target.hp -= real; return real; }

  function applyStatus(target, id, turns, data){ target.status.push({id:id, turns:turns, data:data||{}}); }
  function hasStatus(target, id){ for(var i=0;i<target.status.length;i++){ if(target.status[i].id===id) return true; } return false; }

  function tickStatuses(target, log){ for(var i=target.status.length-1;i>=0;i--){ var s=target.status[i]; if(s.id==='poison'){ var d=4; target.hp -= d; log.push(target.name+' takes '+d+' poison'); }
    s.turns--; if(s.turns<=0) target.status.splice(i,1);
  } }

  function battleStep(game, action){
    var b = game.battle; var p = game.player; var log=b.log;
    if(!b) return;
    if(action && b.turn==='player'){
      if(action.type==='attack'){
        var e = b.enemies[ action.targetIndex||0 ]; if(e){ var dmg = Math.floor((p.atk + (p.equipment.weapon.atk||0)) - e.def*0.6); dmg += rngInt(game.rng,-2,2); var real=takeDamage(e,dmg); log.push('You hit '+e.name+' for '+real); pushFloating(game, ''+real, 'dmg'); }
      } else if(action.type==='skill'){
        if(action.id==='fire' && p.mp>=5){ p.mp-=5; var e2=b.enemies[action.targetIndex||0]; if(e2){ var dmg2=Math.floor(p.atk*0.5+10 - e2.def*0.3 + rngInt(game.rng,-1,1)); var real2=takeDamage(e2,dmg2); log.push('Fire hits '+e2.name+' for '+real2); pushFloating(game, ''+real2, 'crit'); } }
        else if(action.id==='shield' && p.mp>=4 && !hasStatus(p,'shield')){ p.mp-=4; applyStatus(p,'shield',5,{def:3}); log.push('Shield up'); pushFloating(game,'Shield','buff'); }
      } else if(action.type==='item'){
        if(action.id==='potion'){
          var it = p.inventory.find(function(i){return i.id==='potion' && i.qty>0;}); if(it){ it.qty--; var heal=20; p.hp=Math.min(p.maxHp,p.hp+heal); log.push('You use Potion +'+heal); pushFloating(game,'+'+heal,'heal'); }
        } else if(action.id==='ether'){
          var it2 = p.inventory.find(function(i){return i.id==='ether' && i.qty>0;}); if(it2){ it2.qty--; var heal2=10; p.mp=Math.min(p.maxMp,p.mp+heal2); log.push('You use Ether +'+heal2+' MP'); pushFloating(game,'+'+heal2,'mana'); }
        }
      } else if(action.type==='run'){
        if(game.rng()<0.5){ log.push('Ran away'); game.phase='playing'; game.battle=null; return; } else { log.push('Cannot escape'); }
      }
      b.turn='enemy';
    }
    if(b.turn==='enemy'){
      for(var i=0;i<b.enemies.length;i++){
        var e3=b.enemies[i]; if(e3.hp<=0) continue;
        var doSkill = (e3.skills.indexOf('poisonClaw')>=0 && game.rng()<0.35 && !hasStatus(p,'poison'));
        if(doSkill){ applyStatus(p,'poison',3,{}); log.push(e3.name+' poisoned you'); pushFloating(game,'Poison','debuff'); }
        else{
          var dmg3=Math.floor(e3.atk - (p.def + (p.equipment.armor.def||0) + (hasStatus(p,'shield')?3:0))*0.6 + rngInt(game.rng,-1,1));
          var real3=takeDamage(p,dmg3); log.push(e3.name+' hits you '+real3); pushFloating(game,''+real3,'hurt');
        }
        if(p.hp<=0) break;
      }
      // tick end-of-round statuses
      tickStatuses(p,log); for(var j=0;j<b.enemies.length;j++){ tickStatuses(b.enemies[j],log); }
      // remove dead enemies
      b.enemies = b.enemies.filter(function(e){ return e.hp>0; });
      if(p.hp<=0){ game.phase='defeat'; game.battle=null; game.score=scoreFrom(game); return; }
      if(b.enemies.length===0){
        var base = (game.world.floor===3?40: game.world.floor===2?20:12);
        var rExp = base; var rGold = Math.floor(base*0.6);
        game.player.exp += rExp; game.player.gold += rGold;
        game.world.stats.enemiesDefeated += 1;
        levelUpIfNeeded(game.player);
        game.phase='playing'; game.battle=null; pushFloating(game,'Victory','event');
        if(game.world.floor===3){ game.phase='victory'; game.world.floorCleared = 3; game.score=scoreFrom(game); }
        return;
      }
      b.round++; b.turn='player';
    }
  }

  function openChest(game){ var m=getMap(game); var p=game.player; var pos=game.playerPos; if(m.tiles[pos.y][pos.x]!==4) return; var roll = game.rng(); var txt='';
    if(roll<0.4){ var it=p.inventory.find(function(i){return i.id==='potion';}); if(!it){ p.inventory.push({id:'potion',name:'Potion',qty:1}); } else it.qty++; txt='Found Potion'; }
    else if(roll<0.7){ var it2=p.inventory.find(function(i){return i.id==='ether';}); if(!it2){ p.inventory.push({id:'ether',name:'Ether',qty:1}); } else it2.qty++; txt='Found Ether'; }
    else { if(game.rng()<0.5){ var wpn={name:'Bronze Sword', atk:3}; p.equipment.weapon=wpn; txt='Equipped '+wpn.name; } else { var arm={name:'Leather', def:2}; p.equipment.armor=arm; txt='Equipped '+arm.name; } }
    m.tiles[pos.y][pos.x]=1; game.world.stats.chestsOpened++; pushFloating(game,txt,'loot'); }

  function talkNPC(game){ var m=getMap(game); var pos=game.playerPos; if(m.tiles[pos.y][pos.x]!==3) return; var w=game.world; w.branch.talkedNPC=true; if(!w.branch.helpedNPC){ w.message='NPC: Will you help me clear the dungeon?'; w.awaitChoice=true; } }
  function chooseNPC(game, accept){ var w=game.world; if(!w.awaitChoice) return; w.awaitChoice=false; if(accept){ w.branch.helpedNPC=true; game.player.hp=Math.min(game.player.maxHp, game.player.hp+20); pushFloating(game,'NPC healed you','heal'); } else { game.player.gold+=10; pushFloating(game,'NPC paid you','gold'); } }

  function movePlayer(game, dx, dy){ var m=getMap(game); var nx=game.playerPos.x+dx; var ny=game.playerPos.y+dy; if(!canWalk(m,nx,ny)) return; game.playerPos.x=nx; game.playerPos.y=ny; game.world.message=''; var tile=m.tiles[ny][nx]; if(tile===2){ game.world.atStairs=true; } else { game.world.atStairs=false; } tryEncounter(game); }

  function nextFloor(game){ if(game.world.floor<3){ game.world.floor++; var m=getMap(game); game.playerPos = {x:m.spawn.x, y:m.spawn.y}; if(game.world.floor===3){ /* escalate */ } } }

  function setupFirstFloor(game){ var m=getMap(game); game.playerPos = {x:m.spawn.x, y:m.spawn.y}; }

  function advance(game, input, dt){
    dt = dt||0; if(!game) return game;
    for(var i=game.floating.length-1;i>=0;i--){ var f=game.floating[i]; f.t+=dt; if(f.t>1.0) game.floating.splice(i,1); }

    input = input||{}; var type=input.type||'';
    if(game.phase==='title'){
      if(type==='start'){ game.phase='onboarding'; game.world.message='Welcome'; }
      else if(type==='load' && input.snapshot){ return createGame({seed:input.snapshot.seed, snapshot: clone(input.snapshot)}); }
      return game;
    }
    if(game.phase==='onboarding'){
      setupFirstFloor(game); if(type==='confirm'){ game.phase='playing'; pushFloating(game,'Begin','event'); }
      return game;
    }
    if(game.phase==='pause'){
      if(type==='resume'){ game.phase='playing'; }
      else if(type==='quit'){ game.phase='title'; }
      return game;
    }
    if(game.phase==='playing'){
      if(type==='pause'){ game.phase='pause'; return game; }
      if(game.world.awaitChoice){ if(type==='choice'){ chooseNPC(game, !!input.accept); } return game; }
      if(type==='move'){
        var d=input.dir; if(d==='up') movePlayer(game,0,-1); else if(d==='down') movePlayer(game,0,1); else if(d==='left') movePlayer(game,-1,0); else if(d==='right') movePlayer(game,1,0);
      } else if(type==='interact'){
        var m=getMap(game); var t=m.tiles[game.playerPos.y][game.playerPos.x]; if(t===4) openChest(game); else if(t===3) talkNPC(game); else if(t===2){ nextFloor(game); }
      }
      if(game.player.hp<=0){ game.phase='defeat'; game.score=scoreFrom(game); }
      return game;
    }
    if(game.phase==='battle'){
      battleStep(game, input && input.battleAction? input.battleAction : null);
      return game;
    }
    return game;
  }

  var api = { createGame:createGame, advance:advance };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== 'undefined' ? window : globalThis));
