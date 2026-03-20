"""simstb_konfig.py - SimSTB - Konfigurationsdaten
Das Modul Konfiguration stellt zentrale Konfigurationsdaten, wie z.B.
Längen, Dateinamen inkl. Pfad oder Signalformen zur Verfügung.
Name, Organisaion:          Markus Breuer, STMB
Erstellt, Letzte Änderung:  28.07.2021, 20.03.2026
"""

from pathlib import Path
import os
import sys
import toml
import threading

# Default name for the configuration file
KONFIG_DATEINAME = "config.toml"


class Konfig:
    """Klasse mit zentralen Konfigurationsdaten"""

    _konfig = None  # Klassenvariable für die Konfiguration
    _lock = threading.Lock()  # Sperre für thread-sichere Zugriffe

    def __init__(self, konfig_dateiname=KONFIG_DATEINAME):
        """Konstruktor der Klasse"""
        with Konfig._lock:
            if Konfig._konfig is None:  # Nur laden, wenn noch nicht geladen
                self.konfig_dateiname = konfig_dateiname
                if "SIMSTB_CONFIG_FILE" in os.environ:
                    # Overwrite default value with environment value
                    self.konfig_dateiname = Path(os.environ["SIMSTB_CONFIG_FILE"])
                # Absoluten Pfad zur Konfigurationsdatei ermitteln
                try:
                    basisverzeichnis = Path(os.getenv("SIMSTB_WURZEL"))
                except Exception as e:
                    print("Umgebungsvariable SIMSTB_WURZEL nichtgesetzt -> Bitte Umgebungsvariable SIMSTB_WURZEL setzen -> Programmabbruch")
                    sys.exit(1)
                self.konfig_dateiname = basisverzeichnis / self.konfig_dateiname
                # Konfigurationsdaten aus der TOML-Datei laden
                try:
                    Konfig._konfig = toml.load(self.konfig_dateiname)
                except Exception as e:
                    msg = f"Fehler beim Laden der Konfigurationsdatei:{self.konfig_dateiname}"
                    raise FileNotFoundError(msg) from e
                # Relative Pfade durch absolute Pfade ersetzen
                schluesselliste = ["LOGDATEI", "MODELL_DATEI", "ANAAUS", "ANAEIN", "DIGAUS", "DIGEIN"]
                basisverzeichnis = Path(os.getenv("SIMSTB_WURZEL"))
                for schluessel in schluesselliste:
                    if schluessel in Konfig._konfig:
                        Konfig._konfig[schluessel] = str(basisverzeichnis / Konfig._konfig[schluessel])
                # Konfiguration ergänzen
                Konfig._konfig["BASISVERZEICHNIS"] = str(basisverzeichnis)
                Konfig._konfig["KONFIG_DATEINAME"] = str(self.konfig_dateiname)

    def konfiguration_bereitstellen(self):
        """Stellt die Konfigurationsdaten bereit"""
        return Konfig._konfig
