""" simstb_cli.py - CLI-Werkzeug für Projekt SimSTB
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  17.03.2026, 18.03.2026
    """


import argparse
import sim_basis.version as ver
import sim_werkzeuge.simstb_gui as gui
import sim_werkzeuge.simstb_init as init

# from .config import show_config
# from .runtime import init_runtime, start_gui

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
        print("Konfiguration anzeigen... (Funktion noch nicht implementiert)")
        # show_config()
    elif args.init:
        init.init_runtime()
    elif args.gui:
        print("GUI starten ...")
        gui.main()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
