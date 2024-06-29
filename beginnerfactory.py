import enemyfactory
import EasyTroll
import EasyOgre
import EasyGoblin
import random
class BeginnerFactory (enemyfactory.EnemyFactory):
    '''This is the easy factory that will be used for a easier game for the user'''
    def create_random_enemy(self):
        '''This will randomely generate a enemy for the user to fight with in the game
        Args:
        self: The only way to declare things in this class itself
        Return:
        Enemies(classes): Three different enemies will be generated for the user to fight with'''
        randomEnemy = random.randint(1,3)
        if randomEnemy == 1:
            return EasyTroll.EasyTroll()
        elif randomEnemy == 2:
            return EasyOgre.EasyOgre()
        elif randomEnemy == 3:
            return EasyGoblin.EasyGoblin()
        
