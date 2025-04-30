import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

class IBoleto(ABC):
    @abstractmethod
    def get_precio(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Boleto(IBoleto):
    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.get_precio()}"

class Palco(Boleto):
    def get_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.dias = dias

    def get_precio(self):
        return 50.0 if self.dias >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias):
        super().__init__(numero)
        self.dias = dias

    def get_precio(self):
        return 25.0 if self.dias >= 10 else 30.0

def crear_boleto():
    tipo = tipo_boleto.get()
    try:
        numero = int(entry_numero.get())
    except ValueError:
        messagebox.showerror("Error", "Número inválido")
        return

    if tipo == "Palco":
        boleto = Palco(numero)
    else:
        try:
            dias = int(entry_dias.get())
        except ValueError:
            messagebox.showerror("Error", "Días inválido")
            return

        if tipo == "Platea":
            boleto = Platea(numero, dias)
        elif tipo == "Galeria":
            boleto = Galeria(numero, dias)
        else:
            return

    resultado.set(str(boleto))


ventana = tk.Tk()
ventana.title("Teatro Municipal - Boletos")

tk.Label(ventana, text="Tipo de boleto:").grid(row=0, column=0, padx=5, pady=5)
tipo_boleto = ttk.Combobox(ventana, values=["Palco", "Platea", "Galeria"])
tipo_boleto.current(0)
tipo_boleto.grid(row=0, column=1)

tk.Label(ventana, text="Número de boleto:").grid(row=1, column=0, padx=5, pady=5)
entry_numero = tk.Entry(ventana)
entry_numero.grid(row=1, column=1)

tk.Label(ventana, text="Días de anticipación:").grid(row=2, column=0, padx=5, pady=5)
entry_dias = tk.Entry(ventana)
entry_dias.grid(row=2, column=1)

btn = tk.Button(ventana, text="Crear Boleto", command=crear_boleto)
btn.grid(row=3, column=0, columnspan=2, pady=10)

resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, fg="blue").grid(row=4, column=0, columnspan=2)

ventana.mainloop()