""" test_dateizugriff.py - SimSTB - Komponententest für Modul simstb_dateizugriff
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  12.01.2025, 06.03.2026
    """

import pytest
import sim_basis.simstb_konfig as kfg
import sim_basis.simstb_dateizugriff as dzg

def test_dateizugriff_digitale_eingaenge_1():
    """Test für Datei DIGEIN alles 0"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["0"] * konfig["DIGMAXLAENGE"]
    dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_digitale_eingaenge_2():
    """Test für Datei DIGEIN alles 1"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["1"] * konfig["DIGMAXLAENGE"]
    dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_digitale_ausgaenge():
    """Test für Datei DIGAUS alles 0"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["0"] * konfig["DIGMAXLAENGE"]
    dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_analoge_eingaenge():
    """Test für Datei ANAEIN alles 0"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["0.0"] * konfig["ANAMAXLAENGE"]
    dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_analoge_ausgaenge_1():
    """Test für Datei ANAAUS alles 0"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["0.0"] * konfig["ANAMAXLAENGE"]
    dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_analoge_ausgaenge_2():
    """Test für Datei ANAAUS alles 1.0"""
    # Testdaten
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten = ["1.0"] * konfig["ANAMAXLAENGE"]
    dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_neu == daten