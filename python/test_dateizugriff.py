""" test_dateizugriff.py - SimSTB - Komponententest für Modul simstb_dateizugriff
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  12.01.2025
    """

import pytest
import simstb_konfig as kfg
import simstb_dateizugriff as dzg

def test_dateizugriff_digitale_eingaenge():
    """Test für Datei DIGEIN"""
    # Testdaten
    daten = ["0"] * kfg.Konfig.DIGMAXLAENGE
    dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_digitale_ausgaenge():
    """Test für Datei DIGAUS"""
    # Testdaten
    daten = ["0"] * kfg.Konfig.DIGMAXLAENGE
    dzg.DateiZugriff(kfg.Konfig.DIGAUS, kfg.Konfig.DIGMAXLAENGE).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(kfg.Konfig.DIGAUS, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_analoge_eingaenge():
    """Test für Datei ANAEIN"""
    # Testdaten
    daten = ["0.0"] * kfg.Konfig.ANAMAXLAENGE
    dzg.DateiZugriff(kfg.Konfig.ANAEIN, kfg.Konfig.ANAMAXLAENGE).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(kfg.Konfig.ANAEIN, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_neu == daten

def test_dateizugriff_analoge_ausgaenge():
    """Test für Datei ANAAUS"""
    # Testdaten
    daten = ["0.0"] * kfg.Konfig.ANAMAXLAENGE
    dzg.DateiZugriff(kfg.Konfig.ANAAUS, kfg.Konfig.ANAMAXLAENGE).schreiben_alle(daten)
    daten_neu = dzg.DateiZugriff(kfg.Konfig.ANAAUS, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_neu == daten