import unittest

from src.package.linearize_package import LinearizePackage


class LinearizePackageTest(unittest.TestCase):
    def setUp(self):
        self.package = LinearizePackage(("127.0.0.1", 5000), 3.14)
        self.package_parsed = LinearizePackage.from_json(self.package.package_json)

    def test_content(self):
        self.assertEqual(self.package.package_type, "linearize")
        self.assertEqual(self.package.address, "127.0.0.1")
        self.assertEqual(self.package.port, 5000)
        self.assertEqual(self.package.position, 3.14)
        self.assertEqual(self.package_parsed.package_type, "linearize")
        self.assertEqual(self.package_parsed.address, "127.0.0.1")
        self.assertEqual(self.package_parsed.port, 5000)
        self.assertEqual(self.package_parsed.position, 3.14)


if __name__ == '__main__':
    unittest.main()
