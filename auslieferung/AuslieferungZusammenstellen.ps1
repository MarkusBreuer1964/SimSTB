<#

.DESCRIPTION
        Dieses Skript baut die Auslieferungsumgebung im Ordner Sim neu auf.
        Hierzu macht es folgende Arbeiten:
        1. Alte Auslieferungsumgebung löschen
        2. Neue Umgebung aufbauen

.NOTES

	Inhalt:
		Projekt: 			SimSTB
		Thema:				Zusammenstellen einer aktuellen Auslieferungsumgebung

	Autor:
		Name:				Markus Breuer
		Organisaion:		STB

	Datum:
		Erstellt:			27.07.2019
		Letzte Änderung:	

#>

$simSTBordner = "Z:\Sonstiges\Markus\Weiterbildung\Java\workspace\SimSTB"
$auslierungsordner = $simSTBordner + "\auslieferung"
$launch4jc = "C:\Program Files (x86)\Launch4j\launch4jc.exe"

Clear-Host
Set-Location $auslierungsordner

Write-Host "Aktuelle Auslierung von SimSTB zusammenstellen"
Write-Host "----------------------------------------------`n"
write-Host "Alte Auslieferungsumgebung löschen"
if( (Test-Path -Path sim) -eq $true) {                                      # Alte Auslieferungsumgebung löschen
    Remove-Item sim -Recurse -Force 
    }

write-Host "Neue Verzeichnisstruktur aufbauen"
New-Item -Path sim -ItemType directory  | Out-Null                          # Neue Verzeichnisstruktur aufbauen
New-Item -Path sim/bin -ItemType directory   | Out-Null
New-Item -Path sim/header -ItemType directory   | Out-Null
New-Item -Path sim/lib -ItemType directory   | Out-Null
New-Item -Path sim/beispiele -ItemType directory   | Out-Null
New-Item -Path sim/dokumentation -ItemType directory   | Out-Null

write-Host "C/C++ - Schnittstelle kopieren"
$quelldatei = $simSTBordner + "\C\simlib\simlib\simulation.h"               # Header kopieren
$zielodrdner = $auslierungsordner + "\sim\header"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\C\simlib\Debug\simlib.lib"                  # Lib kopieren
$zielodrdner = $auslierungsordner + "\sim\lib"
Copy-Item $quelldatei $zielodrdner

write-Host "Dokumentation und Beispiele kopieren"
$quelldatei = $simSTBordner + "\doc\SimSTB-Benutzerdokumentation.pdf"       # Dokumentation kopieren
$zielodrdner = $auslierungsordner + "\sim\dokumentation"
Copy-Item $quelldatei $zielodrdner
$quelldatei = $simSTBordner + "\C\beispiel\beispiel\beispiel.cpp"           # Beispiele kopieren
$zielodrdner = $auslierungsordner + "\sim\beispiele"
Copy-Item $quelldatei $zielodrdner

write-Host "Wrapper Exe für SimSTBmit Hilfe von launcher4j erzeugen"        # Wrapper Exe erzeugen
$launcherConfig = $auslierungsordner +"\JarExe\config.xml"
&($launch4jc) $launcherConfig  
write-Host "SimSTB Steuerprogramm kopieren"
$quelldatei = $auslierungsordner +"\JarExe\SimSTB.exe"                      # Steuerprogramm kopieren
$zielodrdner = $auslierungsordner + "\sim\bin"
Copy-Item $quelldatei $zielodrdner
