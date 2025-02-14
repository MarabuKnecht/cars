import random
import time

from rennwagen import Rennwagen

# 6 Rennwagen definieren
autos = [
    Rennwagen("Eduard", 2, 6, 2),
    Rennwagen("Jalal", 1, 12, 3),
    Rennwagen("Henning", 3, 4, 1),
    Rennwagen("Zakariya", 2, 8, 1),
    Rennwagen("Joel", 2, 10, 0),
    Rennwagen("Sinan", 1, 20, 0),
]

# Rennstrecke
ziel = 50
fuehrendes_auto = None  # Führendes Auto

print("\n🏁 DAS RENNEN BEGINNT! 🏁\n")

while True:
    for auto in autos:
        wurf = auto.fahren()
        print(f"{auto.name} fährt {wurf + auto.buff} Meter (Gesamt: {auto.gefahrene_strecke})")

        # Kommentator-Updates
        if fuehrendes_auto is None or auto.gefahrene_strecke > fuehrendes_auto.gefahrene_strecke:
            fuehrendes_auto = auto
            print(f"🔥 {auto.name} übernimmt die Führung!")
        elif auto.gefahrene_strecke < fuehrendes_auto.gefahrene_strecke - 10:
            print(f"😲 {auto.name} fällt weit zurück!")

        time.sleep(0.5)  # Verzögerung für mehr Spannung

        # Überprüfung auf Gewinner
        if auto.gefahrene_strecke >= ziel:
            print(f"\n🏆 {auto.name} hat das Rennen gewonnen! Herzlichen Glückwunsch! 🏆")
            exit()
