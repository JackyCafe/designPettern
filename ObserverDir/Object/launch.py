from Object import WaterHeater, DrinkMode, WashMode


def main():
    heater = WaterHeater()
    heater.addObserver(DrinkMode())
    heater.addObserver(WashMode())
    heater.setTemperature(104)
    heater.setTemperature(55)

if __name__ == '__main__':
    main()