//
//	Inhalt:
//		Projekt: 			SimMonitor
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Basisfunktionen und Zugriffsfunktionen auf die Austauschdateien
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			15.10.2018
//		Letzte Änderung:	26.07.2019
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <Windows.h>
#include <locale>
#include <string>
#include "simintern.h"

using namespace std;

static void dateiOeffnenEingabeStrom( ifstream *datei, string dateiname);
static void dateiOeffnenAusgabeStrom( ofstream *datei, string dateiname);

//
//	Basisfunktionen zur Simulation digitaler und analoger Ein- und Ausgänge
//

bool digEin( int id)
{
	locale::global(locale("German_germany"));															// Zeichensatz deutsch
	return digEinLesen( id);
}

void digAus( int id, bool wert)
{
	locale::global(locale("German_germany"));															// Zeichensatz deutsch
	digAusSchreiben( id, wert);
	return;
}

double anaEin( int id)
{
	locale::global(locale("German_germany"));															// Zeichensatz deutsch
	return anaEinLesen( id);
}

void anaAus( int id, double wert)
{
	locale::global(locale("German_germany"));															// Zeichensatz deutsch
	anaAusSchreiben( id, wert);
	return;
}


//
//	Hilfsfunktionen zum Datei öffnen
//

static void dateiOeffnenEingabeStrom( ifstream *datei, string dateiname)	// Hilfsfunktion zum Datei öffnen einer Eingabedatei
{
	datei->open( dateiname);												
    if (datei->fail())
    {
        cout << "Fehler beim Öffnen der Datei: " << dateiname << endl;
		system( "PAUSE");
        exit( 1);
    }
}

static void dateiOeffnenAusgabeStrom( ofstream *datei, string dateiname)	// Hilfsfunktion zum Datei öffnen einer Eingabedatei
{
	datei->open( dateiname);								
    if (datei->fail())
    {
        cout << "Fehler beim Öffnen der Datei: " << dateiname << endl;
		system( "PAUSE");
        exit( 1);
    }
}


//
//	Funktionen zur Handhabung der digitalen Eingabe
//

bool digEinLesen( int id)
{
	bool wert;
	bool eingabeVektor[ DIGMAXLAENGE];
 	
	digEinLesen( eingabeVektor);								// Eingabevektor holen
	wert = eingabeVektor[ id];                                  // Rückgabewert extrahieren
	return wert;
}

void digEinLesen( bool eingabeVektor[])
{
	ifstream datei;
	dateiOeffnenEingabeStrom( &datei, digEinDateiname);

    for( int i = 0; i < DIGMAXLAENGE; i++)							// Digitalen Eingabevektor lesen
    {		
		eingabeVektor[ i] = 0;
 		datei >> eingabeVektor[ i];
    }
	
	datei.close( );	
	return;
}

void digEinSchreiben( int id, bool wert)
{
	bool eingabeVektor[ DIGMAXLAENGE];
	ofstream eingabedatei;

	digEinLesen( eingabeVektor);

	eingabeVektor[ id] = wert;                                  // Wert setzen

	dateiOeffnenAusgabeStrom( &eingabedatei, digEinDateiname);

    for( int i = 0; i < DIGMAXLAENGE; i++)                        // Digitalen Eingabevektor zurückschreiben
    {
        eingabedatei << eingabeVektor[ i] << endl;
    }

    eingabedatei.close();

	return;
}

void digEinSchreiben( bool eingabeVektor[])
{
	ofstream eingabedatei;

	dateiOeffnenAusgabeStrom( &eingabedatei, digEinDateiname);

    for( int i = 0; i < DIGMAXLAENGE; i++)                        // Digitalen Eingabevektor zurückschreiben
    {
        eingabedatei << eingabeVektor[ i] << endl;
    }

    eingabedatei.close();

	return;
}

//
//	Funktionen zur Handhabung der digitalen Ausgabe
//

bool digAusLesen( int id)
{
	bool wert;
	bool ausgabeVektor[ DIGMAXLAENGE];

	digAusLesen( ausgabeVektor);								// Ausgabevektor holen
	wert = ausgabeVektor[ id];                                  // Rückgabewert extrahieren
	return wert;
}

