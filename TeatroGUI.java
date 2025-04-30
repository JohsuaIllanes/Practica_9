import java.awt.*;
import javax.swing.*;

// Interfaz
interface IBoleto {
    double getPrecio();
    String toString();
}

// Clase abstracta
abstract class Boleto implements IBoleto {
    protected int numero;

    public Boleto(int numero) {
        this.numero = numero;
    }

    public String toString() {
        return "Número: " + numero + ", Precio: " + getPrecio();
    }
}

// Subclases
class Palco extends Boleto {
    public Palco(int numero) {
        super(numero);
    }

    public double getPrecio() {
        return 100.0;
    }
}

class Platea extends Boleto {
    private int dias;

    public Platea(int numero, int dias) {
        super(numero);
        this.dias = dias;
    }

    public double getPrecio() {
        return dias >= 10 ? 50.0 : 60.0;
    }
}

class Galeria extends Boleto {
    private int dias;

    public Galeria(int numero, int dias) {
        super(numero);
        this.dias = dias;
    }

    public double getPrecio() {
        return dias >= 10 ? 25.0 : 30.0;
    }
}

// Interfaz gráfica
public class TeatroGUI extends JFrame {
    private JComboBox<String> tipoCombo;
    private JTextField numeroField, diasField;
    private JLabel resultadoLabel;

    public TeatroGUI() {
        setTitle("Teatro Municipal - Boletos");
        setLayout(new GridLayout(5, 2, 5, 5));
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        add(new JLabel("Tipo de boleto:"));
        tipoCombo = new JComboBox<>(new String[]{"Palco", "Platea", "Galeria"});
        add(tipoCombo);

        add(new JLabel("Número de boleto:"));
        numeroField = new JTextField();
        add(numeroField);

        add(new JLabel("Días de anticipación:"));
        diasField = new JTextField();
        add(diasField);

        JButton crearBtn = new JButton("Crear Boleto");
        crearBtn.addActionListener(e -> crearBoleto());
        add(crearBtn);

        resultadoLabel = new JLabel("Resultado: ");
        add(resultadoLabel);

        setVisible(true);
    }

    private void crearBoleto() {
        try {
            int numero = Integer.parseInt(numeroField.getText());
            String tipo = (String) tipoCombo.getSelectedItem();
            IBoleto boleto = null;

            if ("Palco".equals(tipo)) {
                boleto = new Palco(numero);
            } else {
                int dias = Integer.parseInt(diasField.getText());
                if ("Platea".equals(tipo)) {
                    boleto = new Platea(numero, dias);
                } else if ("Galeria".equals(tipo)) {
                    boleto = new Galeria(numero, dias);
                }
            }

            resultadoLabel.setText("Resultado: " + boleto.toString());

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Por favor ingresa valores válidos.");
        }
    }

    public static void main(String[] args) {
        new TeatroGUI();
    }
}
