import random

# Creating a Dictionary to store the dice numbers

def roll():
    #function rolls the dice

    Dice = {1: "blank", 2: "blank", 3: "blank", 4: "blank", 5: "blank"}

    for i in range(1,6):

        number = random.randint(1, 6)
        Dice[i] = number
        i += 1

    print(Dice)



if __name__ == '__main__':

    FirstRoll = roll()