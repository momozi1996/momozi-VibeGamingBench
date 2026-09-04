// Generic two-file browser-game contract check.
// Usage: node beh_html.mjs <product_dir>
import { pathToFileURL } from 'node:url';
import { readFile } from 'node:fs/promises';
import vm from 'node:vm';

const product = process.argv[2];
const results = [];
const record = (id, ok, detail) => results.push({ id, ok, detail });

if (!product) {
  record('artifact_argument', false, 'missing product directory argument');
  console.log(JSON.stringify(results));
  process.exit(0);
}

let logic;
try {
  logic = await import(pathToFileURL(`${product}/game_logic.js`).href);
} catch (error) {
  logic = null;
}

// A classic script is intentionally supported so artifacts work from file://
// without the browser's ES-module CORS restriction.
if (!logic || typeof logic.createGame !== 'function' || typeof logic.advance !== 'function') {
  try {
    const source = await readFile(`${product}/game_logic.js`, 'utf8');
    const context = { console };
    context.window = context;
    context.globalThis = context;
    vm.runInNewContext(source, context, {
      filename: `${product}/game_logic.js`,
    });
    logic = context.GameLogic || context.module?.exports || {};
  } catch (error) {
    record('logic_import', false, error.message);
    console.log(JSON.stringify(results));
    process.exit(0);
  }
}

record('exports_create_game', typeof logic.createGame === 'function', 'createGame export');
record('exports_advance', typeof logic.advance === 'function', 'advance export');

if (typeof logic.createGame === 'function' && typeof logic.advance === 'function') {
  try {
    const initial = logic.createGame({});
    const next = logic.advance(initial, {}, 1 / 60);
    record('state_is_object', initial !== null && typeof initial === 'object', 'initial state');
    record('advance_returns_state', next !== null && typeof next === 'object', 'next state');
  } catch (error) {
    record('logic_smoke', false, error.message);
  }
}

console.log(JSON.stringify(results));
