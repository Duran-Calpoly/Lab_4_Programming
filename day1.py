"""CS 1001 - Lab Programming 4: Searching Algorithms

Friday, November 6, 2026

Complete the TODO bodies below. Do not change the function signatures.
Use loops and conditionals to perform the searches yourself; do not use
list.index(), max(), or other built-in functions to perform the search.
Do not modify the input lists.
"""


def find(values: list[int], target: int) -> int | None:
    """Return the index of the first occurrence of target, or None if absent.

    Examples:
        find([4, 9, 2, 9, 5], 9) returns 1
        find([4, 9, 2, 9, 5], 7) returns None
    """
    # TODO (Task 1): Implement a search for the first occurrence.
    raise NotImplementedError


def is_descending(values: list[float]) -> bool:
    """Return True if values are in strictly descending order.

    Each element after the first must be smaller than its predecessor.
    Equal adjacent elements do not satisfy the condition.
    An empty or one-element list returns True.
    """
    # TODO (Task 2): Check adjacent values for a violation of the rule.
    raise NotImplementedError


def index_of_largest(values: list[int]) -> int | None:
    """Return the index of the largest value, or None for an empty list.

    If the largest value occurs more than once, return its first index.
    """
    # TODO (Task 3): Track the index of the largest value seen so far.
    raise NotImplementedError


def largest_between(values: list[int], lower: int, upper: int) -> int | None:
    """Return the index of the largest value in the inclusive index range.

    Return the first index within the range if the largest value repeats.
    Return None if the list is empty, lower > upper, or no valid indexes
    remain after adjusting the bounds. Clamp lower below 0 to 0 and upper
    beyond the end of the list to len(values) - 1.
    """
    # TODO (Task 4): Adjust boundaries and search the valid index range.
    raise NotImplementedError
