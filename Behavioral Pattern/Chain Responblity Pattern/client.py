
import sys
from atm_dispenser_chain import ATMDispenserChain

ATM = ATMDispenserChain()
AMOUNT = int(input("Enter amount to withdrawal : "))
if AMOUNT < 10 or AMOUNT % 10 != 0:
    print("jumlah harus sesuai.")
    sys.exit()
# process the request
ATM.chain1.handle(AMOUNT)
print("Silahkan diambil")
