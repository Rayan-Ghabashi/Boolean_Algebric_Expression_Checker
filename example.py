"""
Full Adder implementation in BytePy and checking the outputs using FuncChecker.
"""

from FuncChecker import FuncChecker

string_output_cout = "00010111"
string_output_s = "01101001"

desired_outputs_cout = FuncChecker.generate_desired_outputs(string_output_cout)
desired_outputs_s = FuncChecker.generate_desired_outputs(string_output_s)

def s(x: "Bytepy", y: "Bytepy", c: "Bytepy") -> "Bytepy":
    return x.xor(y).xor(c) 

def cout(x: "Bytepy", y: "Bytepy", c: "Bytepy") -> "Bytepy":
    return (x * c) + (y * c) + (x * y)
    