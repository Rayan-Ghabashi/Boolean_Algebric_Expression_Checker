# note there are two ways to check the function one is each input(i) -> output(i) == desired(i) and one with the whole processed output with the desired output ; output = desired
# note there are two ways of creating the desired inputs one is to create each input as an array and the other is to create the sequence of desired inputs as an array
# note there are two ways of creating the desired outputs one is to create each desired output as an array and the other is to create the sequence of desired outputs as an array
import inspect
from Bytepy import Bytepy
class FuncChecker:
    def __init__(self, func):
        self.func = func
        self.num_args = len(inspect.signature(func).parameters)
        self.inputs = self.generate_inputs() 
        
    def generate_inputs(self):
        inputs_arr = []
        input = Bytepy("0" * self.num_args)
        
        for i in range(2 ** self.num_args):
            inputs_arr.append(input)
            input = Bytepy(input).add(Bytepy("1"))
        return inputs_arr


test = FuncChecker(Bytepy.notbinary)
print(list(map(lambda x: x.__str__(), test.inputs)))