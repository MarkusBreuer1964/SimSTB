
public class GenOpt {
	int			id;			// Kanal
	Signalform	form;		// Signalform
	double		A;			// Amplitude
	double		T;			// Periodendauer
	
	public GenOpt(int id, Signalform form, double a, double t) {				// Konstruktoren
		this.id = id;
		this.form = form;
		this.A = a;
		this.T = t;
	}
	
	public GenOpt(int id, Signalform form) {
		this.id = id;
		this.form = form;
	}

	public GenOpt() {
	}

	public int getId() {														// Getter and Setter
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public Signalform getForm() {
		return form;
	}
	public void setForm(Signalform form) {
		this.form = form;
	}
	public double getA() {
		return A;
	}
	public void setA(double a) {
		A = a;
	}
	public double getT() {
		return T;
	}
	public void setT(double t) {
		T = t;
	}
}
