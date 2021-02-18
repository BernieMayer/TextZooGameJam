import enum

class ZooCharacter:
    class ZooRaceEnum(enum.Enum):
        eagle =  "Eagle"
        hippo = "Hippo"

        

    class ZooClassEnum(enum.Enum):
        pyromancer = "Pyromancer"

    zooRace = ""
    zooClass = ""


    def setZooRace(self,  zooRaceEnum:ZooRaceEnum):
        self.zooRace = zooRaceEnum

    def setZooClass(self, zooClassEnum:ZooClassEnum):
        self.zooClass = zooClassEnum



    



