//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Hilfsklasse, die Konfigurationsdaten mit Hilfe statischer Methoden liefert
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			20.07.2019
//		Letzte Änderung:	31.07.2019
//


public class Konfig {
	private final static int DIGMAXLAENGE = 16;							// Anzahl der digitalen Kanäle
	private final static int ANAMAXLAENGE = 8;							// Anzahl der analogen Kanäle
	private final static String ANAAUS = "C:\\Sim\\anaaus.txt";			// Namen und Position der Austauschdateien
	private final static String ANAEIN = "C:\\Sim\\anaein.txt";
	private final static String DIGAUS = "C:\\Sim\\digaus.txt";
	private final static String DIGEIN = "C:\\Sim\\digein.txt";

	public static int getDIGMAXLAENGE() {
		return DIGMAXLAENGE;
	}
	public static int getANAMAXLAENGE() {
		return ANAMAXLAENGE;
	}
	public static String getANAAUS() {
		return ANAAUS;
	}
	public static String getANAEIN() {
		return ANAEIN;
	}
	public static String getDIGAUS() {
		return DIGAUS;
	}
	public static String getDIGEIN() {
		return DIGEIN;
	}

}
