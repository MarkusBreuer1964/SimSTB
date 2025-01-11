""" SimSTB - Dateizugriff auf Austauschdateien
        Das Modul Dateizugriff stellt zwei Funktionen zum Lesen und Schreiben der Austauschdateien
        zur Verfügung. Die Datenübergabe erfolgt jeweils als Liste.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  28.07.2021, 11.08.2023
    """

import time


class DateiZugriff:
    """ Klasse zum Zugriff auf die Austauschdateien """

    def __init__(self, dateiname, max_laenge):
        """ Konstruktor des Datenzugriffs auf die Austauschdateien """
        self.dateiname = dateiname
        self.max_laenge = max_laenge

    def lesen_alle(self):
        """ Zeilenweises einlesen der Daten und Rückgabe als Liste """
        daten = []
        with open(self.dateiname, "r", encoding="utf8") as eingabedatei:
            for zeile in eingabedatei:
                zeile = zeile.replace(",", ".")  # deutsches Komma in Austauschdatei
                zeile = zeile.rstrip("\n")
                daten = daten + [zeile]
        # time.sleep(0.25)
        return daten

    def schreiben_alle(self, daten):
        """ Komplettes zurückschreiben aller Daten einer Austauschdatei """
        with open(self.dateiname, "w", encoding="utf8") as ausgabedatei:
            for wert in daten:
                zeile = str(wert)+"\n"
                zeile = zeile.replace(".", ",")  # deutsches Komma in Austauschdatei
                ausgabedatei.write(zeile)
        # time.sleep(0.25)
