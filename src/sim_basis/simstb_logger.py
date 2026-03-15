""" SimSTB - Logger
    Das Modul Logger stellt eine Funktion zur Speicherung von Log-Informationen bereit.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  10.01.2025, 16.03.2026
    """

import sim_basis.simstb_konfig as kfg
import logging

def logging_einrichten():
    """Richtet die Logging-Konfiguration ein"""
    konfigmanager = kfg.Konfig() 
    konfig = konfigmanager.konfiguration_bereitstellen()
    logdateiname = konfig["LOGDATEI"]
    loglevel = konfig.get("LOGLEVEL", "INFO").upper()
    logging.basicConfig(
        filename=logdateiname,
        level=loglevel,
        format="%(asctime)s [PID:%(process)d] [TID:%(thread)d] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%d.%m.%Y %H:%M:%S"
    )
    # Gezielt die Logger von benutzter Drittsoftware ausschalten
    logging.getLogger("filelock").setLevel(logging.CRITICAL)
    logging.getLogger("tkinter").setLevel(logging.CRITICAL)
    # Log-Informationen über Initialisieren des Loggings
    logger = logging.getLogger(__name__)
    logger.info("Logging initialisiert (Logdatei: %s, Loglevel: %s)", logdateiname, loglevel)
