"""
Conversor de temperatura (Celsius / Fahrenheit / Kelvin) con Tkinter.

El usuario selecciona la escala de entrada mediante los radio buttons;
solo ese campo queda habilitado para escribir el valor. Al presionar
"Calcular" se obtienen las otras dos escalas equivalentes.
"""

import tkinter as tk
from tkinter import messagebox


# ----------------------------------------------------------------------
# Funciones auxiliares de conversión.
# Se extraen las fórmulas para eliminar la duplicación que existía en
# los distintos bloques de btnCalcular_Click.
# ----------------------------------------------------------------------

def _celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0


def _celsius_a_kelvin(celsius):
    """Convierte grados Celsius a Kelvin."""
    return celsius + 273.0


def _kelvin_a_celsius(kelvin):
    """Convierte grados Kelvin a Celsius."""
    return kelvin - 273.0


def _fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32.0) * 5.0 / 9.0


# ----------------------------------------------------------------------
# Funciones auxiliares de estado de los campos.
# ----------------------------------------------------------------------

def _habilitar_todos_los_campos():
    """Habilita los tres campos de temperatura (necesario para poder
    escribir en ellos los resultados calculados)."""
    tbCelsius.config(state="normal")
    tbFahrenheit.config(state="normal")
    tbKelvin.config(state="normal")


def _actualizar_estado_campos(campo_habilitado):
    """Deja habilitado únicamente 'campo_habilitado' y deshabilita los otros dos."""
    for campo in (tbCelsius, tbFahrenheit, tbKelvin):
        campo.config(state="normal" if campo is campo_habilitado else "disabled")


# ----------------------------------------------------------------------
# Callbacks de la interfaz (nombres y firmas originales sin modificar).
# ----------------------------------------------------------------------

def radioButton_Selected():
    """Habilita el campo correspondiente a la escala seleccionada y
    deshabilita los otros dos."""
    sel = rbSeleccion.get()

    if sel == "Celsius":
        _actualizar_estado_campos(tbCelsius)
    elif sel == "Kelvin":
        _actualizar_estado_campos(tbKelvin)
    elif sel == "Fahrenheit":
        _actualizar_estado_campos(tbFahrenheit)


def btnCalcular_Click():
    """Calcula la conversión de temperatura a partir del valor ingresado
    en el campo habilitado según la escala seleccionada."""
    try:
        seleccion = rbSeleccion.get()

        if seleccion == "Celsius":
            _habilitar_todos_los_campos()
            celsius = float(tbCelsius.get())
            farenheintt = _celsius_a_fahrenheit(celsius)
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))
            kelvin = _celsius_a_kelvin(celsius)
            tbKelvin.insert(0, str(round(kelvin, 2)))

        elif seleccion == "Kelvin":
            _habilitar_todos_los_campos()
            kelvin = float(tbKelvin.get())
            celsius = _kelvin_a_celsius(kelvin)
            tbCelsius.insert(0, str(round(celsius, 2)))
            farenheintt = _celsius_a_fahrenheit(celsius)
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))
               
        elif seleccion == "Fahrenheit":
            _habilitar_todos_los_campos()
            farenheinth = float(tbFahrenheit.get())
            celsius = _fahrenheit_a_celsius(farenheinth)
            kelvin = _celsius_a_kelvin(celsius)
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
    """Limpia los tres campos de temperatura, los vuelve a habilitar y
    deselecciona la escala de entrada."""
    tbKelvin.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)

    _habilitar_todos_los_campos()
    rbSeleccion.set("")


# ----------------------------------------------------------------------
# Funciones auxiliares de construcción de la interfaz.
# Evitan repetir el mismo bloque de creación de widgets para cada
# campo de texto, radio button y botón.
# ----------------------------------------------------------------------

def _crear_campo_temperatura(texto_etiqueta):
    """Crea la etiqueta y el campo de entrada centrado para una escala de temperatura."""
    tk.Label(ventana, text=texto_etiqueta, font=("Segoe UI", 10, "bold")).pack()
    campo = tk.Entry(ventana, width=18, justify="center")
    campo.pack()
    return campo


def _crear_radio_temperatura(texto, valor):
    """Crea un radio button de selección de escala dentro del LabelFrame."""
    boton_radio = tk.Radiobutton(
        gb, text=texto, value=valor, variable=rbSeleccion, command=radioButton_Selected
    )
    boton_radio.pack()
    return boton_radio


def _crear_boton(texto, color_fondo, comando, color_texto=None):
    """Crea un botón de acción con el estilo indicado."""
    opciones = {"text": texto, "width": 12, "bg": color_fondo, "command": comando, "padx": 6, "pady": 5}
    if color_texto:
        opciones["fg"] = color_texto

    boton = tk.Button(ventana, **opciones)
    boton.pack()
    return boton


# ----------------------------------------------------------------------
# Construcción de la ventana principal.
# ----------------------------------------------------------------------

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Actividad 03 - Conversor Temperatura")
    ventana.geometry("350x400")
    ventana.configure(bg="Purple")

    rbSeleccion = tk.StringVar(value="")

    tbCelsius = _crear_campo_temperatura("Temp. en Celsius:")
    tbFahrenheit = _crear_campo_temperatura("Temp. en Fahrenheit:")
    tbKelvin = _crear_campo_temperatura("Temp. en Kelvin:")

    gb = tk.LabelFrame(ventana, text="Seleccione Temperatura de Entrada:", padx=12, pady=10)
    gb.pack()

    rbKelvin = _crear_radio_temperatura("Kelvin", "Kelvin")
    rbFahrenheit = _crear_radio_temperatura("Fahrenheit", "Fahrenheit")
    rbCelsius = _crear_radio_temperatura("Celsius", "Celsius")

    btnCalcular = _crear_boton("Calcular", "#7CFC00", btnCalcular_Click)
    btnLimpiar = _crear_boton("Limpiar", "#FF3030", btnLimpiar_Click, color_texto="white")

    _habilitar_todos_los_campos()

    ventana.mainloop()