"""momozi CLI: run (评测一个任务) / leaderboard (生成榜单)。"""
from __future__ import annotations
import argparse

from .run import run_task


def _cli():
    p = argparse.ArgumentParser(prog="momozi")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="跑一个任务：python -m momozi run <task.yaml>")
    r.add_argument("task")
    r.add_argument("--agent", default="mock")
    r.add_argument("--out", default=None)
    r.add_argument("--rounds", default=None)
    r.add_argument("--judge-agent", default=None)
    r.add_argument("--skip-judge", action="store_true")

    s = sub.add_parser("leaderboard", help="从 agent-v2/legacy 结果生成排行榜")
    s.add_argument("--results-dir", default="runs")
    s.add_argument("--out", default="leaderboard.json")
    s.add_argument("--markdown-out", default="LEADERBOARD.md")

    args = p.parse_args()
    if args.cmd == "run":
        run_task(args.task, args.agent, args.out,
                 rounds_filter=args.rounds.split(",") if args.rounds else None,
                 skip_judge=args.skip_judge, judge_agent=args.judge_agent)
    elif args.cmd == "leaderboard":
        from .leaderboard import write_leaderboard
        data = write_leaderboard(args.results_dir, args.out, args.markdown_out)
        print(f"wrote {args.out} ({data['n_runs']} runs)")
    return 0
