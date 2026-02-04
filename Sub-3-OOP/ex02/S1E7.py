from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Changes is_alive from True to False"""
        self.is_alive = False
    
    def __str__(self):
        """Returns a string representing the specs of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representing the specs of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """A Lannister always pays his debt"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Changes is_alive from True to False"""
        self.is_alive = False

    def __str__(self):
        """Returns a string representing the specs of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representing the specs of the class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Alternate method to instance a Lannister"""
        return cls(first_name, is_alive)