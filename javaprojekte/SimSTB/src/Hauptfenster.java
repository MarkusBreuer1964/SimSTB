//
//	Inhalt:
//		Projekt: 			SimSTB
//		Thema:				Simulation digitaler und analoger Ein- und Ausgaben
//		Datei:				Hauptfenster und Startpunkt des Steuerungs- und Monitor-Programms 
//							- GUI grösstenteils mit WindowBuilder generiert
//							- Actionhandler jeweils als eingebettete Klassen realisiert
//
//	Autor:
//		Name:				Markus Breuer
//		Organisaion:		STB
//
//	Datum:
//		Erstellt:			20.07.2019
//		Letzte Änderung:	06.01.2020
//


import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.event.CellEditorListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.TableModelEvent;
import javax.swing.event.TableModelListener;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.Timer;

import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.awt.event.ActionEvent;
import java.awt.Color;
import java.awt.Component;

import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Font;
import javax.swing.JTextField;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.InputMethodListener;
import java.awt.event.InputMethodEvent;
import java.awt.Toolkit;
import javax.swing.ImageIcon;


public class Hauptfenster extends JFrame {

	private JPanel contentPane;
	private JTable tblDE;
	private JTable tblDA;
	private JTable tblAE;
	private JTable tblAA;
	private JLabel lblDatum;
	private JLabel lblZeit;
	private JButton btnAufz;

