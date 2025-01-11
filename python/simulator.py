""" SimSTB - Simulatorschnittstelle
        Das Modul Simulatorschnittstelle stellt vier Funktionen
        zur Simulation digitaler und analoger Ein- und Ausgaben bereit
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  20.06.2023, 27.06.2023
    """

from simstb_konfig import Konfig
from simstb_dateizugriff import DateiZugriff

def dig_ein( id):
    zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
    daten = zugriff.lesen_alle()
    wert = bool(int(daten[ id]))
    return wert

def dig_aus( id, wert):
    zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE)
    daten = zugriff.lesen_alle()
    daten[ id] = str(int(wert))
    zugriff.schreiben_alle(daten)


def ana_ein( id):
    zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
    daten = zugriff.lesen_alle()
    wert = float(daten[ id])
    return wert

def ana_aus( id, wert):
    zugriff = DateiZugriff(Konfig.ANAAUS, Konfig.ANAMAXLAENGE)
    daten = zugriff.lesen_alle()
    daten[ id] = str(float(wert))
    zugriff.schreiben_alle(daten)

def test():
    print("DIG[0]: ", dig_ein(0))
    print("DIG[15]: ", dig_ein(15))
    print("ANA[0]: ", ana_ein(0))
    dig_aus(15, True)
    ana_aus(7, 123.456)

if __name__ == "__main__":
    test()
