""" SimSTB - Modell 1 - LED-Anzeige

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Realisierung von Modell 1 - LED-Anzeige.

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           09.08.2021
    Letzte Änderung:    
    """

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import sys
from tkinter import font
from tkinter.font import Font
from simstb_konfig import Konfig
from simstb_dateizugriff import DateiZugriff

ANZAHL_LED = 8

class Modell_1:
    """ Klasse Modell_1 - LED-Anzeige """

    def __init__(self, hauptfenster):
        """ Konstruktor, in dem das GUI für Modell 1 aufgebaut wird """
        self.fenster = hauptfenster
        self.fenster.iconbitmap("simstb.ico")
        self.fenster.protocol("WM_DELETE_WINDOW", lambda: self.beenden())
        
        # Styles festlegen
        self.festlegen_Styles()

        self.led_aus = PhotoImage(file="led_grau.png")
        self.led_an = PhotoImage(file="led_blau.png")

        # Hauptrahmen anlegen
        hauptrahmen = ttk.Frame(master=self.fenster, padding="5", style="Haupt.TFrame")
        hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)

        # Titelbereich einfügen
        ttk.Label(master=hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(master=hauptrahmen, text="Modell 1 - LED-Anzeige", style="HauptLabel2.TLabel").grid(column=2, row=1, sticky="NW")

        # Unterrahmen 1 und Knöpfe

        unterrahmen1 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen1.grid(column=1, row=2, columnspan=2, sticky="NWES")
        self.LED = []
        for i in range(ANZAHL_LED): 
            eintrag = ttk.Label(unterrahmen1, image=self.led_aus, style="BlockLabel.TLabel")
            eintrag.grid(column=i+1, row=1, sticky="NW")
            ttk.Label(master=unterrahmen1, text="DA"+str(i), style="BlockLabel.TLabel").grid(column=i+1, row=2, sticky="NW")
            self.LED.append(eintrag)

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

        sblock.configure( "Haupt.TFrame", background = Konfig.HAUPT_BACKGROUND)
        sblock.configure( "HauptLabel2.TLabel", background =Konfig.HAUPT_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure( "HauptLabel1.TLabel", background =Konfig.HAUPT_BACKGROUND, font=("Tahoma", 24, "bold"))

        sblock.configure( "Block.TFrame", background = Konfig.BLOCK_BACKGROUND, relief=RAISED)
        sblock.configure( "BlockLabel2.TLabel", background =Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockLabel.TLabel", background =Konfig.BLOCK_BACKGROUND)
        sblock.configure( "BlockStatusLabelGen.TLabel", background =Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockStatusLabelDat.TLabel", background =Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure( "BlockCheckbutton.TCheckbutton", background = Konfig.BLOCK_BACKGROUND)
        sblock.configure( "Unterblock.TFrame", background = Konfig.BLOCK_BACKGROUND)

    def setzen_abstaende(self, hauptrahmen, unterrahmen1):
        """ Feinschliff Layout - Abstände zwischen Fensterelementen setzen"""
        for element in hauptrahmen.winfo_children():
            element.grid_configure(padx="20", pady="20")
        for element in unterrahmen1.winfo_children():
            element.grid_configure(padx="10", pady="10")
 
    # Callback-Funktion und Hilfsfunktionen für Daten laden und aktualisieren - Timer und Konstruktor

    def aktualisieren(self):
        self.aktualisieren_ausgangswerte()
        self.fenster.after(1000, self.aktualisieren)

    def aktualisieren_ausgangswerte(self):
        da_zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE)
        da_daten= da_zugriff.lesen_alle()
        for i in range(ANZAHL_LED):
            if int(da_daten[i]) == 0:
                self.LED[i].configure(image=self.led_aus)
            else:
                self.LED[i].configure(image=self.led_an)


    # Callback-Funktion fürs Beenden

    def beenden(self):
        """ Modell 1 beenden """
        sys.exit ("Modell 1 beendet")


def hauptprogramm():
    fenster = Tk(className="SimSTB - Modell 1 - LED-Anzeige")  # Rohes Fenster erstellen
    TS = Modell_1(fenster)  # Oberfläche Simulator aufbauen
    fenster.mainloop()  # Hauptschleife starten

hauptprogramm()
