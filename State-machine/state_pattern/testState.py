from state_pattern import Water, LiquidState, SolidState, GaseousState


def main():
    water = Water(LiquidState("液體"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.raiseTemperature(18)
    water.behavior()
    water.raiseTemperature(110)
    water.behavior()


if __name__ == '__main__':
    main()
