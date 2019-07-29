import java.io.IOException;

public class Setzer {

	public static void anaAus0() {
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

	public static void anaEin0() {
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

	public static void digAus0() {
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

	public static void digEin0() {
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

	public static void digEin1() {
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

	public static void digEin(int id, int wert) {
		try {
			DigDatei de = new DigDatei(  Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());			
			de.schreiben( id, wert);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void anaEin(int id, double wert) {
		try {
			AnaDatei ae = new AnaDatei(  Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());			
			ae.schreiben( id, wert);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
