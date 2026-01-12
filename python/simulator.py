""" SimSTB - Simulatorschnittstelle
        Das Modul Simulatorschnittstelle stellt vier Funktionen
        zur Simulation digitaler und analoger Ein- und Ausgaben bereit
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  20.06.2023, 06.02.2023
    """

import simstb_logger as log
import simstb_konfig as kfg
import simstb_dateizugriff as dzg

def dig_ein( id):
    """Schnittstellenfunktion und digitalen Eingang zu lesen """
    zugriff = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE)
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != kfg.Konfig.DIGMAXLAENGE:
        log.msg_loggen(
            f"Simulatorschnittstelle dig_ein - Indexproblem: Zugriffsindex: {id}, Feldlänge: {len(daten)}, Dateilänge: {kfg.Konfig.DIGMAXLAENGE} -> None zurückgeliefert"
        )
        wert = None
    else:
        wert = bool(int(daten[ id]))
    return wert

def dig_aus( id, wert):
    """Schnittstellenfunktion und digitalen Ausgang zu setzen """
    zugriff = dzg.DateiZugriff(kfg.Konfig.DIGAUS, kfg.Konfig.DIGMAXLAENGE)
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war
    if id >= len(daten) or len(daten) != kfg.Konfig.DIGMAXLAENGE:
        log.msg_loggen(
            f"Simulatorschnittstelle dig_aus - Indexproblem: Zugriffsindex: {id} Feldlänge: {len(daten)} Dateilänge: {kfg.Konfig.DIGMAXLAENGE}"
        )
        return
    daten[ id] = str(int(wert))
    zugriff.schreiben_alle(daten)

def ana_ein( id):
    """Schnittstellenfunktion und analogen Eingang zu lesen """
    zugriff = dzg.DateiZugriff(kfg.Konfig.ANAEIN, kfg.Konfig.ANAMAXLAENGE)
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != kfg.Konfig.ANAMAXLAENGE:
        log.msg_loggen(
            f"Simulatorschnittstelle ana_ein - Indexproblem: Zugriffsindex: {id} Feldlänge: {len(daten)} Dateilänge: {kfg.Konfig.ANAMAXLAENGE} -> None zurückgeliefert"
        )
        wert = None
    else:
        wert = float(daten[ id])
    return wert

def ana_aus( id, wert):
    """Schnittstellenfunktion und analogen Ausgang zu setzen """
    zugriff = dzg.DateiZugriff(kfg.Konfig.ANAAUS, kfg.Konfig.ANAMAXLAENGE)
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != kfg.Konfig.ANAMAXLAENGE:
        log.msg_loggen(
            f"Simulatorschnittstelle ana_aus - Indexproblem: Zugriffsindex: {id} Feldlänge: {len(daten)} Dateilänge: {kfg.Konfig.ANAMAXLAENGE}"
        )
    daten[ id] = str(float(wert))
    zugriff.schreiben_alle(daten)
