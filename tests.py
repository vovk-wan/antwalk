# -*- coding=utf-8 -*-
import unittest

from main import (
    extract_number, check_point, get_neighboring_points, get_all_point)


class TestCaseAntWalk(unittest.TestCase):

    def test_extract_number(self):
        self.assertListEqual(extract_number(1234), [4, 3, 2, 1])

    def test_check_point(self):
        self.assertTrue(check_point((1, 1)))
        self.assertTrue(check_point((55, 555)))
        self.assertTrue(check_point((5, 125)))
        self.assertFalse(check_point((55, 556)))
        self.assertFalse(check_point((324532455, 556)))

    def test_get_neighboring_points(self):
        self.assertSetEqual(
            get_neighboring_points((1, 1)),
            {(1, 0), (1, 2), (0, 1), (2, 1)}
        )
        self.assertSetEqual(
            get_neighboring_points((10, 5)),
            {(10, 4), (10, 6), (9, 5), (11, 5)}
        )

    def test_get_all_point(self):
        expected = {
            (1002, 1000), (1003, 1000), (1001, 1000), (1001, 1001),
            (1000, 1002), (1000, 1001), (1000, 1000), (1001, 1002),
            (1000, 1003), (1002, 1001)
        }
        self.assertSetEqual(get_all_point((1000, 1000), 5), expected)
        expected = {
            (1002, 1000), (1003, 1002), (1002, 1003), (1001, 1003),
            (1002, 1002), (1003, 1000), (1004, 1001), (1001, 1000),
            (1003, 1001), (1001, 1001), (1000, 1002), (1000, 1001),
            (1000, 1000), (1002, 1001), (1005, 1000), (1000, 1005),
            (1000, 1004), (1001, 1002), (1000, 1003), (1001, 1004),
            (1004, 1000)
        }
        self.assertSetEqual(get_all_point((1000, 1000), 7), expected)


if __name__ == "__main__":
    unittest.main()
