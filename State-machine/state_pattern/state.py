import abc


class State(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self._name = name

    def getName(self) -> str:
        return self._name

    @abc.abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):

    def __init__(self,name):
        super(SolidState, self).__init__(name)

    def behavior(self, water):
        print(f"固體:{water.getTemperature()}")


class LiquidState(State):

    def __init__(self,name):
        super(LiquidState, self).__init__(name)

    def behavior(self, water):
        print(f"液體:{water.getTemperature()}")


class GaseousState(State):

    def __init__(self, name):
        super(GaseousState, self).__init__(name)

    def behavior(self, water):
        print(f"氣體:{water.getTemperature()}")

