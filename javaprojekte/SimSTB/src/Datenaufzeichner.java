//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Datenaufzeichner
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			20.07.2019
//		Letzte Änderung:	01.08.2019
//


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.Timer;

public class Datenaufzeichner {

	private int intervall;													// Aufzeichnungsintervall
	private String dateiname;												// Name der Log-Datei
	private Timer t;														// Timer; s.u.
	private int anzahlDatensaetze;											// Anzahl der aufgezeichneten datensätze
	
	public Datenaufzeichner(int intervall, String dateiname) {
		super();
		this.intervall = intervall;
		this.dateiname = dateiname;
	}
	
	public void start() {													// Start der Datenaufzeichnung
		try {
			FileWriter writer = new FileWriter( dateiname, false);			// bestehende Datei löschen
			writer.write("Zeit" );											// Überschriftenzeile ausgeben
			for( int i = 0; i < 16; i++) {								
				writer.write(" ; ");
				String s = "DE" + String.valueOf(i);
				writer.write(s );
		    }
			for( int i = 0; i < 16; i++) {								
				writer.write(" ; ");
				String s = "DA" + String.valueOf(i);
				writer.write(s );
			}
			for( int i = 0; i < 8; i++) {								
				writer.write(" ; ");
				String s = "AE" + String.valueOf(i);
				writer.write(s );
			}
			for( int i = 0; i < 8; i++) {								
				writer.write(" ; ");
				String s = "AA" + String.valueOf(i);
				writer.write(s );
			}
			writer.write(System.getProperty("line.separator"));
			writer.flush();
			writer.close();			

			anzahlDatensaetze = 0;
			
			t = new Timer( 1000 * intervall, new ActionListener() {			// Timer, um periodisch jeweils eine Aufzeichnungszeile zu erzeugen
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

public void schreiben() {													// Eine Aufzeichnungszeile herausschreiben
    	
		try {
			FileWriter writer = new FileWriter( dateiname, true);
			DigDatei de = new DigDatei( Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());
			DigDatei da = new DigDatei( Konfig.getDIGMAXLAENGE(), Konfig.getDIGAUS());
			AnaDatei ae = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());
			AnaDatei aa = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAAUS());
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
			
			anzahlDatensaetze++;
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void stop() {																		// Datenaufzeichnung beenden
		t.stop();
	}

	public int getAnzahlDatensaetze() {
		return anzahlDatensaetze;
	}

	public String getDateiname() {
		return dateiname;
	}
}
