""" SimSTB - Setzer für Werte

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Setzer stellt verschiedene Funktioen bereit, die als Reaktion auf Knöpfe
    die Werte in den Austauschdateien setzen.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           28.07.2021
    Letzte Änderung:    05.03.2026
    """

import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg

class Setzer:
    def __init__(self):
        """ Konstruktor des Setzers """
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()

    def setzen0_eingaenge(self):
        """ Alle Eingänge auf 0 setzen """
        daten = [0] * self.konfig["DIGMAXLAENGE"]
        de_zugriff = dzg.DateiZugriff(self.konfig["DIGEIN"], self.konfig["DIGMAXLAENGE"])
        de_zugriff.schreiben_alle(daten)
        daten = [0] * self.konfig["ANAMAXLAENGE"]
        ae_zugriff = dzg.DateiZugriff(self.konfig["ANAEIN"], self.konfig["ANAMAXLAENGE"])
        ae_zugriff.schreiben_alle(daten)

    def setzen0_ausgaenge(self):
        """ Alle Ausgänge auf 0 setzen """
        daten = [0] * self.konfig["DIGMAXLAENGE"]
        da_zugriff = dzg.DateiZugriff(self.konfig["DIGAUS"], self.konfig["DIGMAXLAENGE"])
        da_zugriff.schreiben_alle(daten)
        daten = [0] * self.konfig["ANAMAXLAENGE"]
        aa_zugriff = dzg.DateiZugriff(self.konfig["ANAAUS"], self.konfig["ANAMAXLAENGE"])
        aa_zugriff.schreiben_alle(daten)

    def setzen0_alles(self):
        """ Alle Eingänge und Ausgänge auf 0 setzen """
        self.setzen0_eingaenge()
        self.setzen0_ausgaenge()

    def setzen0_digitale_eingaenge(self):
        """ Digitale Eingänge auf 0 setzen """
        daten = [0] * self.konfig["DIGMAXLAENGE"]
        de_zugriff = dzg.DateiZugriff(self.konfig["DIGEIN"], self.konfig["DIGMAXLAENGE"])
        de_zugriff.schreiben_alle(daten)

    def setzen1_digitale_eingaenge(self):
        """ Digitale Eingänge auf 1 setzen """
        daten = [1] * self.konfig["DIGMAXLAENGE"]
        de_zugriff = dzg.DateiZugriff(self.konfig["DIGEIN"], self.konfig["DIGMAXLAENGE"])
        de_zugriff.schreiben_alle(daten)
