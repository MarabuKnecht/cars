import random


class Wuerfel:

    """Diese methode initialisiert den Würfel und seine Attribute."""

    def __init__(self, seiten_anzahl: int, wuerfel_name: str):
        self.seiten_anzahl = seiten_anzahl
        self.wuerfel_name = wuerfel_name

    def wuerfeln(self):
        """
        Die Methode wählt eine zufällige Zahl im bereich zwischen 1 und
        der Seitenanzahl des Würfels aus.
        """

        return random.randint(1, self.seiten_anzahl)