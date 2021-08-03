""" SimSTB - Dateizugriff auf Austauschdateien

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Dateizugriff stellt zwei Funktionen zum Lesen und Schreiben der Austauschdateien
    zur Verfügung. Die Datenübergabe erfolgt jeweils als Liste.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           28.07.2021
    Letzte Änderung:    02.08.2021
    """

class DateiZugriff:
    def __init__(self, dateiname, max_laenge):
        """ Konstruktor des Datenzugriffs auf die Austauschdateien """
        self.dateiname = dateiname
        self.max_laenge = max_laenge

    def lesen_alle(self):
        """ Zeilenweises einlesen der Daten und Rückgabe als Liste """
        daten = []
        with open(self.dateiname, "r") as f:
            for zeile in f:
                zeile = zeile.replace(",",".")  # deutsches Komma in Austauschdatei
                zeile = zeile.rstrip("\n")
                daten = daten + [zeile]
        return daten

    def schreiben_alle(self, daten):
        """ Komplettes zurückschreiben aller Daten einer Austauschdatei """
        with open(self.dateiname, "w") as f:
            for wert in daten:
                zeile = str(wert)+"\n"
                zeile = zeile.replace(".",",")  # deutsches Komma in Austauschdatei
                f.write(zeile)
        return 
