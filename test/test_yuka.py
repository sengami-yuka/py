import unittest


class TestYuka(unittest.TestCase):
    def test_yuka(self):
        self.assertEqual(True, False)

    def test_yuka2(self):
        self.assertEqual(1, 1)

    def test_yuka3(self):
        self.assertLess(1, 2)

    def test_yuka4(self):
        self.assertGreaterEqual(33, 33)

    def test_yuka5(self):
        self.assertGreaterEqual(44, 33)

    def test_yuka6(self):
        self.assertGreaterEqual(55, 33)

    def test_yuka7(self):
        self.assertGreaterEqual(44, 33)

    def test_yuka8(self):
        self.assertGreaterEqual(44, 33)
        self.assertGreaterEqual(33, 33)


if __name__ == '__main__':
    unittest.main()
