""" SimSTB - Starten von Modellen

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Modelle stellt zwei Klassen zum Starten von Modellen
    zur Verfügung.
    1. In der Klasse ModellGUI wird ein Toplevel-Fenster erzeugt, in dem
    der Benutzer die Generatoroptionen setzen kann und den Generator 
    starten und stoppen.
    2. Die Klasse GeneratorController sorgz dafür, dass das eigentliche Modell
    als eigener Prozess läuft.
 
    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           10.08.2021
    Letzte Änderung:    
    """

from tkinter import *
from tkinter import ttk
from simstb_konfig import Konfig
import json
import subprocess

class ModellGUI:
    """ Klasse Modell GUI """

    def __init__(self, hauptfenster):
        """ Konstruktor, in dem das GUI zum Szarten von Modellen aufgebaut wird """
        self.hauptfenster = hauptfenster
        self.controller = ModellController()
        self.aktiv = True

        self.modelle = self.lese_modell_datei()

        # Top-Level Fenster für Funktionsgenerator anlegen
        self.modellfenster = Toplevel(self.hauptfenster)  
        self.modellfenster.iconbitmap("simstb.ico")
        self.modellfenster.title("SimSTB - Modelle")     
        self.modellfenster.protocol("WM_DELETE_WINDOW", lambda: self.schliessen())
       
        # Hauptrahmen anlegen
        hauptrahmen = ttk.Frame(master=self.modellfenster, padding="5", style="Haupt.TFrame")
        hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.modellfenster.columnconfigure(1, weight=1)
        self.modellfenster.rowconfigure(1, weight=1)

        # Titelbereich einfügen
        ttk.Label(master=hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(master=hauptrahmen, text="Modelle", style="HauptLabel2.TLabel").grid(column=2, row=1, sticky="NW")

        # Unterrahmen 1 und Elemente für Einstellungen
        unterrahmen1 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen1.grid(column=1, row=3, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen1, text="Modelle Auswahl", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=5, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Modell", style="BlockLabel.TLabel").grid(column=1, row=1, columnspan=5, sticky="NW")
        self.modell_name = StringVar() # Signalform
        modell_namen = []
        for modell in self.modelle:
            modell_namen = modell_namen + [modell["name"]]
        if len( modell_namen)>0:
            self.modell_name.set(modell_namen[0])
        ttk.Combobox(master=unterrahmen1, values=modell_namen, state="readonly", textvariable=self.modell_name).grid(column=2, row=2, sticky="NEW")
         
        # Unterrahmen 2 und Knöpfe für Steuerung
        unterrahmen2 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen2.grid(column=1, row=4, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen2, text="Modell Steuerung", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=2, sticky="NW")
        ttk.Button(master=unterrahmen2, text="Starten", command=lambda: self.start()).grid(column=1, row=2, sticky="NW")

        # Globaler Knopf
        ttk.Button(master=hauptrahmen, text="Schließen", command=lambda: self.schliessen()).grid(column=2, row=5, sticky="NE")

        for element in hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")
        for element in unterrahmen1.winfo_children():
            element.grid_configure(padx="2", pady="2")


    def lese_modell_datei(self):
        with open(Konfig.MODELL_DATEI) as f:
            data = json.load(f)
        return data


    def exrahiere_optionen( self):
        """ Ausgewähltes Modell mit Details extrahieren """

        name = self.modell_name.get()
        for modell in self.modelle:
           if modell["name"] == name:
               opt= modell
        return opt

    def start(self):
        """ Generatorfenster schliessen """
        #opt= self.exrahiere_optionen()
        opt= self.exrahiere_optionen()
        self.controller.start( opt)


    def schliessen(self):
        """ Generatorfenster schliessen """
        self.aktiv = False
        self.modellfenster.destroy()


class ModellController:

    def __init__(self):
        """ Konstruktor des Modell Controllers """
        self.t = None

    def start(self, optionen):
        """ Modell starten """
        exe = str(optionen["exe"])
        print( "Modell gestartet", exe)
        subprocess.Popen(exe)

