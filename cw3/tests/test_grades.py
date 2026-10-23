
"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""

import pytest
from sut import grade_from_percent


# EP – poprawne klasy równoważności
@pytest.mark.parametrize("percent, grade", [
    (25, 2.0),
    (55, 3.0),
    (65, 3.5),
    (75, 4.0),
    (85, 4.5),
    (95, 5.0),
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# EP – wartości spoza zakresu
@pytest.mark.parametrize("percent", [
    -10,
    110,
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# EP – niepoprawne typy danych
@pytest.mark.parametrize("percent", [
    pytest.param(50.5, marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param("50", marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    None,
    pytest.param(True, marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
])

def test_ep_wrong_type(percent):
    with pytest.raises(TypeError):
        grade_from_percent(percent)


# AWB 2p – wartości na granicach przedziałów
@pytest.mark.parametrize("percent, expected", [
    (-1, ValueError),
    (0, 2.0),
    (50, 2.0),
    (51, 3.0),
    (60, 3.0),
    (61, 3.5),
    (70, 3.5),
    (71, 4.0),
    (80, 4.0),
    (81, 4.5),
    pytest.param(90, 4.5, marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    (91, 5.0),
    (100, 5.0),
    (101, ValueError),
])
def test_bva_2p(percent, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            grade_from_percent(percent)
    else:
        assert grade_from_percent(percent) == expected


# AWB 3p – dodatkowe wartości obok granic
@pytest.mark.parametrize("percent, expected", [
    (1, 2.0),
    (49, 2.0),
    (52, 3.0),
    (59, 3.0),
    (62, 3.5),
    (69, 3.5),
    (72, 4.0),
    (79, 4.0),
    (82, 4.5),
    (89, 4.5),
    (92, 5.0),
    (99, 5.0),
])
def test_bva_3p_extra(percent, expected):
    assert grade_from_percent(percent) == expected
