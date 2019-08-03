<#

.DESCRIPTION
        Dieses Skript baut die Auslieferungsumgebung im Ordner Sim neu auf.
        Hierzu macht es folgende Arbeiten:
        1. Alte Auslieferungsumgebung löschen
        2 Neue Umgebung aufbauen
        3.a Austauschdateien kopieren
        3.b C/C++ - Schnittstelle kopieren
        3.c Dokumentation und Beispiele kopieren
        4.a Ausführbare-Jar-Datei SimSTB.jar erzeugen
        4.b Wrapper-Exe SimSTB.exe erzeugen
        4.c SimSTB.exe kopieren
        4.d Temporäre Zwischendateien weglöschen
        4.e JRE Bundle kopieren
        5. Zip-Datei erzeugen
        6. Lokale Laufzeitumgebung aktualisieren

.NOTES

	Inhalt:
		Projekt: 			SimSTB
		Thema:				Zusammenstellen einer aktuellen Auslieferungsumgebung

	Autor:
		Name:				Markus Breuer
		Organisaion:		STB

	Datum:
		Erstellt:			27.07.2019
		Letzte Änderung:	29.07.2019

#>

$simSTBordner = "Z:\Sonstiges\Markus\Weiterbildung\Java\workspace\SimSTB"
$auslierungsordner = $simSTBordner + "\auslieferung"
$launch4jc = "C:\Program Files (x86)\Launch4j\launch4jc.exe"
$laufzeitUmgebung = "C:\Sim"

Clear-Host
Set-Location $auslierungsordner

Write-Host "Aktuelle Auslierung von SimSTB zusammenstellen"
Write-Host "----------------------------------------------`n"
write-Host "1. Alte Auslieferungsumgebung löschen"
if( (Test-Path -Path sim) -eq $true) {                                      # Alte Auslieferungsumgebung löschen
    Remove-Item sim -Recurse -Force 
    }
Write-Host ""

write-Host "2.a Neue Verzeichnisstruktur aufbauen"
New-Item -Path sim -ItemType directory  | Out-Null                          # Neue Verzeichnisstruktur aufbauen
New-Item -Path sim/bin -ItemType directory   | Out-Null
New-Item -Path sim/header -ItemType directory   | Out-Null
New-Item -Path sim/lib -ItemType directory   | Out-Null
New-Item -Path sim/beispiele -ItemType directory   | Out-Null
New-Item -Path sim/dokumentation -ItemType directory   | Out-Null
Write-Host ""

write-Host "3.a Austauschdateien kopieren"                                  # Austauschdateien kopieren
$quelldateien = $auslierungsordner + "\austauschdateien\*"
$zielodrdner = $auslierungsordner + "\sim\"
Copy-Item $quelldateien $zielodrdner
Write-Host ""

write-Host "3.b C/C++ - Schnittstelle kopieren"
$quelldatei = $simSTBordner + "\cprojekte\simlib\simlib\simulation.h"       # Header kopieren
$zielodrdner = $auslierungsordner + "\sim\header"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\cprojekte\simlib\Debug\simlib.lib"          # Lib kopieren
$zielodrdner = $auslierungsordner + "\sim\lib"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\cprojekte\simlib2019.lib"                   # Workaround-Lib kopieren
$zielodrdner = $auslierungsordner + "\sim\lib"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

write-Host "3.c Dokumentation und Beispiele kopieren"
$quelldatei = $simSTBordner + "\doc\SimSTB-Benutzerdokumentation.pdf"       # Dokumentation kopieren
$zielodrdner = $auslierungsordner + "\sim\dokumentation"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\cprojekte\beispiel\beispiel\beispiel.cpp"   # Beispiele kopieren
$zielodrdner = $auslierungsordner + "\sim\beispiele"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\README.md"                                  # README und LICENSE kopieren
$zielodrdner = $auslierungsordner + "\sim"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\LICENSE.txt"                                
$zielodrdner = $auslierungsordner + "\sim"
Copy-Item $quelldatei $zielodrdner
Write-Host ""

write-Host "4.a Ausführbare-Jar-Datei SimSTB.jar erzeugen"                  # Ausführbare Jar-Datei SimSTB.jar erzeugen
ant -buildfile .\JarExe\exportjar.xml
Write-Host ""
write-Host "4.b Wrapper-Exe SimSTB.exe erzeugen"                            # Wrapper Exe erzeugen
$launcherConfig = $auslierungsordner +"\JarExe\config.xml"
&($launch4jc) $launcherConfig  
Write-Host ""
write-Host "4.c SimSTB.exe kopieren"
$quelldatei = $auslierungsordner +"\JarExe\SimSTB.exe"                      # Steuerprogramm kopieren
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
Write-Host ""
write-Host "4.d Temporäre Zwischendateien weglöschen"                       # Temporäre Zwischendateien weglöschen
$jarexeordner = $auslierungsordner + "\JarExe"
Set-Location $jarexeordner
Remove-Item *.exe
Remove-Item *.jar
Set-Location $auslierungsordner
write-Host "4.e JRE Bundle kopieren"                                        # JRE Bundle kopieren
$quelldatei = $auslierungsordner +"\JarExe\bundlejre"                      
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner -Recurse
Write-Host ""

write-Host "5. Zip-Datei erzeugen"
if( (Test-Path -Path sim.zip) -eq $true) {                                      # Zip-Datei erzeugen
    Remove-Item sim.zip  
    }
Compress-Archive -Path sim/* -DestinationPath sim.zip
Write-Host ""

$titel = "Laufzeitumgebung?"
$meldung = "Laufzeitumgebung aktualisieren?"
$ja = New-Object System.Management.Automation.Host.ChoiceDescription "&Ja", "Ja"
$nein = New-Object System.Management.Automation.Host.ChoiceDescription "&Nein", "Nein"
$optionen = [System.Management.Automation.Host.ChoiceDescription[]]($ja, $nein)
$auswahl=$host.ui.PromptForChoice($titel, $meldung, $optionen, 1)
if( $auswahl -eq 0) {
    write-Host "6. Laufzeitumgebung aktualisieren"
    if( (Test-Path -Path $laufzeitUmgebung) -eq $true) {                        # Alte Laufzeitumgebung löschen
        Remove-Item $laufzeitUmgebung -Recurse -Force 
        }
    New-Item -Path $laufzeitUmgebung -ItemType directory   | Out-Null           # Neu Laufzeitumgebung kopieren
    $quelldateien = $auslierungsordner + "\sim\*"
    Copy-Item $quelldateien $laufzeitUmgebung -Recurse
    }