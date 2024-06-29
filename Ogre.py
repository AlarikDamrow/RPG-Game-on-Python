import entity
import random
class Ogre(entity.Entity):
    '''One of harder enemies'''
    def __init__(self):
        '''This is how we initialize this class
        Args:
        self: This is how to modify the class'''
        super().__init__("Goblin",random.randint(8,12))
    def attack(self,entity):
        '''This is how the hero will take damage from the enemy
        Args:
        self: This is how stuff is added to the class
        entity (class): This is the class being affected by this method
        Return:
        A string is returned to indicate a attack was present'''
        damage = random.randint(6,10)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
