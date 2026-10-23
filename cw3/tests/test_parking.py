
"""Testy czarnoskrzynkowe: parking_fee (PK-1 ... PK-5)."""

import pytest
from sut import parking_fee


# EP – poprawne klasy równoważności
@pytest.mark.parametrize("minutes, fee", [
    (10, 0.0),
    (30, 5.0),
    (90, 10.0),
    (150, 15.0),
    (600, 20.0),
])
def test_ep_valid_classes(minutes, fee):
    assert parking_fee(minutes) == fee


# EP – wartości spoza zakresu
@pytest.mark.parametrize("minutes", [
    -10,
    1500,
])
def test_ep_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)


# EP – niepoprawne typy danych
@pytest.mark.parametrize("minutes", [
    15.5,
    "60",
    None,
    True,
])
def test_ep_wrong_type(minutes):
    with pytest.raises(TypeError):
        parking_fee(minutes)


# AWB 2p – granice przedziałów
@pytest.mark.parametrize("minutes, expected", [
    (-1, ValueError),
    (0, 0.0),
    (15, 0.0),
    (16, 5.0),
    (60, 5.0),
    (61, 10.0),
    (120, 10.0),
    (121, 15.0),
    (180, 15.0),
    (181, 20.0),
    (1440, 20.0),
    (1441, ValueError),
])
def test_bva_2p(minutes, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            parking_fee(minutes)
    else:
        assert parking_fee(minutes) == expected


# AWB 3p – dodatkowe wartości obok granic
@pytest.mark.parametrize("minutes, expected", [
    pytest.param(1, 0.0, marks=pytest.mark.xfail(reason="DEF-03", strict=True)),
    (14, 0.0),
    (17, 5.0),
    (59, 5.0),
    (62, 10.0),
    (119, 10.0),
    (122, 15.0),
    (179, 15.0),
    (182, 20.0),
    (1439, 20.0),
])
def test_bva_3p_extra(minutes, expected):
    assert parking_fee(minutes) == expected
