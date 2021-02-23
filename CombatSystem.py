import ZooCharacter
import Enemy
from random import randint

class CombatSystem:

    def performCombat(self, zooCharacter:ZooCharacter, enemy:Enemy):

        if (zooCharacter.combat_mode == ZooCharacter.ZooCharacter.CombatMode.attack):
            zooCharacter_attack_roll = randint(4, 12)
            enemyDefense_roll = randint(2, 12)

            if (zooCharacter_attack_roll < enemyDefense_roll):
                enemy.health -= 2
            else:
                zooCharacter.health -= 2
        elif (zooCharacter.combat_mode == ZooCharacter.ZooCharacter.CombatMode.block):
            zooCharacter_attack_roll = randint(0, 8)
            enemyDefense_roll = randint(1, 10)

            if (enemyDefense_roll > zooCharacter_attack_roll):
                zooCharacter.health -= 1
            