from customtkinter import CTkButton, CTkLabel, CTkFrame, CTk
import customtkinter
from recursos import colores_ui, imagenes

from md_paquetes import md_paquetes_ui
from md_equipos import md_equipos_ui
from md_pagos import md_pagos_ui

#cargamos los elementos
ui_colores = colores_ui()
ui_iconos = imagenes()


def md_panel_ui(loginWindows, username, db_name):
    loginWindows.destroy()

    panelWindows = CTk()
    panelWindows.title(f"Panel de Administrador para: {username}, conexion {db_name}")
    panelWindows.geometry("900x550")
    panelWindows.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    #funciones para enviar los valores
    def llamar_modulo_paquetes():
        md_paquetes_ui(db_name)
    
    def llamar_modulo_equipos():
        md_equipos_ui(db_name)
    
    def llamar_modulo_pagos():
        md_pagos_ui(db_name)
    
    #creamos los contenedores
    contenedor_opciones = CTkFrame(panelWindows, border_color=ui_colores["marcos"], border_width=2,
                                   corner_radius=2, fg_color=ui_colores["enfasis"])

    contenedor_imagen = CTkFrame(panelWindows, border_color=ui_colores["marcos"], border_width=2,
                                 corner_radius=2, fg_color="transparent")

    fondo = CTkLabel(contenedor_imagen, text="", image=ui_iconos["fondo_panel"])

    #elementos de las opciones (botones) 
    #1.- Crear cliente
    #2.- Registrar pago
    #3.- Crear paquetes
    #4-. Crear equipos
    btnCrearCliente = CTkButton(contenedor_opciones, text="Clientes", image=ui_iconos["crear-cliente"],
                                border_color=ui_colores["marcos"],
                                border_width=2,
                                fg_color=ui_colores["botones"])

    btnRegistrarPago = CTkButton(contenedor_opciones, text="Pagos", image=ui_iconos["registrar-pago"],
                                border_color=ui_colores["marcos"],
                                border_width=2,
                                fg_color=ui_colores["botones"],
                                command=llamar_modulo_pagos)

    btnCrearPaquetes = CTkButton(contenedor_opciones, text="Paquetes", image=ui_iconos["crear-paquete"],
                                border_color=ui_colores["marcos"],
                                border_width=2,
                                fg_color=ui_colores["botones"],
                                command=llamar_modulo_paquetes)

    btnCrearEquipos = CTkButton(contenedor_opciones, text="Equipos", image=ui_iconos["crear-equipos"],
                                border_color=ui_colores["marcos"],
                                border_width=2,
                                fg_color=ui_colores["botones"],
                                command=llamar_modulo_equipos)


    #posicion de los elementos
    contenedor_opciones.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    btnCrearCliente.pack(padx=10, pady=10)
    btnRegistrarPago.pack(padx=10, pady=10)
    btnCrearPaquetes.pack(padx=10, pady=10)
    btnCrearEquipos.pack(padx=10, pady=10)

    contenedor_imagen.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    fondo.pack(padx=2, pady=2)
    panelWindows.mainloop()