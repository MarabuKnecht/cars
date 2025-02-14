from model.rennwagen import Rennwagen
from model.rennen import Rennen


def main():

# Silas 1, Sinan 2, Henning 3, Eduard 4, Jalal 5, Zakariya 6, Joel 7
    wagen1 = Rennwagen("silas super sahne schliten",4,4,0)
    wagen2 = Rennwagen("Toretto", 3, 4, 2)
    wagen3 = Rennwagen("DerStein", 2, 4,4)
    wagen4 = Rennwagen("Eduard", 2, 8, 1)
    wagen5 = Rennwagen()
    wagen6 = Rennwagen("McQueen", 2, 6,3)
    wagen7 = Rennwagen("Ford Focus", 1,12,1)

    rennen = Rennen()
    rennen.startetrennen(wagen1,wagen2,wagen3,wagen4,wagen5,wagen6,wagen7)