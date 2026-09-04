'use strict';
const fs = require('fs');
const path = require('path');
const tests = [];
function test(name, fn){ tests.push({name, fn}); }
function assert(cond, msg){ if(!cond) throw new Error(msg||'assert failed'); }
function assertEq(a,b,msg){ if(a!==b) throw new Error((msg||'not equal')+`: ${a} !== ${b}`); }
function assertApprox(a,b,eps,msg){ eps = eps||1e-6; if(Math.abs(a-b)>eps) throw new Error((msg||'not approx')+`: ${a} ~ ${b}`); }

// expose globals for test files
global.test = test; global.assert = assert; global.assertEq = assertEq; global.assertApprox = assertApprox;

// load test files
require('./test_game_logic.js');

(async function(){
  let pass=0, fail=0; const results=[]; const start=Date.now();
  for(const t of tests){
    const t0=Date.now();
    try{ await t.fn(); pass++; results.push({name:t.name, status:'pass', ms:Date.now()-t0}); }
    catch(e){ fail++; results.push({name:t.name, status:'fail', error:e.message, ms:Date.now()-t0}); }
  }
  const dur = Date.now()-start;
  console.log(`Tests: ${pass+fail}, Passed: ${pass}, Failed: ${fail}, Time: ${dur}ms`);
  for(const r of results){ console.log(`- ${r.status.toUpperCase()} ${r.name} (${r.ms}ms)${r.error? ' :: '+r.error:''}`); }
  fs.writeFileSync(path.join(__dirname,'results.json'), JSON.stringify({summary:{pass,fail,durationMs:dur}, results}, null, 2));
  process.exit(fail?1:0);
})();
