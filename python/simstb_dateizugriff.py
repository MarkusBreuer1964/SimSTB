""" SimSTB - Dateizugriff auf Austauschdateien
        Das Modul Dateizugriff stellt zwei Funktionen zum Lesen und Schreiben der Austauschdateien
        zur Verfügung. Die Datenübergabe erfolgt jeweils als Liste.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  28.07.2021, 10.01.2024
    """


import simstb_logger as log


class DateiZugriff:
    """ Klasse zum Zugriff auf die Austauschdateien """

    def __init__(self, dateiname, max_laenge):
        """ Konstruktor des Datenzugriffs auf die Austauschdateien """
        self.dateiname = dateiname
        self.max_laenge = max_laenge

    def lesen_alle(self):
        """ Zeilenweises einlesen der Daten und Rückgabe als Liste """
        try:
            daten = []
            with open(self.dateiname, "r", encoding="utf8") as eingabedatei:
                for zeile in eingabedatei:
                    zeile = zeile.replace(",", ".")  # deutsches Komma in Austauschdatei
                    zeile = zeile.rstrip("\n")
                    daten = daten + [zeile]
            # Prüfen, ob die Anzahl der Daten stimmt
            if len(daten) != self.max_laenge:
                log.msg_loggen(f"Datei {self.dateiname} Lesezugriff: Falsche Anzahl an Daten: {len(daten)} vorhanden, {self.max_laenge} erwartet, alles auf 0 gesetzt")
                daten = ["0.0"] * self.max_laenge
                self.schreiben_alle(daten)
        except:
            # Fehler beim Lesen der Datei
            daten = ["0.0"] * self.max_laenge
            log.msg_loggen(f"Datei {self.dateiname} Lesezugriff: Fehler bei Dateizugriff: alles auf 0 gesetzt")
            self.schreiben_alle(daten)

        return daten

    def schreiben_alle(self, daten):
        """ Komplettes zurückschreiben aller Daten einer Austauschdatei """
        try:
            with open(self.dateiname, "w", encoding="utf8") as ausgabedatei:
                for wert in daten:
                    zeile = str(wert)+"\n"
                    zeile = zeile.replace(".", ",")  # deutsches Komma in Austauschdatei
                    ausgabedatei.write(zeile)
        except:
            log.msg_loggen(f"Datei {self.dateiname} Schreibzugriff: Fehler bei Dateizugriff")
