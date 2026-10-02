import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import check_canonical


class CanonicalTests(unittest.TestCase):
    def run_check(self, entries, canonical=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            locs = "".join(f"<url><loc>{url}</loc></url>" for url in entries)
            (root / "sitemap.xml").write_text(
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + locs + "</urlset>",
                encoding="utf-8",
            )
            if canonical is not None:
                (root / "guide.html").write_text(
                    f'<link rel="canonical" href="{canonical}">', encoding="utf-8"
                )
            with patch.object(check_canonical, "ROOT", root), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                return check_canonical.check()

    def test_matching_clean_url(self):
        url = check_canonical.HOST + "/guide"
        self.assertEqual(self.run_check([url], url), 0)

    def test_redirect_alias_is_rejected(self):
        url = check_canonical.HOST + "/guide.html"
        self.assertEqual(self.run_check([url], url), 1)

    def test_wrong_canonical_is_rejected(self):
        self.assertEqual(self.run_check([check_canonical.HOST + "/guide"], check_canonical.HOST + "/other"), 1)

    def test_missing_target_is_rejected(self):
        self.assertEqual(self.run_check([check_canonical.HOST + "/guide"]), 1)

    def test_duplicate_is_rejected(self):
        url = check_canonical.HOST + "/guide"
        self.assertEqual(self.run_check([url, url], url), 1)
