from observer_pattern import Observable


class WaterHeater(Observable):
    temperature: int

    def __init__(self):
        super(WaterHeater, self).__init__()
        self.temperature = 25

    def getTemperature(self) -> int:
        return self.temperature

    def setTemperature(self,temperature):
        self.temperature = temperature
        print(f"目前溫度: {self.temperature}")
        self.notify()