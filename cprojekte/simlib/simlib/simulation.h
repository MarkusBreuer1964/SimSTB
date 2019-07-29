//
//	Inhalt:
//		Projekt: 			SimMonitor
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Zentrale Header-Datei der C/C++-Schnittstelle
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			15.10.2018
//		Letzte Änderung:	26.07.2019
//

#define digEinDateiname "C:\\Sim\\digein.txt"
#define digAusDateiname "C:\\Sim\\digaus.txt"
#define anaEinDateiname "C:\\Sim\\anaein.txt"
#define anaAusDateiname "C:\\Sim\\anaaus.txt"

const int DIGMAXLAENGE = 16;
const int ANAMAXLAENGE = 8;

bool digEin( int id);
void digAus( int id, bool wert);

double anaEin( int id);
void anaAus( int id, double wert);

