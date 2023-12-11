"""
Author: Mark Dackus
Date: 26-11-2023
Script: Enquete (Datatypes)
"""

pythonLeukInput = input( "Ik vind Python leuk. Geef een cijfer schaal 1 tot 10: ")
pythonMoeilijkInput = input( "Ik vindt Python moeilijk: Geef een cijfer schaal 1 tot 10: ")
pythonZinvolInput = input( "Ik vindt Python zinvol: Geef een cijfer schaal 1 tot 10: ")
pythonInspirerendInput = input( "Ik vindt Python Inspirerend: Geef een cijfer schaal 1 tot 10: ")

print("Type pythonLeukInput: ", type(pythonLeukInput))
print("Type pythonMoeilijkInput: ", type(pythonMoeilijkInput))
print("type pythonZinvolInput: ", type(pythonZinvolInput))
print("Type pythonInspirerend: ", type(pythonInspirerendInput))

pythonLeuk = int(pythonLeukInput)
pythonMoeilijk = int(pythonMoeilijkInput)
pythonZinvol = int(pythonZinvolInput)
pythonInspirerend = int(pythonInspirerendInput)

gemiddelde = (pythonLeuk + pythonMoeilijk + pythonZinvol + pythonInspirerend) / 4
print("Gemiddelde: ", gemiddelde)



print("Type pythonLeuk: ", type(pythonLeuk))
print("Type pythonMoeilijk: ", type(pythonMoeilijk))
print("type pythonZinvol: ", type(pythonZinvol))
print("Type pythonInspirerend: ", type(pythonInspirerend))

a = 7
b = 4 + 3
c = a == b

print("a: ", a)
print("Type a: ", type(a))
print("b: ", b)
print("type b: ", type(b))
print("c: ", c)
print("Type c: ", type(c))

if gemiddelde < 5.5:
    print("Je hebt een motivatieprobleem")
