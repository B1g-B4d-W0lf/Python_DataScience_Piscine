class calculator:
    """Apply a chosen operation (+*/-) to each scalar in a vector"""

    def __init__(self, vector):
        """Initialize the vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition the given number"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply by the given number"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substract the given number"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide by the given number"""
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"Error '{e}'\nCannot divide by 0.")

