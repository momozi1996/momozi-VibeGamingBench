#!/usr/bin/env python3
"""Repository entry point for the automatic evaluation harness."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momozi.auto_eval import main


if __name__ == "__main__":
    raise SystemExit(main())
