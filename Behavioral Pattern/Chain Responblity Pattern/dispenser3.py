# dispenser untuk uang 100.000 rupiah

from interface_dispenser import IDispenser

# jumlah uang 100 ribu rupiah akan dibagi


class Dispenser3(IDispenser):

    def __init__(self):
        self._successor = None

    # sebagai jumlah uang selanjutnya
    def next_successor(self, successor):

        self._successor = successor

    # menangani permintaan client
    def handle(self, amount):

        # Mengatur jumlah perngeluaran
        if amount >= 100000:
            num = amount // 100000
            remainder = amount % 100000
            print(f"Jumlah kertas uang {num} 100.000 rupiah ")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
