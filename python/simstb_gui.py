""" simstb_gui.py - GUI
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  27.07.2021, 10.01.2024
    """

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import threading
import time
import sys
from simstb_konfig import Konfig
from simstb_dateizugriff import DateiZugriff
from simstb_setzer import Setzer
from simstb_generator import GeneratorGUI
from simstb_datenaufzeichner import DatenaufzeichnerGUI
from simstb_modelle import ModellGUI


INTERVALL = 1


class GUI:
    """Klasse GUI"""

    def __init__(self):
        """Konstruktor, in dem das GUI des Simulators aufgebaut wird"""
        # Fremdwerkzeuge initialisieren
        self.gen_gui = None
        self.dat_gui = None
        self.mod_gui = None
        # GUI aufbauen
        self.hauptrahmen_anlegen()
        self.fensterelemente_festlegen()
        self.festlegen_Styles()
        self.layout_feinschliff()
        # Eingangswerte laden und Aktualisierer starten
        self.aktualisieren_eingangswerte()
        ZeitAktualisierer(self.datum, self.zeit)
        AusgangsdatenAktualisierer(self.DA, self.AA)
        # Hauptschleife GUI starten
        self.fenster.mainloop()

    def hauptrahmen_anlegen(self):
        # Fenster erstellen
        self.fenster = Tk(className="SimSTB - Simulationsumgebung")  # Rohes Fenster erstellen
        self.fenster.iconbitmap("simstb.ico")
        self.fenster.protocol("WM_DELETE_WINDOW", lambda: self.beenden())
        self.fenster.geometry("600x850")
        # Canvas in Fenster erstellen, um das Scrollen zu ermöglichen
        self.canvas = Canvas(self.fenster, bg=Konfig.HAUPT_BACKGROUND)
        self.canvas.grid(row=1, column=1, sticky="nsew")
        # Scrollbar erstellen und an den Canvas binden
        scrollbar = Scrollbar(self.fenster, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")

        # Canvas mit der Scrollbar verbinden
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Hauptrahmen erstellen und in Canvas
        self.hauptrahmen = ttk.Frame(master=self.canvas, padding="5", style="Haupt.TFrame")
        self.hauptrahmen.grid(column=1, row=1, sticky="NWES")
        self._frame_id = self.canvas.create_window((0, 0), window=self.hauptrahmen, anchor="nw")

        return

    def fensterelemente_festlegen(self):
        # Titelbereich einfügen
        ttk.Label(master=self.hauptrahmen, text="SimSTB", style="HauptLabel1.TLabel").grid(column=1, row=1, sticky="NW")
        ttk.Label(
            master=self.hauptrahmen,
            text="Simulationsumgebung für digitale\nund analoge Ein- und Ausgänge",
            style="HauptLabel2.TLabel",
        ).grid(column=2, row=1, columnspan=2, sticky="NW")
        self.datum = StringVar()
        ttk.Label(master=self.hauptrahmen, textvariable=self.datum, style="HauptLabel2.TLabel").grid(column=1, row=2, sticky="NW")
        self.zeit = StringVar()
        ttk.Label(master=self.hauptrahmen, textvariable=self.zeit, style="HauptLabel2.TLabel").grid(column=2, row=2, sticky="NW")

        # Unterrahmen 1 und Knöpfe
        self.unterrahmen1 = ttk.Frame(master=self.hauptrahmen, padding="5", style="Block.TFrame")
        self.unterrahmen1.grid(column=1, row=3, sticky="NWES")
        ttk.Button(master=self.unterrahmen1, text="Alles 0", command=lambda: self.setzen0_alles()).grid(
            column=1, row=1, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen1, text="Alle Ausgänge 0", command=lambda: self.setzen0_ausgaenge()).grid(
            column=1, row=2, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen1, text="Alle Eingänge 0", command=lambda: self.setzen0_eingaenge()).grid(
            column=1, row=3, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen1, text="Digitale Eingänge 0", command=lambda: self.setzen0_digitale_eingaenge()).grid(
            column=1, row=4, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen1, text="Digitale Eingänge 1", command=lambda: self.setzen1_digitale_eingaenge()).grid(
            column=1, row=5, sticky="WE"
        )

        # Unterrahmen 2 und Knöpfe
        self.unterrahmen2 = ttk.Frame(master=self.hauptrahmen, padding="5", style="Block.TFrame")
        self.unterrahmen2.grid(column=1, row=4, sticky="NWES")
        ttk.Button(master=self.unterrahmen2, text="Modelle", command=lambda: self.modelle()).grid(column=1, row=1, sticky="WE")
        ttk.Button(master=self.unterrahmen2, text="Testautomaten", command=lambda: self.testautomaten()).grid(
            column=1, row=2, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen2, text="Funktionsgenerator", command=lambda: self.funktionsgenerator()).grid(
            column=1, row=3, sticky="WE"
        )
        ttk.Button(master=self.unterrahmen2, text="Datenaufzeichnung", command=lambda: self.datenaufzeichnen()).grid(
            column=1, row=4, sticky="NW"
        )

        # Unterrahmen 3 und Inhalt
        self.unterrahmen3 = ttk.Frame(master=self.hauptrahmen, padding="5", style="Block.TFrame")
        self.unterrahmen3.grid(column=2, row=3, rowspan=2, sticky="NWES")
        ttk.Label(master=self.unterrahmen3, text="Digitale\nEingänge", style="BlockLabel2.TLabel").grid(
            column=1, row=1, columnspan=2, sticky="NW"
        )
        unterrahmenDE = ttk.Frame(master=self.unterrahmen3, padding="5", style="Unterblock.TFrame")
        unterrahmenDE.grid(column=1, row=2, columnspan=2, sticky="NWES")
        self.DE = []
        for i in range(Konfig.DIGMAXLAENGE):
            eintrag = IntVar()
            eintrag.set(0)
            ttk.Checkbutton(
                master=unterrahmenDE,
                text="DE" + str(i),
                command=lambda: self.setzen_digitale_eingaenge(),
                variable=eintrag,
                style="BlockCheckbutton.TCheckbutton",
            ).grid(column=1, row=i + 1, sticky="NW")
            self.DE.append(eintrag)
        ttk.Label(master=self.unterrahmen3, text="Digitale\nAusgänge", style="BlockLabel2.TLabel").grid(
            column=3, row=1, columnspan=2, sticky="NW"
        )
        unterrahmenDA = ttk.Frame(master=self.unterrahmen3, padding="5", style="Unterblock.TFrame")
        unterrahmenDA.grid(column=3, row=2, columnspan=2, sticky="NWES")
        self.DA = []
        for i in range(Konfig.DIGMAXLAENGE):
            eintrag = IntVar()
            eintrag.set(0)
            ttk.Checkbutton(
                master=unterrahmenDA, text="DA" + str(i), variable=eintrag, style="BlockCheckbutton.TCheckbutton", state=DISABLED
            ).grid(column=1, row=i + 1, sticky="NW")
            self.DA.append(eintrag)
        ttk.Label(master=self.unterrahmen3, text="Analoge\nEingänge", style="BlockLabel2.TLabel").grid(
            column=1, row=3, columnspan=2, sticky="NW"
        )
        validationAE = (self.fenster.register(self.setzen_analoge_eingaenge_1), "%P")
        unterrahmenAE = ttk.Frame(master=self.unterrahmen3, padding="5", style="Unterblock.TFrame")
        unterrahmenAE.grid(column=1, row=4, columnspan=2, sticky="NWES")
        self.AE = []
        for i in range(Konfig.ANAMAXLAENGE):
            eintrag = DoubleVar()
            eintrag.set(0)
            ttk.Label(master=unterrahmenAE, text="AE" + str(i), style="BlockLabel.TLabel").grid(column=1, row=i + 1, sticky="NW")
            ttk.Entry(master=unterrahmenAE, textvariable=eintrag, validate="focusout", validatecommand=validationAE).grid(
                column=2, row=i + 1, sticky="NW"
            )
            self.AE.append(eintrag)
        ttk.Label(master=self.unterrahmen3, text="Analoge\nAusgänge", style="BlockLabel2.TLabel").grid(
            column=3, row=3, columnspan=2, sticky="NW"
        )
        unterrahmenAA = ttk.Frame(master=self.unterrahmen3, padding="5", style="Unterblock.TFrame")
        unterrahmenAA.grid(column=3, row=4, columnspan=2, sticky="NWES")
        self.AA = []
        for i in range(Konfig.ANAMAXLAENGE):
            eintrag = DoubleVar()
            eintrag.set(0)
            ttk.Label(master=unterrahmenAA, text="AA" + str(i), style="BlockLabel.TLabel").grid(column=1, row=i + 1, sticky="NW")
            ttk.Entry(master=unterrahmenAA, textvariable=eintrag, state=DISABLED).grid(column=2, row=i + 1, sticky="NW")
            self.AA.append(eintrag)

        # Globale Knöpfe einfügen
        ttk.Button(master=self.hauptrahmen, text="Beenden", command=lambda: self.beenden()).grid(column=2, row=5, sticky="NE")

    def festlegen_Styles(self):
        """Festlegen der genutzten Styles"""
        sblock = ttk.Style()

        sblock.configure("TLabel", font=("Tahoma", 11))
        sblock.configure("TButton", font=("Tahoma", 11))
        sblock.configure("TCheckbutton", font=("Tahoma", 11))

        sblock.configure("Haupt.TFrame", background=Konfig.HAUPT_BACKGROUND)
        sblock.configure("HauptLabel2.TLabel", background=Konfig.HAUPT_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure("HauptLabel1.TLabel", background=Konfig.HAUPT_BACKGROUND, font=("Tahoma", 24, "bold"))

        sblock.configure("Block.TFrame", background=Konfig.BLOCK_BACKGROUND, relief=RAISED)
        sblock.configure("BlockLabel2.TLabel", background=Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure("BlockLabel.TLabel", background=Konfig.BLOCK_BACKGROUND)
        sblock.configure("BlockStatusLabelGen.TLabel", background=Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure("BlockStatusLabelDat.TLabel", background=Konfig.BLOCK_BACKGROUND, font=("Tahoma", 11, "bold"))
        sblock.configure("BlockCheckbutton.TCheckbutton", background=Konfig.BLOCK_BACKGROUND)
        sblock.configure("Unterblock.TFrame", background=Konfig.BLOCK_BACKGROUND)

    def layout_feinschliff(self):
        """Feinschlif Layout - Abstände zwischen Fensterelementen setzen"""
        # Abstände setzen
        for element in self.hauptrahmen.winfo_children():
            element.grid_configure(padx="10", pady="10")
        for element in self.unterrahmen1.winfo_children():
            element.grid_configure(padx="2", pady="2")
        for element in self.unterrahmen2.winfo_children():
            element.grid_configure(padx="2", pady="2")
        # Verhalten bei Größenänderungen festlegen
        self.fenster.columnconfigure(1, weight=1)
        self.fenster.rowconfigure(1, weight=1)
        self.canvas.columnconfigure(1, weight=1)
        self.canvas.rowconfigure(1, weight=1)
        self.hauptrahmen.columnconfigure(1, weight=1)
        self.hauptrahmen.columnconfigure(2, weight=1)
        # Das Scrollen anpassen, wenn sich der Inhalt ändert
        self.hauptrahmen.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Callback-Funktion und Hilfsfunktionen für Daten laden und aktualisieren

    def aktualisieren_eingangswerte(self):
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
        de_daten = de_zugriff.lesen_alle()
        for i in range(Konfig.DIGMAXLAENGE):
            self.DE[i].set(de_daten[i])
        ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
        ae_daten = ae_zugriff.lesen_alle()
        for i in range(Konfig.ANAMAXLAENGE):
            self.AE[i].set(ae_daten[i])

    def aktualisieren_ausgangswerte(self):
        da_zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE)
        da_daten = da_zugriff.lesen_alle()
        for i in range(Konfig.DIGMAXLAENGE):
            self.DA[i].set(da_daten[i])
        aa_zugriff = DateiZugriff(Konfig.ANAAUS, Konfig.ANAMAXLAENGE)
        aa_daten = aa_zugriff.lesen_alle()
        for i in range(Konfig.ANAMAXLAENGE):
            self.AA[i].set(aa_daten[i])

    # Callback-Funktionen für die Knöpfe zum Setzen der Ein- und Ausgänge - Unterrahmen 1

    def setzen0_alles(self):
        """Alle Ein- und Ausgänge auf 0 setzen"""
        setzer = Setzer()
        setzer.setzen0_alles()
        self.aktualisieren_eingangswerte()

    def setzen0_ausgaenge(self):
        """Alle Ausgänge auf 0 setzen"""
        setzer = Setzer()
        setzer.setzen0_ausgaenge()

    def setzen0_eingaenge(self):
        """Alle Eingänge auf 0 setzen"""
        setzer = Setzer()
        setzer.setzen0_eingaenge()
        self.aktualisieren_eingangswerte()

    def setzen0_digitale_eingaenge(self):
        """Digitale Eingänge auf 0 setzen"""
        setzer = Setzer()
        setzer.setzen0_digitale_eingaenge()
        self.aktualisieren_eingangswerte()

    def setzen1_digitale_eingaenge(self):
        """Digitale Eingänge auf 1 setzen"""
        setzer = Setzer()
        setzer.setzen1_digitale_eingaenge()
        self.aktualisieren_eingangswerte()

    # Callback-Funktionen für das Setzen einzelner digitaler oder analoger Eingangskanälen - Unterrahmen 3

    def setzen_digitale_eingaenge(self):
        """Digitale Eingänge setzen"""
        de_daten = []
        for i in range(Konfig.DIGMAXLAENGE):
            de_daten = de_daten + [int(self.DE[i].get())]
        de_zugriff = DateiZugriff(Konfig.DIGEIN, Konfig.DIGMAXLAENGE)
        de_zugriff.schreiben_alle(de_daten)
        self.aktualisieren_eingangswerte()

    def setzen_analoge_eingaenge_2(self):
        """Analoge Eingänge setzen - Durchführung"""
        ae_daten = []
        for i in range(Konfig.ANAMAXLAENGE):
            ae_daten = ae_daten + [float(self.AE[i].get())]
        ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
        ae_zugriff.schreiben_alle(ae_daten)

    def setzen_analoge_eingaenge_1(self, eintrag_neu):
        """Analoge Eingänge setzen - Testen der Eingabe"""
        try:
            float(eintrag_neu)
            self.setzen_analoge_eingaenge_2()
            return True
        except ValueError:
            messagebox.showerror(message="Kein gültiger Analogwert!", title="SimSTB Fehlermeldung")
            self.aktualisieren_eingangswerte()
            return False

    # Callback-Funktion und Hilfsfunktionen für Modelle zu starten - Unterrahmen 2

    def modell_gui_aktiv(self):
        """Testen, ob ein Modell aktiv ist"""
        if self.mod_gui is None:
            return False
        elif self.mod_gui.aktiv is False:
            return False
        return True

    def modelle(self):
        if self.modell_gui_aktiv() is False:
            self.mod_gui = ModellGUI(self.fenster)

    # Callback-Funktion und Hilfsfunktionen für analogen Funktionsgenerator - Unterrahmen 2

    def funktionsgenerator_gui_aktiv(self):
        """Testen, ob der Funktionsgenerator aktiv ist"""
        if self.gen_gui is None:
            return False
        elif self.gen_gui.gen_gui_aktiv is False:
            return False
        return True

    def auto_aktualisieren_analoge_eingaenge(self):
        wiederholen = self.funktionsgenerator_gui_aktiv()
        ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
        ae_daten = ae_zugriff.lesen_alle()
        for i in range(Konfig.ANAMAXLAENGE):
            self.AE[i].set(ae_daten[i])
        if wiederholen is True:
            self.fenster.after(1000, self.auto_aktualisieren_analoge_eingaenge)

    def funktionsgenerator(self):
        if self.funktionsgenerator_gui_aktiv() == False:
            self.gen_gui = GeneratorGUI(self.fenster)
            self.auto_aktualisieren_analoge_eingaenge()

    # Callback-Funktion und Hilfsfunktionen für Datenaufzeichner - Unterrahmen 2

    def datenaufzeichner_gui_aktiv(self):
        if self.dat_gui is None:
            return False
        elif self.dat_gui.dat_gui_aktiv is False:
            return False
        return True

    def datenaufzeichnen(self):
        if self.datenaufzeichner_gui_aktiv() is False:
            self.dat_gui = DatenaufzeichnerGUI(self.fenster)

    # Callback-Funktion für verschiedene noch nicht realisierte Funktionalitäten - Unterrahmen 2

    def testautomaten(self):
        messagebox.showinfo(
            message="Leider nocht nicht implementiert.\nAutomatisiertes Testablaufmodul.", title="SimSTB Information"
        )

    # Callback-Funktion fürs Beenden

    def beenden(self):
        """SimSTB beenden"""
        # Hilfsfenster und Threads beenden
        if self.funktionsgenerator_gui_aktiv():
            self.gen_gui.stop()
            self.gen_gui.schliessen()
        if self.datenaufzeichner_gui_aktiv():
            self.dat_gui.stop()
            self.dat_gui.schliessen()
        if self.modell_gui_aktiv():
            self.mod_gui.schliessen()
        # Hauptprogramm beenden
        sys.exit("Simulator SimSTB beendet")


class AusgangsdatenAktualisierer:
    """Klasse zum Aktualisieren der Ausgangsdaten"""

    def __init__(self, DA, AA):
        """Konstruktor wirft die eigentliche Aktualisieren der Ausgangsdaten an"""
        t_1 = threading.Thread(
            target=AusgangsdatenAktualisierer.aktualisieren,
            args=(
                DA,
                AA,
            ),
            daemon=True,
        )
        t_1.start()

    @staticmethod
    def aktualisieren(DA, AA):
        """Aktualisieren der Daten für digitale und analoge Ausgänge"""
        while True:
            da_zugriff = DateiZugriff(Konfig.DIGAUS, Konfig.DIGMAXLAENGE)
            da_daten = da_zugriff.lesen_alle()
            for i in range(Konfig.DIGMAXLAENGE):
                DA[i].set(da_daten[i])
            aa_zugriff = DateiZugriff(Konfig.ANAAUS, Konfig.ANAMAXLAENGE)
            aa_daten = aa_zugriff.lesen_alle()
            for i in range(Konfig.ANAMAXLAENGE):
                AA[i].set(aa_daten[i])
                time.sleep(INTERVALL)


class AnalogeEingangsdatenAktualisierer:
    """Klasse zum Aktualisieren der Ausgangsdaten"""

    def __init__(self, AE):
        """Konstruktor wirft die eigentliche Aktualisieren der analogen Eingangsdaten an"""
        t_1 = threading.Thread(
            target=AnalogeEingangsdatenAktualisierer.aktualisieren,
            args=(AE,),
            daemon=True,
        )
        t_1.start()

    @staticmethod
    def aktualisieren(AE):
        """Aktualisieren der Daten für analoge Eingänge"""
        while True:
            ae_zugriff = DateiZugriff(Konfig.ANAEIN, Konfig.ANAMAXLAENGE)
            ae_daten = ae_zugriff.lesen_alle()
            for i in range(Konfig.ANAMAXLAENGE):
                AE[i].set(ae_daten[i])


class ZeitAktualisierer:
    """Klasse zum Aktualisieren der Zeit"""

    def __init__(self, wertdatum, wertzeit):
        """Konstruktor wirft die eigentliche Zeitsetzung an"""
        t_2 = threading.Thread(
            target=ZeitAktualisierer.aktualisieren,
            args=(
                wertdatum,
                wertzeit,
            ),
            daemon=True,
        )
        t_2.start()

    @staticmethod
    def aktualisieren(wertdatum, wertzeit):
        """Aktualisieren der Zeit"""
        while True:
            datum = str(datetime.datetime.now().strftime("%d.%m.%Y"))
            wertdatum.set(datum)
            zeit = str(datetime.datetime.now().strftime("%H:%M:%S"))
            wertzeit.set(zeit)
            time.sleep(INTERVALL)


# SimSTB starten
GUI()
