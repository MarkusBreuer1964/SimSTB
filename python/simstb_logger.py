""" SimSTB - Logger
    Das Modul Logger stellt eine Funktion zur Speicherung von Log-Informationen bereit.
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  10.01.2025, 06.02.2025
    """

import os
import datetime
import simstb_konfig as kfg


def msg_loggen(msg):
    """Loggt eine Nachricht in die Logdatei"""
    with open(kfg.Konfig.LOGDATEI, "a", encoding="utf8") as logdatei:
        zeitpunkt = datetime.datetime.now()
        pid =  str(os.getpid())
        zeitpunkt_text = zeitpunkt.strftime("%d.%m.%Y %H:%M:%S")
        logdatei.write(f"{zeitpunkt_text:>20s} - pid: {pid} - {msg}\n")
