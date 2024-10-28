from customtkinter import CTkFrame, CTkEntry, CTkComboBox, CTkButton, CTkToplevel, CTkLabel
from tkinter import ttk, messagebox, END
from doblenet import consultar_pagos, insertar_pago, buscar_pago, buscar_pago_clave
import customtkinter
from recursos import colores_ui

resultado_pago = []
resultado_pago_clave = []

def insetar_datos_tabla(tablaPagos, db_name):
    datos_pagos = consultar_pagos(db_name)

    tablaPagos.delete(*tablaPagos.get_children())

    for consulta_pagos in datos_pagos:
        tablaPagos.insert("", "end", values=consulta_pagos)

def md_pagos_ui(db_name):
    pagosWindows = CTkToplevel()
    pagosWindows.title("Modelo Pagos")
    pagosWindows.geometry("700x500")
    pagosWindows.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    colores = colores_ui()

    #iniciamos funciones busqueda, registro de pago y mas detalles 
    def busqueda_pago():
        if len(nombreEnt.get()) >0:
            nombre = nombreEnt.get()
            datos_pago_cliente = buscar_pago(nombre, db_name)
            if len(datos_pago_cliente) >0:
                global resultado_pago
                resultado_pago = datos_pago_cliente
            else:
                messagebox.showerror("CAP-Online", f"No tenemos ningun dato de la busqueda: {nombre}")

        elif len(claveEnt.get()) > 0:
            clave = claveEnt.get()
            datos_pago_cliente = buscar_pago_clave(clave, db_name)
            if len(datos_pago_cliente) > 0:
                global resultado_pago_clave
                resultado_pago_clave = datos_pago_cliente
            else:
                messagebox.showerror("CAP-Online", f"No tenemos ningun dato de la busqueda: {nombre}")



    #contenedor de la tabla
    contenedor_tabla = CTkFrame(pagosWindows, border_color=colores["marcos"], border_width=2, 
                                corner_radius=2, fg_color="black")
    contenedor_buscador = CTkFrame(pagosWindows, border_color=colores["marcos"], border_width=2,
                                corner_radius=2, fg_color=colores["enfasis"])
    

    #creacion de la tabla
    tablaPagos = ttk.Treeview(contenedor_tabla, columns=("Nombre", "Clave", "Plan", "Mensualidad", "Ultimo Pago", "Proximo Pago"), show="headings")
    tablaPagos.heading("Nombre", text="Nombre")
    tablaPagos.heading("Clave", text="Clave")
    tablaPagos.heading("Plan", text="Plan")
    tablaPagos.heading("Mensualidad", text="Mensualidad")
    tablaPagos.heading("Ultimo Pago", text="Ultimo Pago")
    tablaPagos.heading("Proximo Pago", text="Proximo Pago")

    tablaPagos.column("Nombre", width=100)
    tablaPagos.column("Clave", width=100)
    tablaPagos.column("Plan", width=100)
    tablaPagos.column("Mensualidad", width=100)
    tablaPagos.column("Ultimo Pago", width=100)
    tablaPagos.column("Proximo Pago", width=100)

    #creacion de los elementos para la busqueda por nombre o indentificador de los valores
    nombreEnt = CTkEntry(contenedor_buscador, border_color=colores["marcos"],
                        placeholder_text="Nombre de cliente",
                        border_width=2, corner_radius=2)

    claveEnt = CTkEntry(contenedor_buscador, border_color=colores["marcos"],
                        placeholder_text="Identidicador cliente",
                        border_width=2, corner_radius=2)

    btnBuscar = CTkButton(contenedor_buscador, text="Buscar", border_color=colores["marcos"],
                        border_width=2, corner_radius=2, fg_color=colores["botones"],
                        command=busqueda_pago)


    contenedor_tabla.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.9)
    tablaPagos.pack(fill="both", expand=True)

    contenedor_buscador.place(relx=0.0, rely=0.9, relwidth=1.0, relheight=0.1)
    nombreEnt.grid(column=0, row=0, padx=10, pady=10)
    claveEnt.grid(column=1, row=0, padx=10, pady=10)
    btnBuscar.grid(column=2, row=0, padx=10, pady=10)

    #Iniciamos funciones principales
    insetar_datos_tabla(tablaPagos, db_name)

    pagosWindows.mainloop()
