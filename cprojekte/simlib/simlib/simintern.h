//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Interne Header-Datei der C/C++-Schnittstelle
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			15.10.2018
//		Letzte Änderung:	31.07.2019
//

#include "simulation.h"

bool digEinLesen( int id);
bool digAusLesen( int id);
void digEinSchreiben( int id, bool wert);
void digEinSchreiben( bool eingabeVektor[]);
void digAusSchreiben( int id, bool wert);

void digEinLesen( bool eingabeVektor[]);
void digAusLesen( bool ausgabeVektor[]);

double anaEinLesen( int id);
double anaAusLesen( int id);
void anaEinSchreiben( int id, double wert);
void anaEinSchreiben( double eingabeVektor[]);
void anaAusSchreiben( int id, double wert);

void anaEinLesen( double eingabeVektor[]);
void anaAusLesen( double ausgabeVektor[]);