from mediator_pattern import HouseInfo


class HouseAgency:
    def __init__(self, name: str):
        self._houseInfos = []
        self._name = name

    def getName(self) -> str:
        return self._name

    def addHouseInfo(self, house_info: HouseInfo) -> None:
        self._houseInfos.append(house_info)

    def removeHouseInfo(self, house_info: HouseInfo) -> None:
        for info in self._houseInfos:
            if info == house_info:
                self._houseInfos.remove(info)

    def getSearchCondition(self, description) -> None:
        return description
