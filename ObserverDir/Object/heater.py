from Object import Observable


class WaterHeater(Observable):
    temperature: int

    def __init__(self):
        super(WaterHeater, self).__init__()
        self.temperature = 25

    def getTemperature(self) ->int:
        return self.temperature

    def setTemperature(self,temperature:int)->None:
        self.temperature = temperature
        print(self.temperature)
        self.notify()