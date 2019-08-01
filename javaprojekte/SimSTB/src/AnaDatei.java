//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Klasse zur Handhabung der analogen Austauschdateien
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


public class AnaDatei {
	int MAXLAENGE;											// Dateilänge
	String	dateiname;										// Dateiname
	
	public AnaDatei(int MAXLAENGE, String dateiname) {
		super();
		this.MAXLAENGE = MAXLAENGE;
		this.dateiname = dateiname;
	}

	public double lesen( int id) throws FileNotFoundException {						// Einzelwert aus Datei lesen
		double wert;
		double[] vektor = new double[ MAXLAENGE];
	 	
		lesen( vektor);											// Alle Werte lesen
		wert = vektor[ id];                                  	// Einzelwert extrahieren
		return wert;		
	}

	public void lesen( double wertVektor[]) throws FileNotFoundException {			// Alle Werte aus Datei lesen
		String s;
		Scanner input = new Scanner( new FileReader(dateiname) );

		for( int i = 0; i < MAXLAENGE; i++){
	    	s = input.nextLine();
	    	s = s.replace(',', '.');							// in Austauschdateien deutsche Komma-Konvention
	    	wertVektor[i] = Double.parseDouble(s);
	    }
	    input.close();
	    return;
	}

	public void schreiben( int id, double wert) throws IOException {				// Einzelwert in Datei zurückschreiben
		double[] vektor = new double[ MAXLAENGE];
		
		lesen( vektor);											// Alle Werte lesen
		vektor[ id] = wert;										// Einzelwert setzen
		schreiben( vektor);										// Alle Werte zurückschreiben
		return;
	}

	public void schreiben( double wertVektor[]) throws IOException {				// Alle Werte in Datei zurückschreiben
		FileWriter writer = new FileWriter( dateiname);
    	String s;
    	
	    for( int i = 0; i < MAXLAENGE; i++)                        
	    {
	    	s = Double.toString(wertVektor[ i]);
	    	s = s.replace('.', ',');							// in Austauschdateien deutsche Komma-Konvention
			writer.write(s );
			writer.write(System.getProperty("line.separator"));
	    }
		writer.flush();
		writer.close();	
		return;
	}
}
