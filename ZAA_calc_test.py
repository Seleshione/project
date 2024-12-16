import unittest
from ZAA_calc import process_key, trig_test, evaluate_expression_test, factorial_test, convert_test

class TestCalculator(unittest.TestCase):
    
    # Тесты для process_key
    
    def test_addition(self):
        result = process_key("=", "2+2")
        self.assertEqual(result, "4")

    def test_subtraction(self):
        result = process_key("=", "5-3")
        self.assertEqual(result, "2")

    def test_multiplication(self):
        result = process_key("=", "3*4")
        self.assertEqual(result, "12")

    def test_division(self):
        result = process_key("=", "10/2")
        self.assertEqual(result, "5.0")

    def test_negative_sign(self):
        result = process_key("±", "5")
        self.assertEqual(result, "-5")
        result = process_key("±", "-5")
        self.assertEqual(result, "5")
        
    def test_division_negative_1(self):
        result = process_key("=", "7/0")
        self.assertEqual(result, "Данное выражение не определено")

    def test_clear_entry(self):
        result = process_key("Del", "123")
        self.assertEqual(result, "")
        
    def test_power(self):
        result = process_key("xⁿ", "2")  
        result = process_key("3", result)
        result = process_key("=", result)   
        self.assertEqual(result, "8")  

    def test_power_negative(self):
        result = process_key("xⁿ", "5")  
        result = process_key("2", result)  
        result = process_key("=", result)   
        self.assertEqual(result, "25")  

    def test_power_zero(self):
        result = process_key("xⁿ", "7")  
        result = process_key("0", result)  
        result = process_key("=", result)   
        self.assertEqual(result, "1")  

    def test_power_fraction(self):
        result = process_key("xⁿ", "4")  
        result = process_key("0.5", result)  
        result = process_key("=", result)   
        self.assertEqual(result, "2.0")  
        
    # Тесты для evaluate_expression_test
        
    def test_addition_1(self):
        self.assertEqual(evaluate_expression_test("2 + 3"), 5)

    def test_subtraction_1(self):
        self.assertEqual(evaluate_expression_test("10 - 4"), 6)

    def test_multiplication_1(self):
        self.assertEqual(evaluate_expression_test("3 * 7"), 21)

    def test_division_1(self):
        self.assertEqual(evaluate_expression_test("8 / 2"), 4.0)

    def test_division_by_zero(self):
        self.assertEqual(evaluate_expression_test("5 / 0"), "Данное выражение не определено")

    def test_negative_result(self):
        self.assertEqual(evaluate_expression_test("2 - 5"), -3)

    def test_float_result(self):
        self.assertEqual(evaluate_expression_test("5 / 2"), 2.5)

    def test_combined_operations(self):
        self.assertEqual(evaluate_expression_test("2 + 3 * 4 - 5"), 9)
        
    def test_power_1111(self):
        self.assertEqual(evaluate_expression_test("5 ** 2"), 25)

    def test_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            evaluate_expression_test("2 +")
            
    # Тесты для factorial_test
            
    def test_factorial_of_zero(self):
        self.assertEqual(factorial_test(0), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial_test(5), 120)
        self.assertEqual(factorial_test(3), 6)
        self.assertEqual(factorial_test(1), 1)

    def test_factorial_of_large_integer(self):
        self.assertEqual(factorial_test(10), 3628800)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial_test(-1)

    def test_factorial_of_non_integer(self):
        with self.assertRaises(ValueError):
            factorial_test(4.5)

    # Тесты для convert_test

    def test_convert_positive_integer_to_binary(self):
        self.assertEqual(convert_test(10, 2), '1010')

    def test_convert_positive_integer_to_octal(self):
        self.assertEqual(convert_test(10, 8), '12')

    def test_convert_positive_integer_to_decimal(self):
        self.assertEqual(convert_test(1545, 8), '3011')

    def test_convert_positive_integer_to_hexadecimal(self):
        self.assertEqual(convert_test(255, 16), 'FF')

    def test_convert_zero(self):
        self.assertEqual(convert_test(0, 2), '0')
        
    def test_convert_to_base_3(self):
        self.assertEqual(convert_test(10, 3), '101')

    def test_convert_to_base_4(self):
        self.assertEqual(convert_test(10, 4), '22')

    def test_convert_to_base_5(self):
        self.assertEqual(convert_test(10, 5), '20')

    def test_convert_to_base_6(self):
        self.assertEqual(convert_test(10, 6), '14')

    def test_convert_to_base_7(self):
        self.assertEqual(convert_test(10, 7), '13')

    def test_convert_to_base_9(self):
        self.assertEqual(convert_test(10, 9), '11')

    def test_convert_negative_integer(self):
        with self.assertRaises(ValueError):
            convert_test(-100, 2)
            
    # Тесты для trig_test

    def test_sin_positive(self):
        self.assertEqual(trig_test(30, "sin"), 0.5)

    def test_sin_negative(self):
        self.assertEqual(trig_test(-30, "sin"), -0.5)

    def test_cos_positive(self):
        self.assertEqual(trig_test(60, "cos"), 0.5)

    def test_cos_negative(self):
        self.assertEqual(trig_test(-60, "cos"), 0.5)

    def test_tg_positive(self):
        self.assertEqual(trig_test(45, "tg"), 1.0)

    def test_tg_negative(self):
        self.assertEqual(trig_test(-45, "tg"), -1.0)

    def test_ctg_positive(self):
        self.assertEqual(trig_test(45, "ctg"), 1.0)

    def test_ctg_negative(self):
        self.assertEqual(trig_test(-45, "ctg"), -1.0)

    def test_tg_zero_division(self):
        self.assertEqual(trig_test(90, "tg"), "Тангенс не определён для данного угла.")

    def test_ctg_zero_division(self):
        self.assertEqual(trig_test(0, "ctg"), "Котангенс не определён для данного угла.")

if __name__ == "__main__":
    unittest.main()