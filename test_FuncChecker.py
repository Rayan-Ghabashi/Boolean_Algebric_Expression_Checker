import unittest
from FuncChecker import FuncChecker
from Bytepy import Bytepy


class TestFuncChecker(unittest.TestCase):
    def test_generate_inputs_1_arg(self):
        # Test case for a function with 1 argument
        def dummy_func1(x):
            return x

        checker1 = FuncChecker(dummy_func1)
        expected_inputs1 = [Bytepy("0"), Bytepy("1")]
        self.assertEqual(checker1.__generate_inputs(), expected_inputs1)

    def test_generate_inputs_2_args(self):
        # Test case for a function with 2 arguments
        def dummy_func2(x, y):
            return x + y

        checker2 = FuncChecker(dummy_func2)
        expected_inputs2 = [Bytepy("00"), Bytepy("01"), Bytepy("10"), Bytepy("11")]
        self.assertEqual(checker2.__generate_inputs(), expected_inputs2)

    def test_generate_inputs_3_args(self):
        # Test case for a function with 3 arguments
        def dummy_func3(x, y, z):
            return x + y + z

        checker3 = FuncChecker(dummy_func3)
        expected_inputs3 = [
            Bytepy("000"),
            Bytepy("001"),
            Bytepy("010"),
            Bytepy("011"),
            Bytepy("100"),
            Bytepy("101"),
            Bytepy("110"),
            Bytepy("111"),
        ]
        self.assertEqual(checker3.__generate_inputs(), expected_inputs3)
    def test_generate_inputs_6_args(self):
        def dummy_func6(a, b, c, d, e, f):
            return a + b + c + d + e + f

        checker6 = FuncChecker(dummy_func6)
        expected_inputs6 = [Bytepy(format(i, "06b")) for i in range(64)]
        self.assertEqual(checker6.__generate_inputs(), expected_inputs6)

    def test_FuncChecker_error(self):
        def dummy_func_error():
            pass

        with self.assertRaises(ValueError):
            checker_error = FuncChecker(dummy_func_error)
    def test_generate_desired_outputs_1_arg(self):
        def dummy_func1(x, y):
            return x + y
        checker1 = FuncChecker(dummy_func1)
        expected_outputs1 = [Bytepy("0"), Bytepy("1"), Bytepy("1"), Bytepy("1")]
        self.assertEqual(checker1.generate_desired_outputs(), expected_outputs1)

if __name__ == "__main__":
    unittest.main()
