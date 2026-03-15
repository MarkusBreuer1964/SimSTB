""" test_04simulator.py - SimSTB - Komponententest für Modul simulator.py
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  15.01.2025
    """

import pytest
import sim_schnittstelle.simulator as sim
import sim_basis.simstb_dateizugriff as dzg
import sim_basis.simstb_konfig as kfg

def test_dig_ein():
    """Test der Schnittstelle für digitale Eingänge DIGEIN"""
    # Testdaten erzeugen und in die Datei DIGEIN schreiben
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_dig = ["1"] * konfig["DIGMAXLAENGE"]
    daten_dig[7] = 0
    dzg.DateiZugriff(konfig["DIGEIN"], konfig["DIGMAXLAENGE"]).schreiben_alle(daten_dig)
    # Testen lesen digitaler Eingang
    d_0 = sim.dig_ein(0)
    d_7 = sim.dig_ein(7)
    d_15 = sim.dig_ein(15)
    # Ergebnisse prüfen
    assert d_0 == 1
    assert d_7 == 0
    assert d_15 == 1

def test_dig_aus():
    """Test der digitalem Schnittstellenfunktionen"""
    # Testen schreiben digitaler Ausgang
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    sim.dig_aus(0, 0)
    sim.dig_aus(7, 1)
    sim.dig_aus(15, 0)
    # Daten aus Datei zurücklesen
    daten_dig = dzg.DateiZugriff(konfig["DIGAUS"], konfig["DIGMAXLAENGE"]).lesen_alle()
    # Ergebnisse prüfen
    assert int(daten_dig[0]) == 0
    assert int(daten_dig[7]) == 1
    assert int(daten_dig[15]) == 0

def test_ana_ein():
    """Test der Schnittstellenfunktionen für analoge Eingänge ANAEIN"""
    # Testen erzeugen und in Datei ANAEIN schreiben
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    daten_ana = ["0.0"] * konfig["ANAMAXLAENGE"]
    daten_ana[3] = 123.456
    dzg.DateiZugriff(konfig["ANAEIN"], konfig["ANAMAXLAENGE"]).schreiben_alle(daten_ana)
    # Testen lesen analoger Eingang
    a_0 = sim.ana_ein(0)
    a_3 = sim.ana_ein(3)
    a_7 = sim.ana_ein(7)
    # Ergebnisse prüfen
    assert a_0 == 0.0
    assert a_3 == 123.456
    assert a_7 == 0.0

def test_ana_aus():
    """Test der analogen Schnittstellenfunktionen"""
    # Testen schreiben analoger Ausgang
    konfigkonfigmanager = kfg.Konfig() 
    konfig = konfigkonfigmanager.konfiguration_bereitstellen()
    sim.ana_aus(0, -17.7)
    sim.ana_aus(3, 654.321)
    sim.ana_aus(7, 0.0)
    # Daten aus Datei zurücklesen
    daten_ana = dzg.DateiZugriff(konfig["ANAAUS"], konfig["ANAMAXLAENGE"]).lesen_alle()
    # Ergebnisse prüfen
    assert float(daten_ana[0]) == -17.7
    assert float(daten_ana[3]) == 654.321
    assert float(daten_ana[7]) == 0.0