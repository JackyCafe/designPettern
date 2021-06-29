class Observable:
    observers: list

    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self,observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update(self)