""" SimSTB - Konfigurationsdaten

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Konfiguration stellt zentrale Konfigurationsdaten, wie z.B.
    Längen, Dateinamen inkl. Pfad oder Signalformen zur Verfügung.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           28.07.2021
    Letzte Änderung:    10.08.2021
    """

class Konfig:
    DIGMAXLAENGE  = 16							# Anzahl der digitalen Kanäle
    ANAMAXLAENGE = 8							# Anzahl der analogen Kanäle
    ANAAUS = "C:\\Sim\\anaaus.txt"			    # Namen und Position der Austauschdateien
    ANAEIN = "C:\\Sim\\anaein.txt"
    DIGAUS = "C:\\Sim\\digaus.txt"
    DIGEIN = "C:\\Sim\\digein.txt"
    SIGNALFORMEN = ["Zufall", "Sinus", "Rechteck", "Dreieck"] # Signalformen für analogen Zufallgenerator
    AKTIVE_BACKGROUND =  "#90EE90"              # Hintergrundfarben
    HAUPT_BACKGROUND =  "#b7d7e8"
    BLOCK_BACKGROUND =  "#cfe0e8"
    MODELL_DATEI = "modelle.json"
