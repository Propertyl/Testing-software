from main import get_bmi_category

def test_bmi_logic():
    print("Запуск тестів з використанням assert...")

    bmi, cat = get_bmi_category(75, 180)
    assert bmi == 23.1, f"Очікували 23.1, але отримали {bmi}"
    assert cat == "Надмірна вага", f"Очікували 'Надмірна вага', але отримали '{cat}'"

    bmi, cat = get_bmi_category(110, 180)
    assert cat == "Надмірна вага", "Помилка: категорія мала бути 'Надмірна вага'"

    bmi, cat = get_bmi_category(50, 165)
    assert cat == "Недостатня вага", f"Очікували 'Недостатня вага', отримали {cat}"

    print("Всі тести з assert пройдено успішно!")

if __name__ == "__main__":
    try:
        run_assert_tests()
    except AssertionError as e:
        print(f"Тест провалено: {e}")
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")