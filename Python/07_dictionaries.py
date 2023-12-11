"""
Author: Mark Dackus
Date: 26-11-2023
Script: Dictionaries
"""
import os
import datetime

# Haal de datum en tijd van vandaag op en sla deze op in de variable today.
vandaag_datumtijd = datetime.date.today()

# Verander het formaat naar YYYY-MM-DD. Sla
# Bijvoorbeeld 2023-11-26
vandaag_datum = vandaag_datumtijd.strftime("%Y-%m-%d")

gebruiker = {
    "username": "administrator",
    "firstname": "Gerard",
    "lastname": "Hoeven",
    "woonplaats": "Maastricht",
    "creationDate": vandaag_datum
}

print("Gebruikersnaam: ", gebruiker["username"])
print("Voornaam: ", gebruiker["firstname"])
print("Achernaam: ", gebruiker["lastname"])
print("Aanmaakdatum: ", gebruiker["creationDate"])
print("Woonplaats: ", gebruiker["woonplaats"])

gebruiker["username"] = "admin"
print("Nieuwe gebruikersnaam: ", gebruiker["username"])

gebruiker2 = {
    "username": "administrator2",
    "firstname": "Bert",
    "lastname": "Jan",
    "woonplaats": "Geleen",
    "creationDate": vandaag_datum
}

print("Gebruikersnaam: ", gebruiker2["username"])
print("Voornaam: ", gebruiker2["firstname"])
print("Achernaam: ", gebruiker2["lastname"])
print("Aanmaakdatum: ", gebruiker2["creationDate"])
print("Woonplaats: ", gebruiker2["woonplaats"])

gebruiker2["username"] = "admin"
print("Nieuwe gebruikersnaam: ", gebruiker2["username"])