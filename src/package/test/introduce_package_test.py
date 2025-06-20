import unittest

from src.package.introduce_package import IntroducePackage


class IntroducePackageTest(unittest.TestCase):
    def setUp(self):
        self.package = IntroducePackage(False)
        self.package_parsed = IntroducePackage.from_json(self.package.package_json)

    def test_content(self):
        self.assertEqual(self.package.package_type, "introduce")
        self.assertEqual(self.package.rl, False)
        self.assertEqual(self.package_parsed.package_type, "introduce")
        self.assertEqual(self.package_parsed.rl, False)

if __name__ == '__main__':
    unittest.main()
