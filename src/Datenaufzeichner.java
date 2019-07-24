import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.Timer;

public class Datenaufzeichner {

	private int intervall;
	private String dateiname;
	private Timer t;
	
	public Datenaufzeichner(int intervall, String dateiname) {
		super();
		this.intervall = intervall;
		this.dateiname = dateiname;
	}
	
	public void start() {
		try {
			FileWriter writer = new FileWriter( dateiname, false);											// bestehende Datei löschen
			writer.write("Zeit" );
			for( int i = 0; i < 16; i++) {								// Tabelle DE füllen
				writer.write(" ; ");
				String s = "DE" + String.valueOf(i);
				writer.write(s );
		    }
			for( int i = 0; i < 16; i++) {								// Tabelle DA füllen
				writer.write(" ; ");
				String s = "DA" + String.valueOf(i);
				writer.write(s );
			}
			for( int i = 0; i < 8; i++) {								// Tabelle AE füllen
				writer.write(" ; ");
				String s = "AE" + String.valueOf(i);
				writer.write(s );
			}
			for( int i = 0; i < 8; i++) {								// Tabelle AA füllen
				writer.write(" ; ");
				String s = "AA" + String.valueOf(i);
				writer.write(s );
			}
			writer.write(System.getProperty("line.separator"));
			writer.flush();
			writer.close();			

			t = new Timer( 1000 * intervall, new ActionListener() {		
				  public void actionPerformed( ActionEvent e ) {
				    schreiben();
				  }
				});
			t.start();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

	
	}

public void schreiben() {
    	
		try {
			FileWriter writer = new FileWriter( dateiname, true);
			DigDatei de = new DigDatei( Konfig.getDIGMAXLAENGE(), "C:\\Sim\\digein.txt");
			DigDatei da = new DigDatei( Konfig.getDIGMAXLAENGE(), "C:\\Sim\\digaus.txt");
			AnaDatei ae = new AnaDatei( Konfig.getANAMAXLAENGE(), "C:\\Sim\\anaein.txt");
			AnaDatei aa = new AnaDatei( Konfig.getANAMAXLAENGE(), "C:\\Sim\\anaaus.txt");
			int[] dvektor = new int[ Konfig.getDIGMAXLAENGE()];
			double[] avektor = new double[ Konfig.getANAMAXLAENGE()];
			String s;
			boolean first = true;
			
			SimpleDateFormat  formatZeit = new SimpleDateFormat("HH:mm:ss");					// Zeit rausschreiben
			s =  formatZeit.format(new Date());
			writer.write(s );
			
			de.lesen(dvektor);
			for( int i = 0; i < Konfig.getDIGMAXLAENGE(); i++) {								// DE rausschreiben
				writer.write(" ; ");
		    	s = Integer.toString(dvektor[ i]);
				writer.write(s );
		    }

			da.lesen(dvektor);
			for( int i = 0; i < Konfig.getDIGMAXLAENGE(); i++) {								//  DA rausschreiben
				writer.write(" ; ");
		    	s = Integer.toString(dvektor[ i]);
				writer.write(s );
			}		

			ae.lesen(avektor);
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {								//  AE rausschreiben 
				writer.write(" ; ");
		    	s = Double.toString(avektor[ i]);
				writer.write(s );
			}
			
			aa.lesen(avektor);
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {								//  AA rausschreiben
				writer.write(" ; ");
		    	s = Double.toString(avektor[ i]);
				writer.write(s );
			}	

			writer.write(System.getProperty("line.separator"));
			writer.flush();
			writer.close();			
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void stop() {
		t.stop();
	}
}