void digAusLesen( bool ausgabeVektor[])
{
	ifstream datei;
	dateiOeffnenEingabeStrom( &datei, digAusDateiname);

    for( int i = 0; i < DIGMAXLAENGE; i++)					 	// Digitalen Ausgabevektor lesen
    {		
		ausgabeVektor[ i] = 0;
 		datei >> ausgabeVektor[ i];
    }
	
	datei.close( );	

	return;
}

void digAusSchreiben( int id, bool wert)
{
	bool ausgabeVektor[ DIGMAXLAENGE];
	ofstream ausgabedatei;

	digAusLesen( ausgabeVektor);

	ausgabeVektor[ id] = wert;                                  // Wert setzen

	dateiOeffnenAusgabeStrom( &ausgabedatei, digAusDateiname);
    for( int i = 0; i < DIGMAXLAENGE; i++)                       // Digitalen Ausgabevektor zurückschreiben
    {
        ausgabedatei << ausgabeVektor[ i] << endl;
    }
    ausgabedatei.close();

	return;
}


//
//	Funktionen zur Handhabung der analogen Eingabe
//

double anaEinLesen( int id)
{
	double wert;
	double eingabeVektor[ ANAMAXLAENGE];

	anaEinLesen( eingabeVektor);
	wert = eingabeVektor[ id];                                  // Rückgabewert extrahieren
	return wert;
}

void anaEinLesen( double eingabeVektor[])
{
	ifstream datei;
	dateiOeffnenEingabeStrom( &datei, anaEinDateiname);
	
    for( int i = 0; i < ANAMAXLAENGE; i++)							// Digitalen Eingabevektor lesen
    {		
		eingabeVektor[ i] = 0;
 		datei >> eingabeVektor[ i];
    }
	
	datei.close( );	

	return;

}

void anaEinSchreiben( int id, double wert)
{
	double eingabeVektor[ ANAMAXLAENGE];
	ofstream eingabedatei;

	anaEinLesen( eingabeVektor);

	eingabeVektor[ id] = wert;                                  // Wert setzen

	dateiOeffnenAusgabeStrom( &eingabedatei, anaEinDateiname);
    for( int i = 0; i < ANAMAXLAENGE; i++)                        // Digitalen Eingabevektor zurückschreiben
    {
        eingabedatei << eingabeVektor[ i] << endl;
    }
    eingabedatei.close();

	return;
}

void anaEinSchreiben( double eingabeVektor[])
{
	ofstream eingabedatei;

	dateiOeffnenAusgabeStrom( &eingabedatei, anaEinDateiname);
    for( int i = 0; i < ANAMAXLAENGE; i++)                        // Digitalen Eingabevektor zurückschreiben
    {
        eingabedatei << eingabeVektor[ i] << endl;
    }
    eingabedatei.close();

	return;
}


//
//	Funktionen zur Handhabung der analogen Ausgabe
//

double anaAusLesen( int id)
{
	double wert;
	double ausgabeVektor[ ANAMAXLAENGE];

	anaAusLesen( ausgabeVektor);
	wert = ausgabeVektor[ id];                                  // Rückgabewert extrahieren
	return wert;
}

void anaAusLesen( double ausgabeVektor[])
{
	ifstream datei;
	dateiOeffnenEingabeStrom( &datei, anaAusDateiname);

    for( int i = 0; i < ANAMAXLAENGE; i++)					 	// Digitalen Ausgabevektor lesen
    {		
		ausgabeVektor[ i] = 0;
 		datei >> ausgabeVektor[ i];
    }
	
	datei.close( );	

	return;
}


void anaAusSchreiben( int id, double wert)
{
	double ausgabeVektor[ ANAMAXLAENGE];
	ofstream ausgabedatei;

	anaAusLesen( ausgabeVektor);

	ausgabeVektor[ id] = wert;                                  // Wert setzen

	dateiOeffnenAusgabeStrom( &ausgabedatei, anaAusDateiname);
    for( int i = 0; i < ANAMAXLAENGE; i++)                       // Digitalen Ausgabevektor zurückschreiben
    {
        ausgabedatei << ausgabeVektor[ i] << endl;
    }
    ausgabedatei.close();

	return;
}