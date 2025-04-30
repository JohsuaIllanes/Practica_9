import tkinter as tk
from tkinter import messagebox

# Clases
class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.precio = 50.0 if dias >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.precio = 25.0 if dias >= 10 else 30.0

# Función para vender el boleto
def vender_boleto():
    try:
        numero = int(entry_numero.get())
        dias = int(entry_dias.get()) if tipo_boleto.get() != "Palco" else 0

        if tipo_boleto.get() == "Palco":
            boleto = Palco(numero)
        elif tipo_boleto.get() == "Platea":
            boleto = Platea(numero, dias)
        elif tipo_boleto.get() == "Galeria":
            boleto = Galeria(numero, dias)
        else:
            messagebox.showwarning("Atención", "Seleccione un tipo de boleto.")
            return

        label_info.config(text="Información: " + str(boleto))
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos en los campos.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Teatro Municipal")
ventana.geometry("370x320")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Teatro Municipal", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Datos del Boleto
tk.Label(ventana, text="Datos del Boleto", font=("Arial", 10, "bold")).pack()

# Tipo de boleto
tipo_boleto = tk.StringVar()

frame_radio = tk.Frame(ventana)
frame_radio.pack(pady=5)

tk.Radiobutton(frame_radio, text="Palco", variable=tipo_boleto, value="Palco").pack(side="left", padx=10)
tk.Radiobutton(frame_radio, text="Platea", variable=tipo_boleto, value="Platea").pack(side="left", padx=10)
tk.Radiobutton(frame_radio, text="Galeria", variable=tipo_boleto, value="Galeria").pack(side="left", padx=10)

# Número de boleto
frame_num = tk.Frame(ventana)
frame_num.pack(pady=5)
tk.Label(frame_num, text="Número:").pack(side="left", padx=5)
entry_numero = tk.Entry(frame_num, width=10)
entry_numero.pack(side="left")

# Días de anticipación
frame_dias = tk.Frame(ventana)
frame_dias.pack(pady=5)
tk.Label(frame_dias, text="Cant. días para el evento:").pack(side="left")
entry_dias = tk.Entry(frame_dias, width=10)
entry_dias.pack(side="left")

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
tk.Button(frame_botones, text="Vender", width=12, command=vender_boleto).pack(side="left", padx=10)
tk.Button(frame_botones, text="Salir", width=12, command=ventana.quit).pack(side="left", padx=10)

# Resultado
label_info = tk.Label(ventana, text="Información:", font=("Arial", 10), fg="blue")
label_info.pack(pady=10)

ventana.mainloop()
