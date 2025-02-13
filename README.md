# Racer-Brettspiel
Unser Ziel ist es ein Brettspiel zu entwickeln in dem die Spieler versuchen mit ihrem Rennwagen zuerst ins Ziel zu gelangen.
Die Rennwagen sollen unterschiedlich sein und trotzdem soll jeder Spieler, potenziell mit jedem Wagen gewinnen können.  

Jeder Wagen kann definiert werden mit:  
  - Wieviele Würfel pro Runde  
  - Wieviele Seiten haben die Würfel  
  - Statischer Bonus  

Die Wagen dürfen sich pro Runde um soviele Meter
fortbewegen wie die Augenanzahl + Bonus angibt.

Mithilfe eines Programms sollen wir nun 12 verschiedene
Wagen definieren (einer pro Person in unserem Team) und testen
ob jeder dieser Wagen gewinnen kann.  

Rennwagen sollen:  
  - Jede Runde mind. einen Meter nach vorne fahren  
  - Nie Rückwärts fahren  
  - müssen immer mind. einen Würfelwurf pro Runde haben  
  - unterscheidbar sein (mind. durch Namen und mindestens einen der anderen Werte)  
  - bei 10000 Spielen mind. einmal gewonnen haben  

Nun wollen wir das Programm auch als Spiel nutzen können, dafür wurden folgende Features identifiziert:  
  - In der Konsole sollen nun auch Kommentatoren den Rennverlauf beschreiben. Ausgabe immer wenn ein Wagen die Spitzenposition einnimmt, oder wenn ein Wagen weit zurück fällt.  
  - Der Gewinner bekommt eine Personalisierte Glückwunschsnachricht.  
  - Die Ausgaben sind so verzögert, das man die Konsolenausgaben mitlesen kann. Man hat das Gefühl dabei zu sein.  
