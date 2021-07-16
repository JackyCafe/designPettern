from abc import abstractmethod

from decorator_pattern import Person


class ClothingDecorator(Person):

    def __init__(self, person):
        self._person = person

    def wear(self):
        self._person.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass