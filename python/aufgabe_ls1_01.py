""" aufgabe_ls1_01.py - Realisierung der Klasse Schüler
    Name, Organisaion:          Markus Breuer, BK-GuT
    Erstellt, Letzte Änderung:  11.06.2021, 17.07.2023
    """


class Schueler:
    """Definition der Klasse Schüler"""

    def __init__(self, n, g, a):
        """Konstruktor der Klasse Schüler"""
        print(n, ": Ich werde eingeschult")
        self.name = n
        self.groesse = g
        self.alter = a
        self.klasse = 1

    def lernen(self):
        """Methode lernen der Klasse Schüler"""
        print(self.name, ": Ich lerne")

    def chillen(self):
        """Methode chillen der Klasse Schüler"""
        print(self.name, ": Ich chille")

    def zocken(self):
        """Methode zocken der Klasse Schüler"""
        print(self.name, ": Ich zocke")

    def saufen(self):
        """Methode saufen der Klasse Schüler"""
        print(self.name, ": Ich saufe")

    def versetzen(self):
        """Methode versetzen der Klasse Schüler"""
        print(self.name, ": Ich werde versetzt")
        self.klasse = self.klasse + 1

    def vorstellen(self):
        """Methode vorstellen der Klasse Schüler"""
        print("")
        print("==================================")
        print("Name:", self.name)
        print("Größe:", self.groesse)
        print("Alter:", self.alter)
        print("Klasse:", self.klasse)
        print("==================================")
        print("")


def testen():
    """Hauptprogramm"""
    jan = Schueler("Jan", 120, 6)
    maximilian = Schueler("Max", 130, 6)
    mr_bizeps = Schueler("Mr. Bizeps", 125, 7)
    doerte = Schueler("Dörte", 110, 6)
    doerte.lernen()
    maximilian.zocken()
    mr_bizeps.saufen()
    jan.versetzen()
    jan.vorstellen()


testen()
