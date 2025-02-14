from wuerfel import Wuerfel

class Rennwagen:
    """
    Klasse zur Repräsentation eines Rennwagens mit Würfeln und einem festen
    Bonuswert.
    """
    def __init__(self, name, wuerfel_anzahl, wuerfel_seiten, buff):
        if wuerfel_anzahl <= 0 or wuerfel_anzahl > 10:
            raise ValueError("Ein Rennwagen muss 1 bis 10 Würfel haben.")
        if wuerfel_seiten < 2 or wuerfel_seiten > 20:
            raise ValueError("Ein Würfel muss zwischen 2 und 20 Seiten haben.")

        self.name = name  # Name des Rennwagens
        self.wuerfel = [Wuerfel(wuerfel_seiten) for _ in range(wuerfel_anzahl)]
        # Liste der Würfel
        self.buff = buff  # Fester Bonuswert
        self.gefahrene_strecke = 0  # die gefahrene Strecke des Rennwagens
        self.siege = 0  # Anzahl der gewonnenen Rennen

    def fahren(self):
        """
        Berechnet die gefahrene Strecke basierend auf den Würfelwürfen und dem
        Bonuswert.
        Aktualisiert die Position des Rennwagens.
        """
        wurf = sum(w.wuerfeln() for w in self.wuerfel)
        self.gefahrene_strecke += wurf + self.buff
        return wurf + self.buff

    def erhoehe_siegesanzahl(self):
        """
        Erhöht die Anzahl der Siege des Rennwagens um 1.
        """
        self.siege += 1

    def get_siege(self):
        """
        Gibt die Anzahl der Siege des Rennwagens zurück.
        """
        return self.siege

    def reset_position(self):
        """
        Setzt die Position des Rennwagens zurück
        """
        self.gefahrene_strecke = 0


