import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check


class TestDriverVersions(unittest.TestCase):
    def test_current_is_ok(self):
        self.assertEqual(check("HP-LaserJet-M404", "2.1")[0], "OK")

    def test_old_is_outdated(self):
        self.assertEqual(check("HP-LaserJet-M404", "1.9")[0], "OUTDATED")

    def test_unknown_model(self):
        self.assertEqual(check("Mystery-9", "9.9")[0], "UNKNOWN")

    def test_unparsable_version(self):
        self.assertEqual(check("HP-LaserJet-M404", "beta")[0], "UNKNOWN")
