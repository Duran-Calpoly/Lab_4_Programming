"""CS 1001 - Lab Programming 4: Searching Algorithms

Starter unit tests for day1.py.

These tests will fail with NotImplementedError until you complete the TODOs.
Add MULTIPLE additional tests for EACH task, including boundary cases.
Use self.assertEqual(...) rather than bare assert statements.

Run with: python -m unittest test_1.py
"""

import unittest

from day1 import find, is_descending, index_of_largest, largest_between


class TestFind(unittest.TestCase):
    def test_first_occurrence(self):
        self.assertEqual(1, find([4, 9, 2, 9, 5], 9))

    def test_target_absent(self):
        self.assertEqual(None, find([4, 9, 2, 9, 5], 7))

    # TODO: Add tests for a target at the beginning/end, an empty list,
    # and a search that leaves the input unchanged.


class TestIsDescending(unittest.TestCase):
    def test_strictly_descending(self):
        self.assertEqual(True, is_descending([9.0, 7.0, 4.0, 1.0]))

    def test_equal_adjacent_values(self):
        self.assertEqual(False, is_descending([9.0, 7.0, 7.0, 1.0]))

    # TODO: Add tests for an empty list, a single element, two elements,
    # and a violation near either end of a list.


class TestIndexOfLargest(unittest.TestCase):
    def test_largest_in_middle(self):
        self.assertEqual(1, index_of_largest([4, 9, 2, 7]))

    def test_first_of_repeated_largest(self):
        self.assertEqual(1, index_of_largest([4, 9, 2, 9]))

    # TODO: Add tests for the largest at the beginning/end, negative values,
    # a single-element list, an empty list, and unchanged inputs.


class TestLargestBetween(unittest.TestCase):
    def test_inclusive_range(self):
        self.assertEqual(4, largest_between([8, 3, 12, 7, 15, 4], 1, 4))

    def test_lower_greater_than_upper(self):
        self.assertEqual(None, largest_between([8, 3, 12, 7], 3, 1))

    # TODO: Add tests for a one-index range, out-of-bounds indexes,
    # a range outside the list, an empty list, and duplicate maxima.


if __name__ == "__main__":
    unittest.main()
