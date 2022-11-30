# dispenser untuk uang 20.000 rupiah

from interface_dispenser import IDispenser

# jumlah uang 20.000 rupiah akan dibagi


class Dispenser1(IDispenser):

    def __init__(self):
        self._successor = None

    # sebagai pernerus selanjutnya
    def next_successor(self, successor):
        self._successor = successor

    # mengatur jumlah uang
    def handle(self, amount):
        if amount >= 20000:
            num = amount // 20000
            remainder = amount % 20000
            print(f"Jumlah kertas uang {num} 20.000 rupiah")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
