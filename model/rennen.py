from Rennwagen import Rennwagen
from comments import autos
class Rennen:
    """legt eine klasse an"""
    def __init__(self):
        """setzt die Straekenlaenge auf 100"""
        self.Rennen_laenge = 100

    def startetrennen (self, autos):
        """Stratet das Rennen"""
        wagenliste = autos
        wagenImZiel = False
        gewinnerstrecke = 0
        gewinnerliste = []
        """inizialiesiert ein parr werte die später gebraucht erden"""
        while wagenImZiel == False:
            """ueberprueft ob das rennen zu ende ist """
            for car in wagenliste:
                """durchlauft alle ngelegten objekte der klasse Wagen"""
                car.fahren()
                """startet die naeste runde"""
                aktulerwagenstandort = car.getZuruekgelegteStrecke()
                """holt sich vom akuellen wagen seine position"""
                if aktulerwagenstandort >= 100:
                    """ueberprueft ob der wagen im ziel ist """
                    wagenImZiel = True
                    """setzt die bedingung das das ende nach der runde 
                    endet auf Wahr"""
                    if aktulerwagenstandort > gewinnerstrecke:
                        """ueberprueft ob das auto am weitesten vorne 
                        liegt"""
                        gewinnerstrecke = aktulerwagenstandort
                        """akualiesiert die strecke die das auto gefahren 
                        ist was am weitesten gefahren ist """
                        gewinnerliste = [car]
                        """ueberschreibt die liste mit gewinnern """
                    elif aktulerwagenstandort == gewinnerstrecke:
                        """ueberprueft ob ein auto genau so weit wie das 
                        gewinner auto ist """
                        gewinnerliste = gewinnerliste + [car]
                        """fuegt wenn wahr das auto der liste hinzu"""
                    else:
                        print ("das rennen geht weiter")
            if wagenImZiel == True:
                for car in wagenliste:
                    car.reset_position()
                    """bringt die autos wieder auf die startposition für das 
                    nächste rennen"""
                    for gewinnercar in gewinnerliste :
                        if gewinnercar == car :
                            """ueberprueft ob das aktuelle auto gewonnen hat"""
                        gewinnercar.erhoehe_siegesanzahl()
                        """gibt den autos bescheid wer gewonne hat"""