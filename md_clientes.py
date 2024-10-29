from recursos import colores_ui
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkFrame, CTkToplevel
from tkinter import ttk, messagebox

def md_clientes_ui(db_name):
    #clave, nombre, direccion, telefono, antena, router, paquete, ip, velocidad, fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api
    """La clave del cliente se debe generar de manera automatica con random en un rango de 1 a 980.
    tanto la antena, como router deben de ser cargados desde db.
    La velocidad debe ser llenada automaticamente dependiendo del paquete que se escoja.
    La fecha instalacion debe ser automatica con la fecha del equipo, proximo pago debe ser (fechaActual + 31days).
    Estado por defecto es "Activo" y api es un numero random de 1 a 30
    """
