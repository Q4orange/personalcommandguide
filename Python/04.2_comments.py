aantal_behaalde_punten = int(input("behaald punt: "))

def calculate_grade( aantal_behaalde_punten, max_aantal_punten ):
    cijfer = ( 9 * aantal_behaalde_punten ) / max_aantal_punten + 1
    return cijfer

behaalde_cijfer = calculate_grade(aantal_behaalde_punten , 48)

print(round(behaalde_cijfer, 1))