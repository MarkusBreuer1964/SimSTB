//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Klasse zum Setzen der digitalen und analogen Werte in der Schnittstelle
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			20.07.2019
//		Letzte Änderung:	31.07.2019
//


import java.io.IOException;


public class Setzer {

	public static void anaAus0() {																// Alle analogen Ausgänge auf 0 setzen
		try {
			AnaDatei aa = new AnaDatei( Konfig.getANAMAXLAENGE() , Konfig.getANAAUS());
			double[] dvektor = new double[ Konfig.getANAMAXLAENGE()];
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {								
				dvektor[i] = 0;
			}
			aa.schreiben( dvektor);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void anaEin0() {																// Alle analogen Eingänge auf 0 setzen
		try {
			AnaDatei ae = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());
			double[] dvektor = new double[ Konfig.getANAMAXLAENGE()];
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {								
				dvektor[i] = 0;
			}
			ae.schreiben( dvektor);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void digAus0() {																// Alle digitalen Ausgänge auf 0 setzen
		try {
			DigDatei da = new DigDatei( Konfig.getDIGMAXLAENGE(), Konfig.getDIGAUS());
			int[] dvektor = new int[  Konfig.getDIGMAXLAENGE()];
			for( int i = 0; i <  Konfig.getDIGMAXLAENGE(); i++) {								
				dvektor[i] = 0;
			}
			da.schreiben( dvektor);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void digEin0() {																// Alle digitalen Eingänge auf 0 setzen
		try {
			DigDatei de = new DigDatei(  Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());
			int[] dvektor = new int[  Konfig.getDIGMAXLAENGE()];
			for( int i = 0; i <  Konfig.getDIGMAXLAENGE(); i++) {								
				dvektor[i] = 0;
			}
			de.schreiben( dvektor);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void digEin1() {																// Alle digitalen Eingänge auf 1 setzen
		try {
			DigDatei de = new DigDatei(  Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());
			int[] dvektor = new int[  Konfig.getDIGMAXLAENGE()];
			for( int i = 0; i <  Konfig.getDIGMAXLAENGE(); i++) {								
				dvektor[i] = 1;
			}
			de.schreiben( dvektor);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void digEin(int id, int wert) {												// Speziellen digitalen Eingang setzen
		try {
			DigDatei de = new DigDatei(  Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());			
			de.schreiben( id, wert);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void anaEin(int id, double wert) {											// Speziellen analogen Eingang setzen
		try {
			AnaDatei ae = new AnaDatei(  Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());			
			ae.schreiben( id, wert);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
