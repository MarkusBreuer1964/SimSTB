""" test_04setzer.py - SimSTB - Komponententest für Modul simstb_setzer
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  15.01.2025, 15.03.2026
    """

import pytest
import sim_werkzeuge.simstb_setzer as stz
import sim_basis.simstb_dateizugriff as dzg
import sim_basis.simstb_konfig as kfg

def test_setzen0_eingaenge():
    """Test der Methode setzen0_eingaenge"""
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["0"] * konfig["DIGMAXLAENGE"]
    daten_ana = ["0"] * konfig["ANAMAXLAENGE"]
    stz.Setzer().setzen0_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_ausgaenge():
    """Test der Methode setzen0_ausgaenge"""
    konfigkonfigmanager = kfg.Konfig()
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["0"] * konfig["DIGMAXLAENGE"]
    daten_ana = ["0"] * konfig["ANAMAXLAENGE"]
    stz.Setzer().setzen0_ausgaenge()
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"]).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_alles():
    """Test der Methode setzen0_alles"""
    konfigkonfigmanager = kfg.Konfig()
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["0"] * konfig["DIGMAXLAENGE"]
    daten_ana = ["0"] * konfig["ANAMAXLAENGE"]
    stz.Setzer().setzen0_alles()
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"]).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_digitale_eingaenge():
    """Test der Methode setzen0_digitale_eingaenge"""
    konfigkonfigmanager = kfg.Konfig()
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["0"] * konfig["DIGMAXLAENGE"]
    stz.Setzer().setzen0_digitale_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    assert daten_dig_neu == daten_dig


def test_setzen1_digitale_eingaenge():
    """Test der Methode setzen1_digitale_eingaenge"""
    konfigkonfigmanager = kfg.Konfig()
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["1"] * konfig["DIGMAXLAENGE"]
    stz.Setzer().setzen1_digitale_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).lesen_alle()
    assert daten_dig_neu == daten_dig
