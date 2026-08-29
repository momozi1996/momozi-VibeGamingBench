import unittest

from momozi.scoring import fuse_scores


class ScoringTests(unittest.TestCase):
    def test_weights_sum_to_one_and_raw_score(self):
        result = fuse_scores(
            static_score=100,
            dynamic_score=100,
            visual_score=100,
            design_score=100,
        )
        self.assertEqual(result["raw"], 100.0)
        self.assertEqual(result["final"], 100.0)

    def test_build_cap(self):
        result = fuse_scores(
            static_score=100,
            dynamic_score=100,
            visual_score=100,
            design_score=100,
            failure_codes=["STATIC_BUILD_FAIL"],
        )
        self.assertEqual(result["final"], 20.0)
        self.assertEqual(result["hard_cap"]["code"], "STATIC_BUILD_FAIL")

    def test_page_load_cap_has_precedence(self):
        result = fuse_scores(
            static_score=100,
            dynamic_score=100,
            visual_score=100,
            design_score=100,
            failure_codes=["STATIC_BUILD_FAIL", "D_PAGE_LOAD_FAIL"],
        )
        self.assertEqual(result["final"], 10.0)

    def test_server_start_cap_matches_boot_failure(self):
        result = fuse_scores(
            static_score=100,
            dynamic_score=100,
            visual_score=100,
            design_score=100,
            failure_codes=["D_SERVER_START_FAIL"],
        )
        self.assertEqual(result["final"], 10.0)


if __name__ == "__main__":
    unittest.main()
