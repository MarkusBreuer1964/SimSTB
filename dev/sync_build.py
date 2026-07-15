#!/usr/bin/env python3

""" sync_build.py - Das Skript erzeugt a) eine version.py mit den Build-Daten und stellt b) die zum Aufbau der Laufzeitumgebung notwendigen 
Daten unter src/sim_basis/resources zusammen.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  15.03.2026, 15.07.2026
    """


from datetime import datetime
import toml
import shutil
import os
from importlib.resources import files


def hauptprogramm():
    """Hauptprogramm des Skripts, das die version.py erstellt und die Ressourcen zusammenstellt"""
    print("Starte Vorbereitung der Build-Phase ...")
    version, _ = versions_datei_erstellen()
    readme_version_aktualisieren(version)
    tox_ini_version_aktualisieren(version)
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
    return version, zeit


def readme_version_aktualisieren(version):
    """Update the version line in README.md."""
    readme_pfad = "README.md"

    with open(readme_pfad, "r", encoding="utf-8") as datei:
        zeilen = datei.readlines()

    aktualisierte_zeilen = []
    versionszeile_gefunden = False

    for zeile in zeilen:
        if zeile.startswith("Aktuelle Version: "):
            aktualisierte_zeilen.append(f"Aktuelle Version: {version}\n")
            versionszeile_gefunden = True
        else:
            aktualisierte_zeilen.append(zeile)

    if versionszeile_gefunden:
        with open(readme_pfad, "w", encoding="utf-8") as datei:
            datei.writelines(aktualisierte_zeilen)
        print(f"2. README.md Version auf {version} aktualisiert.")
    else:
        print("2. Hinweis: Keine Versionszeile in README.md gefunden.")


def tox_ini_version_aktualisieren(version):
    """Update the PACKAGE_VERSION line in tox.ini."""
    tox_pfad = "tox.ini"

    with open(tox_pfad, "r", encoding="utf-8") as datei:
        zeilen = datei.readlines()

    aktualisierte_zeilen = []
    versionszeile_gefunden = False

    for zeile in zeilen:
        if zeile.startswith("    PACKAGE_VERSION = "):
            aktualisierte_zeilen.append(f"    PACKAGE_VERSION = {version}\n")
            versionszeile_gefunden = True
        else:
            aktualisierte_zeilen.append(zeile)

    if versionszeile_gefunden:
        with open(tox_pfad, "w", encoding="utf-8") as datei:
            datei.writelines(aktualisierte_zeilen)
        print(f"3. tox.ini Version auf {version} aktualisiert.")
    else:
        print("3. Hinweis: Keine PACKAGE_VERSION-Zeile in tox.ini gefunden.")


def resources_zusammenstellen():
    """Stellt die zum Aufbau der Laufzeitumgebung notwendigen Daten unter src/sim_basis/resources zusammen"""

    zielverzeichnis = "src/sim_basis/resources"

    # Neues leeres Zielverzeichnis für die Ressourcen erstellen
    if os.path.exists(zielverzeichnis):
        shutil.rmtree(zielverzeichnis)
    os.makedirs(zielverzeichnis)

    # Verzeichnis mit Austauschdateien kopieren
    os.makedirs(os.path.join(zielverzeichnis, "data"), exist_ok=True)
    quellverzeichnis = "templates/daten"
    datenverzeichnis = os.path.join(zielverzeichnis, "data")
    shutil.copytree(quellverzeichnis, datenverzeichnis, dirs_exist_ok=True)
 
    # Verzeichnis mit Dokumentation zusammenkopieren
    os.makedirs(os.path.join(zielverzeichnis, "doc"), exist_ok=True)
    os.makedirs(os.path.join(zielverzeichnis, "doc", "bilder"), exist_ok=True)
    quelldatei = "doc/SimSTB-Benutzerdokumentation.pdf"
    zieldatei = os.path.join(zielverzeichnis, "doc", "SimSTB-Benutzerdokumentation.pdf")
    shutil.copy(quelldatei, zieldatei)
    quelldatei = "doc/beispiel.py"
    zieldatei = os.path.join(zielverzeichnis, "doc", "beispiel.py")
    shutil.copy(quelldatei, zieldatei)
    quelldatei = "doc/bilder"
    zieldatei = os.path.join(zielverzeichnis, "doc", "bilder")
    shutil.copytree(quelldatei, zieldatei, dirs_exist_ok=True)

    # Einzeldateien direkt in ressources kopieren
    quelldatei_liste = ["CONTRIBUTING.md", "LICENSE.txt", "README.md","templates/config.toml", "templates/modelle.json"]
    for quelldatei in quelldatei_liste:
        zieldatei = os.path.join(zielverzeichnis, os.path.basename(quelldatei))
        shutil.copy(quelldatei, zieldatei)
    print(f"4. Ressourcen unter {zielverzeichnis} zusammengestellt.")


if __name__ == "__main__":
    hauptprogramm()
