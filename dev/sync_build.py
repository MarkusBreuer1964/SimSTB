""" sync_build.py - Das Skript erzeugt a) eine version.py mit den Build-Daten und stellt b) die zum Aufbau der Laufzeitumgebung notwendigen 
Daten unter src/sim_basis/resources zusammen.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  15.03.2026, 18.03.2026
    """
# build_timestamp.py
from datetime import datetime
import toml
import shutil
import os


def hauptprogramm():
    """Hauptprogramm des Skripts, das die version.py erstellt und die Ressourcen zusammenstellt"""
    print("Starte Vorbereitung der Build-Phase ...")
    versions_datei_erstellen()
    resources_zusammenstellen()
    print("Build-Phase vorbereitet")


def versions_datei_erstellen():
    """Erstellt die version.py mit den Build-Daten; Verion aus pyproject.toml, Datum aus aktuellem Zeitpunkt"""
    with open("src/sim_basis/version.py", "w") as f:
        toml_data = toml.load("pyproject.toml")
        version = toml_data["project"]["version"]
        zeit = datetime.now().strftime("%d.%m.%Y")
        f.write(f"# Build Data, automatisch generiert, nicht manuell ändern!\n")
        f.write(f"SIMSTB_VERSION='{version}'\n")
        f.write(f"SIMSTB_VERSION_DATE='{zeit}'\n")
    print(f"1. version.py mit Version {version} und Datum {zeit} erstellt.")


def resources_zusammenstellen():
    """Stellt die zum Aufbau der Laufzeitumgebung notwendigen Daten unter src/sim_basis/resources zusammen"""

    zielverzeichnis = "src/sim_basis/resources"

    # Neues leeres Zielverzeichnis für die Ressourcen erstellen
    if os.path.exists(zielverzeichnis):
        shutil.rmtree(zielverzeichnis)
    os.makedirs(zielverzeichnis)

    # Verzeichnis mit Austauschdateien kopieren
    os.makedirs(os.path.join(zielverzeichnis, "daten"), exist_ok=True)
    quellverzeichnis = "templates/daten"
    datenverzeichnis = os.path.join(zielverzeichnis, "daten")
    shutil.copytree(quellverzeichnis, datenverzeichnis, dirs_exist_ok=True)
 
    # Verzeichnis mit Dokumentation zusammenkopieren
    os.makedirs(os.path.join(zielverzeichnis, "docs"), exist_ok=True)
    quelldatei = "docs/SimSTB-Benutzerdokumentation.pdf"
    zieldatei = os.path.join(zielverzeichnis, "docs", "SimSTB-Benutzerdokumentation.pdf")
    shutil.copy(quelldatei, zieldatei)
    quelldatei = "docs/beispiel.py"
    zieldatei = os.path.join(zielverzeichnis, "docs", "beispiel.py")
    shutil.copy(quelldatei, zieldatei)

    # Einzeldateien direkt in ressources kopieren
    quelldatei_liste = ["CONTRIBUTING.md", "LICENSE.txt", "README.md","templates/config.toml", "templates/modelle.json"]
    for quelldatei in quelldatei_liste:
        zieldatei = os.path.join(zielverzeichnis, os.path.basename(quelldatei))
        shutil.copy(quelldatei, zieldatei)
    print(f"2. Ressourcen unter {zielverzeichnis} zusammengestellt.")

if __name__ == "__main__":
    hauptprogramm()
