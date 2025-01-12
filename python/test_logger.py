""" test_dateizugriff.py - SimSTB - Komponententest für Modul simstb_dateizugriff
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  12.01.2025
    """

import pytest
import simstb_logger as log

def test_dateizugriff_klasse():
    msg = "Testnachricht"
    assert log.msg_loggen(msg) == None
