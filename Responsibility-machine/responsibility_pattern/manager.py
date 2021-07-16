from abc import ABCMeta, abstractmethod


class Manager(metaclass=ABCMeta):
    def __init__(self, name, title):
        self._name = name
        self._title = title
        self._nextHandler = None

    def getName(self) -> str:
        return self._name

    def getTitle(self) -> str:
        return self._title

    def setNextHandler(self,nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self,person):
        pass



