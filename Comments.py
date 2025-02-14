import random
import time

class Auto:
    def __init__(self, name, wurfel_anzahl, wurfel_seiten, bonus):
        self.name = name
        self.wurfel_anzahl = wurfel_anzahl
        self.wurfel_seiten = wurfel_seiten
        self.bonus = bonus
        self.position = 0  # Startposition

    def fahren(self):
        wurf = sum(random.randint(1, self.wurfel_seiten) for _ in range(self.wurfel_anzahl))
        self.position += wurf + self.bonus
        return wurf

# 6 Rennwagen definieren
autos = [
    Auto("Eduard", 2, 6, 2),
    Auto("Jalal", 1, 12, 3),
    Auto("Hennig", 3, 4, 1),
    Auto("Zakariya", 2, 8, 1),
    Auto("Joel", 2, 10, 0),
    Auto("Sinan", 1, 20, 0),
]

# Rennstrecke
ziel = 50
fuehrendes_auto = None  # Führendes Auto

print("\n🏁 DAS RENNEN BEGINNT! 🏁\n")

while True:
    for auto in autos:
        wurf = auto.fahren()
        print(f"{auto.name} fährt {wurf + auto.bonus} Meter (Gesamt: {auto.position})")

        # Kommentator-Updates
        if fuehrendes_auto is None or auto.position > fuehrendes_auto.position:
            fuehrendes_auto = auto
            print(f"🔥 {auto.name} übernimmt die Führung!")
        elif auto.position < fuehrendes_auto.position - 10:
            print(f"😲 {auto.name} fällt weit zurück!")

        time.sleep(0.5)  # Verzögerung für mehr Spannung

        # Überprüfung auf Gewinner
        if auto.position >= ziel:
            print(f"\n🏆 {auto.name} hat das Rennen gewonnen! Herzlichen Glückwunsch! 🏆")
            exit()
