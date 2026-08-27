#!/bin/bash
# 端到端冒烟测试：mock 参考实现应得满结构+全行为通过。
set -e
cd "$(dirname "$0")/.."
echo "== behavior suite on reference =="
node bench/tests/beh_behavior.mjs bench/references/tg1
echo "== mock end-to-end =="
python3 -m momozi run bench/tasks/tg1_paddle_breakout/tg1_paddle_breakout.task.yaml --agent mock \
  | python3 -c "import sys,json; d=json.load(sys.stdin); s=d['scores']; assert s['B']==1.0, s; assert s['S']==1.0, s; print('OK B=%.2f S=%.2f' % (s['B'], s['S']))"
echo "== syntax =="
python3 -c "import momozi.run, momozi.judge, momozi.leaderboard, momozi.verify; print('python imports ok')"
