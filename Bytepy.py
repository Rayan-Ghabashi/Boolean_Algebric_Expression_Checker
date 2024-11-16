from typing import Union


class Bytepy:
    """
    A class to represent and manipulate binary numbers.

    Attributes:
        __binary (str): The binary string.
        __binary_length (int): The length of the binary string.

    Methods:
        __normalize_binary(): Normalizes the binary string to the specified length.
        __find_binary_length(other): Finds the maximum binary length between two Bytepy objects.
        __add__(other): Performs bitwise OR operation between two Bytepy objects.
        __mul__(other): Performs bitwise AND operation between two Bytepy objects.
        __neg__(): Negates the binary number using one's complement within the bit length.
        __eq__(other): Checks if two Bytepy objects are equal.
        __iter__(): Iterates over the bits of the binary string.
        __str__(): Returns the binary string representation of the Bytepy object.
        __repr__(): Returns the string representation of the Bytepy object.

    Examples:
        >>> A = Bytepy("1010")
        >>> B = Bytepy("0101")
        >>> C = A + B
        >>> print(C)
        1111

        >>> D = A * B
        >>> print(D)
        0000

        >>> E = -A
        >>> print(E)
        0101
    """

    def __init__(
        self, input: Union[str, "Bytepy.Bytepy"], is_base10: bool = False, binary_length: int = None
    ):
        """
        Initialize a Bytepy object.

        Args:
            input (Union[str, Bytepy]): The input binary string or Bytepy object.
            is_base10 (bool): If True, the input is treated as a base-10 number.
            binary_length (int): The length of the binary string.
        """
        if isinstance(input, Bytepy):
            self.__binary: str = input.__binary
            self.__binary_length = input.__binary_length
            self.__normalize_binary()
        elif isinstance(input, str):
            if is_base10:
                self.__binary: str = bin(int(input))[2:]

            else:
                self.__binary: str = input

            if binary_length:
                self.__binary_length: int = binary_length
                self.__normalize_binary()
            else:
                self.__binary_length: int = len(self.__binary)
        else:
            raise ValueError("input must be of type string or Bytepy")

        if not all(bit in "01" for bit in self.__binary):
            raise ValueError(
                "input must be a binary string containing only 0s and 1s")

    @property
    def __integer(self) -> int:
        """
        Convert the binary string to an integer.

        Returns:
            int: The integer representation of the binary string.
        """
        return int(self.__binary, 2)

    def __normalize_binary(self):
        """
        Normalize the binary string to the specified length.
        """
        self.__binary = self.__binary.zfill(self.__binary_length)

    def __find_binary_length(self, other):
        """
        Find the maximum binary length between two Bytepy objects.

        Args:
            other (Bytepy): The other Bytepy object.

        Returns:
            int: The maximum binary length.
        """
        biggest = max(self.__binary_length, other.__binary_length)
        return biggest

    def xor(self, other: "Bytepy"):
        """
        Perform bitwise XOR operation between two Bytepy objects.

        Args:
            other (Bytepy): The other Bytepy object.

        Returns:
            Bytepy: The result of the bitwise XOR operation.
        """
        binary_length = self.__find_binary_length(other)
        result = self.__integer ^ other.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)
    def __add__(self, other: "Bytepy"):
        """
        Perform bitwise OR operation between two Bytepy objects.

        Args:
            other (Bytepy): The other Bytepy object.

        Returns:
            Bytepy: The result of the bitwise OR operation.
        """
        binary_length = self.__find_binary_length(other)
        result = self.__integer | other.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)

    def __mul__(self, other: "Bytepy"):
        """
        Perform bitwise AND operation between two Bytepy objects.

        Args:
            other (Bytepy): The other Bytepy object.

        Returns:
            Bytepy: The result of the bitwise AND operation.
        """
        binary_length = self.__find_binary_length(other)
        result = self.__integer & other.__integer
        result = str(result)
        return Bytepy(result, is_base10=True, binary_length=binary_length)

    def __neg__(self):
        """
        Negate the binary number using one's complement within the bit length.

        Returns:
            Bytepy: The negated Bytepy object.
        """
        # Compute the maximum value for the given bit length
        max_value = (1 << self.__binary_length) - 1
        # Compute one's complement within the bit length
        result_int = (~self.__integer) & max_value
        # Convert back to binary string with proper padding
        result_bin = bin(result_int)[2:].zfill(self.__binary_length)
        return Bytepy(result_bin, binary_length=self.__binary_length)

    def __eq__(self, other):
        """
        Check if two Bytepy objects are equal.

        Args:
            other (Bytepy): The other Bytepy object.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, Bytepy):
            return self.__integer == other.__integer
        else:
            return False

    def __iter__(self):
        """
        Iterate over the bits of the binary string.

        Yields:
            Bytepy: The next bit as a Bytepy object.
        """
        self.__index = 0
        self.__max = len(self.__binary)
        while self.__index < self.__max:
            result = self.__binary[self.__index]
            self.__index += 1
            yield Bytepy(result)

    def __str__(self):
        """
        Return the binary string representation of the Bytepy object.

        Returns:
            str: The binary string.
        """
        return self.__binary

    def __repr__(self):
        """
        Return the string representation of the Bytepy object.

        Returns:
            str: The string representation.
        """
        return f"Bytepy({self.__binary})"
