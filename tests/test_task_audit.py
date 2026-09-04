import tempfile
import unittest
from pathlib import Path

from scripts.audit_tasks import audit_tasks


class TaskAuditTests(unittest.TestCase):
    def test_current_pool_audit(self):
        root = Path(__file__).resolve().parents[1] / "bench" / "tasks"
        data = audit_tasks(root)
        self.assertEqual(data["status"], "pass")
        self.assertEqual(data["concept_count"], 711)
        self.assertEqual(data["task_count"], 1422)


if __name__ == "__main__":
    unittest.main()
