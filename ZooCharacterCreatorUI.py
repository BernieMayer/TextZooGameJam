import ZooCharacter as ZooCharacter

class ZooCharacterCreatorUI:

    def __init__(self):
        pass

    def runCharacterCreatorUI(self):
        print("The choices for character race are:")
        
        for race in ZooCharacter.ZooCharacter.ZooRaceEnum:
            print(race.value)
        