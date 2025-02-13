import random
import time

class Car:
    def __init__(self, name, dice_count, dice_sides, bonus):
        self.name = name
        self.dice_count = dice_count
        self.dice_sides = dice_sides
        self.bonus = bonus
        self.position = 0  # Startposition

    def move(self):
        roll = sum(random.randint(1, self.dice_sides) for _ in range(self.dice_count))
        self.position += roll + self.bonus
        return roll

# Rennwagen definieren
cars = [
    Car("Shadow Striker", 2, 6, 2),
    Car("Crimson Comet", 1, 12, 3),
    Car("Solar Storm", 3, 4, 1),
    Car("Emerald Thunder", 2, 8, 1),
]

# Rennstrecke
finish_line = 50
leader = None  # Führendes Auto

print("\n DAS RENNEN BEGINNT! \n")

while True:
    for car in cars:
        roll = car.move()
        print(f"{car.name} fährt {roll + car.bonus} Meter (Gesamt: {car.position})")

        # Kommentator-Updates
        if leader is None or car.position > leader.position:
            leader = car
            print(f" {car.name} übernimmt die Führung!")
        elif car.position < leader.position - 10:
            print(f" {car.name} fällt weit zurück!")

        time.sleep(0.5)  # Verzögerung für mehr Spannung

        # Überprüfung auf Gewinner
        if car.position >= finish_line:
            print(f"\n {car.name} hat das Rennen gewonnen! Glückwunsch!")
            exit()