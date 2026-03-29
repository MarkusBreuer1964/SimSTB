""" systemtest_01.py - SimSTB - Systemtest ffür Laufzeitumgebung
    Name, Organisaion:          Markus Breuer, STMB
    Erstellt, Letzte Änderung:  26.03.2026
    """

import pytest
import subprocess

def test_simstb_cli_version():
    """Prüft, ob simstb_cli --version korrekt ausgeführt wird."""
    
    
    result = subprocess.run(
        ["simstb_cli", "--version"],
        capture_output=True, 
        text=True            
    )   
    # Ergebnis prüfen 
    assert result.returncode == 0
    output = result.stdout.strip()  
    assert "version" in output.lower()



def test_simstb_cli_hilfe():
    """Prüft, ob simstb_cli --hilfe korrekt ausgeführt wird."""
    
    # Prozess ausführen
    result = subprocess.run(
        ["simstb_cli", "--hilfe"],
        capture_output=True,
        text=True
    )
    # Ergebnis prüfen 
    assert result.returncode == 0
    output = result.stdout.strip()
    assert str("CLI-Werkzeug für Projekt SimSTB").lower() in output.lower()


