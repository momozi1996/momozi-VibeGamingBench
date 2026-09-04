(function (root) {
  'use strict';

  // Utility
  const deepCopy = (o) => {
    if (o === null || typeof o !== 'object') return o;
    if (Array.isArray(o)) return o.map(deepCopy);
    const out = {};
    for (const key of Object.keys(o)) out[key] = deepCopy(o[key]);
    return out;
  };
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

  // Gate definitions
  const GateDefs = {
    AND: { in: 2, out: 1, fn: (ins) => (ins[0] & ins[1])|0 },
    OR:  { in: 2, out: 1, fn: (ins) => (ins[0] | ins[1])|0 },
    NOT: { in: 1, out: 1, fn: (ins) => (ins[0]?0:1) },
    XOR: { in: 2, out: 1, fn: (ins) => (ins[0]^ins[1])|0 },
    DEL: { in: 1, out: 1, fn: (ins, ctx) => ctx.prev(ins[0]) }, // 1-tick delay
  };

  // Inputs: signal helpers
  const Sig = {
    const: (v) => (t)=> v?1:0,
    pattern: (bits) => (t)=> bits[t % bits.length] === '1' ? 1 : 0,
    pulse: (period=2) => (t)=> ((Math.floor(t/period) % 2)===0) ? 1:0,
  };

  // Level set
  function makeLevels(){
    // expected functions accept (t, ins) where ins is map by label
    const L = [];
    // 1. Invert It
    L.push({
      name: 'Invert It',
      targetDesc: 'Q = NOT(A)',
      width: 14, height: 9, steps: 8,
      toolbox: { NOT: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('10101010') } ],
      outputs: [ { id:'Q', label:'Q', y:2, desc:'NOT(A)', expected: (t,ins)=> (ins.A(t)?0:1) } ],
    });
    // 2. AND Basics
    L.push({
      name: 'AND Basics',
      targetDesc: 'Q = A AND B',
      width: 14, height: 9, steps: 8,
      toolbox: { AND: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('11001100') }, { id:'B', label:'B', y:4, signal: Sig.pattern('10101010') } ],
      outputs: [ { id:'Q', label:'Q', y:3, desc:'A AND B', expected: (t,ins)=> (ins.A(t)&ins.B(t))|0 } ],
    });
    // 3. OR Basics
    L.push({
      name: 'OR Basics', targetDesc: 'Q = A OR B', width: 14, height: 9, steps: 8,
      toolbox: { OR: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('10001000') }, { id:'B', label:'B', y:4, signal: Sig.pattern('00100010') } ],
      outputs: [ { id:'Q', label:'Q', y:3, desc:'A OR B', expected: (t,ins)=> (ins.A(t)|ins.B(t))|0 } ],
    });
    // 4. XOR Lesson
    L.push({
      name: 'Exclusive', targetDesc: 'Q = A XOR B', width: 14, height: 9, steps: 8,
      toolbox: { XOR: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('10101010') }, { id:'B', label:'B', y:4, signal: Sig.pattern('11001100') } ],
      outputs: [ { id:'Q', label:'Q', y:3, desc:'A XOR B', expected: (t,ins)=> (ins.A(t)^ins.B(t))|0 } ],
    });
    // 5. Half Adder (Sum XOR, Carry AND)
    L.push({
      name: 'Half Adder', targetDesc: 'Sum = A XOR B; Carry = A AND B', width: 14, height: 9, steps: 8,
      toolbox: { XOR: 1, AND: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('10101010') }, { id:'B', label:'B', y:4, signal: Sig.pattern('11001100') } ],
      outputs: [
        { id:'S', label:'Sum', y:3, desc:'A XOR B', expected: (t,ins)=> (ins.A(t)^ins.B(t))|0 },
        { id:'C', label:'Carry', y:5, desc:'A AND B', expected: (t,ins)=> (ins.A(t)&ins.B(t))|0 },
      ],
    });
    // 6. Delay Line
    L.push({
      name: 'Delay Line', targetDesc: 'Q = DEL(A)', width: 14, height: 9, steps: 8,
      toolbox: { DEL: 1 },
      inputs: [ { id:'A', label:'A', y:2, signal: Sig.pattern('11000011') } ],
      outputs: [ { id:'Q', label:'Q', y:2, desc:'A delayed by 1', expected: (t,ins)=> (t<=0?0:ins.A(t-1)) } ],
    });
    // 7. Mux 2:1 (build from basics)
    L.push({
      name: '2:1 Mux', targetDesc: 'Q = (A & ~S) | (B & S)', width: 16, height: 9, steps: 8,
      toolbox: { AND: 2, OR: 1, NOT: 1 },
      inputs: [
        { id:'A', label:'A', y:2, signal: Sig.pattern('10101010') },
        { id:'B', label:'B', y:4, signal: Sig.pattern('11001100') },
        { id:'S', label:'S', y:6, signal: Sig.pattern('00110011') },
      ],
      outputs: [ { id:'Q', label:'Q', y:3, desc:'(A & ~S) | (B & S)', expected: (t,ins)=> ((ins.A(t)&(ins.S(t)?0:1)) | (ins.B(t)&ins.S(t)))|0 } ],
    });
    // 8. Chain Logic
    L.push({
      name: 'Chain Logic', targetDesc: 'Q = NOT(A XOR (B OR C))', width: 16, height: 10, steps: 8,
      toolbox: { NOT: 1, XOR: 1, OR: 1 },
      inputs: [
        { id:'A', label:'A', y:2, signal: Sig.pattern('10101010') },
        { id:'B', label:'B', y:4, signal: Sig.pattern('10001000') },
        { id:'C', label:'C', y:6, signal: Sig.pattern('00100010') },
      ],
      outputs: [ { id:'Q', label:'Q', y:5, desc:'NOT(A XOR (B OR C))', expected: (t,ins)=> ( (ins.A(t) ^ (ins.B(t)|ins.C(t))) ? 0:1 ) } ],
    });
    return L;
  }

  function createLevelState(level){
    const nodes = {}; const wires = []; const wireByTarget = {};
    let nextNodeId = 1;
    // Place inputs left (x=0) and outputs right (x=width-1)
    level.inputs.forEach(inp=>{
      const id = nextNodeId++; nodes[id] = { id, kind:'IN', label: inp.label, pos:{ x: 0, y: inp.y }, in:0, out:1, signal: inp.signal };
      inp._nodeId = id;
    });
    level.outputs.forEach(out=>{
      const id = nextNodeId++; nodes[id] = { id, kind:'OUT', label: out.label, pos:{ x: level.width-1, y: out.y }, in:1, out:0 };
      out._nodeId = id;
    });
    const board = {
      width: level.width, height: level.height,
      nodes, nextNodeId,
      wires, wireByTarget,
      used: {},
      toolbox: Object.assign({ AND:0, OR:0, NOT:0, XOR:0, DEL:0 }, level.toolbox||{}),
      occupied: {},
    };
    // mark reserved edge slots
    for(const id in nodes){ const n=nodes[id]; board.occupied[posKey(n.pos.x, n.pos.y)] = true; }
    return board;
  }

  function posKey(x,y){ return `${x},${y}`; }

  function createGame(opts){
    const levels = makeLevels();
    const levelIndex = 0;
    const level = deepCopy(levels[levelIndex]);
    const board = createLevelState(level);
    const game = {
      phase: 'title',
      levelIndex, levels,
      level,
      board,
      sim: { running:false, accum:0, tick:0, step:0, steps: level.steps, lastValues:{}, compare:{} },
      message: 'Welcome',
      justWon: false,
    };
    return game;
  }

  // Evaluation engine
  function evaluateAt(game, tick){
    const { board, level } = game;
    const memo = {};
    const ctx = {
      prev: (v)=> v, // replaced below by delayed accessor since we pass constants for inputs
    };
    function valueOfNode(nodeId){
      const key = `${nodeId}@${tick}`; if(key in memo) return memo[key];
      const node = board.nodes[nodeId]; if(!node){ memo[key]=0; return 0; }
      let out=0;
      if(node.kind==='IN'){
        out = node.signal(tick);
      } else if(node.kind in GateDefs){
        const def = GateDefs[node.kind];
        const ins = new Array(def.in).fill(0);
        for(let i=0;i<def.in;i++){
          const wid = board.wireByTarget[`${node.id}:in:${i}`];
          if(!wid){ ins[i]=0; continue; }
          const w = board.wires.find(w=>w.id===wid);
          const src = w && w.from && board.nodes[w.from.nodeId];
          ins[i] = src ? valueOfNode(src.id) : 0;
        }
        ctx.prev = (v)=>{ // return delayed value for DEL gate
          // For DEL: we expect ins[0] to be the immediate, we look at previous tick
          // fallback to 0 at t<=0
          return tick<=0 ? 0 : v;
        };
        if(node.kind==='DEL'){
          // override first input by previous tick value
          const wid = board.wireByTarget[`${node.id}:in:0`];
          if(wid){ const w = board.wires.find(w=>w.id===wid); if(w){ const src=board.nodes[w.from.nodeId]; ins[0] = (tick<=0?0:valueOfNodeAt(src.id, tick-1, board)); } }
          out = ins[0];
        } else {
          out = def.fn(ins, ctx);
        }
      } else if(node.kind==='OUT'){
        const wid = board.wireByTarget[`${node.id}:in:0`];
        if(!wid){ out=0; } else { const w = board.wires.find(w=>w.id===wid); const src = w && board.nodes[w.from.nodeId]; out = src ? valueOfNode(src.id) : 0; }
      }
      memo[key]=out; return out;
    }
    const lastValues = {}; for(const id in board.nodes){ lastValues[id] = valueOfNode(+id); }
    // Compute expected outputs per level definition
    const insMap = {}; game.level.inputs.forEach(inp=>{ insMap[inp.label] = (t)=> board.nodes[inp._nodeId].signal(t); });
    const compare = {};
    for(const out of level.outputs){
      const n = board.nodes[out._nodeId];
      const actual = valueOfNode(n.id);
      const expected = out.expected(tick, insMap);
      compare[out.label] = { actual, expected, ok: actual===expected };
    }
    return { lastValues, compare };
  }

  function valueOfNodeAt(nodeId, tick, board){
    // Simple helper for DEL to fetch previous outputs (
    // this performs a limited DFS similar to evaluateAt; for DEL only we just evaluate upstream IN or gates without DEL recursion.
    // For robustness we could reuse evaluateAt with a temp game, but we'll keep this minimal.
    return 0; // placeholder not used directly since evaluateAt computes DEL inline.
  }

  function placeGate(board, gateType, pos){
    gateType = gateType.toUpperCase();
    const def = GateDefs[gateType]; if(!def) return { ok:false, msg:'Unknown gate' };
    const key = posKey(pos.x,pos.y);
    if(board.occupied[key]) return { ok:false, msg:'Cell occupied' };
    if(pos.x<=0 || pos.x>=board.width-1) return { ok:false, msg:'Place inside work area' };
    const have = board.toolbox[gateType]||0; const used=board.used[gateType]||0; if(used>=have) return { ok:false, msg:'No gates left' };
    const id = board.nextNodeId++;
    board.nodes[id] = { id, kind: gateType, pos: { x: pos.x, y: pos.y }, in: def.in, out: def.out };
    board.occupied[key]=true; board.used[gateType]=(board.used[gateType]||0)+1;
    return { ok:true, msg:`Placed ${gateType}` };
  }

  function connect(board, from, to){
    // from: { nodeId, pin }, to: { nodeId, pin }
    const nFrom = board.nodes[from.nodeId]; const nTo = board.nodes[to.nodeId];
    if(!nFrom || !nTo) return { ok:false, msg:'Invalid nodes' };
    if(nTo.kind==='IN' || nFrom.kind==='OUT' && nTo.kind==='OUT'){
      // allow IN/OUT connections? We require OUT target be an input side: only connect OUT -> IN side
    }
    // Only from output to input
    if(nFrom.out<=0) return { ok:false, msg:'Source has no output' };
    if(nTo.in<=0) return { ok:false, msg:'Target has no input' };
    const key = `${nTo.id}:in:${to.pin}`;
    // Remove existing wire to this input
    const existing = board.wireByTarget[key];
    if(existing){ const idx = board.wires.findIndex(w=>w.id===existing); if(idx>=0) board.wires.splice(idx,1); delete board.wireByTarget[key]; }
    const wid = (board.wires.reduce((m,w)=>Math.max(m,w.id||0),0)+1)||1;
    board.wires.push({ id: wid, from: { nodeId: nFrom.id, pin: 0 }, to: { nodeId: nTo.id, pin: to.pin } });
    board.wireByTarget[key] = wid;
    return { ok:true, msg:'Connected' };
  }

  function removeWireAtInput(board, nodeId, pin){
    const key = `${nodeId}:in:${pin}`; const wid = board.wireByTarget[key]; if(!wid) return { ok:false, msg:'No wire' };
    const idx = board.wires.findIndex(w=>w.id===wid); if(idx>=0) board.wires.splice(idx,1); delete board.wireByTarget[key]; return { ok:true, msg:'Wire removed' };
  }

  function deleteNode(board, nodeId){
    const n = board.nodes[nodeId]; if(!n) return { ok:false, msg:'No node' };
    if(n.kind==='IN'||n.kind==='OUT') return { ok:false, msg:'Cannot delete terminals' };
    // remove wires attached
    board.wires = board.wires.filter(w=>{
      const keep = !(w.from.nodeId===nodeId || w.to.nodeId===nodeId);
      if(!keep){ const key = `${w.to.nodeId}:in:${w.to.pin}`; delete board.wireByTarget[key]; }
      return keep;
    });
    delete board.nodes[nodeId];
    board.occupied[posKey(n.pos.x,n.pos.y)] = false;
    board.used[n.kind] = Math.max(0, (board.used[n.kind]||1)-1);
    return { ok:true, msg:'Deleted' };
  }

  function resetLevel(game){
    const level = deepCopy(game.levels[game.levelIndex]);
    game.level = level; game.board = createLevelState(level);
    game.sim = { running:false, accum:0, tick:0, step:0, steps: level.steps, lastValues:{}, compare:{} };
    game.message = 'Level reset';
    game.phase = 'play';
    return game;
  }

  function nextLevel(game){
    const ni = Math.min(game.levels.length-1, game.levelIndex+1);
    game.levelIndex = ni;
    const level = deepCopy(game.levels[ni]);
    game.level = level; game.board = createLevelState(level);
    game.sim = { running:false, accum:0, tick:0, step:0, steps: level.steps, lastValues:{}, compare:{} };
    game.message = `Level ${ni+1}`; game.phase='play';
    return game;
  }

  function startCampaign(game){ game.phase='play'; game.message='Build the circuit'; return game; }
  function startSandbox(game){ // unlock a sandbox board
    const level = { name:'Sandbox', targetDesc:'Free build', width: 18, height: 12, steps:8,
      inputs:[ { id:'A', label:'A', y:3, signal: Sig.pattern('10101010') }, { id:'B', label:'B', y:5, signal: Sig.pattern('11001100') } ],
      outputs:[ { id:'Q', label:'Q', y:4, desc:'Echo A', expected:(t,ins)=> ins.A(t) } ],
      toolbox: { AND:4, OR:4, NOT:4, XOR:4, DEL:4 }
    };
    game.level = level; game.board=createLevelState(deepCopy(level)); game.phase='play'; game.message='Sandbox'; return game;
  }

  function advance(prevGame, input, dt){
    // Pure: do not mutate prevGame
    let game = deepCopy(prevGame);
    // default: keep phase
    const actions = (input && input.actions) ? input.actions : [];
    for(const a of actions){
      switch(a.type){
        case 'StartCampaign': game = startCampaign(game); break;
        case 'StartSandbox': game = startSandbox(game); break;
        case 'PlaceGate': {
          const res = placeGate(game.board, a.gateType, a.pos); game.message = res.msg; break;
        }
        case 'Connect': {
          const res = connect(game.board, a.from, a.to); game.message = res.msg; break;
        }
        case 'RemoveWireAtInput': {
          const res = removeWireAtInput(game.board, a.nodeId, a.pin); game.message = res.msg; break;
        }
        case 'DeleteNode': {
          const res = deleteNode(game.board, a.nodeId); game.message = res.msg; break;
        }
        case 'ResetLevel': game = resetLevel(game); break;
        case 'NextLevel': game = nextLevel(game); break;
        case 'StartTest': game.sim.running = true; game.sim.accum=0; game.sim.tick=0; game.sim.step=0; game.message='Testing...'; break;
        case 'StopTest': game.sim.running = false; game.message='Stopped'; break;
        case 'Tick': default: break;
      }
    }

    // Tick simulation time
    const stepDur = 0.5; // seconds per tick
    if(game.sim.running){
      game.sim.accum += dt;
      while(game.sim.accum >= stepDur){
        game.sim.accum -= stepDur; game.sim.tick++;
        const sim = evaluateAt(game, game.sim.tick);
        game.sim.lastValues = sim.lastValues; game.sim.compare = sim.compare;
        // stop when reached steps
        if(game.sim.tick >= game.level.steps-1){
          // determine success
          let ok=true; for(const k in sim.compare){ if(!sim.compare[k].ok) { ok=false; break; } }
          if(ok){ game.phase='win'; game.sim.running=false; game.message='Level Complete'; game.justWon=true; }
          else { game.message='Mismatch — keep tweaking'; }
          break;
        }
      }
    } else {
      // still compute lastValues for static display
      const sim = evaluateAt(game, Math.max(0, game.sim.tick)); game.sim.lastValues = sim.lastValues; game.sim.compare = sim.compare;
    }
    return game;
  }

  function render(){ /* optional; we render in index.html */ }

  const api = { createGame, advance, render };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.GameLogic = api;
}(typeof window !== 'undefined' ? window : globalThis));
