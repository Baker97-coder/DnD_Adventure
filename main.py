import random

# main

print("Welcome to my text-based DnD adventure" + "\n")


with open("Eldar_Dracarys.txt", "r") as character_sheet:
    data = character_sheet.readlines()

name, Strength, S_modifier,\
Dexterity, D_modifier, Constitution, C_modifier, Intelligence,\
I_modifier, Wisdom, W_modifier, Charisma, CH_modifier, Hit_points,\
Current_hit_point, potential_attack_damage\
= [d.split(":")[1].split("/n")[0] for d in data]

print("Your character that you have loaded in" + "\n")
print(name)
