from abc import ABCMeta, abstractmethod

# Interface Subject


class IObservable(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def transfer(observer):
        ""

    @staticmethod
    @abstractmethod
    def notify(observer):
        ""

# Subject


class Subject(IObservable):

    def __init__(self):
        self._observers = set()

    def transfer(self, observer):
        self._observers.add(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)

# Implementasi Observer


class IObserver(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        ""

# Observe concrete


class Observer(IObserver):

    def __init__(self, observable):
        observable.transfer(self)

    def notify(self, *args):
        print(f"Observer no_struk:{id(self)} data struk {args} ")


# The Client
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)


SUBJECT.notify("jumlah penarikan", {200000})

SUBJECT.transfer(OBSERVER_A)
SUBJECT.notify("Data Struk", {"jumlah saldo": 800000})
