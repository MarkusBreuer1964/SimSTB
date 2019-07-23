import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class AnaDatei {
	int MAXLAENGE;
	String	dateiname;
	
	public AnaDatei(int MAXLAENGE, String dateiname) {
		super();
		this.MAXLAENGE = MAXLAENGE;
		this.dateiname = dateiname;
	}

	public double lesen( int id) throws FileNotFoundException {
		double wert;
		double[] vektor = new double[ MAXLAENGE];
	 	
		lesen( vektor);											// Vektor holen
		wert = vektor[ id];                                  	// Rückgabewert extrahieren
		return wert;		
	}

	public void lesen( double wertVektor[]) throws FileNotFoundException {

		String s;
		Scanner input = new Scanner( new FileReader(dateiname) );

		for( int i = 0; i < MAXLAENGE; i++){
	    	s = input.nextLine();
	    	s = s.replace(',', '.');
	    	wertVektor[i] = Double.parseDouble(s);
	    }

	    input.close();
	    return;
	}

	public void schreiben( int id, double wert) throws IOException {
		double[] vektor = new double[ MAXLAENGE];
		lesen( vektor);
		vektor[ id] = wert;
		schreiben( vektor);
		
	}

	public void schreiben( double wertVektor[]) throws IOException {
		FileWriter writer = new FileWriter( dateiname);
    	String s;
    	
	    for( int i = 0; i < MAXLAENGE; i++)                        // Analogen Eingabevektor zurückschreiben
	    {
	    	s = Double.toString(wertVektor[ i]);
	    	s = s.replace('.', ',');
			writer.write(s );
			writer.write(System.getProperty("line.separator"));
	    }
		writer.flush();
		writer.close();			
	}
}
