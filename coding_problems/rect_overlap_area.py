import unittest
import collections


Rect = collections.namedtuple('Rect', ['x1', 'y1', 'x2', 'y2'])


def overlap_area(r1, r2):
    return max(0, min(r1.x2, r2.x2) - max(r1.x1, r2.x1)) * max(0, min(r1.y2, r2.y2) - max(r1.y1, r2.y1))


class MyTest(unittest.TestCase):
    def test_not_overlap(self):
        area = overlap_area(Rect(0, 0, 2, 2), Rect(3, 3, 5, 5))
        self.assertEqual(area, 0)

    def test_overlap(self):
        area = overlap_area(Rect(0, 0, 3, 3), Rect(1, 2, 5, 5))
        self.assertEqual(area, 2)

        area = overlap_area(Rect(0, 0, 3, 3), Rect(0, 0, 5, 5))
        self.assertEqual(area, 9)

        area = overlap_area(Rect(0, 0, 3, 3), Rect(1, 1, 2, 2))
        self.assertEqual(area, 1)


if __name__ == '__main__':
    unittest.main()
