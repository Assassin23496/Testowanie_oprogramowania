
"""Testy czarnoskrzynkowe: validate_password."""

import pytest
from sut import validate_password


# EP – poprawne hasła
@pytest.mark.parametrize("password", [
    "haslo123",
    pytest.param("haslo12!", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("moje haslo1", marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
    "żółw1234",
])
def test_ep_valid_classes(password):
    assert validate_password(password) is True


# EP – niepoprawne hasła
@pytest.mark.parametrize("password", [
    "abc123",
    "abcdefghij12345678901",
    "12345678",
    "abcdefgh",
])
def test_ep_invalid_classes(password):
    assert validate_password(password) is False


# EP – niepoprawne typy danych
@pytest.mark.parametrize("password", [
    12345678,
    None,
    True,
])
def test_ep_wrong_type(password):
    with pytest.raises(TypeError):
        validate_password(password)


# AWB 2p – granice długości hasła
@pytest.mark.parametrize("password, expected", [
    ("abc1234", False),                # 7 znaków
    ("abc12345", True),                # 8 znaków
    ("abcdefghij1234567890", True),    # 20 znaków
    ("abcdefghij12345678901", False),  # 21 znaków
])
def test_bva_2p(password, expected):
    assert validate_password(password) is expected


# AWB 3p – wartości dodatkowe
@pytest.mark.parametrize("password, expected", [
    ("abc123", False),                 # 6 znaków
    ("abc123456", True),               # 9 znaków
    ("abcdefghij123456789", True),     # 19 znaków
    ("abcdefghij123456789012", False), # 22 znaki
])
def test_bva_3p_extra(password, expected):
    assert validate_password(password) is expected

def test_password_20_polish_chars():
    password = "żółw1234abcdefghij12"
    assert len(password) == 20
    assert validate_password(password) is True



# Each Choice – minimalny zestaw przypadków
@pytest.mark.parametrize("password, expected", [
    ("abc123", False),       # za krótkie
    ("abc12345", True),      # poprawne
    ("abcdefghij12345678901", False),  # za długie
    ("abcdefgh", False),     # bez cyfry
    ("12345678", False),     # bez litery
    ("żółw1234", True),      # polskie litery
    pytest.param(
        "haslo12!",
        True,
        marks=pytest.mark.xfail(reason="DEF-04", strict=True)
    ),
    pytest.param(
        "moje haslo1",
        True,
        marks=pytest.mark.xfail(reason="DEF-05", strict=True)
    ),
])
def test_each_choice_password(password, expected):
    assert validate_password(password) is expected

