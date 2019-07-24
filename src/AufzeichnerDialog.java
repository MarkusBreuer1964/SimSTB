import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.Toolkit;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class AufzeichnerDialog extends JDialog implements ActionListener {

	private final JPanel contentPanel = new JPanel();
	private JTextField textField;
	private JTextField textField_1;
	private JButton okButton; 
	private JButton cancelButton;
	private boolean result = false;
	private int intervall;
	private String dateiname;
	
	/**
	 * Create the dialog.
	 */
	public AufzeichnerDialog() {
		setTitle("SimSTB - Datenaufzeichnung");
		setIconImage(Toolkit.getDefaultToolkit().getImage("Z:\\Sonstiges\\Markus\\Weiterbildung\\Java\\workspace\\SimSTB\\bilder\\settings-gears.png"));
		setBounds(100, 100, 679, 142);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		
		JLabel lblIntervals = new JLabel("Interval (s)");
		lblIntervals.setBounds(10, 11, 73, 14);
		contentPanel.add(lblIntervals);
		
		textField = new JTextField();
		textField.setText("5");
		textField.setBounds(79, 8, 46, 20);
		contentPanel.add(textField);
		textField.setColumns(10);
		
		JLabel lblLogdatei = new JLabel("Log-Datei");
		lblLogdatei.setBounds(10, 36, 46, 14);
		contentPanel.add(lblLogdatei);
		
		textField_1 = new JTextField();
		textField_1.setBounds(79, 33, 383, 20);
		contentPanel.add(textField_1);
		textField_1.setColumns(10);
		
		JButton btnDatei = new JButton("Datei");
		btnDatei.setBounds(472, 32, 89, 23);
		contentPanel.add(btnDatei);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				okButton = new JButton("Datenaufzeichnung starten");
				okButton.addActionListener( this);
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				cancelButton = new JButton("Cancel");
				cancelButton.addActionListener( this);
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}
	
	   public void actionPerformed(ActionEvent arg0) {
		      Object source = arg0.getSource();
		      if (source == okButton) {
		    	  result = true;
		    	  intervall = Integer.parseInt(textField.getText());
		    	  dateiname = textField_1.getText();
		      }
		      else {
		         result = false;
		      }
		      this.setVisible(false);
		   }
	   

	public boolean run() {
		      this.setVisible(true);
		      return result;
		   }

	public int getIntervall() {
		return intervall;
	}

	public String getDateiname() {
		return dateiname;
	}

}
