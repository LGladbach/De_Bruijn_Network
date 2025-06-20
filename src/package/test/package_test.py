import unittest
from src.package.package import Package


class PackageTest(unittest.TestCase):
    def setUp(self):
        self.package = Package("This is a type", "This should be data")
        self.package_parsed = Package.from_json(self.package.package_json)

    def test_content(self):
        self.assertEqual(self.package.package_type, "This is a type")
        self.assertEqual(self.package.package_data, "This should be data")
        self.assertEqual(self.package_parsed.package_type, "This is a type")
        self.assertEqual(self.package_parsed.package_data, "This should be data")


if __name__ == '__main__':
    unittest.main()
