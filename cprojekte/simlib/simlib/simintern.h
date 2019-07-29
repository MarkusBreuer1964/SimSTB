//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			24.12.2018
//		Letzte Änderung:	26.07.2019
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