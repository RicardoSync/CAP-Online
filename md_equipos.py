from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkFrame, CTk
from recursos import imagenes, colores_ui, fuentes
import customtkinter

#llamamos los recursos
ui_colores = colores_ui()
ui_fuentes = fuentes()

def md_equipos_ui(db_name):
	equiposWindows = customtkinter.CTk()
	equiposWindows.title("Modulo Equipos")
	equiposWindows.geometry("700x500")
	equiposWindows.resizable(False, False)
	customtkinter.set_appearance_mode("dark")
	customtkinter.set_default_color_theme("blue")

	#contenedores
	contenedor_antenas = CTkFrame(equiposWindows, border_color=ui_colores["marcos"])