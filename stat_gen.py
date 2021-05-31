import random
import math

character_race = []
# ability score order: [Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma]
ability_scores = []
scores = {}


def race_check(race):
    character_race.clear()

    if race.lower() == "dragonborn":
        character_race.append(race)

    elif race.lower() == "dwarf":
        character_race.append(race)

    elif race.lower() == "elf":
        character_race.append(race)

    elif race.lower() == "gnome":
        character_race.append(race)

    elif race.lower() == "half-elf":
        character_race.append(race)

    elif race.lower() == "halfling":
        character_race.append(race)

    elif race.lower() == "half-orc":
        character_race.append(race)

    elif race.lower() == "human":
        character_race.append(race)

    elif race.lower() == "tiefling":
        character_race.append(race)


def apply_racial_stat():
    temp = character_race[0]

    if temp == "DRAGONBORN":
        temp_score = ability_scores[0]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(0, temp_score)

        temp_score = ability_scores[5]
        ability_scores.remove(temp_score)
        temp_score += 1
        ability_scores.insert(5, temp_score)

        scores['Strength'] = ability_scores[0]
        scores['Charisma'] = ability_scores[5]

    elif temp == "DWARF":
        temp_score = ability_scores[2]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(2, temp_score)

        scores['Constitution'] = ability_scores[2]

    elif temp == "ELF":
        temp_score = ability_scores[1]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(1, temp_score)

        scores['Dexterity'] = ability_scores[1]

    elif temp == "GNOME":
        temp_score = ability_scores[3]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(3, temp_score)

        scores['Intelligence'] = ability_scores[3]

    elif temp == "HALF-ELF":
        temp_score = ability_scores[5]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(5, temp_score)
        scores['Charisma'] = ability_scores[5]

        # Pick 2 random stats to increase by 1
        stat1 = random.randint(0, 4)
        stat2 = random.randint(0, 4)

        token = False
        while not token:
            if stat1 == stat2:
                stat2 = random.randint(0, 4)
            else:
                token = True

        temp_score = ability_scores[stat1]
        ability_scores.remove(temp_score)
        temp_score += 1
        ability_scores.insert(stat1, temp_score)

        if stat1 == 0:
            scores['Strength'] = ability_scores[0]
        elif stat1 == 1:
            scores['Dexterity'] = ability_scores[1]
        elif stat1 == 2:
            scores['Constitution'] = ability_scores[2]
        elif stat1 == 3:
            scores['Intelligence'] = ability_scores[3]
        elif stat1 == 4:
            scores['Wisdom'] = ability_scores[4]

        temp_score = ability_scores[stat2]
        ability_scores.remove(temp_score)
        temp_score += 1
        ability_scores.insert(stat2, temp_score)

        if stat2 == 0:
            scores['Strength'] = ability_scores[0]
        elif stat2 == 1:
            scores['Dexterity'] = ability_scores[1]
        elif stat2 == 2:
            scores['Constitution'] = ability_scores[2]
        elif stat2 == 3:
            scores['Intelligence'] = ability_scores[3]
        elif stat2 == 4:
            scores['Wisdom'] = ability_scores[4]

    elif temp == "HALFLING":
        temp_score = ability_scores[1]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(1, temp_score)

        scores['Dexterity'] = ability_scores[1]

    elif temp == "HALF-ORC":
        temp_score = ability_scores[0]
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(0, temp_score)

        temp_score = ability_scores[2]
        ability_scores.remove(temp_score)
        temp_score += 1
        ability_scores.insert(2, temp_score)

        scores['Strength'] = ability_scores[0]
        scores['Constitution'] = ability_scores[2]

    # same bug with tiefling, however seems to occur more often
    elif temp == "HUMAN":
        for x in range(len(ability_scores)):
            temp_score = ability_scores[x]
            ability_scores.remove(temp_score)
            temp_score += 1
            ability_scores.insert(x, temp_score)

        scores['Strength'] = ability_scores[0]
        scores['Dexterity'] = ability_scores[1]
        scores['Constitution'] = ability_scores[2]
        scores['Intelligence'] = ability_scores[3]
        scores['Wisdom'] = ability_scores[4]
        scores['Charisma'] = ability_scores[5]

    # bug occurring post stat adjustment (potentially affecting tieflings and humans)
    # flips the stats on index 0 with index 1 and vice versa (seems to only trigger occasionally)
    elif temp == "TIEFLING":
        temp_score = ability_scores[5]
        # print(temp_score)
        ability_scores.remove(temp_score)
        temp_score += 2
        ability_scores.insert(5, temp_score)
        # print(ability_scores[5])
        scores['Charisma'] = ability_scores[5]

        temp_score = ability_scores[3]
        # print(temp_score)
        ability_scores.remove(temp_score)
        temp_score += 1
        ability_scores.insert(3, temp_score)
        # print(ability_scores[3])
        scores['Intelligence'] = ability_scores[3]

    """
    print("Ability Scores post racial stat adjustment:")
    print(scores)
    """


def generate_ability_score(dice_type):
    # dice_rolls is used to find ability scores using 4d6 for a potentially more balanced character
    dice_rolls = []
    # big_counter keeps track of how far down the ability scores are, ie: if it's completed 1 or 5 scores
    big_counter = 0
    counter = 0
    if dice_type.lower() == "d6" or dice_type.lower() == "4d6":
        while big_counter < 6:
            total = 0
            while counter < 4:
                dice_rolls.append(random.randint(1, 6))
                counter += 1

            temp = dice_rolls[0]
            for x in range(len(dice_rolls)):
                if dice_rolls[x] < temp:
                    temp = dice_rolls[x]
            dice_rolls.remove(temp)

            for y in dice_rolls:
                total += y
            ability_scores.append(total)
            dice_rolls.clear()

            big_counter += 1
            counter = 0

        scores['Strength'] = ability_scores[0]
        scores['Dexterity'] = ability_scores[1]
        scores['Constitution'] = ability_scores[2]
        scores['Intelligence'] = ability_scores[3]
        scores['Wisdom'] = ability_scores[4]
        scores['Charisma'] = ability_scores[5]

        print(scores)
        apply_racial_stat()

    if dice_type.lower() == "d20":
        while len(ability_scores) < 6:
            ability_scores.append(random.randint(1, 20))

        scores['Strength'] = ability_scores[0]
        scores['Dexterity'] = ability_scores[1]
        scores['Constitution'] = ability_scores[2]
        scores['Intelligence'] = ability_scores[3]
        scores['Wisdom'] = ability_scores[4]
        scores['Charisma'] = ability_scores[5]

        print(scores)
        apply_racial_stat()


def stat_modifier():
    # ((stat - 10)/2).floor = stat mod
    for x in range(len(ability_scores)):
        temp = ability_scores[x]
        modifier = math.floor((temp - 10)/2)

    pass


def pass_scores():
    return scores
