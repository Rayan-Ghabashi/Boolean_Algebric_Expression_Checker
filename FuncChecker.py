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
        self.outputs = self.generate_outputs()

    def generate_inputs(self):
        inputs_arr = []
        input = Bytepy("0", binary_length=self.num_args)

        for i in range(2**self.num_args):
            inputs_arr.append(input)
            input = Bytepy(input).add(Bytepy("1"))
            input = Bytepy(input, binary_length=self.num_args)
        return inputs_arr

    def generate_outputs(self):
        outputs = []
        for input in self.inputs:
             outputs.append(self.func(*input))
        return outputs
    
    def check_outputs(self, desired_outputs):
        for i in range(len(self.outputs)):
            if self.outputs[i] != desired_outputs[i]:
                print(repr(self.outputs[i]), repr(desired_outputs[i]))
                return False
        return True

if __name__ == '__main__':
   ... 
