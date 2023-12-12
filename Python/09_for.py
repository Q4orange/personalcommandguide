"""
Author: Mark Dackus
Date: 26-11-2023
Script: for loop
"""
# Let op! Als je dit script voor de tweede keer runt krijg je een foutmelding
# omdat de bestanden al bestaan. Verwijder dan eerst de aangemaakte bestanden.
bestanden_aan_te_maken = ["read.me", "license", "app.js"]

for bestandsnaam in bestanden_aan_te_maken:
    print("Bestandsnaam: ", bestandsnaam)
    
    with open(bestandsnaam, 'w') as f:
        f.write('Dit is het bestand ' + bestandsnaam)

# for a in range(11):
#     print(a)

for a in range(0, 101, 10):
    print(a)

import random

cijfers = []
for i in range(100):
    cijfers.append(round(random.uniform(0, 10), 1))

print("De 100 random getallen tussen 0 en 10, afgerond op 1 decimaal:")
for cijfer in cijfers:
    print(cijfer)