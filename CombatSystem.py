import ZooCharacter
import Enemy

class CombatSystem:

    def performCombat(self, zooCharacter:ZooCharacter, enemy:Enemy):

        if (zooCharacter.combat_mode == ZooCharacter.ZooCharacter.CombatMode.attack):
            enemy.health -= zooCharacter.combat_factor/2
        elif (zooCharacter.combat_mode == ZooCharacter.ZooCharacter.CombatMode.block):
            zooCharacter.health -= 2
            