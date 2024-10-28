import tkinter as tk
from tkinter import ttk

# Función para obtener la información de la fila seleccionada
def obtener_fila_seleccionada():
    # Obtener el ID de la fila seleccionada
    seleccion = tree.selection()
    if seleccion:
        # Obtener los valores de la fila seleccionada
        valores = tree.item(seleccion[0], "values")
        print("Valores de la fila seleccionada:", valores)
    else:
        print("No hay ninguna fila seleccionada.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Configuración del Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")
tree.heading("col1", text="Columna 1")
tree.heading("col2", text="Columna 2")
tree.heading("col3", text="Columna 3")

# Agregar algunas filas
tree.insert("", "end", values=("Dato 1", "Dato 2", "Dato 3"))
tree.insert("", "end", values=("Dato 4", "Dato 5", "Dato 6"))
tree.insert("", "end", values=("Dato 7", "Dato 8", "Dato 9"))

# Colocar el Treeview en la ventana
tree.pack()

# Botón para obtener la fila seleccionada
boton = tk.Button(root, text="Obtener Fila Seleccionada", command=obtener_fila_seleccionada)
boton.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()
