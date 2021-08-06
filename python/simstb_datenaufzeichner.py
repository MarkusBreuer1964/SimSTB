""" SimSTB - Datenaufzeichner

    SimSTB - Simulation digitaler und analoger Ein- und Ausgaben

    Das Modul Datenaufzeichner stellt drei Klassen zur Realisierung des
    Datenaufzeichners zur Verfügung.
    1. In der Klasse DatenaufzeichnerGUI wird ein Toplevel-Fenster erzeugt, in dem
    der Benutzer die Generatoroptionen setzen kann und den Generator 
    starten und stoppen.
    2. Die Klasse DatenaufzeichnerController sorgz dafür, dass der eigentliche
    Datenaufzeichner in einem eigenen Thread läuft.
    3. Die Klasse Datenaufzeichner enthält die eigentliche Datenaufzeichnung

    Name:               Markus Breuer
    Organisaion:        STB

    Erstellt:           06.08.2021
    Letzte Änderung:    
    """

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
import time
from simstb_konfig import Konfig
from simstb_dateizugriff import DateiZugriff

class DatenaufzeichnerGUI:
    """ Klasse Datenaufzeichner GUI """

    def __init__(self, hauptfenster):
        """ Konstruktor, in dem das GUI des Datenaufzeichners aufgebaut wird """
        self.dat_gui_aktiv = True
        self.hauptfenster = hauptfenster
        self.controller = DatenaufzeichnerController()

        # Top-Level Fenster für Datenaufzeichner anlegen
        self.datenaufzeichnerfenster = Toplevel(self.hauptfenster)  
        self.datenaufzeichnerfenster.iconbitmap("simstb.ico")
        self.datenaufzeichnerfenster.title("SimSTB - Datenaufzeichner")     
        self.datenaufzeichnerfenster.protocol("WM_DELETE_WINDOW", lambda: self.schliessen())
       
        # Hauptrahmen anlegen
        hauptrahmen = ttk.Frame(master=self.datenaufzeichnerfenster, padding="5", style="Haupt.TFrame")
        hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self.datenaufzeichnerfenster.columnconfigure(1, weight=1)
        self.datenaufzeichnerfenster.rowconfigure(1, weight=1)

        # Titelbereich einfügen
        ttk.Label(master=hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(master=hauptrahmen, text="Datenaufzeichner", style="HauptLabel2.TLabel").grid(column=2, row=1, sticky="NW")

        # Unterrahmen 1 und Elemente für Einstellungen
        unterrahmen1 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen1.grid(column=1, row=3, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen1, text="Datenaufzeichner Einstellungen", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=3, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Interval (s)", style="BlockLabel.TLabel").grid(column=1, row=2, sticky="NW") # Intervall
        self.intervall = IntVar() 
        self.intervall.set(5)
        ttk.Entry(master=unterrahmen1, textvariable=self.intervall).grid(column=2, row=2, sticky="NW")
        ttk.Label(master=unterrahmen1, text="Log-Datei", style="BlockLabel.TLabel").grid(column=1, row=3, sticky="NW")
        self.dateiname = StringVar() 
        self.dateiname.set("simstb.log")
        ttk.Entry(master=unterrahmen1, textvariable=self.dateiname).grid(column=2, row=3, sticky="NW")
        ttk.Button(master=unterrahmen1, text="Datei", command=lambda: self.auswaehlen_datei()).grid(column=3, row=3, sticky="NW")

        # Unterrahmen 2 und Knöpfe für Steuerung
        unterrahmen2 = ttk.Frame(master=hauptrahmen, padding="5", style="Block.TFrame")
        unterrahmen2.grid(column=1, row=4, columnspan=2, sticky="NWES")
        ttk.Label(master=unterrahmen2, text="Datenaufzeichner Steuerung", style="BlockLabel2.TLabel").grid(column=1, row=1, columnspan=2, sticky="NW")
        ttk.Button(master=unterrahmen2, text="Starten", command=lambda: self.start()).grid(column=1, row=2, sticky="NW")
        ttk.Button(master=unterrahmen2, text="Stoppen", command=lambda: self.stop()).grid(column=2, row=2, sticky="NW")
        self.gen_status = StringVar()
        self.gen_status.set( "Datenaufzeichner nicht aktiv")
        ttk.Label(master=unterrahmen2, textvariable=self.gen_status, style="BlockStatusLabelDat.TLabel").grid(column=3, row=2, columnspan=2, sticky="NE")

        # Globaler Knopf
        ttk.Button(master=hauptrahmen, text="Schließen", command=lambda: self.schliessen()).grid(column=2, row=5, sticky="NE")

        for element in hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")
        for element in unterrahmen1.winfo_children():
            element.grid_configure(padx="2", pady="2")


    def auswaehlen_datei(self):
        """ Dateinamen interaktiv auswählen """
        dateiname = filedialog.asksaveasfilename()
        if dateiname != None:
            self.dateiname.set(dateiname)


    def exrahiere_optionen( self):
        """ Dictionary mit Optionen für atenaufzeichner erstellen """
        opt = { "intervall": int(self.intervall.get()), "dateiname":str(self.dateiname.get())}
        return opt

    def start(self):
        """ DatenaufzeichnerGUI schliessen """
        opt= self.exrahiere_optionen()
        if self.controller.ist_am_laufen() == False:
            self.controller.start( opt)
            self.gen_status.set( "Datenaufzeichner aktiv")
            sblock = ttk.Style()
            sblock.configure( "BlockStatusLabelDat.TLabel", background = Konfig.AKTIVE_BACKGROUND)

    def stop(self):
        """ Generatorfenster schliessen """
        if self.controller.ist_am_laufen() == True:
            self.controller.stop()
            self.gen_status.set( "Datenaufzeichner nicht aktiv")
            sblock = ttk.Style()
            sblock.configure( "BlockStatusLabelDat.TLabel", background =Konfig.BLOCK_BACKGROUND)

    def schliessen(self):
        """ Datenaufzeichnerfenster schliessen """
        if self.controller.ist_am_laufen() == True:
            self.stop()
        self.datenaufzeichnerfenster.destroy()
        self.dat_gui_aktiv = False

class DatenaufzeichnerController:

    def __init__(self):
        """ Konstruktor des Datenaufzeichner Controllers """
        self.t = None

    def start(self, optionen):
        """ Datenaufzeichner starten """
        self.t = threading.Thread(target=self.doit, args=(optionen,))
        self.t.start()
        
    def stop(self):
        """ Funktionsgenerator beenden """
        self.t.do_run = False
        self.t = None

    def ist_am_laufen(self):
        if self.t == None:
            return False
        else:
            return True

    def doit(self, opt):
        t = threading.currentThread()
        dat_gen = Datenaufzeichner(opt)
        while getattr(t, "do_run",True):
            dat_gen.schreibe_daten()
            time.sleep(opt["intervall"])


class Datenaufzeichner:
    def __init__(self,opt):
        """ Konstruktor des Datenaufzeichners """
        self.dateiname = opt["dateiname"]
        self.schreibe_kopfzeile()

    def schreibe_kopfzeile(self):
        zeile = "Zeit"
        for i in range(Konfig.DIGMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + "DE" + str(i)
        for i in range(Konfig.ANAMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + "AE" + str(i)
        for i in range(Konfig.DIGMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + "DA" + str(i)
        for i in range(Konfig.ANAMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + "AA" + str(i)
        zeile = zeile + "\n"
        with open(self.dateiname, "w") as f:
            f.write(zeile)    

    def schreibe_daten(self):
        zeile = time.strftime("%H:%M:%S") # Zeit rausschreiben
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)  # Digitale Eingänge rausschreiben
        de_daten= de_zugriff.lesen_alle()
        for i in range(Konfig.DIGMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + de_daten[i]
        ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE) # Analoge Eingänge rausschreiben
        ae_daten= ae_zugriff.lesen_alle()
        for i in range(Konfig.ANAMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + ae_daten[i]
        da_zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE) # Digitale Ausgänge rausschreiben
        da_daten= da_zugriff.lesen_alle()
        for i in range(Konfig.DIGMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + da_daten[i]
        aa_zugriff = DateiZugriff(Konfig.ANAAUS, Konfig.ANAMAXLAENGE) # Analoge Ausgänge rausschreiben
        aa_daten= aa_zugriff.lesen_alle()
        for i in range(Konfig.ANAMAXLAENGE):
            zeile = zeile + ";"
            zeile = zeile + aa_daten[i]
        zeile = zeile + "\n" # Zeilenvorschub
        zeile = zeile.replace(".",",")  # deutsches Komma in Logdatei
        with open(self.dateiname, "a") as f:
            f.write(zeile)
