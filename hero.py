import entity
import random
import map
class Hero(entity.Entity):
    '''This is the class that will build the hero needed for the game'''
    def __init__(self,name):
        '''This is the initializer for future classes that will use this for the game when
        it comes to the hero that is needed
        Args:
        self: This is how we access the class
        name (string) : This is the name of the hero that the user will give
        '''
        super().__init__(name,25)
        self._loc = [0,0]
    @property
    def loc(self):
        '''This is a getter method that will be used to get the location of the hero
        that will be use for future methods
        Args:
        self: This is how we access the class
        Returns:
        self._loc (list): This is the x and y location of the hero on the map that will be
        used in the game
        '''
        return self._loc
    def attack(self,entity):
        '''This a modified version of the attack that was taken from the entity abstract class
        and is now being redefined for this class purpose
        Args:
        self: This is how we access the class
        entity(class): This is the enemy class that will be passed in to recieve the damage
        that is needed to continue the game properly
        Returns:
        self.name + "attacks a " + entity.name + "for " + str(damage) + "damage." :
        This is being return to notify the user of what has happened in the game and how
        much damaged that was given to the enemy in the game'''
        damage = random.randint(2,5)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
    def go_north (self):
        '''This is the method that will allow the player to move north and not go out
        of bounds on the map
        Args:
        self: This is how we access the class
        Returns:
        "x" (char): This is returned based on the condition in the if loop
        mapita[self.loc[0]][self.loc[1]]: This allows movement on the map if the loop
        condition was not fufilled'''
        mapita = map.Map()
        if (self._loc[0]-1 < 0):
            return "x"
        else:
            self._loc[0] -= 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_south (self):
        '''This is the method that will allow the player to move south and not go out
        of bounds on the map
        Args:
        self: This is how we access the class
        Returns:
        "x" (char): This is returned based on the condition in the if loop
        mapita[self.loc[0]][self.loc[1]]: This allows movement on the map if the loop
        condition was not fufilled'''
        mapita = map.Map()
        if (self._loc[0]+1 > 4):
            return "x"
        else:
            self._loc[0] += 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_east (self):
        '''This is the method that will allow the player to move east and not go out
        of bounds on the map
        Args:
        self: This is how we access the class
        Returns:
        "x" (char): This is returned based on the condition in the if loop
        mapita[self.loc[0]][self.loc[1]]: This allows movement on the map if the loop
        condition was not fufilled'''
        mapita = map.Map()
        if (self._loc[1]+1 > 4):
            return "x"
        else:
            self._loc[1] += 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_west (self):
        '''This is the method that will allow the player to move west and not go out
        of bounds on the map
        Args:
        self: This is how we access the class
        Returns:
        "x" (char): This is returned based on the condition in the if loop
        mapita[self.loc[0]][self.loc[1]]: This allows movement on the map if the loop
        condition was not fufilled'''
        mapita = map.Map()
        if (self._loc[1]-1 < 0):
            return "x"
        else:
            self._loc[1] -= 1
            return mapita[self.loc[0]][self.loc[1]]
