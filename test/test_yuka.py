import unittest


class TestYuka(unittest.TestCase):
    def test_yuka(self):
        self.assertEqual(True, False)

    def test_yuka2(self):
        self.assertEqual(1, 1)

    def test_yuka3(self):
        self.assertLess(1, 2)


if __name__ == '__main__':
    unittest.main()
