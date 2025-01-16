""" test_konfig.py - SimSTB - Komponententest für Modul simstb_konfig
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  12.01.2025
    """

import pytest
import simstb_konfig as kfg

def test_konfig_klasse():
    assert kfg.Konfig.DIGMAXLAENGE == 16
    assert kfg.Konfig.ANAMAXLAENGE == 8
    assert kfg.Konfig.ANAAUS == "C:\\Sim\\anaaus.txt"
    assert kfg.Konfig.ANAEIN == "C:\\Sim\\anaein.txt"
    assert kfg.Konfig.DIGAUS == "C:\\Sim\\digaus.txt"
    assert kfg.Konfig.DIGEIN == "C:\\Sim\\digein.txt"
    assert kfg.Konfig.SIGNALFORMEN == ["Zufall", "Sinus", "Rechteck", "Dreieck"]
    assert kfg.Konfig.AKTIVE_BACKGROUND == "#90EE90"
    assert kfg.Konfig.HAUPT_BACKGROUND == "#b7d7e8"
    assert kfg.Konfig.BLOCK_BACKGROUND == "#cfe0e8"
    assert kfg.Konfig.MODELL_DATEI == "modelle.json"
    assert kfg.Konfig.LOGDATEI == "C:\\Sim\\simstb.log"
