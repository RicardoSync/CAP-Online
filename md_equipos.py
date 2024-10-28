from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkToplevel
from tkinter import messagebox, ttk, END
from recursos import colores_ui, fuentes
import customtkinter
from doblenet import consultar_modems, insertar_modem, buscar_modem, eliminar_modem, consultar_antena, insertar_antena, buscar_antena, eliminar_antena
#obtenemos los elementos basicos
ui_colores = colores_ui()
ui_fuentes = fuentes()

def get_datos_modem(tablaModem, db_name):
    datos = consultar_modems(db_name)

    tablaModem.delete(*tablaModem.get_children())

    for cosulta_modem_resultado in datos:
        tablaModem.insert("", "end", values=cosulta_modem_resultado)

def get_datos_antenas(tablaAntenas, db_name):
    datos_antena = consultar_antena(db_name)

    tablaAntenas.delete(*tablaAntenas.get_children())

    for consulta_antena in datos_antena:
        tablaAntenas.insert("", "end", values=consulta_antena)


#iniciamos la ventana
def md_equipos_ui(db_name):    
    equiposWindows = CTkToplevel()
    equiposWindows.title("Modulo Equipos")
    equiposWindows.geometry("700x500")
    equiposWindows.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    #funciones basicas
    def almacenar_modem():
        if len(nombreModem.get()) > 0:
            nombre = nombreModem.get()
            modelo = modeloModem.get()
            insertar_modem(nombre, modelo, db_name)
            nombreModem.delete(0, END)
            modeloModem.delete(0, END)
            get_datos_modem(tablaModem, db_name)
        else:
            messagebox.showerror("CAP-Online", "Ingresa un nombre, no dejes vacio el campo")
    
    def busqueda_chida():
        if len(nombreModem.get()) > 0:
            nombre = nombreModem.get()
            nombreModem.delete(0, END)
            modeloModem.delete(0, END)

            resultado = buscar_modem(nombre, db_name)

            if len(resultado) > 0:
                nombreModem.insert(0, resultado[0][0])
                modeloModem.insert(0, resultado[0][1])
                btnEliminar.place(relx=0.50, rely=0.70, relwidth=0.45)
        else:
            messagebox.showerror("CAP-Online", "No podemos buscar un nombre vacio, llena el campo")
    
    def eliminar_informacion():
        if len(nombreModem.get()) > 0:
            nombre = nombreModem.get()
            eliminar_modem(nombre, db_name)
            nombreModem.delete(0, END)
            modeloModem.delete(0, END)
            get_datos_modem(tablaModem, db_name)

        else:
            messagebox.showerror("CAP-Online", "Lo siento no podemos eliminar nada si no tenemos un nombre :(")
    
    def insertar_antena_db():
        if len(nombreAntena.get()) > 0:
            nombre = nombreAntena.get()
            modelo = modeloAntena.get()
            insertar_antena(nombre, modelo, db_name)
            get_datos_antenas(tablaAntenas, db_name)
            nombreAntena.delete(0, END)
            modeloAntena.delete(0, END)
        else:
            messagebox.showerror("CAP-Online", "No podemos almacenar una antena sin nombre, ingresa uno")
    
    def buscar_antena_db():
        if len(nombreAntena.get()) > 0:
            nombre = nombreAntena.get()
            busqueda = buscar_antena(nombre, db_name)

            if len(busqueda) > 0:
                nombreAntena.delete(0, END)
                modeloAntena.delete(0, END)

                nombreAntena.insert(0, busqueda[0][0])
                modeloAntena.insert(0, busqueda[0][1])
                btnEliminar_antena.place(relx=0.50, rely=0.70, relwidth=0.45)

            else:
                messagebox.showerror("CAP-Online", "No podemos encontrar ningun elemento")
        else:
            messagebox.showerror("CAP-Online", "No podemos buscar ninguna antena, si no tenemos antena")

    def eliminacion_antenas():
        if len(nombreAntena.get()) > 0:
            nombre = nombreAntena.get()
            eliminar_antena(nombre, db_name)
            nombreAntena.delete(0, END)
            modeloAntena.delete(0, END)
            get_datos_antenas(tablaAntenas, db_name)
        else:
            messagebox.showerror("CAP-Online", "No podemos elimnar un nombre en vacio, ingresa uno")
            
    #creamos el contenedor de modem
    contenedor_modem = CTkFrame(equiposWindows, border_color=ui_colores["marcos"], border_width=2,
                                corner_radius=2, fg_color=ui_colores["enfasis"])
    
    #creamos el contenedor de las antenas
    contenedor_antenas = CTkFrame(equiposWindows, border_color=ui_colores["marcos"], border_width=2,
                                corner_radius=2, fg_color=ui_colores["enfasis"])
    
    #creamos la tabla de modems
    tablaModem = ttk.Treeview(contenedor_modem, columns=("Nombre", "Modelo"), show="headings")
    tablaModem.heading("Nombre", text="Nombre")
    tablaModem.heading("Modelo", text="Modelo")

    tablaModem.column("Nombre", width=150)
    tablaModem.column("Modelo", width=150)

    #creamos los botones de los modems
    btnAgregar = CTkButton(contenedor_modem, text="Agregar", border_color=ui_colores["marcos"], border_width=2,
                        fg_color=ui_colores["botones"],
                        command=almacenar_modem)

    btnBuscar = CTkButton(contenedor_modem, text="Buscar", border_color=ui_colores["marcos"], border_width=2,
                        fg_color=ui_colores["botones"],
                        command=busqueda_chida)
    
    btnEliminar = CTkButton(contenedor_modem, text="Eliminar", border_color=ui_colores["marcos"], border_width=2,
                            fg_color=ui_colores["eliminar"],
                            command=eliminar_informacion)
    
    labelModem = CTkLabel(contenedor_modem, text="Datos Modem / Router", font=ui_fuentes["titulos"])
    
    #creamos las entradas
    nombreModem = CTkEntry(contenedor_modem, placeholder_text="Nombre del router", border_color=ui_colores["marcos"],
                        border_width=2)
    modeloModem = CTkEntry(contenedor_modem, placeholder_text="Modelo del roter", border_color=ui_colores["marcos"],
                        border_width=2)
    

    #creamos la tabla de antenas
    tablaAntenas = ttk.Treeview(contenedor_antenas, columns=("Nombre", "Modelo"), show="headings")
    tablaAntenas.heading("Nombre", text="Nombre")
    tablaAntenas.heading("Modelo", text="Modelo")

    tablaAntenas.column("Nombre", width=150)
    tablaAntenas.column("Modelo", width=150)

    #creamos los botones de los modems
    labelAntena = CTkLabel(contenedor_antenas, text="Datos Antena", font=ui_fuentes["titulos"])

    btnAgregar_antena = CTkButton(contenedor_antenas, text="Agregar", border_color=ui_colores["marcos"], border_width=2,
                        fg_color=ui_colores["botones"],
                        command=insertar_antena_db)

    btnBuscar_antena = CTkButton(contenedor_antenas, text="Buscar", border_color=ui_colores["marcos"], border_width=2,
                        fg_color=ui_colores["botones"],
                        command=buscar_antena_db)
    
    btnEliminar_antena = CTkButton(contenedor_antenas, text="Eliminar", border_color=ui_colores["marcos"], border_width=2,
                            fg_color=ui_colores["eliminar"],
                            command=eliminacion_antenas)
    
    #creamos las entradas
    nombreAntena = CTkEntry(contenedor_antenas, placeholder_text="Nombre de la antena", border_color=ui_colores["marcos"],
                        border_width=2)
    modeloAntena = CTkEntry(contenedor_antenas, placeholder_text="Modelo de la antena", border_color=ui_colores["marcos"],
                        border_width=2)

    #llamamos a las funciones principales
    get_datos_modem(tablaModem, db_name)
    get_datos_antenas(tablaAntenas, db_name)


    #posiciones de los elementos
    contenedor_modem.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.5)
    tablaModem.place(relx=0.05, rely=0.10)
    labelModem.place(relx=0.50, rely=0.10)
    nombreModem.place(relx=0.50, rely=0.30, relwidth=0.20)
    modeloModem.place(relx=0.75, rely=0.30, relwidth=0.20)
    btnAgregar.place(relx=0.50, rely=0.50, relwidth=0.20)
    btnBuscar.place(relx=0.75, rely=0.50, relwidth=0.20)

    contenedor_antenas.place(relx=0.0, rely=0.5, relwidth=1.0, relheight=0.5)
    tablaAntenas.place(relx=0.05, rely=0.10)
    labelAntena.place(relx=0.50, rely=0.10)
    nombreAntena.place(relx=0.50, rely=0.30, relwidth=0.20)
    modeloAntena.place(relx=0.75, rely=0.30, relwidth=0.20)
    btnAgregar_antena.place(relx=0.50, rely=0.50, relwidth=0.20)
    btnBuscar_antena.place(relx=0.75, rely=0.50, relwidth=0.20)

    equiposWindows.mainloop()
