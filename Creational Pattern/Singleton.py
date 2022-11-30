
class Mesincuci(object):
    __instance = None
    def __new__(cls, val=None):
        if Mesincuci.__instance is None:
            Mesincuci.__instance = object.__new__(cls)
        Mesincuci.__instance.val = val
        return Mesincuci.__instance
 
 
x = Mesincuci()
x.val = 'Baju a'
print(f'Baju yang ada di mesin cuci = {x.val}')
 
y = Mesincuci()
y.val = 'baju b'
print(f'Baju yang ada di mesin cuci = {y.val}')
   
print(f'apakah x dan y objek adalah yang sama? {(x == y)}, karena hanya ada satu jenis instance ')
