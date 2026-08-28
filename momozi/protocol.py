"""L1 契约行为套件协议：node 脚本读 env.ARTIFACT，stdout JSON 数组。
[{id, ok, detail}, ...] — harness 消费通过率与回归。
通用两文件契约套件放在 bench/tests/beh_html.mjs；专项套例放 tasks/<id>/tests/。
"""

BEHAVIOR_PROTOCOL_VERSION = 1
RUNNER_ARGS = ["node", "<script.mjs>", "<artifact_dir>"]
OUTPUT_FORMAT = [
    {"id": "B0_xxx", "ok": "true|false", "detail": "string"},
]
