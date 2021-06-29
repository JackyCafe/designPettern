import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self,observable, object_id=0):
        pass
