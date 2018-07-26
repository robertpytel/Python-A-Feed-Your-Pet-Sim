# -*- coding: utf-8 -*-
from random import randint
from enum import Enum
"""
Robert Pytel
Activity A application
Accepting user input from commmand line
7/24/2018
"""
# wanted to use http://www.panda3d.org/download.php, could not
# could not use Tkinter: https://www.youtube.com/watch?v=KEnDTjBMLhU
# inspiration from
# http://inventwithpython.com/pygame/chapter2.html#
# https://stackoverflow.com/questions/38635419/searching-in-google-with-python
"""
SOURCES:
    https://stackoverflow.com/questions/18406165/creating-a-timer-in-python
"""


class colors(Enum):
    Blue = 1
    Red = 2
    Green = 3


class pets(Enum):
    Dog = 1
    Cat = 2
    Python = 3


class PET:
    dead = False
    isA = ""
    color = ""
    name = ""
    health = randint(8, 20)
    thirst = 0


def gameOver():
    print ("GAME OVER! {0} DIED!".format(pet.name))
    pet.dead = True


# Introduction
playerName = input("Hello! Welcome to Pet Sim!\nWhat is your name?\n")
print("\nHello {0}!".format(playerName))

pet = PET()

# Choose your pet!
pet.isA = input("Please choose one of these pets: {0}, {1} or {2}\n".format(
    pets.Cat.name, pets.Dog.name, pets.Python.name))
while (not (
       (pet.isA.upper() == "CAT") or
       (pet.isA.upper() == "DOG") or
       (pet.isA.upper() == "PYTHON"))):
    pet.isA = input("Please choose one of these pets: {0}, {1} or {2}\n"
                    .format(pets.Cat.name, pets.Dog.name, pets.Python.name))

# Choose your pet's name!
pet.name = input("What is your {0}'s name?\n".format(pet.isA))

# Choose your pet's color!
pet.color = input("Alright {0}! What color is {1}? (blue, red, green)\n"
                  .format(playerName, pet.name))
while (not (
       (pet.color.upper() == "BLUE") or
       (pet.color.upper() == "RED") or
       (pet.color.upper() == "GREEN"))):
    pet.color = input("Alright {0}! What color is {1}? (blue, red, green)\n"
                      .format(playerName, pet.name))

# Game start!
input("Alright! Just hit enter to start!\n")


def main():
    while (not pet.dead):
        """Pet STATS"""
        print(playerName)
        print("{0}, your {1} {2}".format(pet.name, pet.color, pet.isA))
        print("health: {0}".format(pet.health))
        print("thirst: {0}".format(pet.thirst))

        """If your pet is dead, game over"""
        if (pet.health <= 0 or pet.thirst >= 10):
            gameOver()
            break
        """If your pet is extrememly healthy, it is immortal. You win!"""
        if (pet.health >= 25):
            print("{0} is immortal now!".format(pet.name))
            print("GAME OVER!")
            pet.dead = True
            break

        """Maintain your pet"""
        """FOOD"""
        food = input("Will you feed {0}? (y/n)\n".format(pet.name))
        if (food.strip().upper() == "Y"):
            pet.health += 1  # increase health by one
        else:
            pet.health -= 2  # decrease health by two
        if (pet.health < 0):
            pet.health = 0  # prevent less than zero

        """WATER"""
        water = input("Will you give {0} a drink of water? (y/n)\n"
                      .format(pet.name))
        if (water.strip().upper() == "Y"):
            pet.thirst -= 1  # decrease thirst by one
            if (pet.thirst < 0):
                pet.thirst = 0  # prevent less than zero
        else:
            pet.thirst += 2  # increase thirst by one

        print("\n")  # skip a line!


# main function runner
if __name__ == '__main__':
    main()
