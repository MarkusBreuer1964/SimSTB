import java.io.IOException;

public class FktGen {

	public void generate( GenOpt opt) {
		long		startZeit;
		long		aktuelleZeit;
		double		t;
		double		wert = 0;
		
		startZeit = System.currentTimeMillis();							// Startzeitpunkt
		
		while( true) {
			aktuelleZeit = System.currentTimeMillis();	
			t = (aktuelleZeit - startZeit) / 1000;
			
			switch( opt.getForm()){										// Signalformverteiler
			case ZUFALL:
				wert = erzeugeZufall( opt.getA());
				break;
			case SINUS:
				wert = erzeugeSinus( opt.getA(), opt.getT(), t);
				break;
			}
			
			try {
				AnaDatei ae = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());
				ae.schreiben( opt.getId(), wert);
			} catch (IOException e) {
				e.printStackTrace();
			}
			try {
				Thread.sleep(250);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	private double erzeugeZufall( double A) {									// Zufallszahl zwischen -A und A generieren
		double		wert;
		
		wert = 2*A* Math.random() - A;
		
		return wert;
	}

	private double erzeugeSinus( double A, double T, double t) {				// Sinuswert generieren
		double		wert;
		
		wert = A * Math.sin( 2 * Math.PI * t / T);
		
		return wert;
	}
	
}		// Ende Klasse FktGen
