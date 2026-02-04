from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract Class with die method"""

    def __init__(self, first_name, is_alive=True):
        """Constructor takes a First Name and the optionnal Alive status as bool"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """To be defined in Child CLasses"""
        pass

class Stark(Character):
    """Child Class inheriting from Character Abstract Class"""

    def die(self):
        """Changes is_alive from True to False"""
        self.is_alive = False
        
