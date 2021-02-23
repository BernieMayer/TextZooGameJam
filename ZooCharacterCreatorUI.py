import ZooCharacter as ZooCharacter

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
        

        
                
            


        



        
        
        

        


    
    

        