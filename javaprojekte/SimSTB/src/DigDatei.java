//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Klasse zur Handhabung der digitalen Austauschdateien
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			20.07.2019
//		Letzte Änderung:	01.08.2019
//


import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class DigDatei {
	int MAXLAENGE;											// Dateilänge
	String	dateiname;										// Dateiname
	
	public DigDatei(int MAXLAENGE, String dateiname) {
		super();
		this.MAXLAENGE = MAXLAENGE;
		this.dateiname = dateiname;
	}

	public int lesen( int id) throws FileNotFoundException {					// Einzelwert aus Datei lesen
		int wert;
		int[] vektor = new int[ MAXLAENGE];
	 	
		lesen( vektor);											// Alle Werte lesen											
		wert = vektor[ id];                                   	// Einzelwert extrahieren
		return wert;		
	}

	public void lesen( int wertVektor[]) throws FileNotFoundException {			// Alle Werte aus Datei lesen
		String s;
		Scanner input = new Scanner( new FileReader( dateiname) );

		for( int i = 0; i < MAXLAENGE; i++){
	    	s = input.nextLine();
	    	wertVektor[i] = Integer.parseInt(s);
	    }

	    input.close();
	    return;
	}

	public void schreiben( int id, int wert) throws IOException {				// Einzelwert in Datei zurückschreiben
		int[] vektor = new int[ MAXLAENGE];
		
		lesen( vektor);											// Alle Werte lesen
		vektor[ id] = wert;										// Einzelwert setzen
		schreiben( vektor);										// Alle Werte zurückschreiben
		return;
	}

	public void schreiben( int wertVektor[]) throws IOException {
		FileWriter writer = new FileWriter( dateiname);
		
	    for( int i = 0; i < MAXLAENGE; i++)                        // Digitalen Eingabevektor zurückschreiben
	    {
			writer.write(Integer.toString(wertVektor[ i]) );
			writer.write(System.getProperty("line.separator"));
	    }
		writer.flush();
		writer.close();		
		return;
	}
}
