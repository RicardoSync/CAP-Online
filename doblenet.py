import mysql.connector
from tkinter import messagebox

def conexion_logica(db_name):
    return mysql.connector.connect(
        host="200.234.224.17",
        user="ciso",
        password="ciso",
        database=db_name,
        port=3389
    )

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

def consultar_paquetes(db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos conectar el modulo (Consulta de paquetes), error: {err}")
    
    escobedo = doblenet.cursor()
    escobedo.execute("SELECT nombre, velocidad, precio FROM paquetes")
    resultado_paquetes = escobedo.fetchall()

    escobedo.close()
    return resultado_paquetes

def insertar_elementos_paquetes(nombre, velocidad, precio, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos conectar el modulo (Insertar Elementos en Paquetes), error {err}")

    escobedo = doblenet.cursor()
    sql = "INSERT INTO paquetes (nombre, velocidad, precio) VALUES (%s, %s, %s)"
    valores = (nombre, velocidad, precio)

    escobedo.execute(sql, valores)
    doblenet.commit()
    doblenet.close()

    messagebox.showinfo("CAP-Online", f"{escobedo.rowcount} elemento(s) afectado(s)")
    escobedo.close()

def buscar_paquetes(nombre, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenenmos un error al conectar en el modulo (Buscar Paquetes), error {err}")
    
    escobedo = doblenet.cursor()
    sql = "SELECT nombre, velocidad, precio FROM paquetes WHERE nombre = %s"
    valores = (nombre, )

    escobedo.execute(sql, valores)

    resultado_paquetes_nombre = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return resultado_paquetes_nombre 


def eliminar_paquete(nombre, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenemos un error en el modulo (Eliminar Paquetes), error {err}")

    escobedo = doblenet.cursor()

    sql = "DELETE FROM paquetes WHERE nombre = %s"
    valores = (nombre, )

    escobedo.execute(sql, valores)
    doblenet.commit()
    doblenet.close()

    messagebox.showinfo("CAP-Online", f"{escobedo.rowcount} elemento(s) fueron afectado(s)")
    escobedo.close()

