from model.rennwagen import Rennwagen
from model.rennen import Rennen


def main():

    wagen1 = Rennwagen()
    wagen2 = Rennwagen()
    wagen3 = Rennwagen()
    wagen4 = Rennwagen()
    wagen5 = Rennwagen()
    wagen6 = Rennwagen()

    rennen = Rennen()
    rennen.startetrennen(wagen1,wagen2,wagen2,wagen3,wagen4,wagen5,wagen6)