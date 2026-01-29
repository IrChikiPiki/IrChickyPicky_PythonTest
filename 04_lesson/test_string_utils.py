import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" 123", "123"),
    ("   ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("sky pro", "sky pro"),
    (" 123 ", "123 "),
    ("__", "__"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (["SkyPro", "S"], True),
    (["SkyPro", "U"], False),
    (["Sky Pro", " "], True),
])
def test_contains_positve(input_str, expected):
    assert string_utils.contains(input_str[0], input_str[1]) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (["SkyPro", "s"], False),
    (["SkyPro", "pro"], False),
    (["Sky Pro !", "!"], True),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str[0], input_str[1]) == expected