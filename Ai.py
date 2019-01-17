import Creature
import Battle
import Map
import random

def ai_class(selection):
    if selection == 1:
        Hero = Creature.Knight
        print("Ai is a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif selection == 2:
        Hero = Creature.Mage
        print("Ai is a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability:  You have 80% chanse to escape" + "\n\n")
    elif selection == 3:
        Hero = Creature.Theif
        print("Ai is a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You have 25% chanse to dubble your damage" + "\n\n")
    else:
        print("Invalid selection")

def ai_map(size):
    if size == '1':
        Map.mapsize(4, 4)
    elif size == '2':
        Map.mapsize(5, 5)
    elif size == '3':
        Map.mapsize(8, 8)

def ai_start_room():
    start_room = random.randint(1, 4)
    if start_room == 1:
        curx = 0
        cury = 0
    elif start_room == 2:
        curx = Map.sizex - 1
        cury = 0
    elif start_room == 3:
        curx = 0
        cury = Map.sizey - 1
    elif start_room == 4:
        curx = Map.sizex - 1
        cury = Map.sizey - 1
    else:
        print("Invalid selection")

    print("AI picked", cury, curx, " as its starting position")

def random_direction():
    direction = random.randint(1, 4)
    return direction

def ai_move():
    while True:
        if random_direction() == 1:
            Map.prevx = Map.curx
            Map.prevy = Map.cury

            for newroom in Map.mapcord:
                if newroom.gety() == (Map.cury - 1) and newroom.getx() == Map.curx:
                    cury = (newroom.gety())
                    break
            if Map.cury == Map.prevy:
                print("Ai searches the wall for a door but are unable to find one.")
                continue

        elif random_direction() == 2:
            Map.prevx = Map.curx
            Map.prevy = Map.cury

            for newroom in Map.mapcord:
                if newroom.gety() == (cury + 1) and newroom.getx() == Map.curx:
                    Map.cury = (newroom.gety())
                    break
            if Map.cury == Map.prevy:
                print("Ai searches the wall for a door but are unable to find one.")
                continue

        elif random_direction() == 3:
            Map.prevx = Map.curx
            Map.prevy = Map.cury

            for newroom in Map.mapcord:
                if newroom.getx() == (Map.curx - 1) and newroom.gety() == Map.cury:
                    Map.curx = (newroom.getx())
                    break
            if Map.curx == Map.prevx:
                print("Ai searches the wall for a door but are unable to find one.")
                continue

        elif random_direction() == 4:
            Map.prevx = Map.curx
            Map.prevy = Map.cury

            for newroom in Map.mapcord:
                if newroom.getx() == (Map.curx + 1) and newroom.gety() == Map.cury:
                    Map.curx = (newroom.getx())
                    break
            if Map.curx == Map.prevx:
                print("Ai searches the wall for a door but are unable to find one.")
                continue

        print(Map.cury, Map.curx)