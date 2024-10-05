import pytest
from leet_code_python.arrays.contains_duplicate_217 import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 1], True),
        ([], False),
        ([10], False),
    ],
)
def test_contains_duplicate(nums, expected):
    sol = Solution()
    assert sol.contains_duplicate(nums) == expected
