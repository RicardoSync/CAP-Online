import mysql.connector
from tkinter import messagebox

def login(username, password):
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host='200.234.224.17',  # Cambia esto si es necesario
            database='spider-user',
            user="ciso",
            password="ciso",
            port=3389
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT data FROM usuarios WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()

            if result:
                # Obtener el nombre de la base de datos
                database_name = result[0]
                print(f"Inicio de sesión exitoso. Base de datos: {database_name}")
                return database_name
            else:
                print("Credenciales inválidas.")
                return None

    except mysql.connector.Err as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
