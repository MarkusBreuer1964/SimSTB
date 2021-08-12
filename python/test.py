from tkinter import *     
from tkinter import ttk

""""
class Modell_1:
 
    def __init__(self, hauptfenster):
        self.fenster = hauptfenster
        self.fenster.iconbitmap("simstb.ico")

        img = PhotoImage(file="led_grau_transparent.png")      
        label1 = ttk.Label(self.fenster, image=img)      
        label1.grid(column=1, row=1) 
        


def hauptprogramm():
    fenster = Tk(className="SimSTB - Modell 1 - LED-Anzeige")  # Rohes Fenster erstellen
    TS = Modell_1(fenster)  # Oberfläche Simulator aufbauen
    fenster.mainloop()  # Hauptschleife starten

hauptprogramm()

"""

class Modell_1:
    def __init__(self):

        fenster = Tk(className="SimSTB - Modell 1 - LED-Anzeige")  # Rohes Fenster erstellen
        fenster.iconbitmap("simstb.ico")

        img = PhotoImage(file="led_blau_transparent.png") 
        for i in range(8):   
            label1 = ttk.Label(fenster, image=img)      
            label1.grid(column=i+1, row=1) 

        fenster.mainloop()  # Hauptschleife starten

Modell_1()  # Hauptschleife starten
