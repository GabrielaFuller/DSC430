#Gabriela Fuller
#“I have not given or received any unauthorized assistance on this assignment.”
#https://youtu.be/Kyol9n1iMIo

import random

class sixside:
    #Represents a standard six-sided die.#

    def __init__(self):
        #Initializes the die with a random face value.#
        self.face_value = random.randint(1, 6)

    def roll(self):
        #Rolls the die, generating a new random face value.#
        self.face_value = random.randint(1, 6)

    def get_face_value(self):
        #Returns the current face value of the die.#
        return self.face_value

    def __repr__(self):
        #Returns a string representation of the die in sixside(face_value) format.#
        return f"sixside({self.face_value})"

class tenside(sixside):
    #Represents a ten-sided die, inheriting properties and methods from sixside.#

    def __init__(self):
        #Initializes the die with a random face value (1-10).#
        self.face_value = random.randint(1, 10)

class twentyside(sixside):
    #Represents a twenty-sided die, inheriting properties and methods from sixside.#

    def __init__(self):
        #Initializes the die with a random face value (1-20).#
        self.face_value = random.randint(1, 20)

class Cup:
    #Represents a cup containing multiple dice of different types.#

    def __init__(self, num_six=1, num_ten=1, num_twenty=1):
        #Initializes the cup with the specified number of dice of each type.#
        self.dice = []
        for _ in range(num_six):
            self.dice.append(sixside())
        for _ in range(num_ten):
            self.dice.append(tenside())
        for _ in range(num_twenty):
            self.dice.append(twentyside())

    def roll(self):
        #Rolls all the dice in the cup, updating their face values.#
        for die in self.dice:
            die.roll()

    def get_sum(self):
        #Calculates and returns the sum of the face values of all dice in the cup.#
        return sum(die.get_face_value() for die in self.dice)

    def __repr__(self):
        #Returns a string representation of the cup showing its dice content.#
        dice_counts = [
            f"{type(die).__name__}" for die in self.dice
        ]
        return f"Cup({', '.join(dice_counts)})"

# Example usage:
d = sixside()
d.roll()
print(d)  # Output: sixside(3)

d = tenside()
d.roll()
print(d)  # Output: tenside(8)

cup = Cup(2, 1, 3)
print(cup)  # Output: Cup(sixside, tenside, twentyside, twentyside, twentyside)

cup.roll()
print(cup.get_sum())  # Output: 35 (or a different random sum)
