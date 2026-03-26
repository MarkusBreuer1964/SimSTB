""" simstb_init.py - Initialisierungder Laufzeitumgebung
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  17.03.2026, 25.3.2026
    """

from pathlib import Path
from importlib.resources import files
import shutil
import sys

def init_runtime():
    """Baut die Laufzeitumgebung aus mehreren Verzeichnissen/Dateien auf."""
    print("Laufzeitumgebung wird initialisiert...")

    # 1. Aktuelles Arbeitsverzeichnis ermitteln und anzeigen
    current_dir = Path.cwd()
    print(f"Aktuelles Arbeitsverzeichnis: {current_dir}")

    # 2. Benutzer fragen, ob hier die Laufzeitumgebung eingerichtet werden soll
    confirmation = input(
        f"Soll die Laufzeitumgebung für simstb in '{current_dir}' eingerichtet werden? (j/n): "
    ).strip().lower()
    if confirmation != "j":
        print("Abbruch. Keine Änderungen vorgenommen.")
        return

    # 3. Verzeichnisse erstellen
    sim_dir = current_dir / "sim"
    data_dir = sim_dir / "data"
    doc_dir = sim_dir / "doc"
    bilder_dir = doc_dir /"bilder"
    try:
        # Hauptverzeichnis 'sim' erstellen
        sim_dir.mkdir(exist_ok=False)
        print(f"Verzeichnis '{sim_dir}' erstellt.")
        # Unterverzeichnisse 'data' und 'doc' erstellen
        data_dir.mkdir(exist_ok=False)
        doc_dir.mkdir(exist_ok=False)
        bilder_dir.mkdir(exist_ok=False)
        print(f"Unterverzeichnisse '{data_dir}', '{doc_dir}' und '{bilder_dir}' erstellt.")
    except FileExistsError:
        print(f"Fehler: Das Verzeichnis '{sim_dir}' existiert bereits.")
        sys.exit(11)
    except Exception as e:
        print(f"Fehler beim Erstellen der Verzeichnisse: {e}")
        sys.exit(12)
    
    # 4. Dateien in doc-Unterverzeichnis und data-Unterverzeichnis kopieren
    ziel = doc_dir
    ressourcen_pfad = files("sim_basis.resources.doc") 
    for quelle in ressourcen_pfad.iterdir():
        if quelle.is_file():
            shutil.copy2(quelle, ziel)
    print(f"Verzeichnis {ziel} mit Dateien gefüllt.")
    ziel = bilder_dir
    ressourcen_pfad = files("sim_basis.resources.doc.bilder") 
    for quelle in ressourcen_pfad.iterdir():
        if quelle.is_file():
            shutil.copy2(quelle, ziel)
    print(f"Verzeichnis {ziel} mit Dateien gefüllt.")
    ziel = data_dir
    ressourcen_pfad = files("sim_basis.resources.data") 
    for quelle in ressourcen_pfad.iterdir():
        if quelle.is_file():
            shutil.copy2(quelle, ziel)
    print(f"Verzeichnis {ziel} mit Dateien gefüllt.")

    # 5. Dateien in Hauptverzeichnis kopieren
    ziel = sim_dir
    ressourcen_pfad = files("sim_basis.resources") 
    for quelle in ressourcen_pfad.iterdir():
        if quelle.is_file():
            shutil.copy2(quelle, ziel)
    print(f"Verzeichnis {ziel} mit Dateien gefüllt.")

    print(f"Laufzeitumgebung '{sim_dir}' erfolgreich initialisiert.\n")

    # 6. Hinweis auf Umgebungsvariable ausgeben
    print(f"Bitte setzen Sie die Umgebungsvariable SIMSTB_WURZEL auf den Pfad {sim_dir} der Laufzeitumgebung.\n")
    