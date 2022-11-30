from __future__ import annotations
from abc import ABC, abstractmethod


class Card:

    _state = None

    def __init__(self, state: State) -> None:
        self.SetCard(state)

    def SetCard(self, state: State):

        self._state = state
        self._state.Card = self

    def presentState(self):
        print(f"Card didalam {type(self._state).__name__}")

    def pushOklBtn(self):
        self._state.pushOklBtn()

    def pushCancelBtn(self):
        self._state.pushCancelBtn()


class State(ABC):
    @property
    def Card(self) -> Card:
        return self._Card

    @Card.setter
    def Card(self, Card: Card) -> None:
        self._Card = Card


class mesinATM(State):

    def pushOklBtn(self) -> None:
        print("kartu anda sudah didalam mesin atm")

    def pushCancelBtn(self) -> None:
        print("Card keluar mesinATM.")
        self.Card.SetCard(ditanganPengguna())


class ditanganPengguna(State):

    def pushOklBtn(self) -> None:
        print("kartu anda keluar dari  mesin atm...")
        self.Card.SetCard(mesinATM())

    def pushCancelBtn(self) -> None:
        print("kartu anda sudah diluar mesin atm")


if __name__ == "__main__":

    # client code
    myCard = Card(mesinATM())
    myCard.pushOklBtn()
    myCard.presentState()

    myCard.pushCancelBtn()

    myCard.presentState()


# from __future__ import annotations
# from abc import ABC, abstractmethod


# #objek
# class Card:

#     #sebagai referensi class card
#     _state = None

#     #untuk membuat koonfigurasi state card
#     def __init__(self, state: State) -> None:
#         self.SetCard(state)

#     #card akan mengubah perilaku objek ketika dijalankan program
#     def SetCard(self, state: State):

#         self._state = state
#         self._state.Card = self

#     # untuk mengubah suatu status objek ketika dijalankan
#     def presentState(self):
#         print(f"Card di {type(self._state).__name__}")

#     # adalah sebagai metode untuk menjalankan mesin ATM
#     def pushOklBtn(self):
#         self._state.pushOklBtn()

#     def pushCancelBtn(self):
#         self._state.pushCancelBtn()


# #class state ini akan dideklarasi oleh concrete sebagai mesin atm, lalu state juga akan mengbalikan objek context dengan renferensi class card
# class State(ABC):

#     #@property digunakan untuk membuat metode context() sebagai properti
#     @property
#     def Card(self) -> Card:
#         return self._Card

# #@context.setter sebagai unntuk mengambil nilai pada artribut context objek yaitu card

#     @Card.setter
#     def Card(self, Card: Card) -> None:
#         self._Card = Card

# #menentukan status conteks objek diclass yang akan diimplemnatsi interface,setelah itu dipanggil status keadaan kontex berubah class mesin itu sendiri memiliki 2 status yaitu tombol keluar mesin atm dan masuk didalam mesim atm
# # concrete states
# class mesinATM(State):

#     #jika masukan pin dan menekan tombol ok maka card akan masuk ke mesin ATM
#     def pushOklBtn(self) -> None:
#         print("Card masuk mesin atm")

#     # jika menkan tombol cancel maka card akan keluar dari mesin atm lalu berubah status statenya menjadi ditangan pengguna.
#     def pushCancelBtn(self) -> None:
#         print("Card keluar mesinATM.")
#         self.Card.SetCard(tanganpengguna())


# class tanganpengguna(State):

#     #jika masukan pin dan menekan tombol ok maka card akan masuk ke mesin ATM
#     def pushOkBtn(self) -> None:
#         print("Card masuk mesin atm  ")
#         self.Card.setCard(mesinATM())

#     # jika menkan tombol cancel maka card akan keluar dari mesin atm lalu berubah status statenya menjadi ditangan pengguna.
#     def pushCancelBtn(self) -> None:
#         print("keluar dari mesin atm")

# #lalu menegesekusi progaram
# if __name__ == "__main__":

#     #client
#     myCard = Card(mesinATM())
#     myCard.pushOklBtn()
#     myCard.presentState()

#     #sebagai status dari concert state
#     myCard.pushCancelBtn()
#     myCard.presentState()
