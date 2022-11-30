"Mesin atm"
from dispenser1 import Dispenser1
from dispenser2 import Dispenser2
from dispenser3 import Dispenser3


class ATMDispenserChain:  # pylint: disable=too-few-public-methods
    "rantai client"

    def __init__(self):
        # menginisialisasi rantai penerus
        self.chain1 = Dispenser3()
        self.chain2 = Dispenser2()
        self.chain3 = Dispenser1()
       # Mengatur rantai penerus default yang akan memproses 100-an
        # pertama, 50-an kedua dan 20-an terakhir.
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
