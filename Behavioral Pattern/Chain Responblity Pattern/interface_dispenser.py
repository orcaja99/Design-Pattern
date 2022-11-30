
from abc import ABCMeta, abstractmethod


class IDispenser(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def next_successor(successor):
        "untuk menangani ranati keselanjutnya"

    @staticmethod
    @abstractmethod
    def handle(amount):
        "untuk sebagai funsgi menangani jumlah"
