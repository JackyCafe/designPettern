from Object import Observer, WaterHeater


class WashMode(Observer):
    def update(self, observable, object_id=0):
        if isinstance(observable, WaterHeater) and 40 < observable.getTemperature() < 60:
            print("適合洗澡")


class DrinkMode(Observer):
    def update(self, observable, object_id=0):
        if isinstance(observable, WaterHeater) and observable.getTemperature() > 100:
            print("適合泡茶")
