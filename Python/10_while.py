"""
Author: Mark Dackus
Date: 26-11-2023
Script: while
"""

import random
tafel_van = 10
invoer_juist = False
while not invoer_juist:
    tafel_van_input = input("Van welk getal wil je het tafeltje: (tussen 1 en 100): ")
    if (tafel_van_input.isdigit()):
        tafel_van = int(tafel_van_input)
        invoer_juist = True

start = 0
while (start < 25):
    start = start + 1
    antwoord = start * tafel_van
    print(f"{start} x {tafel_van} = {antwoord}")

tafel = random.randint(1, 100)

antwoord = int(input(f"Wat is {tafel} x 7? "))

if antwoord == tafel * 7:
    print("Super gedaan!")
else:
    print(f"Helaas, het juiste antwoord is {tafel * 7}.")

getal = random.randint(1, 10)

antwoord = 0
while antwoord != getal:
    antwoord = int(input("Raad het getal tussen 1 en 10: "))
    if antwoord == getal:
        print("Super gedaan!")
    else:
        print("Helaas, probeer het nog eens.")