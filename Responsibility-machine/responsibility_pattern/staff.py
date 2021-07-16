from responsibility_pattern import Manager, Person


class Supervisor(Manager):
    def __init__(self, name, title):
        super(Supervisor, self).__init__(name, title)

    def handleRequest(self, person: Person):
        if person.getDayOff() <= 2:
            print(f"同意{person.getName()} 請假，審核者{self.getName()} {(self.getTitle())}")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class DepartmentManager(Manager):

    def __init__(self, name, title):
        super(DepartmentManager, self).__init__(name, title)

    def handleRequest(self, person):
        if 2 <= person.getDayOff() <= 5:
            print(f"同意{person.getName()} 請假，審核者{self.getName()} {(self.getTitle())}")
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class CEO(Manager):
    def __init__(self, name, title):
        super(CEO, self).__init__(name, title)

    def handleRequest(self, person):
        if 5 < person.getDayOff() <= 30:
            print(f"同意{person.getName()} 請假，審核者{self.getName()} {(self.getTitle())}")

        if self._nextHandler is not None:
            self._nextHandler.handleRequest(person)


class Administrator(Manager):
    def __init__(self,name,title):
        super(Administrator, self).__init__(name,title)

    def handleRequest(self, person):
        print(f'{person.getName()} 請假已簽核，處理人{self.getName()} {self.getTitle()}')