import ZooCharacter as ZooCharacter
import CombatSystem
import Enemy



class ZooCharacterCreatorUI:

    def __init__(self):
        pass

    def runCharacterCreatorUI(self):
        raceEnum = None
        classEnum = None

        print("The choices for zoo race are:")
        
        for race in ZooCharacter.ZooCharacter.ZooRaceEnum:
            print(race.value)

        print("")
        _input = input() 

        for race in ZooCharacter.ZooCharacter.ZooRaceEnum:
            if _input == race.value: 
                raceEnum = race
                print("Character race validated")

        print("The choices zoo class are:")
        
        for zooClass in ZooCharacter.ZooCharacter.ZooClassEnum:
            print(zooClass.value)
        
        _input = input()  

        for zooClass in ZooCharacter.ZooCharacter.ZooClassEnum:
            if _input == zooClass.value:
                classEnum = zooClass
                print("Zoo class validated")
        zooCharacter = ZooCharacter.ZooCharacter(raceEnum, classEnum)
        
        print("This is your character!")
        print(repr(zooCharacter))

        combat_system = CombatSystem.CombatSystem()

        numEnemiesDefeated = 0
        current_enemy = Enemy.Enemy()


        while (zooCharacter.health > 0 ):
            #get input for movement 
            self.__handle_combat_input(zooCharacter)
            #handle combat
            combat_system.performCombat(zooCharacter, current_enemy)
            if (current_enemy.health < 0):
                numEnemiesDefeated += 1
                current_enemy = Enemy.Enemy()
            
            


        print(f"Your zoo chatacter has defeated {numEnemiesDefeated} enemies")


    
    def __handle_combat_input(self, zooCharacter):
        valid_input = False 
        while( not valid_input):
            print("Your options for combat are: \nattack \nblock \n")
            _input = input()

            for combatOption in ZooCharacter.ZooCharacter.CombatMode:
                if _input == combatOption.value:
                    valid_input = True
                    zooCharacter.set_combat_mode(combatOption)



        

        
                
            


        



        
        
        

        


    
    

        