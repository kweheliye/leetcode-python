import pytest
from leet_code_python.arrays.valid_anagram_247 import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("abc", "cba", True),
    ],
)
def test_valid_anagram(s: str, t: str, expected: bool):
    sol = Solution()
    assert sol.is_anagram(s, t) == expected
