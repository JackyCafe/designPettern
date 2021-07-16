from mediator_pattern import HouseInfo


class HouseOwner:
    _houseInfo:HouseInfo

    def __init__(self, name):
        self._name = name
        self._houseInfo = None

    def getName(self):
        return self._name

    def setHouseInfo(self, address, area, price, has_window, bathroom, kitchen):
        self._houseInfo = HouseInfo(area, price, has_window, bathroom, kitchen, address, self)

    def publishHouseInfo(self, agency):
        self._houseInfo.showInfo()