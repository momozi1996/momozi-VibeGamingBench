"""Static evaluation wrapper preserving the existing BUILD and contract paths."""
from __future__ import annotations

from pathlib import Path

from .run import ROOT
from .run_zhen import build_gate_product
from .verifiers import BehaviorSuite


STATIC_EVALUATOR_VERSION = "1.0"


class StaticEvaluator:
    """Expose artifact and API contract evidence independently of runtime."""

    version = STATIC_EVALUATOR_VERSION

    def evaluate(self, task, product_dir: Path) -> dict:
        # BehaviorSuite uses its workspace as the subprocess cwd. Resolve the
        # artifact first so a caller passing a relative path does not make the
        # suite look for ``product_dir/product_dir/game_logic.js``.
        product_dir = Path(product_dir).resolve()
        build = build_gate_product(product_dir)
        suite_name = task.behavior.get("script", "beh_html.mjs")
        local_suite = product_dir / suite_name
        public_suite = ROOT / "bench" / "tests" / Path(suite_name).name
        script_path = local_suite if local_suite.exists() else public_suite
        suite = BehaviorSuite(
            product_dir,
            suite_name,
            timeout=int(task.behavior.get("timeout", 300)),
            artifact_dir=product_dir,
            script_path=script_path,
        )
        results = suite.run()
        passed = sum(1 for item in results if item.get("ok"))
        total = len(results)
        contract = {
            "pass_rate": round(passed / total, 6) if total else 0.0,
            "passed": passed,
            "total": total,
            "results": results,
        }
        failures = []
        if not build["ok"]:
            failures.append(
                {
                    "code": "STATIC_BUILD_FAIL",
                    "detail": build.get("detail", "static BUILD gate failed"),
                }
            )
        if contract["pass_rate"] < 1.0:
            failures.append(
                {
                    "code": "STATIC_CONTRACT_FAIL",
                    "detail": (
                        f"{contract['passed']}/{contract['total']} contract checks passed"
                    ),
                }
            )
        return {
            "version": self.version,
            "status": "pass" if not failures else "fail",
            "build": build,
            "contract": contract,
            "failure_details": failures,
        }
