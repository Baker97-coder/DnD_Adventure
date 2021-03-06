import random
import sys


def check_if_player_is_dead():
    if Current_hit_point == 0:
        print("You have died.")
        sys.exit()


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


def sword_bow_attack(enemy):
    if "bow" in player_attack:
        print("\nyou take out an arrow with a silent confidence that speaks to your skill \n"
              "and pull it against the string. You let it fly")
        enemy.skel_current_hitpoints = skeleton_damage(enemy.skel_current_hitpoints)
    else:
        print("You hold your sword as a fire burns hot inside you and you strike!")
        enemy.skel_current_hitpoints = skeleton_damage(enemy.skel_current_hitpoints)
    return enemy.skel_current_hitpoints


def skel_attack_to_player(skeleton, current_hit_points):
    enemy_damage = random.randint(1, skeleton.skel_attack)
    print("The skeleton hits you with his sword, you take " + str(enemy_damage) + " damage")
    current_hit_points = int(current_hit_points) - enemy_damage
    print("You have " + str(Current_hit_point) + " hitpoints\n")
    return current_hit_points

# main


print("Welcome to my text-based DnD adventure" + "\n")


with open("Eldar_Dracarys.txt", "r") as character_sheet:
    data = character_sheet.readlines()

# assignment unpacking
# for getting the player sheet into the game, character sheet must follow this format

name, Strength, S_modifier,\
Dexterity, D_modifier, Constitution, C_modifier, Intelligence,\
I_modifier, Wisdom, W_modifier, Charisma, CH_modifier, Hit_points,\
Current_hit_point, potential_attack_damage\
= [d.split(":")[1].split("/n")[0] for d in data]


# for getting a skeleton (game enemy) into the game
with open("Skeleton.txt", "r") as skeleton_sheet:
    skel_data = skeleton_sheet.readlines()

skel_attack, skel_hitpoints, skel_current_hitpoints = [d.split(":")[1].split("/n")[0] for d in skel_data]


class Skeletons:
    def __init__(self, attack, hitpoints, current_hitpoints, distance):
        self.skel_attack = int(attack)
        self.skel_hitpoints = int(hitpoints)
        self.skel_current_hitpoints = int(current_hitpoints)
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

# first encounter with a skeleton

while first_skel.skel_current_hitpoints > 0:
    player_attack = input("do you use your bow or sword? : ")
    sword_bow_attack(first_skel)

    if first_skel.skel_distance <= 0 & first_skel.skel_current_hitpoints > 0:
        Current_hit_point = skel_attack_to_player(first_skel, Current_hit_point)
    first_skel.skel_distance -= 1

    check_if_player_is_dead()

print("After your victory, you continue deeper into the cave. You realize you haven't made any\n"
      "kind of turn or twist, it just goes further. Eventually you come across a door on your right.\n"
      "It's an ancient door and you're not sure it will even open due to its age.\n")

first_door = input("Do you try to open and enter the room? (y) or (n) : ")

has_read_note = False

# second encounter with enemies

if "y" in first_door:
    if int(Strength) > 10:
        print("You open the door even though its hinges were rusted and the door was heavy.\n"
              "You walk in and see a chest at the back of the room. As you approach it, two skeletons\n"
              "appear from the ground. they both have swords with one being 15 ft away. and the other\n"
              "being 30 ft away. You must fight.\n")

        room_skel1 = Skeletons(skel_attack, skel_hitpoints, skel_current_hitpoints, 1)
        room_skel2 = Skeletons(skel_attack, skel_hitpoints, skel_current_hitpoints, 2)

        while room_skel1.skel_current_hitpoints > 0 or room_skel2.skel_current_hitpoints > 0:
            player_attack = input("do you use your bow or sword? : ")

            if room_skel1.skel_current_hitpoints > 0 and room_skel2.skel_current_hitpoints > 0:
                attack_which = int(input("Which skeleton? (1) for first one (he is closest), (2) for second one : "))
            elif room_skel2.skel_current_hitpoints > 0 and room_skel1.skel_current_hitpoints <= 0:
                attack_which = 2
            elif room_skel2.skel_current_hitpoints <= 0 and room_skel1.skel_current_hitpoints > 0:
                attack_which = 1

            if attack_which == 1:
                room_skel1.skel_current_hitpoints = sword_bow_attack(room_skel1)
            else:
                room_skel2.skel_current_hitpoints = sword_bow_attack(room_skel2)

            if room_skel1.skel_distance <= 0 and room_skel1.skel_current_hitpoints > 0:
                Current_hit_point = skel_attack_to_player(room_skel1, Current_hit_point)
            if room_skel2.skel_distance <= 0 and room_skel2.skel_current_hitpoints > 0:
                Current_hit_point = skel_attack_to_player(room_skel2, Current_hit_point)

            room_skel1.skel_distance -= 1
            room_skel2.skel_distance -= 1

            check_if_player_is_dead()

            print("\nYou defeated the skeletons and you open the chest to find a note that read\n"
                  "'The Dragon loves when you compliment him on his gold stash.'")
            has_read_note = True

    else:
        print("you could not open the door, it was too heavy. You continue on.\n")

print("You start your way down the cave again.\n")
print("As you make your way further, you notice the cave starts the widen gradually. You see a light far into the \n"
      "distance. When you reach near the end of the tunnel, you stare at the mountains of gold, diamonds, rubies, \n"
      "Then you see the dragon. She's massive. It dwarfs war elephants. Its scales are a beautiful dark red with its \n"
      "wings on its two front 'arms'. It doesnt notice you.\n")

does_player_sneak = input(int("You see two ways to go about this.\n\n"
                              "1) You sneak closer to the dragon to either talk to it or attempt to kill it\n\n"
                              "2) You can run in, bows blazing and attempt to scare it. Doing so might intimidate the\n"
                              "dragon or it might not, it's a risk you'd have to take.\n\n"
                              "What do you chose to do? (1) for sneaking (2) for running in : "))

# Third and final encounter with the dragon

if does_player_sneak == 1:
    print("\nYou choose to sneak closer to the dragon. He does not see or hear you.\n")
    player_attack_or_negotiate = input(int(("You are now close to the dragon. You think of two options before you\n"
                                            "1) You could choose to attack the dragon 2) You could choose to negotiate"
                                            "with the dragon : ")))
    if player_attack_or_negotiate == 1:

    else:

else:
    print("You charge in and yell with a battle cry that echos the cave. The dragon hears you and turns to face you,\n"
          " ready for battle.")
    print("As you get closer the dragon rears its head and its throat begins to bellow and turn into a searing blue\n"
          " color. The dragon unleashes hell from its mouth and the gates welcome you with open arms as you are\n"
          " incinerated instantly. Your hitpoints are reduced to zero.")

    Current_hit_point = 0
    check_if_player_is_dead()