import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JComboBox;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.DefaultComboBoxModel;

public class FktGenHauptfenster extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FktGenHauptfenster frame = new FktGenHauptfenster();
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
	public FktGenHauptfenster() {
		setIconImage(Toolkit.getDefaultToolkit().getImage(Hauptfenster.class.getResource("/bilder/settings-gears.png")));
		setResizable(false);
		setTitle("SimSTB - Funktionsgenerator");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 350, 229);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(220, 220, 220));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(null);
		setContentPane(contentPane);
		
		JLabel lblU1 = new JLabel("SimSTB");
		lblU1.setFont(new Font("Tahoma", Font.BOLD, 36));
		lblU1.setBounds(10, 5, 150, 50);
		contentPane.add(lblU1);
		
		JLabel lblU2 = new JLabel("<html>Analoger<br>Funktionsgenerator</html>");
		lblU2.setBounds(170, 5, 150, 50);
		contentPane.add(lblU2);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"AE0", "AE1", "AE2", "AE3", "AE4", "AE5", "AE6", "AE7"}));
		comboBox.setBounds(105, 66, 67, 20);
		contentPane.add(comboBox);
		
		JLabel lblNewLabel = new JLabel("Kanal");
		lblNewLabel.setBounds(10, 69, 46, 14);
		contentPane.add(lblNewLabel);
		
		JLabel lblSignalform = new JLabel("Signalform");
		lblSignalform.setBounds(10, 97, 70, 14);
		contentPane.add(lblSignalform);
		
		JComboBox comboBox_1 = new JComboBox();
		comboBox_1.setModel(new DefaultComboBoxModel(new String[] {"Zufall", "Sinus"}));
		comboBox_1.setBounds(105, 97, 67, 20);
		contentPane.add(comboBox_1);
		
		JLabel lblAmplitude = new JLabel("Amplitude");
		lblAmplitude.setBounds(10, 133, 67, 14);
		contentPane.add(lblAmplitude);
		
		textField = new JTextField();
		textField.setBounds(105, 130, 67, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JLabel lblPeriodendauer = new JLabel("P.dauer (s)");
		lblPeriodendauer.setBounds(10, 164, 86, 14);
		contentPane.add(lblPeriodendauer);
		
		textField_1 = new JTextField();
		textField_1.setBounds(105, 161, 67, 20);
		contentPane.add(textField_1);
		textField_1.setColumns(10);
		
		JButton btnNewButton = new JButton("Start");
		btnNewButton.setBounds(190, 66, 130, 50);
		contentPane.add(btnNewButton);
		
		JButton btnBeenden = new JButton("Beenden");
		btnBeenden.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		btnBeenden.setFont(new Font("Tahoma", Font.PLAIN, 11));
		btnBeenden.setBounds(190, 133, 130, 50);
		btnBeenden.setBackground(new Color(255, 99, 71));
		contentPane.add(btnBeenden);

	}
}
