from model.rennwagen import Rennwagen
from model.rennen import Rennen


def main():

# Silas 1, Sinan 2, Hennin 3, Eduard 4, Jalal 5, Zakariya 6, Joel 7
    wagen1 = Rennwagen("silas super schlieten",4,4,0)
    wagen2 = Rennwagen()
    wagen3 = Rennwagen()
    wagen4 = Rennwagen()
    wagen5 = Rennwagen()
    wagen6 = Rennwagen()
    wagen7 = Rennwagen()

    rennen = Rennen()
    rennen.startetrennen(wagen1,wagen2,wagen3,wagen4,wagen5,wagen6,wagen7)