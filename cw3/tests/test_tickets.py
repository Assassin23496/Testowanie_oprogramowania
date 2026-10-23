
"""Testy czarnoskrzynkowe: ticket_price (BL-1 ... BL-4)."""

import pytest
from sut import ticket_price


# EP – poprawne klasy równoważności
@pytest.mark.parametrize("age, expected", [
    (3, 0.0),
    (12, 10.0),
    (40, 20.0),
    (70, 10.0),
])
def test_ep_valid_classes(age, expected):
    assert ticket_price(age) == expected


# EP – wartości spoza zakresu
@pytest.mark.parametrize("age", [
    -5,
    125,
])
def test_ep_out_of_range(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# EP – niepoprawne typy danych
@pytest.mark.parametrize("age", [
    18.5,
    "18",
    None,
    True,
])
def test_ep_wrong_type(age):
    with pytest.raises(TypeError):
        ticket_price(age)


# AWB 2p – granice przedziałów
@pytest.mark.parametrize("age, expected", [
    (-1, ValueError),
    (0, 0.0),
    (6, 0.0),
    (7, 10.0),
    (18, 10.0),
    (19, 20.0),
    (64, 20.0),
    (65, 10.0),
    pytest.param(120, 10.0, marks=pytest.mark.xfail(reason="DEF-06", strict=True)),
    (121, ValueError),
])
def test_bva_2p(age, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            ticket_price(age)
    else:
        assert ticket_price(age) == expected


# AWB 3p – dodatkowe wartości
@pytest.mark.parametrize("age, expected", [
    (1, 0.0),
    (5, 0.0),
    (8, 10.0),
    (17, 10.0),
    (20, 20.0),
    (63, 20.0),
    (66, 10.0),
    pytest.param(119, 10.0, marks=pytest.mark.xfail(reason="DEF-06", strict=True)),
])
def test_bva_3p_extra(age, expected):
    assert ticket_price(age) == expected
