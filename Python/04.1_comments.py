cijfers = [30, 29, 34, 31, 28, 38, 29, 17, 18, 22, 41, 39, 43, 29, 47, 33, 36, 37, 39, 20, 3, 48, 28, 29, 29, 41, 41]


def calculate_grade( aantal_behaalde_punten, max_aantal_punten ):


    cijfer = ( 9 * aantal_behaalde_punten ) / max_aantal_punten + 1

    return cijfer


for cijfer in cijfers:
    behaald_cijfer = calculate_grade(cijfer, 48)
    print(round(behaald_cijfer, 1))
