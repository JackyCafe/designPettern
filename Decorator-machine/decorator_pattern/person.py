from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("著裝")