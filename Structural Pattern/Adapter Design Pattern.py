class pagi:
    def get(self):
        return 'Selamat Pagi'

class malam:
    def get(self):
        return 'Selamat Malam'

class Adapter:
    def __init__(self, cls):
        self.cls = cls

    def get(self):
        return str(self.cls.get())

def main(obj):
    print("Sapa : " + obj.get())

if __name__ == '__main__':
    obj = Adapter(malam())
    main(obj)