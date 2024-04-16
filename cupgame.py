#Gabriela Fuller
#“I have not given or received any unauthorized assistance on this assignment.”
#https://youtu.be/_-at3BLiETs
import random

class sixside:
    def __init__(self):
        self.face_value = random.randint(1, 6)

    def roll(self):
        self.face_value = random.randint(1, 6)

    def get_face_value(self):
        return self.face_value

    def __repr__(self):
        return f"sixside({self.face_value})"

class tenside(sixside):
    def roll(self):
        self.face_value = random.randint(1, 10)

    def __repr__(self):
        return f"tenside({self.face_value})"

class twentyside(sixside):
    def roll(self):
        self.face_value = random.randint(1, 20)

    def __repr__(self):
        return f"twentyside({self.face_value})"

class Cup: #cup containing random dice 
    def __init__(self, num_six=1, num_ten=1, num_twenty=1):
        self.dice = []
        for _ in range(num_six):
            self.dice.append(sixside())
        for _ in range(num_ten):
            self.dice.append(tenside())
        for _ in range(num_twenty):
            self.dice.append(twentyside())

    def roll(self):
        for die in self.dice:
            die.roll()

    def get_sum(self):
        return sum(die.get_face_value() for die in self.dice)

    def __repr__(self):
        dice_counts = [
            f"{type(die).__name__}({die.face_value})"
            for die in self.dice
        ]
        return f"Cup({', '.join(dice_counts)})"

def play_dice_game():
    score = 0
    name = input("Hello! What's your name? ")

    while True:
        play_again = input(f"Hi {name}, would you like to play a dice game (y/n)? ").lower()
        if play_again != "y":
            break

        goal = random.randint(1, 100)
        print(f"The goal is {goal}.")

        num_six = int(input("How many six-sided dice do you want to roll? "))
        num_ten = int(input("How many ten-sided dice do you want to roll? "))
        num_twenty = int(input("How many twenty-sided dice do you want to roll? "))
#prompts the user for the number of each type of die they want to roll, creates a cup with the specified dice
        cup = Cup(num_six, num_ten, num_twenty)
        cup.roll()
        roll_sum = cup.get_sum()
        print(f"You rolled {roll_sum}.")
#rolls the cup, and calculates the sum of the face values. Based on the roll and the goal, it awards points to the user and updates the score
        if roll_sum == goal:
            score += 10
            print("Perfect match! You earned 10 points.")
        elif goal - 3 <= roll_sum < goal:
            score += 5
            print("Close enough! You earned 5 points.")
        elif goal - 10 <= roll_sum < goal:
            score += 2
            print("Not bad! You earned 2 points.")
        else:
            print("Oh no! You didn't score this time.")

        print(f"Your current score is {score}.")
#Finally, it asks if the user wants to play again, and if not, it exits the loop and displays the final score.
    print(f"Your final score is {score}. Thanks for playing, {name}!")

if __name__ == "__main__":
    play_dice_game()




