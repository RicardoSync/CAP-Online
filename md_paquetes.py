from doblenet import consultar_paquetes, insertar_elementos_paquetes, buscar_paquetes, eliminar_paquete
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkToplevel
import customtkinter
from tkinter import ttk, messagebox, END
from recursos import colores_ui, imagenes, fuentes

#definimos los recursos
ui_colores = colores_ui()
ui_iconos = imagenes()
ui_fuentes = fuentes()

#funcion para buscar e insertar los datos en tabla
def get_datos(tabla, db_name):
    datos = consultar_paquetes(db_name)

    tabla.delete(*tabla.get_children())

    for resultado_paquetes in datos:
        tabla.insert("", "end", values=resultado_paquetes)
    

def md_paquetes_ui(db_name):
    paquetesWindoes = CTkToplevel()
    paquetesWindoes.title("Modulo Paquetes")
    paquetesWindoes.geometry("700x600")
    paquetesWindoes.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")


    #funciones que llaman los valores
    def limpieza():
        nombreent.delete(0, END)
        velocidadent.delete(0, END)
        precioent.delete(0, END)


    def actualiar_tabla():
        get_datos(tabla, db_name)
    
    def insertar_elementos():
        if len(nombreent.get()) > 0:
            nombre = nombreent.get()
            velocidad = velocidadent.get()
            precio = precioent.get()

            insertar_elementos_paquetes(nombre, velocidad, precio, db_name)
            limpieza()
            actualiar_tabla()
        
        else:
            messagebox.showerror("CAP-Online", "Por favor ingrese un nombre, no deje el campo vacio")

    def buscar_elementos():
        if len(nombreent.get()) > 0:
            nombre = nombreent.get()
            resultado_busqueda = buscar_paquetes(nombre, db_name)
            if len(resultado_busqueda) > 0:
                limpieza()
                nombreent.insert(0, resultado_busqueda[0][0])
                velocidadent.insert(0, resultado_busqueda[0][1])
                precioent.insert(0, resultado_busqueda[0][2])
                btnEliminar.place(relx=0.74, rely=0.3)

            else:
                messagebox.showerror("CAP-Online", "No encontramos ningun elemento con ese nombre, intenta con otro")

        else:
            messagebox.showerror("CAP-Online", "Por favor ingresa un nombre para buscar, no dejes el campo vacio")
        
    def eliminar_elementos():
        pregunta = messagebox.askyesno("CAP-Online", "Estas seguro que quieres eliminar el elmento?")

        if pregunta == True:
            if len(nombreent.get()) > 0:
                nombre = nombreent.get()
                eliminar_paquete(nombre, db_name)
            else:
                messagebox.showerror("CAP-Online", "Antes de eliminar, procura que el campo del nombre no este vacio")
        else:
            messagebox.showinfo("CAP-Online", 'No se elimino ningun elemento')
    
    #contenedor de la tabla
    contenedor_tabla = CTkFrame(paquetesWindoes, border_color=ui_colores["marcos"], border_width=2,
                                corner_radius=2, fg_color=ui_colores["enfasis"])
    
    contenedor_formulario = CTkFrame(paquetesWindoes, border_color=ui_colores["marcos"], border_width=2,
                                    corner_radius=2, fg_color=ui_colores["enfasis"])
    

    #creamos la tabla
    tabla = ttk.Treeview(contenedor_tabla, columns=("Nombre", "Velocidad", "Precio"), show="headings")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Velocidad", text="Velocidad")
    tabla.heading("Precio", text="Precio")

    tabla.column("Nombre", width=100)
    tabla.column("Velocidad", width=100)
    tabla.column("Precio", width=100)

    
    #botones que vamos a usar Guardar, Limpiar, Buscar, Eliminar y Refrescar
    btnGuardar = CTkButton(contenedor_formulario, text="Guardar", border_color=ui_colores["marcos"],
                        border_width=2, fg_color=ui_colores["botones"],
                        command=insertar_elementos)
    
    btnLimpiar = CTkButton(contenedor_formulario, text="Limpiar", border_color=ui_colores["marcos"],
                        border_width=2, fg_color=ui_colores["botones"],
                        command=limpieza)
    
    btnBuscar = CTkButton(contenedor_formulario, text="Buscar", border_color=ui_colores['marcos'],
                        border_width=2, fg_color=ui_colores["botones"],
                        command=buscar_elementos)
    
    btnRefrescar = CTkButton(contenedor_tabla, text="Recargar", border_color=ui_colores["marcos"],
                            border_width=2, fg_color=ui_colores["actualizar"],
                            command=actualiar_tabla)
    
    btnEliminar = CTkButton(contenedor_tabla, text="Eliminar", border_color=ui_colores["marcos"],
                            border_width=2, fg_color=ui_colores["eliminar"],
                            command=eliminar_elementos)
    

    #elementos del formulario
    nombrelb = CTkLabel(contenedor_formulario, text="Nombre", font=ui_fuentes["etiqueta"])
    nombreent = CTkEntry(contenedor_formulario, placeholder_text="Paquete Basico", border_color=ui_colores["marcos"],
                        border_width=2, width=200)
    
    velocidadlb = CTkLabel(contenedor_formulario, text="Velocidad Disponible", font=ui_fuentes["etiqueta"])
    velocidadent = CTkEntry(contenedor_formulario, placeholder_text="100M/40M", border_color=ui_colores["marcos"],
                            border_width=2, width=200)
    
    preciolb = CTkLabel(contenedor_formulario, text="Precio Mensual", font=ui_fuentes["etiqueta"])
    precioent = CTkEntry(contenedor_formulario, placeholder_text="300", border_color=ui_colores["marcos"],
                        border_width=2, width=200)
    

    #poscion de los elementos
    contenedor_tabla.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.4)
    tabla.place(relx=0.1, rely=0.1, relwidth=0.6, relheight=0.8)
    btnRefrescar.place(relx=0.74, rely=0.1)

    contenedor_formulario.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
    nombrelb.grid(column=0, row=0, padx=10, pady=10)
    nombreent.grid(column=1, row=0, padx=10, pady=10)

    velocidadlb.grid(column=0, row=1, padx=10, pady=10)
    velocidadent.grid(column=1, row=1, padx=10, pady=10)
    preciolb.grid(column=0, row=2, padx=10, pady=10)
    precioent.grid(column=1, row=2, padx=10, pady=10)

    btnBuscar.grid(column=0, row=3, padx=10, pady=10)
    btnGuardar.grid(column=1, row=3, padx=10, pady=10)
    btnLimpiar.grid(column=2, row=3, padx=10, pady=10)
    get_datos(tabla, db_name)
    paquetesWindoes.mainloop()


