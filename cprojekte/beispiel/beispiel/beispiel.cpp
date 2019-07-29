//
//	Inhalt:
//		Projekt: 			Beispiel_ls4_01
//		Thema:				Beispiel für die Nutzung analoger Eingabesignale bei der Simulation
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			24.12.2018
//		Letzte Änderung:	26.07.2019
//

#include <cstdlib>
#include <iostream>
#include <locale>
#include <Windows.h>
#include "simulation.h"

using namespace std;

int main()
{
	bool	ende = false;
	double	wert;
	
	locale::global(locale("German_germany"));															// Zeichensatz deutsch

	cout << "Beispielprogramm für Simulationsumgebung" << endl;
	cout << "----------------------------------------" << endl << endl;
	cout << "Die am analogen Eingang Kanal 0 liegenden Eingangssignale" << endl;
	cout << "werden im Sekundentakt eingelesen. Beendet wird das Einlesen," << endl;
	cout << "sobald am digitalen Eingang Kanal 0 eine 1 anliegt." << endl;
	cout << "Am Ende werden noch ein digitales und analoges Ausgabesignal gesetzt." << endl << endl;

	while( ende != true)
	{
		wert = anaEin( 0);											// Einlesen eines analogen Eingabesignals über Kanal 0
		cout << wert << endl;
		Sleep( 1000);												
		ende = digEin( 0);											// Einlesen eines digitalen Eingabesignals über Kanal 0
	}

	digAus( 15, 1);													// Ausgabe eines digitalen Ausgabesignals über Kanal 15
	anaAus( 7, -123.456);											// Ausgabe eines analogen Ausgabesignals über Kanal 7

    cout << "Beispielprogramm beendet" << endl << endl;
	system( "Pause");
    return 0;
}
