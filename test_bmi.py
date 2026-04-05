import unittest
from main import get_bmi_category

class TestBMI(unittest.TestCase):

    def test_normal_weight(self):
        bmi, cat = get_bmi_category(70, 175)
        self.assertEqual(cat, "Норма")
        self.assertEqual(bmi, 99.9)

    def test_underweight(self):
        bmi, cat = get_bmi_category(45, 160)
        self.assertEqual(cat, "Недостатня вага")

    def test_error_on_zero_height(self):
        with self.assertRaises(ValueError):
            get_bmi_category(70, 0)


if __name__ == "__main__":
    unittest.main()