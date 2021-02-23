


from random import randint

class Enemy:

    health = 0


    def __init__(self):
        self.health = randint(0, 4)