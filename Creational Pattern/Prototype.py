import copy
from copy import deepcopy


#membuat class mob
class entity:
    def __init__(self,health,defense,attack):
        
        self.health = health
        self.defense = defense
        self.attack = attack
  
#membuat class prototype
class Prototype:
    def __init__(self):
        self._objects = {}
 
    def register(self, nama, obj):
        self._objects[nama] = obj
 
    def unregister(self, nama):
        del self._objects[nama]
 
    def clone(self, nama, **kwargs):
        cloned_obj = deepcopy(self._objects.get(nama))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj



monster_template = entity(180,5,8)
print((f'Stat entity biasa{monster_template.__dict__}')


#register monster_template agar bisa di clone
prototype = Prototype()
prototype.register('monster', monster_template)
monster = prototype.clone('monster',health=100,attack=5,defense=5)
print((f'Stat Monster{monster.__dict__}')

monster_chief = prototype.clone('monster',health=200,attack=10)
print(f'Stat Monster Chief{monster_chief.__dict__}')
