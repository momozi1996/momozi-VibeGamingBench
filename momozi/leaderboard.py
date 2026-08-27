"""Leaderboard 生成：扫 runs/ 下所有 *.<agent>.json 聚合。"""
from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict


def _load_runs(results_dir: str):
    rows = []
    for f in sorted(Path(results_dir).rglob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if "scores" in data and "task" in data:
            rows.append(data)
    return rows


def build_leaderboard(results_dir: str = "runs"):
    rows = _load_runs(results_dir)
    by_agent = defaultdict(list)
    for r in rows:
        by_agent[r.get("agent", "?")].append(r)

    leaderboard = []
    for agent, rs in by_agent.items():
        B = sum(r["scores"]["B"] for r in rs) / len(rs)
        S = sum(r["scores"]["S"] for r in rs) / len(rs)
        P_vals = [r["scores"]["P"] for r in rs if r["scores"].get("P") is not None]
        P = (sum(P_vals) / len(P_vals)) if P_vals else None
        # 总分：P 缺失时按剩余 0.75 归回统一
        if P is None:
            total = (B * 0.55 + S * 0.20) / 0.75
        else:
            total = B * 0.55 + S * 0.20 + P * 0.25
        leaderboard.append({
            "agent": agent,
            "runs": len(rs),
            "B_mean": round(B, 4),
            "S_mean": round(S, 4),
            "P_mean": round(P, 4) if P is not None else None,
            "total": round(total, 4),
        })
    leaderboard.sort(key=lambda x: x["total"], reverse=True)
    return {"leaderboard": leaderboard, "n_runs": len(rows)}


def to_markdown(data: dict) -> str:
    lb = data.get("leaderboard", [])
    if not lb:
        return "# Leaderboard\n\n（暂无结果）\n"
    head = ["| 排名 | agent | total | B(行为) | S(结构) | P(呈现) | runs |",
            "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(lb, 1):
        p = r["P_mean"]
        head.append(f"| {i} | `{r['agent']}` | **{r['total']:.4f}** | {r['B_mean']:.4f} | {r['S_mean']:.4f} | {('%.4f'%p) if p is not None else '—'} | {r['runs']} |")
    return "# momozi-3A-GamegenBench Leaderboard\n\n" + "\n".join(head) + "\n"


if __name__ == "__main__":
    import sys
    data = build_leaderboard(sys.argv[1] if len(sys.argv) > 1 else "runs")
    print(to_markdown(data))
