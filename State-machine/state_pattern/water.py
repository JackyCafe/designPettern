from state_pattern import SolidState, State, LiquidState, GaseousState


class Water:
    _temperature: int

    def __init__(self, state):
        self._temperature = 25
        self._state = state

    def setState(self, state):
        self._state = state

    def changeState(self, state):
        if self._state:
            print(f"from state {self._state.getName()} -->{state.getName()}")
        else:
            print(f"Initial stat {state.getName()}")

    def getTemperature(self):
        return self._temperature

    def setTemperature(self, temperature):
        self._temperature = temperature
        if self._temperature <= 0:
            self.changeState(SolidState("固態"))
        elif self._temperature < 100:
            self.changeState(LiquidState("液態"))
        elif self._temperature > 100:
            self.changeState(GaseousState("氣態"))

    def raiseTemperature(self, step):
        self.setTemperature(self._temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self._temperature - step)

    def behavior(self):
        self._state.behavior(self)
