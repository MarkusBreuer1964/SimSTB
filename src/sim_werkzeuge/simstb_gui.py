""" simstb_gui.py - GUI
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  27.07.2021,20.03.2026
    """


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import logging
import os
import sys
import threading
import screeninfo as si
import sim_basis.version as ver
import sim_basis.simstb_logger as log
import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg
from sim_werkzeuge.simstb_setzer import Setzer
from sim_werkzeuge.simstb_generator import GeneratorGUI
from sim_werkzeuge.simstb_datenaufzeichner import DatenaufzeichnerGUI
from sim_werkzeuge.simstb_modelle import ModellGUI



class GUI:
    """Klasse GUI"""

    def __init__(self):
        """Konstruktor, in dem das GUI des Simulators aufgebaut wird"""
        # Konfigurationsdatei laden
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        # Logging initialisieren und Log-Messages rausschreiben
        log.logging_einrichten()
        self.logger = logging.getLogger(__name__)
        self.logger.info("SimSTB GUI - Simulator gestartet")
        self.logger.debug("AktuellesArbeitsverzeichnis: " + os.getcwd())
        self.logger.debug("Basisverzeichnis: " + self.konfig["BASISVERZEICHNIS"])
        self.logger.debug("Konfigurationsdatei: " + self.konfig["KONFIG_DATEINAME"])
        self.logger.debug("Logdatei: " + self.konfig["LOGDATEI"])
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
        aktualisierungsvektor = {"zeit": 1,"de": 0,"ae": 0,"da": 1,"aa": 1}
        self.aktualisierer = Aktualisierer(self, aktualisierungsvektor)
        # Hauptschleife GUI starten
        self.fenster.mainloop()

    def fenstergroesse_festlegen(self):
        monitor = si.get_monitors()[0]  # Holen des ersten Monitors
        bildschirmhoehe = monitor.height
        if 0.9 * bildschirmhoehe > 850:
            fensterhoehe = 850
        else:
            fensterhoehe = 0.9 * bildschirmhoehe
        fenstergroesse ="600x"+str(int(fensterhoehe))
        return fenstergroesse

    def hauptrahmen_anlegen(self):
        # Fenster erstellen
        self.fenster = Tk(className="SimSTB - Simulationsumgebung")  # Rohes Fenster erstellen
        self.fenster.protocol("WM_DELETE_WINDOW", lambda: self.beenden())
        fenstergroesse = self.fenstergroesse_festlegen()
        self.fenster.geometry(fenstergroesse)
        # Canvas in Fenster erstellen, um das Scrollen zu ermöglichen
        self.canvas = Canvas(self.fenster, bg=self.konfig["HAUPT_BACKGROUND"], highlightthickness=0)
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
        for i in range(self.konfig["DIGMAXLAENGE"]):
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
        for i in range(self.konfig["DIGMAXLAENGE"]):
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
        for i in range(self.konfig["ANAMAXLAENGE"]):
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
        for i in range(self.konfig["ANAMAXLAENGE"]):
            eintrag = DoubleVar()
            eintrag.set(0)
            ttk.Label(master=unterrahmenAA, text="AA" + str(i), style="BlockLabel.TLabel").grid(column=1, row=i + 1, sticky="NW")
            ttk.Entry(master=unterrahmenAA, textvariable=eintrag, state=DISABLED).grid(column=2, row=i + 1, sticky="NW")
            self.AA.append(eintrag)

        # Globale Knöpfe einfügen
        ttk.Button(master=self.hauptrahmen, text="Info", command=lambda: self.info()).grid(column=1, row=5, sticky="NW")
        ttk.Button(master=self.hauptrahmen, text="Beenden", command=lambda: self.beenden()).grid(column=2, row=5, sticky="NE")

    def festlegen_Styles(self):
        """Festlegen der genutzten Styles"""
        sblock = ttk.Style()

        sblock.configure("TLabel", font=("Tahoma", 11))
        sblock.configure("TButton", font=("Tahoma", 11))
        sblock.configure("TCheckbutton", font=("Tahoma", 11))

        sblock.configure("Haupt.TFrame", background=self.konfig["HAUPT_BACKGROUND"])
        sblock.configure("HauptLabel2.TLabel", background=self.konfig["HAUPT_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure("HauptLabel1.TLabel", background=self.konfig["HAUPT_BACKGROUND"], font=("Tahoma", 24, "bold"))

        sblock.configure("Block.TFrame", background=self.konfig["BLOCK_BACKGROUND"], relief=RAISED)
        sblock.configure("BlockLabel2.TLabel", background=self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure("BlockLabel.TLabel", background=self.konfig["BLOCK_BACKGROUND"])
        sblock.configure("BlockStatusLabelGen.TLabel", background=self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure("BlockStatusLabelDat.TLabel", background=self.konfig["BLOCK_BACKGROUND"], font=("Tahoma", 11, "bold"))
        sblock.configure("BlockCheckbutton.TCheckbutton", background=self.konfig["BLOCK_BACKGROUND"])
        sblock.configure("Unterblock.TFrame", background=self.konfig["BLOCK_BACKGROUND"])

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
        de_zugriff = dzg.DateiZugriff(self.konfig["DIGEIN"], self.konfig["DIGMAXLAENGE"])
        de_daten = de_zugriff.lesen_alle()
        for i in range(self.konfig["DIGMAXLAENGE"]):
            self.DE[i].set(de_daten[i])
        ae_zugriff = dzg.DateiZugriff(self.konfig["ANAEIN"], self.konfig["ANAMAXLAENGE"])
        ae_daten = ae_zugriff.lesen_alle()
        for i in range(self.konfig["ANAMAXLAENGE"]):
            self.AE[i].set(ae_daten[i])

    def aktualisieren_ausgangswerte(self):
        da_zugriff = dzg.DateiZugriff(self.konfig["DIGAUS"], self.konfig["DIGMAXLAENGE"])
        da_daten = da_zugriff.lesen_alle()
        for i in range(self.konfig["DIGMAXLAENGE"]):
            self.DA[i].set(da_daten[i])
        aa_zugriff = dzg.DateiZugriff(self.konfig["ANAAUS"], self.konfig["ANAMAXLAENGE"])
        aa_daten = aa_zugriff.lesen_alle()
        for i in range(self.konfig["ANAMAXLAENGE"]):
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
        for i in range(self.konfig["DIGMAXLAENGE"]):
            de_daten = de_daten + [int(self.DE[i].get())]
        de_zugriff = dzg.DateiZugriff(self.konfig["DIGEIN"], self.konfig["DIGMAXLAENGE"])
        de_zugriff.schreiben_alle(de_daten)
        self.aktualisieren_eingangswerte()

    def setzen_analoge_eingaenge_2(self):
        """Analoge Eingänge setzen - Durchführung"""
        ae_daten = []
        for i in range(self.konfig["ANAMAXLAENGE"]):
            ae_daten = ae_daten + [float(self.AE[i].get())]
        ae_zugriff = dzg.DateiZugriff(self.konfig["ANAEIN"], self.konfig["ANAMAXLAENGE"])
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
        """Modelle starten"""
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

    def funktionsgenerator(self):
        """Funktionsgenerator starten"""
        if self.funktionsgenerator_gui_aktiv() == False:
            self.gen_gui = GeneratorGUI(self)
            

    # Callback-Funktion und Hilfsfunktionen für Datenaufzeichner - Unterrahmen 2

    def datenaufzeichner_gui_aktiv(self):
        """Testen, ob der Datenaufzeichner aktiv ist"""
        if self.dat_gui is None:
            return False
        elif self.dat_gui.dat_gui_aktiv is False:
            return False
        return True

    def datenaufzeichnen(self):
        """Datenaufzeichner starten"""
        if self.datenaufzeichner_gui_aktiv() is False:
            self.dat_gui = DatenaufzeichnerGUI(self.fenster)

    # Callback-Funktion für verschiedene noch nicht realisierte Funktionalitäten - Unterrahmen 2

    def testautomaten(self):
        """Testautomaten starten"""
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
        self.logger.info("SimSTB GUI - Simulator beendet\n\n")
        sys.exit(0)

    # Callback-Funktion für Info-Knopf

    def info(self):
        """SimSTB info"""
        # Prozess-ID ermitteln
        prozess_id =  str(os.getpid())
        # Version ermitteln   
        info_text="SimSTB\n"
        info_text = info_text + "Version: " + ver.SIMSTB_VERSION + "\n"
        info_text = info_text + "Erstellungsdatum: " + ver.SIMSTB_VERSION_DATE + "\n\n"
        info_text = info_text + "Prozess-ID: " + prozess_id + "\n"
        messagebox.showinfo(
            message=info_text, title="SimSTB Information"
        )

class Aktualisierer:
    """Klasse zum Aktualisieren des GUI"""

    def __init__(self, GUI, aktualisierungsvektor):
        """Konstruktor wirft die eigentliche Aktualisieren des GUI an"""
        self.GUI = GUI
        self.aktualisierungsvektor = aktualisierungsvektor
        # Konfigurationsdatei laden
        konfigkonfigmanager = kfg.Konfig() 
        self.konfig = konfigkonfigmanager.konfiguration_bereitstellen()
        #Logging initialisieren und Log-Messages rausschreiben
        self.logger = logging.getLogger(__name__)
        self.logger.info("Aktualisierer gestartet")
        self.logger.debug("Aktualisierungsvektor - " + str(self.aktualisierungsvektor))
        # Periodisches Aktualisieren des GUI anwerfen
        self._lock = threading.Lock()
        self.GUI.fenster.after(int(self.konfig["INTERVALL"])*1000, self.aktualisieren)
        #self.konfig["INTERVALL"]
    
    def aktualisieren(self):
        if self.aktualisierungsvektor["zeit"] == 1:
            self.zeit_aktualisieren()
        if self.aktualisierungsvektor["de"] == 1:
            pass # bisher nicht erforderlich
        if self.aktualisierungsvektor["ae"] == 1:
            self.ae_aktualisieren()
        if self.aktualisierungsvektor["da"] == 1:
            self.da_aktualisieren()
        if self.aktualisierungsvektor["aa"] == 1:
            self.aa_aktualisieren()
        self.GUI.fenster.after(int(self.konfig["INTERVALL"])*1000, self.aktualisieren)

    def zeit_aktualisieren(self):
        """Aktualisieren der Zeit"""
        datum = str(datetime.datetime.now().strftime("%d.%m.%Y"))
        self.GUI.datum.set(datum)
        zeit = str(datetime.datetime.now().strftime("%H:%M:%S"))
        self.GUI.zeit.set(zeit)

    def da_aktualisieren(self):
        """Aktualisieren der digitalen Ausgänge"""
        da_zugriff = dzg.DateiZugriff(self.konfig["DIGAUS"], self.konfig["DIGMAXLAENGE"])
        da_daten = da_zugriff.lesen_alle()
        for i in range(self.konfig["DIGMAXLAENGE"]):
            self.GUI.DA[i].set(da_daten[i])

    def aa_aktualisieren(self):
        """Aktualisieren der analogen Ausgänge"""
        aa_zugriff = dzg.DateiZugriff(self.konfig["ANAAUS"], self.konfig["ANAMAXLAENGE"])
        aa_daten = aa_zugriff.lesen_alle()
        for i in range(self.konfig["ANAMAXLAENGE"]):
            self.GUI.AA[i].set(aa_daten[i])

    def ae_aktualisieren(self):
        """Aktualisieren der analogen Eingänge"""
        ae_zugriff = dzg.DateiZugriff(self.konfig["ANAEIN"], self.konfig["ANAMAXLAENGE"])
        ae_daten = ae_zugriff.lesen_alle()
        for i in range(self.konfig["ANAMAXLAENGE"]):
            self.GUI.AE[i].set(ae_daten[i])

    def aktualisierungsvektor_setzen(self, key, value=1):
        """Setzt einen Eintrag im Aktualisierungsvektor threadsicher"""
        with self._lock:
            if key not in self.aktualisierungsvektor:
                self.logger.error("Unbekannter Schlüssel beim Setzen des Aktualisierungsvektors: " + key)
            else:
                self.aktualisierungsvektor[key] = value
                self.logger.info("Aktualisierungsvektor aktualisiert. Neuer Aktualisierungsvektor: " + str(self.aktualisierungsvektor))

# SimSTB starten
def main():
    GUI()

if __name__ == "__main__":
    main()