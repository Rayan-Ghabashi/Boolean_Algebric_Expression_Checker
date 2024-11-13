import unittest
from FuncChecker import FuncChecker
from Bytepy import Bytepy
class testFuncchecker(unittest.TestCase):

    def test_generateInput(self):
        result_A = [Bytepy("000"), Bytepy("001"), Bytepy("010"), Bytepy("011"), Bytepy("111")]
        result_B = FuncChecker(lambda x: x).__generate_inputs()
        self.assertEqual(result_A, result_B) 

        