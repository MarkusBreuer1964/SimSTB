""" SimSTB - Modell 2 - Fließband

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Realisierung von Modell 2 - Fließband.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           10.08.2021
    Letzte Änderung:    28.03.2026
    """

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import logging
import os
import time
import sys
from tkinter import font
from tkinter.font import Font
from importlib.resources import files, as_file
import sim_basis.simstb_logger as log
import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg

ANZAHL_LED = 8

class Modell_2:
    """ Klasse Modell_2 - Fließband """

    def __init__(self, hauptfenster):
        """ Konstruktor, in dem das GUI für Modell 2 aufgebaut wird """
        # Konfigurationsdatei laden
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        # Logging initialisieren und Log-Messages rausschreiben
        log.logging_einrichten()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Modell 2 - Fließband gestartet")
        self.logger.debug("AktuellesArbeitsverzeichnis: " + os.getcwd())
        self.logger.debug("Basisverzeichnis: " + self.konfig["BASISVERZEICHNIS"])
        self.logger.debug("Konfigurationsdatei: " + self.konfig["KONFIG_DATEINAME"])
        self.logger.debug("Logdatei: " + self.konfig["LOGDATEI"])
        self.fenster = hauptfenster
        #self.fenster.iconbitmap("simstb.ico")
        self.fenster.protocol("WM_DELETE_WINDOW", lambda: self.beenden())
        
        # Styles festlegen
        self.festlegen_Styles()

        bilder = files("sim_basis.resources.doc.bilder")
        with as_file(bilder / "band_rechts.gif") as p:
            self.band_rechts = PhotoImage(file=str(p))

        # Hauptrahmen anlegen
        hauptrahmen = ttk.Frame(master=self.fenster, padding="5", style="Haupt.TFrame")
        hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)

        # Titelbereich einfügen
        ttk.Label(master=hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(master=hauptrahmen, text="Modell 2 - Fließband (in Arbeit)", style="HauptLabel2.TLabel").grid(column=2, row=1, sticky="NW")

        # Unterrahmen 1 und Knöpfe

        unterrahmen1 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen1.grid(column=1, row=2, columnspan=2, sticky="NWES")
        self.band = ttk.Label(unterrahmen1, image=self.band_rechts, style="BlockLabel.TLabel")
        self.band.grid(column=1, row=1, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Modell Fließband in Arbeit ...", style="BlockLabel.TLabel").grid(column=1, row=2, sticky="NW")

        # Globale Knöpfe einfügen
        ttk.Button(master=hauptrahmen, text="Beenden", command=lambda: self.beenden()).grid(column=2, row=3, sticky="NE")

        self.setzen_abstaende(hauptrahmen, unterrahmen1)

        self.aktualisieren()

    def festlegen_Styles(self):
        """ Festlegen der genutzten Styles """
        sblock = ttk.Style()

        sblock.configure('TLabel', font=("Tahoma", 11))
        sblock.configure('TButton', font=("Tahoma", 11 ))
        sblock.configure('TCheckbutton', font=("Tahoma", 11))

        sblock.configure( "Haupt.TFrame", background = self.konfig["HAUPT_BACKGROUND"])
        sblock.configure( "HauptLabel2.TLabel", background =self.konfig["HAUPT_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure( "HauptLabel1.TLabel", background =self.konfig["HAUPT_BACKGROUND"], font=("Tahoma", 24, "bold"))

        sblock.configure( "Block.TFrame", background = self.konfig["BLOCK_BACKGROUND"], relief=RAISED)
        sblock.configure( "BlockLabel2.TLabel", background =self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockLabel.TLabel", background =self.konfig["BLOCK_BACKGROUND"])
        sblock.configure( "BlockStatusLabelGen.TLabel", background =self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockStatusLabelDat.TLabel", background =self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockCheckbutton.TCheckbutton", background = self.konfig["BLOCK_BACKGROUND"])
        sblock.configure( "Unterblock.TFrame", background = self.konfig["BLOCK_BACKGROUND"], relief=RAISED)

    def setzen_abstaende(self, hauptrahmen, unterrahmen1):
        """ Feinschliff Layout - Abstände zwischen Fensterelementen setzen"""
        for element in hauptrahmen.winfo_children():
            element.grid_configure(padx="20", pady="20")
        for element in unterrahmen1.winfo_children():
            element.grid_configure(padx="10", pady="10")
 
    # Callback-Funktion und Hilfsfunktionen für Daten laden und aktualisieren - Timer und Konstruktor

    def aktualisieren(self):
        self.aktualisieren_modell()
        self.fenster.after(1000, self.aktualisieren)

    def aktualisieren_modell(self):
        da_zugriff = dzg.DateiZugriff(self.konfig["DIGAUS"], self.konfig["DIGMAXLAENGE"])
        da_daten= da_zugriff.lesen_alle()
        return
 

    # Callback-Funktion fürs Beenden

    def beenden(self):
        """ Modell 2 beenden """
        sys.exit (0)


def hauptprogramm():
    fenster = Tk(className="SimSTB - Modell 2 - Fließband")  # Rohes Fenster erstellen
    TS = Modell_2(fenster)  # Oberfläche Simulator aufbauen
    fenster.mainloop()  # Hauptschleife starten

if __name__ == "__main__":
    hauptprogramm()
