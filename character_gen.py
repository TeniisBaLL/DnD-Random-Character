import random
import json
from stat_gen import *
from pathlib import Path

# Adj + race + class + 'from' + location + 'who' + one trait/piece of info on their backstory

character_race = []
char_scream = []
data = {}


def introduction_scream():
    temp = []
    reader = open("lists/intro scream list", 'r')
    for line in reader:
        temp.append(line.strip())
    reader.close()

    x = random.randint(0, len(temp) - 1)

    return temp[x]


def character_scream():
    char_scream.clear()

    tempAdj = []
    tempRace = []
    tempClass = []
    tempLocation = []
    tempTrait = []

    reader = open("lists/adjective list", 'r')
    for line in reader:
        tempAdj.append(line.strip())
    reader.close()
    x = random.randint(0, len(tempAdj) - 1)
    tempA = tempAdj[x]

    reader = open("lists/race list", 'r')
    for line in reader:
        tempRace.append(line.strip())
    reader.close()
    x = random.randint(0, len(tempRace) - 1)
    tempB = tempRace[x]

    reader = open("lists/class list", 'r')
    for line in reader:
        tempClass.append(line.strip())
    reader.close()
    x = random.randint(0, len(tempClass) - 1)
    tempC = tempClass[x]

    reader = open("lists/location list", 'r')
    for line in reader:
        tempLocation.append(line.strip())
    reader.close()
    x = random.randint(0, len(tempLocation) - 1)
    tempD = tempLocation[x]

    reader = open("lists/trait and or backstory list", 'r')
    for line in reader:
        tempTrait.append(line.strip())
    reader.close()
    x = random.randint(0, len(tempTrait) - 1)
    tempE = tempTrait[x]

    quick_character = "{} {} {} FROM {} WHO {}".format(tempA, tempB, tempC, tempD, tempE)
    print(quick_character)

    race_check(tempB)
    character_race.append(tempB)

    char_scream.append(quick_character)


def big_scream():
    print("==========")
    print("{}".format(introduction_scream()))
    character_scream()


def class_saving_throws(class_type):
    pass


def c_page_assembly():
    data['{}'.format(char_scream[0])] = pass_scores()


def save_character():
    user_input = input("SAVE CHARACTER? Y/N: ")
    if user_input.lower() == "y":
        user_input = input("ENTER FILE NAME: ")
        try:
            c_page_assembly()
            base = Path('saved characters')
            char_file = open(base/(str(user_input) + ".json"), 'w')
            json.dump(data, char_file, indent=4)
            char_file.close()
        except Exception as e:
            print("Failed to save\n" + str(e))
    else:
        print("Exiting...")
        exit()
        

def main():
    character_race.clear()
    big_scream()
    user_response = input("WANNA REROLL FOR ANOTHER CHARACTER OR ROLL STATS? Y/N: ")
    if user_response.lower() == "y":
        main()

    elif user_response.lower() == "n":
        token = False
        while not token:
            user_response = input("WANNA ROLL A D20 FOR THIS FUCKER OR PUSSYFOOT WITH 4D6: ")
            if user_response.lower() == "d20" or user_response.lower() == "d6" or user_response.lower() == "4d6":
                generate_ability_score(user_response)
                print("==========")
                token = True
            else:
                print("WRONG DICE")
        save_character()
    else:
        print("Exiting...")
        exit()


main()
