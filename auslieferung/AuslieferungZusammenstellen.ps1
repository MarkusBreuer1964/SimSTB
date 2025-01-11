<#

.DESCRIPTION
        Dieses Skript baut die Auslieferungsumgebung im Ordner Sim neu auf.
        Hierzu macht es folgende Arbeiten:
        1. Alte Auslieferungsumgebung löschen
        2 Neue Umgebung aufbauen
        3.a Austauschdateien kopieren
        3.b1 C/C++ - Schnittstelle kopieren
        3.b2 Python - Schnittstelle kopieren
        3.c Dokumentation und Beispiele kopieren
        4.a simstb_gui.exe erzeugen
        4.b simstb_gui.exe kopieren
        4.c Temporäre Zwischendateien weglöschen
        4.d Benötigte Bild-Dateien kopieren
        4.e Modell-Konfigurations-Datei kopieren
        5. Lokale Laufzeitumgebung aktualisieren

.NOTES

	Inhalt:
		Projekt: 			SimSTB
		Thema:				Zusammenstellen einer aktuellen Auslieferungsumgebung

	Autor:
		Name:				Markus Breuer
		Organisaion:		STMB

	Datum:
		Erstellt:			27.07.2019
		Letzte Änderung:	21.06.2023

#>

$simSTBordner = "Z:\Sonstiges\Markus\Weiterbildung\Projekt - SimSTB"
$auslierungsordner = $simSTBordner + "\auslieferung"
$pythonordner = $simSTBordner + "\python"
$laufzeitUmgebung = "C:\Sim"

Clear-Host
Set-Location $auslierungsordner

Write-Host "Aktuelle Auslierung von SimSTB zusammenstellen"
Write-Host "----------------------------------------------`n"
write-Host "1. Alte Auslieferungsumgebung löschen"
if ( (Test-Path -Path sim) -eq $true) {
    # Alte Auslieferungsumgebung löschen
    Remove-Item sim -Recurse -Force 
}
Write-Host ""

write-Host "2.a Neue Verzeichnisstruktur aufbauen"
New-Item -Path sim -ItemType directory  | Out-Null                          # Neue Verzeichnisstruktur aufbauen
New-Item -Path sim/bin -ItemType directory   | Out-Null
New-Item -Path sim/header -ItemType directory   | Out-Null
New-Item -Path sim/lib -ItemType directory   | Out-Null
New-Item -Path sim/python -ItemType directory   | Out-Null
New-Item -Path sim/beispiele -ItemType directory   | Out-Null
New-Item -Path sim/dokumentation -ItemType directory   | Out-Null
Write-Host ""

write-Host "3.a Austauschdateien kopieren"                                  # Austauschdateien kopieren
$quelldateien = $auslierungsordner + "\austauschdateien\*"
$zielodrdner = $auslierungsordner + "\sim\"
Copy-Item $quelldateien $zielodrdner
Write-Host ""

write-Host "3.b1 C/C++ - Schnittstelle kopieren"
$quelldatei = $simSTBordner + "\cprojekte\simlib\simlib\simulation.h"       # Header kopieren
$zielodrdner = $auslierungsordner + "\sim\header"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\cprojekte\simlib\Debug\simlib.lib"          # Lib kopieren
$zielodrdner = $auslierungsordner + "\sim\lib"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

write-Host "3.b2 Python - Schnittstelle kopieren"
$quelldatei = $pythonordner + "\simulator.py"       
$zielodrdner = $auslierungsordner + "\sim\python"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $pythonordner + "\simstb_dateizugriff.py"       
$zielodrdner = $auslierungsordner + "\sim\python"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $pythonordner + "\simstb_konfig.py"       
$zielodrdner = $auslierungsordner + "\sim\python"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

write-Host "3.c Dokumentation und Beispiele kopieren"
$quelldatei = $simSTBordner + "\docs\SimSTB-Benutzerdokumentation.pdf"       # Dokumentation kopieren
$zielodrdner = $auslierungsordner + "\sim\dokumentation"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\cprojekte\beispiel\beispiel\beispiel.cpp"   # Beispiele kopieren
$zielodrdner = $auslierungsordner + "\sim\beispiele"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $pythonordner + "\beispiel.py"   
$zielodrdner = $auslierungsordner + "\sim\beispiele"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\README.md"                                  # README und LICENSE kopieren
$zielodrdner = $auslierungsordner + "\sim"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\LICENSE.txt"                                
$zielodrdner = $auslierungsordner + "\sim"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

write-Host "4.a SimSTB.exe und Modelle erzeugen"      #  Exe und Modelle erzeugen
Set-Location $pythonordner
pyinstaller --clean --onefile  --icon simstb.ico --window simstb_gui.py
pyinstaller --clean --onefile  --icon simstb.ico --window simstb_modell_1.py
pyinstaller --clean --onefile  --icon simstb.ico --window simstb_modell_2.py
Write-Host ""
write-Host "4.b SimSTB.exe und Modelle kopieren"                   # Exen und Modelle in bin-Ordner kopieren
$quelldatei = $pythonordner + "\dist\simstb_gui.exe"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $pythonordner + "\dist\simstb_modell_1.exe"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $pythonordner + "\dist\simstb_modell_2.exe"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
Write-Host ""
write-Host "4.c Temporäre Zwischendateien weglöschen"                       # Temporäre Zwischendateien weglöschen
Remove-Item dist -Recurse
Remove-Item build -Recurse
Write-Host ""
Set-Location $auslierungsordner
write-Host "4.d Benötigte Bild-Dateien kopieren"                            # Benötigte Bild-Dateien in bin-Ordner kopieren
$quelldatei = $simSTBordner + "\python\simstb.ico"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\python\*.png"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\python\*.gif"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
Write-Host ""
write-Host "4.e Modell-Konfigurations-Datei kopieren"                            # Modell-Konfigurations-Datei kopieren in bin-Ordner kopieren
$quelldatei = $simSTBordner + "\python\modelle.json"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

$titel = "Laufzeitumgebung?"
$meldung = "Laufzeitumgebung aktualisieren?"
$ja = New-Object System.Management.Automation.Host.ChoiceDescription "&Ja", "Ja"
$nein = New-Object System.Management.Automation.Host.ChoiceDescription "&Nein", "Nein"
$optionen = [System.Management.Automation.Host.ChoiceDescription[]]($ja, $nein)
$auswahl = $host.ui.PromptForChoice($titel, $meldung, $optionen, 1)
if ( $auswahl -eq 0) {
    write-Host "5. Laufzeitumgebung aktualisieren"
    if ( (Test-Path -Path $laufzeitUmgebung) -eq $true) {
        # Alte Laufzeitumgebung löschen
        Remove-Item $laufzeitUmgebung -Recurse -Force 
    }
    New-Item -Path $laufzeitUmgebung -ItemType directory   | Out-Null           # Neu Laufzeitumgebung kopieren
    $quelldateien = $auslierungsordner + "\sim\*"
    Copy-Item $quelldateien $laufzeitUmgebung -Recurse
}