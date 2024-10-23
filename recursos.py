import mysql.connector
from PIL import Image
from customtkinter import CTkImage

def conexion_db():
    return mysql.connector.connect(
        host="200.234.224.17",
        user="ciso",
        password="ciso",
        database="spider-user",
        port=3389
    )

def colores_ui():
    colores = {
        "enfasis": "#023E73",
        "botones": "#0487D9",
        "marcos": "#F2D544",
        "entradas": "#D9AA52",
        "eliminar": "#FF0202",
        "actualizar": "#51A402"
    }
    return colores

def imagenes():
    iconos = {
        "fondo" : CTkImage(light_image=Image.open("img/fondo.jpeg"),
                         dark_image=Image.open("img/fondo.jpeg"),
                         size=(700, 500)),

        "fondo_panel" : CTkImage(light_image=Image.open("img/fondo.jpeg"),
                         dark_image=Image.open("img/fondo.jpeg"),
                         size=(900, 560)),

        "crear-cliente": CTkImage(light_image=Image.open("img/crear-cliente.png"),
                                  dark_image=Image.open("img/crear-cliente.png"),
                                  size=(50,50)),

        "registrar-pago": CTkImage(light_image=Image.open("img/registrar-pago.png"),
                                   dark_image=Image.open("img/registrar-pago.png"),
                                   size=(50,50)),
        
        "crear-paquete": CTkImage(light_image=Image.open("img/paquetes.png"),
                                  dark_image=Image.open("img/paquetes.png"),
                                  size=(50, 50)),
        
        "crear-equipos": CTkImage(light_image=Image.open("img/equipos.png"),
                                  dark_image=Image.open("img/equipos.png"),
                                  size=(50, 50))
        
    }
    return iconos

def fuentes():
    fuentes_master = {
        "etiqueta": ("Arial", 15),
        "titulos": ("Monospace", 20, "bold")
    }
    return fuentes_master