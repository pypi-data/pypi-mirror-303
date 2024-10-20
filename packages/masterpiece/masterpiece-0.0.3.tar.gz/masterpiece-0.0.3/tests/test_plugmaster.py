import unittest
import tempfile
import os

from masterpiece.core import MasterPiece, Composite, PlugMaster


class TestPlugMaster(unittest.TestCase):
    """Unit tests for `Application` class."""

    def test_get_classid(self):
        """Assert that the meta-class driven class initialization works."""
        classid = PlugMaster.get_class_id()
        self.assertEqual("PlugMaster", classid)


if __name__ == "__main__":
    unittest.main()
