import pytest
from main import get_bmi_category

@pytest.fixture
def default_weight():
    return 70

@pytest.mark.skip(reason="Ця логіка ще в розробці")
def test_future_feature():
    assert 1 == 2

@pytest.mark.xfail(reason="Знаємо, що межі округлення іноді дають похибку")
def test_edge_case_precision():
    bmi, cat = get_bmi_category(50.123, 165.789)
    assert bmi == 18.2

@pytest.mark.parametrize("weight, height, expected_cat", [
    (45, 160, "Недостатня вага"),
    (70, 175, "Норма"),
    (100, 180, "Надмірна вага"),
])



def test_bmi_categories(weight, height, expected_cat):
    bmi, cat = get_bmi_category(weight, height)
    assert cat == expected_cat

def test_with_fixture(default_weight):
    bmi, cat = get_bmi_category(default_weight, 175)
    assert cat == "Норма"

def test_zero_height_error():
    with pytest.raises(ValueError, match="Зріст має бути більшим за 0"):
        get_bmi_category(70, 0)

def test_intentional_failure():
    bmi, cat = get_bmi_category(100, 170)
    assert cat == "Норма"

def test_bmi_value_mismatch():
    bmi, cat = get_bmi_category(80, 180)
    assert bmi == 20.0, f"Очікували ІМТ 20.0, але отримали {bmi}"