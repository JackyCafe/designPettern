class Person:
    def __init__(self, name, day_off, reason):
        self._reason = reason
        self._day_off = day_off
        self._name = name
        self._leader = None

    def getName(self) -> str:
        return self._name

    def getDayOff(self) -> int:
        return self._day_off

    def getReason(self) -> str:
        return self._reason

    def setLeader(self, leader):
        self._leader = leader

    def request(self):
        print(f'請假{self._day_off} 天，請假事由 {self._reason}')
        if self._leader is not None:
            self._leader.handleRequest(self)