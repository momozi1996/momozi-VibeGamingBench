# Agent Harness Contract

VibeGamingBench treats an **Agent Harness** as the execution carrier for the
coding agent under evaluation. The harness may invoke any model or agent
runtime, but the benchmark owns task selection, artifact collection,
deterministic checks, runtime smoke, scoring, and statistical aggregation.

## Required Outcome

For each task, the harness must create these files in the supplied product
directory:

```text
{product_dir}/index.html
{product_dir}/game_logic.js
```

`index.html` must contain the browser game entry point and a Canvas/WebGL
rendering signal. `game_logic.js` must export:

```javascript
export function createGame(opts) {}
export function advance(game, input, dt) {}
```

The rules layer should remain independent of DOM and rendering code so the
public Node behavior suite can import it deterministically.

## Command Contract

Pass a command template with `--harness-command`. The command is tokenized
without invoking a shell and may use these placeholders:

| Placeholder | Meaning |
|---|---|
| `{prompt_file}` | Absolute path to the current single-language prompt |
| `{product_dir}` | Absolute directory where the two artifact files must be written |
| `{workspace}` | Isolated task workspace |
| `{task_file}` | Absolute path to the task YAML |
| `{task_id}` | Current task ID |

Example:

```bash
python3 scripts/auto_evaluate.py \
  --task mz_sports-fishing-tournament-en \
  --harness-command 'my-harness --prompt {prompt_file} --output {product_dir}' \
  --model-label my-agent \
  --harness-label my-harness
```

The benchmark also exports the same values as environment variables:

```text
MOMOZI_PROMPT_FILE
MOMOZI_PRODUCT_DIR
MOMOZI_WORKSPACE
MOMOZI_TASK_FILE
MOMOZI_TASK_ID
```

The harness should return exit code `0` only after artifact delivery is
complete. Standard output and standard error are retained as bounded
generation evidence; secrets must not be printed.

## Submission Metadata

The runner records:

```text
agent.name
agent.version
agent.model
agent.model_version
agent.harness
```

When available, include temperature, maximum steps/time, internet access,
token usage, tool-call count, wall-clock time, and estimated cost in the
harness-side metadata. Cost is diagnostic and is not a primary benchmark score.

## Isolation and Network

Each task receives an isolated workspace. The harness may use its own model
service, but generated browser artifacts are evaluated with a local HTTP server
and a fixed Chromium context:

```yaml
viewport: 1280x720
locale: en-US
timezone: UTC
device_scale_factor: 1
network: disabled by default
```

Pinned Three.js CDN references allowed by the task contract may be permitted;
all other external runtime requests are blocked by default.

## Evaluation Boundary

The harness is not responsible for assigning benchmark scores. VibeGamingBench
performs:

1. Static BUILD and contract evaluation.
2. Dynamic runtime smoke and screenshot capture.
3. Code and screenshot-grounded judge calls.
4. Score fusion, hard caps, balanced aggregation, and confidence intervals.

Dynamic evaluation is intentionally lightweight. A runtime pass means the page
loaded, remained alive during the bounded observation window, accepted the
generic probe when enabled, and produced a screenshot. It does not establish
full gameplay competence.

## Failure Handling

The runner records structured failure codes such as
`STATIC_BUILD_FAIL`, `STATIC_CONTRACT_FAIL`, `D_SERVER_START_FAIL`,
`D_PAGE_LOAD_FAIL`, `D_RUNTIME_FATAL`, `D_TIMEOUT`, `D_SCREENSHOT_FAIL`,
`JUDGE_FAIL`, and `SCHEMA_FAIL`. A harness failure is preserved in generation
evidence and cannot be hidden by a later subjective score.
