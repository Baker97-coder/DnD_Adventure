import random
import sys


def skeleton_damage(skeleton_hitpoints):
    player_damage = random.randint(1, int(potential_attack_damage))
    print("You deal " + str(player_damage) + " damage towards the skeleton")
    skeleton_hitpoints = skeleton_hitpoints - player_damage
    if skeleton_hitpoints <= 0:
        print("you killed the skeleton! he returns to the under.")
    else:
        print("The skeleton staggers, but is 'alive'.")
    print("")
    return skeleton_hitpoints


# main

print("Welcome to my text-based DnD adventure" + "\n")


with open("Eldar_Dracarys.txt", "r") as character_sheet:
    data = character_sheet.readlines()

# assignment unpacking
# for getting the player sheet into the game

name, Strength, S_modifier,\
Dexterity, D_modifier, Constitution, C_modifier, Intelligence,\
I_modifier, Wisdom, W_modifier, Charisma, CH_modifier, Hit_points,\
Current_hit_point, potential_attack_damage\
= [d.split(":")[1].split("/n")[0] for d in data]


# for getting a skeleton into the game
with open("Skeleton.txt", "r") as skeleton_sheet:
    skel_data = skeleton_sheet.readlines()

skel_attack, skel_hitpoints, skel_current_hitpoints = [d.split(":")[1].split("/n")[0] for d in skel_data]


class Skeletons:
    def __init__ (self, skel_attack, skel_hitpoints, skel_current_hitpoints, distance):
        self.skel_attack = int(skel_attack)
        self.skel_hitpoints = int(skel_hitpoints)
        self.skel_current_hitpoints = int(skel_current_hitpoints)
        self.skel_distance = int(distance)


print("Your character that you have loaded in" + "\n")
print(name)

game_action = input("you approach a cave with a wide mouth. It is very mysterious and you feel danger emanating "
                    "from it. do you enter? (y) or (n) : ")

print("")

if "n" in game_action:
    print("You go home to your mom and she makes you cookies, the end")
    sys.exit()

print("you enter the cave and it's dark with few torches lighting your way. you're not sure how the torches stay \n"\
      "lit as the cave looks looks like it hasn't been entered in centuries. you also notice that the cave seems.. \n"\
      "artificial. The cave is still rock and has random bumps to it, but the ground is relatively level and \n"\
      "easy to walk across. It is also follows an slight incline down into the ground." + "\n")

print("you hear a shuffling slowly, but steadily getting louder. after walking towards it, you see a skeleton with a "
      "sword! It's starts walking towards you and it looks like it's going to attack!")


first_skel = Skeletons(skel_attack, skel_hitpoints, skel_current_hitpoints, 1)

# first encounter with a skeleton, i initialize a skeleton instance and the while statement
# keeps running while the skeleton hit points are over 0

while first_skel.skel_current_hitpoints > 0:
    player_attack = input("do you use your bow or sword? : ")
    if "bow" in player_attack:
        print("\nyou take out an arrow with a silent confidence that speaks to your skill \n"
              "and pull it against the string. You let it fly")
        first_skel.skel_current_hitpoints = skeleton_damage(first_skel.skel_current_hitpoints)
    else:
        print("You hold your sword as a fire burns hot inside you and you strike!")
        first_skel.skel_current_hitpoints = skeleton_damage(first_skel.skel_current_hitpoints)
    if first_skel.skel_distance > 0:
        first_skel.skel_distance = first_skel.skel_distance - 1
    elif first_skel.skel_distance > 0 & first_skel.skel_current_hitpoints > 0:
        enemy_damage = random.randint(1, first_skel.skel_attack)
        print("The skeleton hits you with his sword, you take " + str(enemy_damage))
        Current_hit_point = int(Current_hit_point) - enemy_damage
        print("You have " + str(Current_hit_point) + " hitpoints")