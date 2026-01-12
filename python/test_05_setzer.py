""" test_04setzer.py - SimSTB - Komponententest für Modul simstb_setzer
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  15.01.2025
    """

import pytest
import simstb_konfig as kfg
import simstb_dateizugriff as dzg
import simstb_setzer as stz

def test_setzen0_eingaenge():
    """Test der Methode setzen0_eingaenge"""
    daten_dig = ["0"] * kfg.Konfig.DIGMAXLAENGE
    daten_ana = ["0"] * kfg.Konfig.ANAMAXLAENGE
    stz.Setzer().setzen0_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(kfg.Konfig.ANAEIN, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_ausgaenge():
    """Test der Methode setzen0_ausgaenge"""
    daten_dig = ["0"] * kfg.Konfig.DIGMAXLAENGE
    daten_ana = ["0"] * kfg.Konfig.ANAMAXLAENGE
    stz.Setzer().setzen0_ausgaenge()
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGAUS, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(kfg.Konfig.ANAAUS, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_alles():
    """Test der Methode setzen0_alles"""
    daten_dig = ["0"] * kfg.Konfig.DIGMAXLAENGE
    daten_ana = ["0"] * kfg.Konfig.ANAMAXLAENGE
    stz.Setzer().setzen0_alles()
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(kfg.Konfig.ANAEIN, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGAUS, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    daten_ana_neu = dzg.DateiZugriff(kfg.Konfig.ANAAUS, kfg.Konfig.ANAMAXLAENGE).lesen_alle()
    assert daten_ana_neu == daten_ana
    assert daten_dig_neu == daten_dig


def test_setzen0_digitale_eingaenge():
    """Test der Methode setzen0_digitale_eingaenge"""
    daten_dig = ["0"] * kfg.Konfig.DIGMAXLAENGE
    stz.Setzer().setzen0_digitale_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    assert daten_dig_neu == daten_dig


def test_setzen1_digitale_eingaenge():
    """Test der Methode setzen1_digitale_eingaenge"""
    daten_dig = ["1"] * kfg.Konfig.DIGMAXLAENGE
    stz.Setzer().setzen1_digitale_eingaenge()
    daten_dig_neu = dzg.DateiZugriff(kfg.Konfig.DIGEIN, kfg.Konfig.DIGMAXLAENGE).lesen_alle()
    assert daten_dig_neu == daten_dig
