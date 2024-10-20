import unittest
import tempfile
import os
from masterpiece.core import MasterPiece


class TestMasterPiece(unittest.TestCase):
    """Unit tests for `MasterPiece` class."""

    def test_get_classid(self):
        classid = MasterPiece.get_class_id()
        self.assertEqual("MasterPiece", classid)

    def test_serialization(self):
        mp = MasterPiece("foo")

        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "masterpiece.json")
            with open(filename, "w") as f:
                mp.serialize_to_json(f)
            mp2 = MasterPiece("bar")
            with open(filename, "r") as f:
                mp2.deserialize_from_json(f)
            self.assertEqual("foo", mp2.name)
            self.assertIsNone(mp2.payload)

    def test_serialization_with_payload(self):
        payload = MasterPiece("bar")
        mp = MasterPiece("foo", payload)

        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "masterpiece.json")
            with open(filename, "w") as f:
                mp.serialize_to_json(f)
            mp2 = MasterPiece("bar")
            with open(filename, "r") as f:
                mp2.deserialize_from_json(f)
            self.assertEqual("foo", mp2.name)
            self.assertIsNotNone(mp2.payload)
            self.assertEqual("bar", mp2.payload.name)


if __name__ == "__main__":

    unittest.main()
