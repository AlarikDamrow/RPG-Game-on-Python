import abc
class Entity (abc.ABC):
    '''This is the abstract class that will be used to create other classes more actual
    application of these modules and also redefinition of these modules.'''
    def __init__(self, name, max_hp):
        '''This is the initializer for future classes that will use them for the game
        Args:
        self: This is how we access the class
        name (string): This will be the name of the class for runtime of game
        max_hp (int): This is the max hp a class will have during the game'''
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    @property
    def name(self):
        '''This is the getter for name to be used within the game
        Args:
        self: This is how we access the class
        Returns:
        self._name (string): As mentioned this is the getter of name so it will return
        the name on request'''
        return self._name

    @property
    def hp(self):
        '''This is the getter of hp that will be used within the game
        Args:
        self: This is how we access the class
        Returns:
        self._hp (int): Since this is the getter of hp it will return the hp that class
        has at that time
        '''
        return self._hp
 
    def take_damage (self, dmg):
        '''This method is responsible for the damage that will be given to this
        class when needed and requested
        Args:
        self: This is how we access the class
        dmg(int): This is the amount of damage that will be given to this class
        '''
        if (self._hp - dmg) < 0:
            self._hp = 0
        else:
            self._hp = self._hp - dmg
    def heal (self):
        '''This method will heal the class to full health meaning health will be maxed
        out on request
        Args:
        self: This is how we access the class
        '''
        self._hp = self._max_hp
    def __str__(self):
        '''This the string method of class and how the class will print itself out on request
        Args:
        self: This is how we access the class
        Returns:
        form (string): This is the format of how it will look when requested for a print
        '''
        form = self._name+"\n"
        form += "HP:"+str(self._hp)+"/"+str(self._max_hp)
        return form

    @abc.abstractmethod
    def attack(self,entity):
        '''This is the attack method that will be redefined in other classes due to
        differences in use. It will deal damage to another class
        Args:
        self: This is how we access the class
        entity (Class): This is the other class that will take some damage
        '''
        pass
