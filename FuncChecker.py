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
        self.inputs = self.__generate_inputs()
        self.outputs = self.__generate_outputs()

    def __generate_inputs(self):
        inputs_arr = []
        input = Bytepy("0", binary_length=self.num_args)

        for i in range(2**self.num_args):
            inputs_arr.append(input)
            input = Bytepy(input).add(Bytepy("1"))
            input = Bytepy(input, binary_length=self.num_args)
        return inputs_arr

    def __generate_outputs(self):
        outputs = []
        for input in self.inputs:
             outputs.append(self.func(*input))
        return outputs
    def generate_desired_outputs(string):
        desired_outputs = []
        for i in range(len(string)):
            if string[i].lower() == "x":
                desired_outputs.append(Bytepy("1"))
            desired_outputs.append(Bytepy(string[i]))
        return desired_outputs

    def check_outputs(self, desired_outputs):
        for i in range(len(self.outputs)):
            if self.outputs[i] != desired_outputs[i]:
                print(repr(self.outputs[i]), repr(desired_outputs[i]))
                print(f"at index {i}")
                return False
        return True

if __name__ == '__main__':
    def dummy_func(A1, A0, B1, B0):
       return A1*-B1 + A1*A0*-B0 + A0*-B1*-B0
    
    desired_outputs = FuncChecker.generate_desired_outputs("0000100011001110")
    checker = FuncChecker(dummy_func)
    print(f"Outputs: {checker.outputs}")
    print(checker.check_outputs(desired_outputs))
    