# dispenser untuk uang 50.000 rupiah

from interface_dispenser import IDispenser


# jumlah uang 50.000 rupiah akan dibagi
class Dispenser2(IDispenser):

    def __init__(self):
        self._successor = None

    # sebagai jumlah uang selanjutnya
    def next_successor(self, successor):
        self._successor = successor

    # menangani permintaan client
    def handle(self, amount):

        # mengatur jumlah uang
        if amount >= 50000:
            num = amount // 50000
            remainder = amount % 50000
            print(f"Jumlah kertas uang {num} 50.000 rupiah")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
