from typing import Union


class Bytepy:
    def __init__(
        self, input: Union[str, "Bytepy.Bytepy"], is_base10=False, binary_length=None
    ):
        if isinstance(input, Bytepy):
            self.__integer = input.__integer
            self.__binary = input.__binary
            self.__binary_length = input.__binary_length
            self.__normalizeBinary()
        elif isinstance(input, str):
            if is_base10:
                self.__integer = int(input)
                self.__binary = bin(int(input))[2:]

            else:
                self.__integer = self.__bitToInt(input)
                self.__binary = input

            if binary_length:
                self.__binary_length = binary_length
                self.__normalizeBinary()
            else:
                self.__binary_length = len(self.__binary)
        else:
            raise ValueError("input must be a string or a Bytepy object")

        if self.__notbinary(self.__binary):
            raise ValueError("Input is not a binary string")

    def add(self, other: "Bytepy"):
        binary_length = self.__findBinaryLength(other)
        result = self.__integer + other.__integer
        result = str(result)
        return Bytepy(result, True, binary_length)

    def __notbinary(self, input):
        integrals = set(input)
        for integral in integrals:
            if integral not in ["0", "1"]:
                return False

    def __bitToInt(self, bits: str):
        # converting the input to a string so that it can be used in the int function
        bits = str(bits)
        return int(bits, 2)

    def __normalizeBinary(self):
        self.__binary = self.__binary.zfill(self.__binary_length)

    def __findBinaryLength(self, other):
        biggest = max(self.__binary_length, other.__binary_length)
        return biggest

    def __add__(self, other: "Bytepy"):
        binary_length = self.__findBinaryLength(other)
        result = self.__integer | other.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)

    def __mul__(self, other: "Bytepy"):
        binary_length = self.__findBinaryLength(other)
        resut = self.__integer & other.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)

    def __neg__(self):
        binary_length = self.__binary_length
        result = ~self.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)

    def __eq__(self, other):
        if isinstance(other, Bytepy):
            return self.__integer == other.__integer
        else:
            return False

    def __iter__(self):
        self.__index = 0
        self.__max = len(self.__binary)
        while self.__index < self.__max:
            result = self.__binary[self.__index]
            self.__index += 1
            yield Bytepy(result)

    def __str__(self):
        return self.__binary

    def __repr__(self):
        return f"Bytepy({self.__binary})"


if __name__ == "__main__":
    ...
