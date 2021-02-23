import enum
from random import randint


class ZooCharacter:
    class ZooRaceEnum(enum.Enum):
        eagle = "Eagle"
        hippo = "Hippo"
        tiger = "Tiger"
        lizard = "Lizard"

        

    class ZooClassEnum(enum.Enum):
        pyromancer = "Pyromancer"
        elementalist = "Elementalist"
        aerotechnician = "Aerotechnician"
        marinist = "Marinist"
    
    class CombatMode(enum.Enum):
        attack = "attack"
        block = "block"

    zooRace = None
    zooClass = None
    combat_factor = 0
    cuteness_factor = 0
    tameness_factor = 0
    health = 0
    combat_mode = None

    MAX_COMBAT_FACTOR = 18
    MIN_COMBAT_FACTOR = 5
    
    MAX_CUTENESS_FACTOR = 10
    MIN_CUTENESS_FACTOR = 2
    
    MAX_TAMENESS_FACTOR = 10
    MIN_TAMENESS_FACTOR = 2

    MAX_STARTING_HEALTH = 14
    MIN_STARTING_HEALTH = 2



    def __init__(self, zooRace, zooClass):
        self.zooRace = zooRace
        self.zooClass = zooClass
        self.__generate_stats()
        self.__apply_class_and_race_bonus()


    def __generate_stats(self):
        self.combat_factor = randint(self.MIN_COMBAT_FACTOR, self.MAX_COMBAT_FACTOR)
        self.cuteness_factor = randint(self.MIN_CUTENESS_FACTOR, self.MAX_CUTENESS_FACTOR)
        self.tameness_factor = randint(self.MIN_TAMENESS_FACTOR, self.MAX_TAMENESS_FACTOR)
        self.health = randint(self.MIN_STARTING_HEALTH, self.MAX_STARTING_HEALTH)


    def __apply_class_and_race_bonus(self):
        if (self.zooRace == ZooCharacter.ZooRaceEnum.eagle):
            self.health += 2
        elif (self.zooRace == ZooCharacter.ZooRaceEnum.hippo):
            self.health -= 2
        elif (self.zooRace == ZooCharacter.ZooRaceEnum.tiger):
            self.health += 2
        elif (self.zooRace == ZooCharacter.ZooRaceEnum.lizard):
            self.health -= 2


    def set_combat_mode(self, combat_mode):
        self.combat_mode = combat_mode   

    def __repr__(self):
        return f"Zoo Race is {self.zooRace.value} Zoo Class is {self.zooClass.value} \n" \
        + f"Combat factor: {self.combat_factor}\n" \
        + f"Cuteness factor: {self.cuteness_factor}\n" \
        + f"Tameness factor: {self.tameness_factor}\n" \
        + f"Health factor: {self.health}\n"
 