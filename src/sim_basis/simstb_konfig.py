""" simstb_konfig.py - SimSTB - Konfigurationsdaten
    Das Modul Konfiguration stellt zentrale Konfigurationsdaten, wie z.B.
    Längen, Dateinamen inkl. Pfad oder Signalformen zur Verfügung.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  28.07.2021, 05.03.2026
    """

from pathlib import Path
import toml
import os


# Default name for the configuration file
KONFIG_DATEINAME = "config.toml"


class Konfig:
    """Klasse mit zentralen Konfigurationsdaten"""
    
    def __init__(self, konfig_dateiname=KONFIG_DATEINAME):
        """Konstruktor der Klasse"""
        self.konfig_dateiname = konfig_dateiname
        if "SIMSTB_CONFIG_FILE" in os.environ:
            # Overwrite default value with environment value
            self.konfig_dateiname = Path(os.environ["SIMSTB_CONFIG_FILE"])
        # Konfigurationsdaten aus der TOML-Datei laden
        try:
            self.konfig = toml.load(self.konfig_dateiname)
        except Exception as e:
            msg = f"Fehler beim Laden der Konfigurationsdatei:{self.konfig_dateiname}" 
            raise FileNotFoundError(msg) from e

    def konfiguration_bereitstellen(self):
        """Stellt die Konfigurationsdaten bereit"""
        return self.konfig