	private boolean aufzeichnung = false;				// Merker, ob Datenaufzeichnung läuft
	private Datenaufzeichner aufzeichner;				// Datenaufzeichner
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Hauptfenster frame = new Hauptfenster();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Hauptfenster() {
		setIconImage(Toolkit.getDefaultToolkit().getImage(Hauptfenster.class.getResource("/bilder/settings-gears.png")));
		setResizable(false);
		setTitle("SimSTB - Simulationsumgebung");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 425, 700);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(220, 220, 220));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JPanel panel_1 = new JPanel();
		panel_1.setBackground(new Color(192, 192, 192));
		panel_1.setBounds(10, 80, 150, 315);
		contentPane.add(panel_1);
		panel_1.setLayout(null);
		
		JButton btnAlles0 = new JButton("Alles 0");
		btnAlles0.addActionListener( actAlles0);
		btnAlles0.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnAlles0.setBackground(new Color(220, 220, 220));
		btnAlles0.setBounds(10, 10, 130, 50);
		panel_1.add(btnAlles0);
		
		JButton btnAus0 = new JButton("Alle Ausg\u00E4nge 0");
		btnAus0.addActionListener( actAlleAus0);
		btnAus0.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnAus0.setBackground(new Color(220, 220, 220));
		btnAus0.setBounds(10, 71, 130, 50);
		panel_1.add(btnAus0);
		
		JButton btnEin0 = new JButton("Alle Eing\u00E4nge 0");
		btnEin0.addActionListener(actAlleEin0);
		btnEin0.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnEin0.setBackground(new Color(220, 220, 220));
		btnEin0.setBounds(10, 132, 130, 50);
		panel_1.add(btnEin0);
		
		JButton btnDigEin0 = new JButton("Digitale Eing\u00E4nge 0");
		btnDigEin0.addActionListener(actDigEin0);
		btnDigEin0.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnDigEin0.setBackground(new Color(220, 220, 220));
		btnDigEin0.setBounds(10, 193, 130, 50);
		panel_1.add(btnDigEin0);
		
		JButton btnDigEin1 = new JButton("Digitale Eing\u00E4nge 1");
		btnDigEin1.addActionListener(actDigEin1);
		btnDigEin1.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnDigEin1.setBounds(10, 254, 130, 50);
		panel_1.add(btnDigEin1);
		btnDigEin1.setBackground(new Color(220, 220, 220));
		
		JPanel panel_2 = new JPanel();
		panel_2.setBackground(new Color(192, 192, 192));
		panel_2.setBounds(10, 405, 150, 191);
		contentPane.add(panel_2);
		panel_2.setLayout(null);
		
		JButton btnModelle = new JButton("Modelle");
		btnModelle.addActionListener( actModelle);
		btnModelle.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnModelle.setBackground(new Color(220, 220, 220));
		btnModelle.setBounds(10, 11, 130, 50);
		panel_2.add(btnModelle);
		
		JButton btnTesten = new JButton("Testautomaten");
		btnTesten.addActionListener( actTest);
		btnTesten.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnTesten.setBackground(new Color(220, 220, 220));
		btnTesten.setBounds(10, 72, 130, 50);
		panel_2.add(btnTesten);
		
		JButton btnGen = new JButton("Funktionsgenerator");
		btnGen.addActionListener( actGen);
		btnGen.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnGen.setBackground(new Color(220, 220, 220));
		btnGen.setBounds(10, 133, 130, 50);
		panel_2.add(btnGen);
		
		JPanel panel = new JPanel();
		panel.setBackground(new Color(192, 192, 192));
		panel.setBounds(170, 80, 239, 516);
		contentPane.add(panel);
		panel.setLayout(null);
		
		tblDE = new JTable();
		tblDE.addMouseListener( actDETBL);
		tblDE.setBackground(new Color(220, 220, 220));
		tblDE.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
			},
			new String[] {
				"", ""
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, false
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		tblDE.getColumnModel().getColumn(0).setResizable(false);
		tblDE.getColumnModel().getColumn(1).setResizable(false);
		
		JLabel lblDE = new JLabel("<html>Digitale <br/>\nEing\u00E4nge</html>");
		lblDE.setBounds(10, 9, 70, 30);
		panel.add(lblDE);
		tblDE.setBounds(10, 50, 70, 256);
		panel.add(tblDE);
		
		JLabel LblDA = new JLabel("<html>Digitale <br/>\r\nAusg\u00E4nge</html>");
		LblDA.setBounds(121, 9, 70, 30);
		panel.add(LblDA);
		
		tblDA = new JTable();
		tblDA.setEnabled(false);
		tblDA.setBackground(new Color(220, 220, 220));
		tblDA.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
			},
			new String[] {
				"", ""
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, false
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		tblDA.getColumnModel().getColumn(0).setResizable(false);
		tblDA.getColumnModel().getColumn(1).setResizable(false);
		tblDA.setBounds(120, 50, 70, 256);
		panel.add(tblDA);
		
		JLabel LblAE = new JLabel("<html>Analoge <br/>\r\nEing\u00E4nge</html>");
		LblAE.setBounds(10, 327, 70, 30);
		panel.add(LblAE);
		
		tblAE = new JTable();
		tblAE.setBackground(new Color(220, 220, 220));
		tblAE.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
			},
			new String[] {
				"", ""
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, true
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		tblAE.getColumnModel().getColumn(0).setResizable(false);
		tblAE.getColumnModel().getColumn(0).setPreferredWidth(35);
		tblAE.getColumnModel().getColumn(0).setMinWidth(35);
		tblAE.getColumnModel().getColumn(0).setMaxWidth(35);
		tblAE.getColumnModel().getColumn(1).setResizable(false);
		tblAE.setBounds(10, 370, 105, 128);
		tblAE.getDefaultEditor(String.class).addCellEditorListener( actAETBL);
		panel.add(tblAE);
		
		JLabel lblAA = new JLabel("<html>Analoge <br/>\r\nAusg\u00E4nge</html>");
		lblAA.setBounds(121, 327, 70, 30);
		panel.add(lblAA);
		
		tblAA = new JTable();
		tblAA.setEnabled(false);
		tblAA.setBackground(new Color(220, 220, 220));
		tblAA.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
				{null, null},
			},
			new String[] {
				"", ""
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, false
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		tblAA.getColumnModel().getColumn(0).setResizable(false);
		tblAA.getColumnModel().getColumn(0).setPreferredWidth(35);
		tblAA.getColumnModel().getColumn(0).setMinWidth(35);
		tblAA.getColumnModel().getColumn(0).setMaxWidth(35);
		tblAA.getColumnModel().getColumn(1).setResizable(false);
		tblAA.setBounds(120, 370, 105, 128);
		panel.add(tblAA);
		
		btnAufz = new JButton("Datenaufzeichnung");
		btnAufz.addActionListener( actAufzeichner);
		btnAufz.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnAufz.setBackground(new Color(220, 220, 220));
		btnAufz.setBounds(20, 610, 130, 50);
		contentPane.add(btnAufz);
		
		JButton btnSimulatorBeenden = new JButton("Beenden");
		btnSimulatorBeenden.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		btnSimulatorBeenden.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnSimulatorBeenden.setBounds(180, 610, 130, 50);
		contentPane.add(btnSimulatorBeenden);
		btnSimulatorBeenden.setBackground(new Color(255, 99, 71));
		
		JLabel lblU1 = new JLabel("SimSTB");
		lblU1.setFont(new Font("Tahoma", Font.BOLD, 36));
		lblU1.setBounds(10, 5, 150, 48);
		contentPane.add(lblU1);
		
		JLabel lblU2 = new JLabel("<html>Simulationsumgebung f\u00FCr digitale <br/> und analoge Ein- und Ausg\u00E4nge </html>");
		lblU2.setBounds(170, 11, 214, 42);
		contentPane.add(lblU2);
		
		lblDatum = new JLabel();
		lblDatum.setText("tt.mm.jjjj");
		lblDatum.setBounds(10, 55, 86, 20);
		contentPane.add(lblDatum);
		
		lblZeit = new JLabel("hh:mm:ss");
		lblZeit.setBounds(170, 55, 106, 14);
		contentPane.add(lblZeit);
		
		tabellenFuellen();											// Tabellen initial füllen

		Timer t = new Timer( 1000, new ActionListener() {			// Timer zum periodischen füllen anlegen und aktivieren
			  public void actionPerformed( ActionEvent e ) {
			    aktualisieren();
			  }
			});
		t.start();
		
		
	}
	
	ActionListener actAlles0 = new ActionListener() {				// Action Handler für Knopf "Alles 0"
		public void actionPerformed(ActionEvent e) {
			Setzer.digEin0();
			Setzer.anaEin0();
			Setzer.digAus0();
			Setzer.anaAus0();	
		}
	};

	ActionListener actAlleAus0 = new ActionListener() {				// Action Handler für Knopf "Alle Ausgänge 0"
		public void actionPerformed(ActionEvent e) {
			Setzer.digAus0();
			Setzer.anaAus0();
		}
	};

	ActionListener actAlleEin0 = new ActionListener() {				// Action Handler für Knopf "Alle Eingänge 0"
		public void actionPerformed(ActionEvent e) {
			Setzer.digEin0();
			Setzer.anaEin0();
		}
	};

	ActionListener actDigEin0 = new ActionListener() {				// Action Handler für Knopf "Dig. Eingänge 0"
		public void actionPerformed(ActionEvent arg0) {
			Setzer.digEin0();
		}
	};

	ActionListener actDigEin1 = new ActionListener() {				// Action Handler für Knopf "Dig. Eingänge 1"
		public void actionPerformed(ActionEvent arg0) {
			Setzer.digEin1();
		}
	};

	ActionListener actModelle = new ActionListener() {
		public void actionPerformed(ActionEvent arg0) {
			JOptionPane.showMessageDialog(rootPane, "Leider nocht nicht implementiert.\nSW-Modelle mit GUI zum Testen von Lösungen.\nAnforderungswunsch R6", "Hinweis",
					JOptionPane.INFORMATION_MESSAGE);
		}
	};
 
	ActionListener actTest = new ActionListener() {
		public void actionPerformed(ActionEvent arg0) {
			JOptionPane.showMessageDialog(rootPane, "Leider nocht nicht implementiert.\nAutomatisiertes Testablaufmodul.\nAnforderungswunsch R9", "Hinweis",
					JOptionPane.INFORMATION_MESSAGE);
		}
	};
 
	ActionListener actGen = new ActionListener() {
		public void actionPerformed(ActionEvent arg0) {
			try {
				Runtime.getRuntime().exec("start-fktgen.bat");
			} catch (IOException e1) {
				e1.printStackTrace();
				JOptionPane.showMessageDialog(rootPane, "Funktionsgenerator konnte nicht gestartet werden", "Fehler",
						JOptionPane.ERROR_MESSAGE);
			}
		}
	};
 
	
	CellEditorListener actAETBL = new CellEditorListener() {		// Action Handler für Tabelle "Analoge Eingänge"	
 		public void editingCanceled(ChangeEvent arg0) {
			// Nicht genutzter Stub		
		}
		public void editingStopped(ChangeEvent e) {				// Wert in Austauschdatei setzen
			double wert = Double.parseDouble( (String) tblAE.getModel().getValueAt( tblAE.getSelectedRow(), 1));
			int id = tblAE.getSelectedRow();
			Setzer.anaEin(id, wert);
			tblAE.clearSelection();			
		}
    };	
    
	MouseListener actDETBL = new MouseAdapter() {					// Action Handler für Tabelle "Digitale Eingänge"
		public void mouseClicked(MouseEvent arg0) {				// Wert in Austauschdatei setzen			
			int alterWert = (int) tblDE.getModel().getValueAt( tblDE.getSelectedRow(), 1);
			int id = tblDE.getSelectedRow();
			if( alterWert == 0) {
				Setzer.digEin(id, 1);
				}
			else {
				Setzer.digEin(id, 0);
				}
			tblDE.clearSelection();
		}
	};

	ActionListener actAufzeichner = new ActionListener() {											// ActionListener für Datenaufzeichnung
		public void actionPerformed(ActionEvent arg0) {
			if( aufzeichnung == false) {											// Datenaufzeichnung starten
				AufzeichnerDialog dialog = new AufzeichnerDialog( );				// Dialog für Einstellungen; muss modal sein				
				dialog.setModal(true);
				boolean erg = dialog.run();
				if( erg == true) {
					aufzeichnung = true;
					int intervall = dialog.getIntervall();
					String dateiname = dialog.getDateiname();
					aufzeichner = new Datenaufzeichner( intervall, dateiname);		// eigentliche Aufzeichnung starten
					aufzeichner.start();
					btnAufz.setText("Aufzeichnung beenden");
				}
			}
			else {																	// Datenaufzeichnung beenden
				aufzeichnung = false;
				aufzeichner.stop();
				String msg = "Datenaufzeichnung beendet.\n" + aufzeichner.getAnzahlDatensaetze() + " Datensätze in Datei " 
				           + aufzeichner.getDateiname() + " geschrieben.";
				JOptionPane.showMessageDialog(rootPane, msg, "Datenaufzeichnung", JOptionPane.INFORMATION_MESSAGE);
				btnAufz.setText("Datenaufzeichnung");
			}
		}
	};

	void tabellenFuellen() {											// Tabellen initial mit Tabellenlabeln und 0 füllen
		for( int i = 0; i < 16; i++) {					// Tabelle DE füllen
			String s = "DE" + String.valueOf(i);
			tblDE.getModel().setValueAt(s, i, 0);
			tblDE.getModel().setValueAt(0, i, 1);
		}
		for( int i = 0; i < 16; i++) {					// Tabelle DA füllen
			String s = "DA" + String.valueOf(i);
			tblDA.getModel().setValueAt(s, i, 0);
			tblDA.getModel().setValueAt(0, i, 1);
		}
		for( int i = 0; i < 8; i++) {					// Tabelle AE füllen
			String s = "AE" + String.valueOf(i);
			tblAE.getModel().setValueAt(s, i, 0);
			tblAE.getModel().setValueAt(0, i, 1);
		}
		for( int i = 0; i < 8; i++) {					// Tabelle AA füllen
			String s = "AA" + String.valueOf(i);
			tblAA.getModel().setValueAt(s, i, 0);
			tblAA.getModel().setValueAt(0, i, 1);
		}
		
	}
	
	void aktualisieren() {												// Benutzeroberfläche periodisch aktualisieren
		try {																	
			DigDatei de = new DigDatei( Konfig.getDIGMAXLAENGE(), Konfig.getDIGEIN());
			DigDatei da = new DigDatei( Konfig.getDIGMAXLAENGE(), Konfig.getDIGAUS());
			AnaDatei ae = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAEIN());
			AnaDatei aa = new AnaDatei( Konfig.getANAMAXLAENGE(), Konfig.getANAAUS());
			int[] dvektor = new int[ Konfig.getDIGMAXLAENGE()];
			double[] avektor = new double[ Konfig.getANAMAXLAENGE()];

			de.lesen(dvektor);
			for( int i = 0; i < Konfig.getDIGMAXLAENGE(); i++) {				// Tabelle DE aktualisieren
				tblDE.getModel().setValueAt(dvektor[i], i, 1);
			}
			da.lesen(dvektor);
			for( int i = 0; i < Konfig.getDIGMAXLAENGE(); i++) {				// Tabelle DA aktualisieren
				tblDA.getModel().setValueAt(dvektor[i], i, 1);
			}		
			ae.lesen(avektor);
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {				// Tabelle AE aktualisieren
				tblAE.getModel().setValueAt(avektor[i], i, 1);
			}
			aa.lesen(avektor);
			for( int i = 0; i < Konfig.getANAMAXLAENGE(); i++) {				// Tabelle AA aktualisieren
				tblAA.getModel().setValueAt(avektor[i], i, 1);			
			}	
		SimpleDateFormat  formatDatum = new SimpleDateFormat("dd.MM.yyyy");		// Datum und Zeit aktualisieren
		lblDatum.setText( formatDatum.format(new Date()));
		SimpleDateFormat  formatZeit = new SimpleDateFormat("HH:mm:ss");
		lblZeit.setText( formatZeit.format(new Date()));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

}
