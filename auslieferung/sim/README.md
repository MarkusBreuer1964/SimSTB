# SimSTB - Simulationsumgebung für digitale und analoge Ein- und Ausgänge 

Die Simulationsumgebung SimSTB ist für die Ausbildung im Bereich C/C++-Programmierung geeignet. Sie ist insbesondere
für den Unterricht bei (elektro)technischen Schülern gedacht.

Oft muss ein Programm nicht nur über die Konsole oder eine graphische Oberfläche mit dem Benutzer kommunizieren, 
sondern auch über analoge und digitale Schnittstellen mit einem technischen System.
Die Simulationsumgebung SimSTB erlaubt es, dies für Schulungszwecke auch ohne zusätzliche Hardware 
mittels Simulation durchzuführen.

Durch das Einbinden der Bibliothek simlib stehen dem Schüler vier einfach zu nutzende Funktionen für die digitale und
analoge Ein- und Ausgabe zur Verfügung. Die analogen und digitalen Werte können über eine graphische Oberfläche
bequem überwacht und gesetzt werden.


![Einsatzkontext](/bilder/Einsatzkontext.png)


## Requirements

- Java Runtime Environment (JRE); für den Fall, das diese nicht vorhanden ist, ist eine Bundle-JRE vorhanden,
  so dass keine Installation der JRE notwendig ist.
- Die Library ist für das an der Schule im Einsatz befindliche VS C++ 2010 ausgelegt. Eine Library für VS C++ 2019
  wurde beigefügt.

## Installation

1. Kopieren Sie das bereitgestellte Simulationsverzeichnis (in GitHub /auslieferung/sim) 
samt Unterverzeichnissen nach „C:\“. Solange Sie nur die Simulationsumgebung nutzen wollen 
und keine Modifikationen an deren Quellcode vornehmen wollen brauchen Sie keine weiteren Dateien. 
2. Kontrollieren Sie, ob folgende Verzeichnis-Struktur und Dateien vorhanden sind.

```

C:
└── Sim
    ├── anaaus.txt
    ├── anaein.txt
    ├── digaus.txt
    ├── digein.txt
    ├── LICENSE.txt
    ├── README.md
    ├── beispiele
    │   └── beispiel.cpp
    ├── bin
    │   └── SimSTB.exe
    │       └── bundlejre ...
    ├── dokumentation
    │   └── SimSTB-Benutzerdokumentation.pdf
    ├── header
    │   └── simulation.h
    └── lib
         └── simlib.lib

```

## Usage

### 1. Simulations Steuerung und Monitor

Mit Hilfe des Programms SimSTB.exe können Sie digitalen und analogen Ein- und Ausgänge überwachen 
und die Eingänge setzen. Die Werte werden im Sekundentakt aktualisiert. Starten können Sie das Programm 
über einen einfachen Doppelklick auf die Exe-Datei.

![SimSTB Benutzeroberfläche](/bilder/SimSTB-GUI.png)

### 2. Erstellung eigener Programme für die Simulationsumgebung SimSTB

Mit Hilfe der vier Funktionen:

- digEin
- digAus
- anaEin
- anaAus

können Sie eigene C++-Programme schreiben. Sie können deren Ausgaben mit der Simulationsumgebung 
überwachen und die Eingänge setzen. 

Um die vier Funktionen zu nutzen, müssen Sie die Header-Datei simulation.h 
in Ihren Quellcode inkludieren und die Bibliothek simlib.lib in Ihr Projekt einbinden.

In der Datei SimSTB-Benutzerdokumentation.pdf finden Sie eine ausführrliche Beschreibung.


## Contribute

Es gibt mehrere Möglichkeiten zum Projet SimSTB beizutragen:
- Benutzen Sie privat oder im Unterrichtseinsatz SimSTB und geben Sie Erfahrungen zurück. 
- Die Erstellung einer Bibliothek, die völlig unabhängig von der erstellenden Entwicklungsumgebung
  und deren Version ist, ist noch nicht optimal gelöst.


## Documentation

- README - Erster Überblick über das Projekt SimSTB; diese lesen Sie gerade
- SimSTB-Benutzerdokumentation - Benutzerdokumentation; beschreibt wie Sie die Simulationsumgebung 
                               installieren und benutzen; wenn Sie die Simulationsumgebung nur nutzen
                               und keine eigenen Änderungen vornehmen wollen, das einzige, was Sie lesen sollten.
- SimSTB-Plannung - Erweiterungswünsche, Restrukturierungsideen und Versionsübersicht
- SimSTB-Intern - Hinweise zur Architektur und zum Design der Simulationsumgebung; Vorgehensweise bei dem Projekt.


## License

[MIT](LICENSE.txt) © [Markus Breuer].
