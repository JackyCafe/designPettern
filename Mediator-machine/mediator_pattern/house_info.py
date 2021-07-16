from mediator_pattern import HouseOwner


class HouseInfo:
    _area: float
    _price: int
    _has_window: bool
    _bathroom: int
    _has_kitchen: bool
    _address: str
    _owner: HouseOwner

    def __init__(self, area: float, price: int
                 , has_window: bool, bathroom: int
                 , has_kitchen: bool, address: str, owner):
        self._area = area
        self._price = price
        self._has_window = has_window
        self._bathroom = bathroom
        self._has_kitchen = has_kitchen
        self._address = address
        self._owner = owner

    def getAddress(self) -> str:
        return self._address

    def getOwner(self) -> str:
        return self._owner.getName()

    def showInfo(self,isShowOwner = True):
        print(f"面積:{self._area},"
              f"價格:{self._price},"
              f"窗戶:{'有' if self._has_window else '沒有'},"
              f"衛浴:{self._bathroom}"
              f"廚房:{'有' if self._has_kitchen else '沒有'}"
              f"位址:{self._address},"
              f"房東:{self.getOwner()}")