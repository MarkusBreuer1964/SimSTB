""" SimSTB - Simulatorschnittstelle
        Das Modul Simulatorschnittstelle stellt vier Funktionen
        zur Simulation digitaler und analoger Ein- und Ausgaben bereit
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  20.06.2023, 20.03.2026
    """

import os
import sys
import logging
import sim_basis.simstb_logger as log
import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg

laufzeitumgebung = False
def in_laufzeitumgebung_wechseln():
    """In Laufzeitumgebung wehseln, damit die Dateien im richtigen Verzeichnis liegen"""
    global laufzeitumgebung
    if laufzeitumgebung is False:
        try:
            pfad = os.environ["SIMSTB_WURZEL"]
            os.chdir(pfad)
            laufzeitumgebung = True
        except KeyError:
            print("Fehler: Umgebungsvariable SIMSTB_WURZEL nichtgesetzt -> Programm wird beendet")
            sys.exit(1)

# Logger-Objekt auf Modulebene, damit es in allen Funktionen genutzt werden kann
logger = None
def logging_lokal_einrichten():
    """Richtet die Logging-Konfiguration ein und gibt einen Logger zurück"""
    global logger
    if logger is None:
        log.logging_einrichten()
        logger = logging.getLogger(__name__)

def dig_ein( id):
    """Schnittstellenfunktion und digitalen Eingang zu lesen """
    in_laufzeitumgebung_wechseln()
    # Logging initialisieren und Log-Message rausschreiben
    logging_lokal_einrichten()
    logger.debug("dig_ein - Aufruf mit id: %d", id)
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    zugriff = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"])
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != konfig["DIGMAXLAENGE"]:
        logger.error(
            f"Simulatorschnittstelle dig_ein - Indexproblem: Zugriffsindex: {id}, Feldlänge: {len(daten)}, Dateilänge: {konfig['DIGMAXLAENGE']} -> None zurückgeliefert"
        )
        wert = None
    else:
        wert = bool(int(daten[ id]))
    return wert

def dig_aus( id, wert):
    """Schnittstellenfunktion und digitalen Ausgang zu setzen """
    in_laufzeitumgebung_wechseln()
    logging_lokal_einrichten()
    logger.debug("dig_aus - Aufruf mit id: %d, wert: %d", id, wert)
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    zugriff = dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"])
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war
    if id >= len(daten) or len(daten) != konfig["DIGMAXLAENGE"]:
        logger.error(
            f"Simulatorschnittstelle dig_aus - Indexproblem: Zugriffsindex: {id}, Feldlänge: {len(daten)}, Dateilänge: {konfig['DIGMAXLAENGE']}"
        )
        return
    daten[ id] = str(int(wert))
    zugriff.schreiben_alle(daten)

def ana_ein( id):
    """Schnittstellenfunktion und analogen Eingang zu lesen """
    in_laufzeitumgebung_wechseln()  
    logging_lokal_einrichten()
    logger.debug("ana_ein - Aufruf mit id: %d", id)
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    zugriff = dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"])
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != konfig["ANAMAXLAENGE"]:
        logger.error(
            f"Simulatorschnittstelle ana_ein - Indexproblem: Zugriffsindex: {id}, Feldlänge: {len(daten)}, Dateilänge: {konfig['ANAMAXLAENGE']} -> None zurückgeliefert"
        )
        wert = None
    else:
        wert = float(daten[ id])
    return wert

def ana_aus( id, wert):
    """Schnittstellenfunktion und analogen Ausgang zu setzen """
    in_laufzeitumgebung_wechseln()
    logging_lokal_einrichten()
    logger.debug("ana_aus - Aufruf mit id: %d, wert: %f", id, wert)
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    zugriff = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"])
    daten = zugriff.lesen_alle()
    # Prüfen, ob Index korrekt war und Antwort setzen
    if id >= len(daten) or len(daten) != konfig["ANAMAXLAENGE"]:
        logger.error(
            f"Simulatorschnittstelle ana_aus - Indexproblem: Zugriffsindex: {id}, Feldlänge: {len(daten)}, Dateilänge: {konfig['ANAMAXLAENGE']}"
        )
        return
    daten[ id] = str(float(wert))
    zugriff.schreiben_alle(daten)
