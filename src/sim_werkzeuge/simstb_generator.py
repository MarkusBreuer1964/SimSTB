""" simstb_generator.py - SimSTB -Analoger Funktionsgenerator
    Das Modul Funktionsgenerator stellt vier Klassen zur Realisierung des
    analogen Funktionsgenerators zur Verfügung.
    1. In der Klasse GeneratorGUI wird ein Toplevel-Fenster erzeugt, in dem
    der Benutzer die Generatoroptionen setzen kann und den Generator
    starten und stoppen.
    2. Die Klasse GeneratorController sorgz dafür, dass der eigentliche
    Generator in einem eigenen Thread läuft.
    3. Die Klasse FunktionsGenerator enthält den eigentlichen Funktionsgenerator
    4. Eine Klasse zur Aktualisierung der analogen Eingänge
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  28.07.2021, 16.03.2026
    """


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
import logging
import time
import random
import math
from datetime import datetime
import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg

class GeneratorGUI:
    """ Klasse Funktionsgenerator GUI """

    def __init__(self, gui):
        """ Konstruktor, in dem das GUI des Funktionsgenerator aufgebaut wird """
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        # Logging initialisieren und Log-Message rausschreiben
        self.logger = logging.getLogger(__name__ + ".GeneratorGUI")
        self.logger.info("Funktionsgenerator GUI gestartet")
        self.gen_gui_aktiv = True
        self.gui = gui
        self.controller = GeneratorController()

        # Top-Level Fenster für Funktionsgenerator anlegen
        self.generatorfenster = Toplevel(self.gui.fenster)
        self.generatorfenster.title("SimSTB - Funktionsgenerator")
        self.generatorfenster.protocol("WM_DELETE_WINDOW", lambda: self.schliessen())

        self.stop_event_ae = threading.Event()

        # Hauptrahmen anlegen
        hauptrahmen = ttk.Frame(master=self.generatorfenster, padding="5", style="Haupt.TFrame")
        hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.generatorfenster.columnconfigure(1, weight=1)
        self.generatorfenster.rowconfigure(1, weight=1)

        # Titelbereich einfügen
        ttk.Label(master=hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(master=hauptrahmen, text="Analoger\nFunktionsgenerator", style="HauptLabel2.TLabel").grid(column=2, row=1, sticky="NW")

        # Unterrahmen 1 und Elemente für Einstellungen
        unterrahmen1 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen1.grid(column=1, row=3, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen1, text="Funktionsgenerator Einstellungen", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=5, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Kanal", style="BlockLabel.TLabel").grid(column=1, row=2, sticky="NW")
        ttk.Label(master=unterrahmen1, text="An/Aus", style="BlockLabel.TLabel").grid(column=2, row=2, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Signalform", style="BlockLabel.TLabel").grid(column=3, row=2, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Amplitude", style="BlockLabel.TLabel").grid(column=4, row=2, sticky="NW")
        ttk.Label(master=unterrahmen1, text="P.Dauer (s)", style="BlockLabel.TLabel").grid(column=5, row=2, sticky="NW")
        self.aktiviert = []
        self.signalform = []
        self.amplitude = []
        self.pdauer = []
        for i in range(self.konfig["ANAMAXLAENGE"]):
            ttk.Label(master=unterrahmen1, text="AE"+str(i), style="BlockLabel.TLabel").grid(column=1, row=i+3, sticky="NW") #Kanal
            eintrag_aktiviert = IntVar() #An/Aus
            eintrag_aktiviert.set(0)
            ttk.Checkbutton(master=unterrahmen1, variable=eintrag_aktiviert, style="BlockCheckbutton.TCheckbutton").grid(column=2, row=i+3, sticky="N")
            self.aktiviert.append(eintrag_aktiviert)
            eintrag_signalform = StringVar() # Signalform
            eintrag_signalform.set(self.konfig["SIGNALFORMEN"][0])
            ttk.Combobox(master=unterrahmen1, values=self.konfig["SIGNALFORMEN"], state="readonly", textvariable=eintrag_signalform).grid(column=3, row=i+3, sticky="NEW")
            self.signalform.append(eintrag_signalform)
            eintrag_amplitude = DoubleVar() # Amplitude
            eintrag_amplitude.set(0)
            ttk.Entry(master=unterrahmen1, textvariable=eintrag_amplitude).grid(column=4, row=i+3, sticky="NW")
            self.amplitude.append(eintrag_amplitude)
            eintrag_pdauer = DoubleVar() # Periodendauer
            eintrag_pdauer.set(0)
            ttk.Entry(master=unterrahmen1, textvariable=eintrag_pdauer).grid(column=5, row=i+3, sticky="NW")
            self.pdauer.append(eintrag_pdauer)

        # Unterrahmen 2 und Knöpfe für Steuerung
        unterrahmen2 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen2.grid(column=1, row=4, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen2, text="Funktionsgenerator Steuerung", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=2, sticky="NW")
        ttk.Button(master=unterrahmen2, text="Starten", command=lambda: self.start()).grid(column=1, row=2, sticky="NW")
        ttk.Button(master=unterrahmen2, text="Stoppen", command=lambda: self.stop()).grid(column=2, row=2, sticky="NW")
        self.gen_status = StringVar()
        self.gen_status.set( "Generator nicht aktiv")
        ttk.Label(master=unterrahmen2, textvariable=self.gen_status, style="BlockStatusLabelGen.TLabel").grid(column=3, row=2, columnspan=2, sticky="NE")

        # Globaler Knopf
        ttk.Button(master=hauptrahmen, text="Schließen", command=lambda: self.schliessen()).grid(column=2, row=5, sticky="NE")

        for element in hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")
        for element in unterrahmen1.winfo_children():
            element.grid_configure(padx="2", pady="2")


    def exrahiere_optionen( self):
        """ Liste mit Dictionaries für Funktionsgeneratoroptionen erstellen """
        opt = []
        for i in range(self.konfig["ANAMAXLAENGE"]):
            eintrag = { "aktiviert": self.aktiviert[i].get(), "signalform":self.signalform[i].get(), "amplitude": self.amplitude[i].get(),"pdauer":self.pdauer[i].get()}
            opt = opt + [eintrag]
        return opt

    def start(self):
        """ Generator starten """
        opt = self.exrahiere_optionen()
        if not self.controller.ist_am_laufen():
            # AE-Aktualisierung starten
            self.gui.aktualisierer.aktualisierungsvektor_setzen("ae", 1)  # AE-Aktualisierung einschalten
            # Generator starten
            self.controller.start(opt)
            # GUI-Status aktualisieren
            self.gen_status.set("Generator aktiv")
            sblock = ttk.Style()
            sblock.configure("BlockStatusLabelGen.TLabel", background=self.konfig["AKTIVE_BACKGROUND"])            

    def stop(self):
        """ Generator stoppen """
        if self.controller.ist_am_laufen():
            # Stop AE-Aktualisierung
            self.gui.aktualisierer.aktualisierungsvektor_setzen("ae", 0)  # AE-Aktualisierung ausschalten
            # Generator stoppen
            self.controller.stop()
                # GUI-Status aktualisieren
            self.gen_status.set("Generator nicht aktiv")
            sblock = ttk.Style()
            sblock.configure("BlockStatusLabelGen.TLabel", background=self.konfig["BLOCK_BACKGROUND"])

    def schliessen(self):
        """ Generatorfenster schliessen """
        self.gui.aktualisierer.aktualisierungsvektor_setzen("ae", 0)  # AE-Aktualisierung ausschalten
        if self.controller.ist_am_laufen():
           self.controller.stop()              # Generator stoppen
        self.generatorfenster.destroy()
        self.gen_gui_aktiv = False
        self.logger.info("Funktionsgenerator GUI geschlossen")


class GeneratorController:
    """ Klasse Funktionsgenerator Controller (thread-safe) """

    def __init__(self):
        """ Konstruktor des Generator Controllers """
        self.t = None
        self.stop_event = threading.Event()
        self.logger = logging.getLogger(__name__ + ".GeneratorController")

    def start(self, optionen):
        """ Funktionsgenerator starten """
        if self.ist_am_laufen():
            self.logger.warning("Funktionsgenerator läuft bereits")
            return

        self.stop_event.clear()
        self.t = threading.Thread(target=self.doit, args=(optionen,), daemon=True)
        self.t.start()

    def stop(self):
        """ Funktionsgenerator beenden """
        if not self.ist_am_laufen():
            return

        self.stop_event.set()
        self.t.join()  # wartet sauber auf Thread-Ende
        self.t = None

    def ist_am_laufen(self):
        """ Test, ob Funktionsgenerator läuft """
        return self.t is not None and self.t.is_alive()

    def doit(self, opt):
        """ Thread-Funktion für Generator """
        fkt_gen = FunktionsGenerator(opt)
        self.logger.info("Funktionsgenerator gestartet")

        try:
            while not self.stop_event.is_set():
                try:
                    fkt_gen.erzeuge_daten()
                except Exception as e:
                    self.logger.error(f"Fehler beim Erzeugen der Daten: {e}")

                # Warte 1 Sekunde ODER sofort abbrechen bei Stop
                self.stop_event.wait(1)
        finally:
            self.logger.info("Funktionsgenerator beendet")


class FunktionsGenerator:
    def __init__(self,opt):
        """ Konstruktor des Funktionsgenerators """
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        self.opt = opt
        self.start_zeit = datetime.now()

    def erzeuge_daten(self):
        akt_zeit = datetime.now()
        t = int((akt_zeit - self.start_zeit).total_seconds())
        ae_zugriff = dzg.DateiZugriff(self.konfig["ANAEIN"], self.konfig["ANAMAXLAENGE"])  # Analoge Eingänge rausschreiben
        ae_daten= ae_zugriff.lesen_alle()
        for i in range(self.konfig["ANAMAXLAENGE"]):
            eintrag = self.opt[i]
            if eintrag["aktiviert"] == 1:
                ae_daten[i] = self.erzeuge_kanaldaten( t, eintrag)
        ae_zugriff.schreiben_alle( ae_daten)

    def erzeuge_kanaldaten(self, t, eintrag):
        wert = 0
        if eintrag["signalform"] == "Zufall":
            A = float(eintrag["amplitude"])
            wert =random.uniform(0,2*A) -A
            wert = round( wert,2)
        if eintrag["signalform"] == "Sinus":
            A = float(eintrag["amplitude"])
            T = float(eintrag["pdauer"])
            wert = A * math.sin( 2 * math.pi * t / T)
            wert = round( wert,2)
        if eintrag["signalform"] == "Rechteck":
            A = float(eintrag["amplitude"])
            T = float(eintrag["pdauer"])
            t = t % T
            if t < T/2:
                wert = 0
            else:
                wert = A
            wert = round( wert,2)
        if eintrag["signalform"] == "Dreieck":
            A = float(eintrag["amplitude"])
            T = float(eintrag["pdauer"])
            m = A/T
            t = t % T
            wert= m*t
            wert = round( wert,2)
        return wert

