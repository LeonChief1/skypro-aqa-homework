import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize( 'string, result', [("skypro", "Skypro"), ("", ""), (" ", " "), ("Skypro", "Skypro"), ("123", "123"), ("04 april 2024", "04 april 2024")])
def test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize( 'string, result', [("   skypro", "skypro"), ("skypro", "skypro"), ("skypro ", "skypro "), ("skypro skypro", "skypro skypro"), ("", ""), (" ", "")])
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

@pytest.mark.parametrize( 'string, delimiter, result', [
    ('a,b,c,d', ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", "", []),
    ("a b c d", " ", ["a", "b", "c", "d"]),
    ("   ", ",", []),
    ("12:35:35", ":", ["12", "35", "35"])
])
def test_to_list(string, delimiter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimiter)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ('skypro', 's', True),
    ('skypro', 'b', False),
    ('', '', True),
    (' ', ' ', True),
    (' skypro', ' ', True)
])
def test_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ('skypro', 's', 'kypro'),
    ('skypro', 'b', 'skypro'),
    ('', '', ''),
    (' ', ' ', ' '),
    (' skypro', ' ', 'skypro'),
    ('skypro', 'pro', 'sky'),
    ('skypro', 'S', 'kypro')
])
def test_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ('skypro', 's', True),
    ('Skypro', 's', True),
    ('Skypro', 'p', False),
    ('Skypro', 'P', False),
    ('', '', True),
    (' ', ' ', True),
    (' ', '', False)
])
def test_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ('skypro', 's', False),
    ('skypro', 'o', True),
    ('skyprO', 'o', True)
])
def test_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [
    ('skypro', False),
    ('', True),
    (' ', True),
    (' skypro skypro', False)
])
def test_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('list, joiner, result', [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", ""),
    ([1], ", ", "1"),
    ([1, 2, 3], "; ", "1; 2; 3"),
    (["a", "b", "c"], "", "abc")
])
def test_list_to_string(list, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(list, joiner)
    assert res == result