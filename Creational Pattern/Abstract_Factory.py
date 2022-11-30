class kategori_game:
     
 
    def __init__(self, factory_kategori = None):
 
 
        self.factory_kategori = factory_kategori
 
    def show_game(self):
 
        Kgame = self.factory_kategori()
 
        print(f'untuk game game di kategori {Kgame} ')
        print(f'kita memiliki {Kgame.isigame()}')
 
 
class RPG:
 
    def isigame(self):
        return "Elden Ring, The Witcher 3 dan Elder Scroll V"
     
    def __str__(self):
        return "RPG"
 
class Fighting:
   
    def isigame(self):
        return "Guilty gear, Tekken 7 dan Super Smash Bros Ultimate"
     
    def __str__(self):
        return "Fighting"
 
class Horror:
   
    def isigame(self):
        return "Resident Evil Village, Outlast dan Little Nightmare"
     
    def __str__(self):
        return "Horror"

kategori_game(Horror).show_game()
