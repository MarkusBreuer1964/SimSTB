""" SimSTB - Dateizugriff auf Austauschdateien
    Das Modul Dateizugriff stellt zwei Funktionen zum Lesen und Schreiben der Austauschdateien
    zur Verfügung. Die Datenübergabe erfolgt jeweils als Liste.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  28.07.2021, 15.03.2026
    """

import filelock
import logging
# import sim_basis.simstb_logger as log
import sim_basis.simstb_konfig as kfg

class DateiZugriff:
    """Klasse zum Zugriff auf die Austauschdateien"""

    def __init__(self, dateiname, max_laenge):
        """Konstruktor des Datenzugriffs auf die Austauschdateien"""
        self.logger = logging.getLogger(__name__)
        self.dateiname = dateiname
        self.max_laenge = max_laenge
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        if dateiname in [self.konfig["DIGEIN"], self.konfig["DIGAUS"]]:
            self.reset_daten = ["0"] * self.max_laenge
        else:
            self.reset_daten = ["0.0"] * self.max_laenge

    def lesen_alle(self):
        """Zeilenweises einlesen der Daten und Rückgabe als Liste"""
        try:
            daten = []
            # Erstelle ein FileLock-Objekt
            lock_path = self.dateiname + ".lock"
            lock = filelock.FileLock(lock_path)
            # Versuche, die Datei zu sperren und darauf zuzugreifen
            with lock:
                with open(self.dateiname, "r", encoding="utf8") as eingabedatei:
                    for zeile in eingabedatei:
                        zeile = zeile.replace(",", ".")  # deutsches Komma in Austauschdatei
                        zeile = zeile.rstrip("\n")
                        daten = daten + [zeile]
                # Prüfen, ob die Anzahl der Daten stimmt
                if len(daten) != self.max_laenge:
                    self.logger.error(
                        f"Dateizugriff lesen_alle 1 - Falsche Anzahl an Daten: Datei {self.dateiname}, gelesen: {len(daten)}, erwartet: {self.max_laenge} -> alles auf 0 gesetzt"
                    )
                    self.schreiben_alle(self.reset_daten)
                    daten = self.reset_daten
        except:
            # Fehler beim Lesen der Datei
            self.logger.error(f"Dateizugriff lesen_alle 2 - Allgemeine Exception: Datei {self.dateiname} -> alles auf 0 gesetzt")
            self.schreiben_alle(self.reset_daten)
            daten = self.reset_daten

        return daten

    def schreiben_alle(self, daten):
        """Komplettes zurückschreiben aller Daten einer Austauschdatei"""
        try:
            with open(self.dateiname, "w", encoding="utf8") as ausgabedatei:
                for wert in daten:
                    zeile = str(wert) + "\n"
                    zeile = zeile.replace(".", ",")  # deutsches Komma in Austauschdatei
                    ausgabedatei.write(zeile)
        except:
            self.logger.error(f"Dateizugriff schreiben_alle - Allgemeine Exception: Datei {self.dateiname} -> alles auf 0 gesetzt")
