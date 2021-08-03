""" SimSTB - Setzer für Werte

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Setzer stellt verschiedene Funktioen bereit, die als Reaktion auf Knöpfe
    die Werte in den Austauschdateien setzen.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           28.07.2021
    Letzte Änderung:    29.07.2021
    """

from simstb_konfig import Konfig
from simstb_dateizugriff import DateiZugriff

class Setzer:
    def __init__(self):
        """ Konstruktor des Setzers """
        pass

    def setzen0_eingaenge(self):
        """ Alle Eingänge auf 0 setzen """
        daten = [0] * Konfig.DIGMAXLAENGE
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
        de_zugriff.schreiben_alle(daten)
        daten = [0] * Konfig.ANAMAXLAENGE
        ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
        ae_zugriff.schreiben_alle(daten)

    def setzen0_ausgaenge(self):
        """ Alle Ausgänge auf 0 setzen """
        daten = [0] * Konfig.DIGMAXLAENGE
        da_zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE)
        da_zugriff.schreiben_alle(daten)
        daten = [0] * Konfig.ANAMAXLAENGE
        aa_zugriff = DateiZugriff(Konfig.ANAAUS, Konfig.ANAMAXLAENGE)
        aa_zugriff.schreiben_alle(daten)

    def setzen0_alles(self):
        """ Alle Eingänge und Ausgänge auf 0 setzen """
        self.setzen0_eingaenge()
        self.setzen0_ausgaenge()

    def setzen0_digitale_eingaenge(self):
        """ Digitale Eingänge auf 0 setzen """
        daten = [0] * Konfig.DIGMAXLAENGE
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
        de_zugriff.schreiben_alle(daten)

    def setzen1_digitale_eingaenge(self):
        """ Digitale Eingänge auf 1 setzen """
        daten = [1] * Konfig.DIGMAXLAENGE
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
        de_zugriff.schreiben_alle(daten)
