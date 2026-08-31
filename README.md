import tkinter as tk
from tkinter import messagebox

def radioButton_Selected():
    sel = rbSeleccion.get()

    if sel == "Celsius":
        tbCelsius.config(state="normal")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="disabled")
    elif sel == "Kelvin":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="normal")
    elif sel == "Fahrenheit":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="normal")
        tbKelvin.config(state="disabled")

def btnCalcular_Click():
    try:
        if rbSeleccion.get() == "Celsius":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            celsius = float(tbCelsius.get())
            print(celsius)
            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))
            kelvin = celsius + 273.0
            print(kelvin)
            tbKelvin.insert(0, str(round(kelvin, 2)))

        elif rbSeleccion.get() == "Kelvin":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            kelvin = float(tbKelvin.get())
            celsius = kelvin - 273.0
            tbCelsius.insert(0, str(round(celsius, 2)))
            print(celsius)
            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))

        elif rbSeleccion.get() == "Fahrenheit":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            farenheinth = float(tbFahrenheit.get())
            print(farenheinth)
            celsius = (farenheinth - 32.0) * 5.0 / 9.0
            print(celsius)
            kelvin = celsius + 273.0
            print(kelvin)
            tbCelsius.insert(0, str(round(celsius, 2)))
            tbKelvin.insert(0, str(round(kelvin, 2)))
        else:
            messagebox.showwarning(
                "Temperatura Seleccionada",
                "Seleccione una temperatura de entrada (Kelvin/Fahrenheit/Celsius)."
            )

    except ValueError:
        messagebox.showerror("Error", "Ingrese un numero valido en el campo habilitado.")

def btnLimpiar_Click():
    tbKelvin.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)

    tbCelsius.config(state="normal")
    tbFahrenheit.config(state="normal")
    tbKelvin.config(state="normal")
    rbSeleccion.set("")

ventana = tk.Tk()
ventana.title("Actividad 03 - Conversor Temperatura")
ventana.geometry("350x400")
ventana.configure(bg="Purple")

rbSeleccion = tk.StringVar(value="")

tk.Label(ventana, text="Temp. en Celsius:", font=("Segoe UI", 10, "bold")).pack()
tbCelsius = tk.Entry(ventana, width=18, justify="center")
tbCelsius.pack()

tk.Label(ventana, text="Temp. en Fahrenheit:", font=("Segoe UI", 10, "bold")).pack()
tbFahrenheit = tk.Entry(ventana, width=18, justify="center")
tbFahrenheit.pack()

tk.Label(ventana, text="Temp. en Kelvin:", font=("Segoe UI", 10, "bold")).pack()
tbKelvin = tk.Entry(ventana, width=18, justify="center")
tbKelvin.pack()

gb = tk.LabelFrame(ventana, text="Seleccione Temperatura de Entrada:", padx=12, pady=10)
gb.pack()

rbKelvin = tk.Radiobutton(gb, text="Kelvin", value="Kelvin", variable=rbSeleccion, command=radioButton_Selected)
rbKelvin.pack()

rbFahrenheit = tk.Radiobutton(gb, text="Fahrenheit", value="Fahrenheit", variable=rbSeleccion, command=radioButton_Selected)
rbFahrenheit.pack()

rbCelsius = tk.Radiobutton(gb, text="Celsius", value="Celsius", variable=rbSeleccion, command=radioButton_Selected)
rbCelsius.pack()

btnCalcular = tk.Button(ventana, text="Calcular", width=12, bg="#7CFC00", command=btnCalcular_Click, padx=6, pady=5)
btnCalcular.pack()

btnLimpiar = tk.Button(ventana, text="Limpiar", width=12, bg="#FF3030", fg="white", command=btnLimpiar_Click, padx=6, pady=5)
btnLimpiar.pack()

tbCelsius.config(state="normal")
tbFahrenheit.config(state="normal")
tbKelvin.config(state="normal")

ventana.mainloop()
