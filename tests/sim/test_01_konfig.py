""" test_konfig.py - SimSTB - Komponententest für Modul simstb_konfig
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  12.01.2025, 05.03.2026
    """

import pytest
import sim_basis.simstb_konfig as kfg
from pathlib import Path

def test_konfig_klasse():
    konfigmanager = kfg.Konfig()
    konfig = konfigmanager.konfiguration_bereitstellen()
    assert konfig["LOGDATEI"] == "./simstb.log"
    assert konfig["DIGMAXLAENGE"] == 16
    assert konfig["ANAMAXLAENGE"] == 8
    assert konfig["SIGNALFORMEN"] == ["Zufall", "Sinus", "Rechteck", "Dreieck"]
    assert konfig["AKTIVE_BACKGROUND"] == "#90EE90" # LightGreen
    assert konfig["HAUPT_BACKGROUND"] == "#b7d7e8" # LightBlue
    assert konfig["BLOCK_BACKGROUND"] == "#cfe0e8" # LightCyan
    assert konfig["MODELL_DATEI"] == "./modelle.json"
