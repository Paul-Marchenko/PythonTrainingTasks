from random import randint

class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self, face):
        x = randint(1, face)
        for number in range(x):
            print(number)

decadent = Die()

decadent.roll_die(6)
#decadent.roll_die(10)
#decadent.roll_die(20)
