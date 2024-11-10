from typing import Union
class Bytepy:
    def __init__(self, input: Union[str, 'Bytepy.Bytepy'], base10 = False):
        if isinstance(input, Bytepy):
            self.__value = input.__value
            self.__binary = input.__binary
        else:
            if base10:
                self.__value = input
                self.__binary = bin(input)[2:]
            else:
                self.__value = self.bitIntToBytes(input)
                self.__binary = input
        if  self.notbinary(self.__binary):
            raise ValueError("Input is not a binary string")
    
    def notbinary(self, input):
        integrals = set(input)
        for integral in integrals:
            if integral not in ["0", "1"]:
                return False 
            

    def bitIntToBytes(self, input):
        return int(input, 2)

    def __add__(self, other: 'Bytepy'):
        return Bytepy(self.__value | other.__value, True)

    def __mul__(self, other: 'Bytepy'):
        return Bytepy(self.__value & other.__value, True)

    def __neg__(self):
        return Bytepy(~self.__value, True)
    
    def add(self, other: 'Bytepy'):
        return Bytepy(self.__value + other.__value, True)
    def __str__(self):
        # change maybe
        return bin(self.__value)[2:]