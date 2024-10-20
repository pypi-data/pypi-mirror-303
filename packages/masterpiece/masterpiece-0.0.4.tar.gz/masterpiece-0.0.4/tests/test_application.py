import unittest
import tempfile
import os

from masterpiece.core import MasterPiece, Composite, Application


class TestApplication(unittest.TestCase):
    """Unit tests for `Application` class."""

    def test_get_classid(self):
        """Assert that the meta-class driven class initialization works."""
        classid = Application.get_class_id()
        self.assertEqual("Application", classid)

    def test_serialization(self):
        """Test serialization"""

        application = Application("testapp")
        composite = Composite("mycomposite")
        child1 = MasterPiece("child1")
        composite.add(child1)
        application.add(composite)

        #  make sure the hierarchy is what we expect
        self.assertEqual(1, len(application.children))

        # serialize
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "application.json")

            with open(filename, "w") as f:
                application.serialize_to_json(f)

            # deserialize
            application2 = Application("bar")
            with open(filename, "r") as f:
                application2.deserialize_from_json(f)
            self.assertEqual("testapp", application2.name)
            #  make sure the hierarchy is what we expect
            self.assertEqual(1, len(application2.children))


if __name__ == "__main__":
    unittest.main()
