import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class DigDatei {
	int MAXLAENGE;
	String	dateiname;
	
	public DigDatei(int MAXLAENGE, String dateiname) {
		super();
		this.MAXLAENGE = MAXLAENGE;
		this.dateiname = dateiname;
	}

	public int lesen( int id) throws FileNotFoundException {
		int wert;
		int[] vektor = new int[ MAXLAENGE];
	 	
		lesen( vektor);											// Vektor holen
		wert = vektor[ id];                                  	// Rückgabewert extrahieren
		return wert;		
	}

	public void lesen( int wertVektor[]) throws FileNotFoundException {

		String s;
		Scanner input = new Scanner( new FileReader( dateiname) );

		for( int i = 0; i < MAXLAENGE; i++){
	    	s = input.nextLine();
	    	wertVektor[i] = Integer.parseInt(s);
	    }

	    input.close();
	    return;
	}

	public void schreiben( int id, int wert) throws IOException {
		int[] vektor = new int[ MAXLAENGE];
		lesen( vektor);
		vektor[ id] = wert;
		schreiben( vektor);
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
	}
}
