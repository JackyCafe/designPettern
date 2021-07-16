from observer_pattern import WaterHeater, DrinkingMode, WashingMode


def main():
    heater = WaterHeater()
    heater.addObserver(DrinkingMode())
    heater.addObserver(WashingMode())
    heater.setTemperature(104)
    heater.setTemperature(55)


if __name__ == '__main__':
    main()