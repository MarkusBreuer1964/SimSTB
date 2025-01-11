""" SimSTB - Simulatorschnittstelle - Beispieldatei für die Nutzung der Schnittstelle
        Das Modul Simulatorschnittstelle stellt vier Funktionen
        zur Simulation digitaler und analoger Ein- und Ausgaben bereit
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  21.06.2023
    """

import time
import simulator as sim


def test():
    """ Testfunktion """
    ende = False
    print("Beispielprogramm für Simulationsumgebung")
    print("----------------------------------------")
    print("Die am analogen Eingang Kanal 0 liegenden Eingangssignale")
    print("werden im Sekundentakt eingelesen. Beendet wird das Einlesen,")
    print("sobald am digitalen Eingang Kanal 0 eine 1 anliegt.")
    print("Am Ende werden noch ein digitales und analoges Ausgabesignal gesetzt.")

    while ende is not True:
        wert = sim.ana_ein(0)											# Einlesen eines analogen Eingabesignals über Kanal 0
        print(wert)
        time.sleep(1)
        ende = sim.dig_ein(0)											# Einlesen eines digitalen Eingabesignals über Kanal 0

    sim.dig_aus(15, 1)													# Ausgabe eines digitalen Ausgabesignals über Kanal 15
    sim.ana_aus(7, -123.456)											# Ausgabe eines analogen Ausgabesignals über Kanal 7

    print("Beispielprogramm beendet")


test()
