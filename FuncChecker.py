# note there are two ways to check the function one is each input(i) -> output(i) == desired(i) and one with the whole processed output with the desired output ; output = desired
# note there are two ways of creating the desired inputs one is to create each input as an array and the other is to create the sequence of desired inputs as an array
# note there are two ways of creating the desired outputs one is to create each desired output as an array and the other is to create the sequence of desired outputs as an array
import inspect
from Bytepy import Bytepy
from typing import Callable


class FuncChecker:
    """
    A class to check the correctness of a function that operates on Bytepy objects.

    Attributes:
        func (Callable[..., Bytepy]): The function to be checked.
        num_args (int): The number of arguments the function takes.
        inputs (list): The generated inputs for the function.
        outputs (list): The outputs of the function for the generated inputs.

    Methods:
        __generate_inputs(): Generates all possible inputs for the function.
        __generate_outputs(): Generates the outputs of the function for the generated inputs.
        generate_desired_outputs(string): Generates the desired outputs from a string.
        check_outputs(desired_outputs): Checks if the function outputs match the desired outputs.

    Examples:
        >>> def dummy_func(A1, A0, B1, B0):
        ...     return A1*-B1 + A1*A0*-B0 + A0*-B1*-B0
        >>> desired_outputs = FuncChecker.generate_desired_outputs("0000100011001110")
        >>> checker = FuncChecker(dummy_func)
        >>> print(f"Outputs: {checker.outputs}")
        >>> print(checker.check_outputs(desired_outputs))
    """

    def __init__(self, func: Callable[..., "Bytepy.Bytepy"]):
        """
        Initialize a FuncChecker object.

        Args:
            func (Callable[..., Bytepy]): The function to be checked.
        """
        self.func = func
        self.num_args = len(inspect.signature(func).parameters)
        if self.num_args == 0:
            raise ValueError("Function must have at least one argument")
        self.inputs = self.__generate_inputs()
        self.outputs = self.__generate_outputs()

    def __generate_inputs(self):
        """
        Generate all possible inputs for the function.

        Returns:
            list: The generated inputs for the function.
        """
        return [Bytepy(bin(i)[2:].zfill(self.num_args)) for i in range(2**self.num_args)]

    def __generate_outputs(self):
        """
        Generate the outputs of the function for the generated inputs.

        Returns:
            list: The outputs of the function for the generated inputs.
        """
        return [self.func(*input) for input in self.inputs]

    @staticmethod
    def generate_desired_outputs(string):
        """
        Generate the desired outputs from a string.

        Args:
            string (str): The string representing the desired outputs.

        Returns:
            list: The desired outputs as Bytepy objects.
        """
        desired_outputs = []
        for i in range(len(string)):
            if string[i].lower() == "x":
                desired_outputs.append(Bytepy("1"))
            else:
                desired_outputs.append(Bytepy(string[i]))
        return desired_outputs

    def check_outputs(self, desired_outputs):
        """
        Check if the function outputs match the desired outputs.

        Args:
            desired_outputs (list): The desired outputs to check against.

        Returns:
            bool: True if the outputs match, False otherwise.
        """
        for i in range(len(self.outputs)):
            if self.outputs[i] != desired_outputs[i]:
                print(repr(self.outputs[i]), repr(desired_outputs[i]))
                print(f"at index {i}")
                return False
        return True
