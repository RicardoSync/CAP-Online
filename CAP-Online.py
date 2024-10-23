from recursos import imagenes, colores_ui, fuentes
import customtkinter
from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkLabel
from doblenet import login
from tkinter import messagebox

from md_panel import md_panel_ui

#funcion de inicio de sesion
def get_datos():
    if len(nombreent.get()) > 0:
        username = nombreent.get()
        password = claveent.get()

        db_name = login(username, password)

        if db_name:
            md_panel_ui(loginWindows, username, db_name)
        else:
            messagebox.showerror("CAP-Online", "Usuario o clave incorrectos")
    else:
        messagebox.showerror("CAP-Online", "Ingresa un usuario, no dejes el campo vaio")


#inicio de sesion
loginWindows = customtkinter.CTk()
loginWindows.title("Inicio de Sesion")
loginWindows.geometry("700x500")
loginWindows.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


#cargamos el fondo
ui_iconos = imagenes()
ui_colores = colores_ui()
ui_fuente = fuentes()

#contenedores de los elementos
contenedo_imagen = CTkFrame(loginWindows, border_color=ui_colores["marcos"], border_width=2,
                            corner_radius=2, fg_color="transparent")

contenedor_formulario = CTkFrame(loginWindows, border_color=ui_colores["marcos"], border_width=2,
                                 corner_radius=2, fg_color=ui_colores["enfasis"])

fondo  = CTkLabel(contenedo_imagen, text="", image=ui_iconos["fondo"])

#elementos de login formulario
titulo = CTkLabel(contenedor_formulario, text="CAP-Online", 
                  font=ui_fuente["titulos"])

nombrelb = CTkLabel(contenedor_formulario, text=("Nombre de usuario"),
                    font=ui_fuente["etiqueta"])

nombreent = CTkEntry(contenedor_formulario, placeholder_text="usuario@doblenet.com",
                     width=200, border_color=ui_colores["entradas"],
                     border_width=2)

clavelb =  CTkLabel(contenedor_formulario, text="Contrasena",
                    font=ui_fuente["etiqueta"])

claveent = CTkEntry(contenedor_formulario, placeholder_text="password",
                    show="*", width=200,
                    border_color=ui_colores["entradas"],
                    border_width=2)

btnInicio = CTkButton(contenedor_formulario, text="Iniciar Sesion",
                      border_color=ui_colores["marcos"],
                      border_width=2,
                      fg_color=ui_colores["botones"],
                      command=get_datos)


#posicion de los elementos
contenedo_imagen.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
fondo.pack(padx=2, pady=2)
contenedor_formulario.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
titulo.pack(padx=10, pady=4)
nombrelb.pack(padx=10, pady=10)
nombreent.pack(padx=10, pady=5)
clavelb.pack(padx=10, pady=10)
claveent.pack(padx=10, pady=5)
btnInicio.pack(padx=10, pady=5)
loginWindows.mainloop()