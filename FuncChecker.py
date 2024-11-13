# note there are two ways to check the function one is each input(i) -> output(i) == desired(i) and one with the whole processed output with the desired output ; output = desired
# note there are two ways of creating the desired inputs one is to create each input as an array and the other is to create the sequence of desired inputs as an array
# note there are two ways of creating the desired outputs one is to create each desired output as an array and the other is to create the sequence of desired outputs as an array
import inspect
from Bytepy import Bytepy
from typing import Callable


class FuncChecker:
    def __init__(self, func: Callable[..., "Bytepy.Bytepy"]):
        self.func = func
        self.num_args = len(inspect.signature(func).parameters)
        if self.num_args == 0:
            raise ValueError("Function must have at least one argument")
        self.inputs = self.generate_inputs()

    def generate_inputs(self):
        inputs_arr = []
        input = Bytepy("0", binary_length=self.num_args)

        for i in range(2**self.num_args):
            inputs_arr.append(input)
            input = Bytepy(input).add(Bytepy("1"))
            input = Bytepy(input, binary_length=self.num_args)
        return inputs_arr

    def generate_desired_outputs(self):
        desired_outputs = []
        print(self.inputs)
        for input in self.inputs:
            print(repr(input))
            desired_outputs.append(self.func(*input))
        return desired_outputs

if __name__ == '__main__':
    def funca(x, y):
        return x + y

    checker1 = FuncChecker(funca)
    checker1.generate_desired_outputs()
