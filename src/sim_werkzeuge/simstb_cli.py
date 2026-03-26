""" simstb_cli.py - CLI-Werkzeug für Projekt SimSTB
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  17.03.2026, 22.03.2026
    """


from pathlib import Path
import os
import sys
import argparse
import sim_basis.version as ver
import sim_basis.simstb_konfig as kfg
import sim_werkzeuge.simstb_gui as gui
import sim_werkzeuge.simstb_init as init

def main():
    parser = argparse.ArgumentParser(description="CLI-Werkeug für Projekt SimSTB")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Zeigt die aktuelle Version an."
    )
    parser.add_argument(
        "--hilfe",
        action="store_true",
        help="Zeigt diese Hilfe an."
    )
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Zeigt die aktuelle Konfiguration an."
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialisiert die Laufzeitumgebung."
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Startet das GUI-Programm."
    )

    args = parser.parse_args()

    if args.version:
        print(f"Version: {ver.SIMSTB_VERSION} (Stand: {ver.SIMSTB_VERSION_DATE})")
    elif args.hilfe:
        parser.print_help()
    elif args.show_config:
        show_config()
    elif args.init:
        init.init_runtime()
    elif args.gui:
        print("GUI starten ...")
        gui.main()
    else:
        parser.print_help()

def show_config():
        try:
            basisverzeichnis = Path(os.getenv("SIMSTB_WURZEL"))
            print(f"\nUmgebungsvariable SIMSTB_WURZEL gesetzt: {basisverzeichnis}\n")
        except Exception as e:
            print("Umgebungsvariable SIMSTB_WURZEL nicht gesetzt -> Bitte Umgebungsvariable SIMSTB_WURZEL setzen -> Programmabbruch")
            sys.exit(1)
        try:
            konfigkonfigmanager = kfg.Konfig() 
            konfig = konfigkonfigmanager.konfiguration_bereitstellen()
            print("Aktuelle Konfiguration SimSTB (Pfade aufgelöst):\n")
            for key, value in konfig.items():
                print(f"{str(key):<20s} : {value}")
        except Exception as e:
            print(f"Fehler beim Laden der Konfigurationsdatei: {e}")
            print("Bitte Konfigurationsdatei überprüfen")
            print("Aufbau der Laufzeitumgebung mit simstb_cli --init vergessen?")
        print("\n")
        
if __name__ == "__main__":
    main()
