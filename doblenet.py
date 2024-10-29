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

def consultar_modems(db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenemos un error en el modulo (Consultar Modems), error {err}")

    escobedo = doblenet.cursor()
    escobedo.execute("SELECT nombre, modelo FROM modem")
    cosulta_modem_resultado = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return cosulta_modem_resultado


def insertar_modem(nombre, modelo, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenemos un error al reconectar en (Modulo Insertar modem), error {err}")
    
    escobedo = doblenet.cursor()
    sql = "INSERT INTO modem (nombre, modelo) VALUES (%s, %s)"
    valores = (nombre, modelo)

    escobedo.execute(sql, valores)
    escobedo.close()
    doblenet.commit()
    doblenet.close()
    messagebox.showinfo("CAP-Online", "Se almaceno de manera correcta el modem")

def buscar_modem(nombre, db_name):
    macos = conexion_logica(db_name)

    if not macos.is_connected:
        try:
            macos.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenemos un error al reconectar en (Modulo buscar modem), error {err}")
    
    cursosr = macos.cursor()
    sql = "SELECT nombre, modelo FROM modem WHERE nombre = %s"
    valores = (nombre, )
    cursosr.execute(sql, valores)

    busqueda_modem = cursosr.fetchall()
    cursosr.close()
    macos.close()
    return busqueda_modem

def eliminar_modem(nombre, db_name):
    nicole = conexion_logica(db_name)

    if not nicole.is_connected:
        try:
            nicole.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Tenemos un error al reconectar en el (Modulo eliminar modem), error {err}")
    

    vida = nicole.cursor()
    sql = "DELETE FROM modem WHERE nombre = %s"
    valores = (nombre, )

    vida.execute(sql, valores)
    nicole.commit()

    messagebox.showerror("CAP-Online", f"{vida.rowcount} linea afectada")
    vida.close()
    nicole.close()

def consultar_antena(db_name):
    gumball = conexion_logica(db_name)

    if not gumball.is_connected:
        try:
            gumball.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Error modulo (modulo consulta antena), error {err}")
    
    darwin = gumball.cursor()
    darwin.execute("SELECT nombre, modelo FROM antenas")
    consulta_antena = darwin.fetchall()
    gumball.close()
    darwin.close()
    return consulta_antena

def insertar_antena(nombre, modelo, db_name):
    vacio = conexion_logica(db_name)
    if not vacio.is_connected:
        try:
            vacio.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Error al intentar reconectar en el modulo (Insertar Antena), error {err}")
    
    penny = vacio.cursor()
    sql = "INSERT INTO antenas (nombre, modelo) VALUES (%s, %s)"
    valores = (nombre, modelo)

    penny.execute(sql, valores)
    vacio.commit()
    penny.close()

    messagebox.showinfo("CAP-Online", "Se almaceno la antena de manera correcta")

def buscar_antena(nombre, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Fallo la reconexion en el modulo (Buscar antena), error {err}")
    
    escobedo = doblenet.cursor()
    sql = "SELECT nombre, modelo FROM antenas WHERE nombre = %s"
    valores = (nombre, )

    escobedo.execute(sql, valores)
    resultado_busqueda_antena = escobedo.fetchall()
    
    escobedo.close()
    doblenet.close()
    return resultado_busqueda_antena

def eliminar_antena(nombre, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos establecer la conexion en la eliminacion de la antena, {err}")
    
    escobedo = doblenet.cursor()
    sql = "DELETE FROM antenas WHERE nombre = %s"
    valores = (nombre, )
    escobedo.execute(sql, valores)

    doblenet.commit()
    doblenet.close()
    messagebox.showerror("CAP-Online", f"{escobedo.rowcount}, lineas afectadas")

def consultar_pagos(db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos conectar el modulo de consulta de pagos {err}")
    
    escobedo = doblenet.cursor()

    escobedo.execute("SELECT nombre, clave, plan, mensualidad, fechaDePago, proximoPago, efectivoIngresado, efectivoCambio, concepto FROM pagos")
    consulta_pagos = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return consulta_pagos

def buscar_pago(nombre, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Error al conectar modulo busqueda {err}")

    escobedo = doblenet.cursor()
    sql = "SELECT nombre, plan, mensualidad, fechaDePago, proximoPago FROM pagos WHERE nombre = %s"
    valores = (nombre,)
    escobedo.execute(sql, valores)
    busqueda_pago_cliente = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return busqueda_pago_cliente

def buscar_pago_clave(clave, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"Error al conectar modulo busqueda {err}")

    escobedo = doblenet.cursor()
    sql = "SELECT nombre, plan, mensualidad, fechaDePago, proximoPago FROM pagos WHERE clave = %s"
    valores = (clave,)
    escobedo.execute(sql, valores)
    busqueda_pago_clave = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return busqueda_pago_clave

def insertar_pago(nombre, clave, plan, fechaDePago, proximoPago, efectivoIngresado, efectivoCambio, concepto, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos establecer conexion al modulo pagos {err}")
    
    escobedo = doblenet.cursor()
    sql = "INSERT INTO pagos (nombre, clave, plan, fechaDePago, proximoPago, efectivoIngresado, efectivoCambio, conecpto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (nombre, clave, plan, fechaDePago, proximoPago, efectivoIngresado, efectivoCambio, concepto)

    escobedo.execute(sql, valores)
    doblenet.commit()
    escobedo.close()
    messagebox.showinfo("CAP-Online", f"Se registro el pago de manera exitosa en DB {db_name}")

def consultar_clientes(db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos reconectarnos con el modulo de consulta de clientes {err}")
    
    escobedo = doblenet.cursor()
    sql = "SELECT clave, nombre, direccion, telefono, antena, router, paquete, ip, velocidad, fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api FROM clientes"
    escobedo.execute(sql)
    consulta_clientes = escobedo.fetchall()
    escobedo.close()
    doblenet.close()
    return consulta_clientes

def insertar_cliente(clave, nombre, direccion, telefono, antena, router, paquete, ip, velocidad, fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api, db_name):
    doblenet = conexion_logica(db_name)

    if not doblenet.is_connected:
        try:
            doblenet.reconnect()
        except mysql.connector.Error as err:
            messagebox.showerror("CAP-Online", f"No podemos reconectarnos con el modulo de insertar cliente {err}")
    escobedo = doblenet.cursor()
    sql = "INSERT INTO clientes (clave, nombre, direccion, telefono, antena, router, paquete, ip, velocidad, fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (clave, nombre, direccion, telefono, antena, router, paquete, ip, velocidad, fechaInstalacion, diaCorte, proximoPago, mensualidad, estado, api)
    escobedo.execute(sql, valores)
    doblenet.commit()
    escobedo.close()
    doblenet.close()
    messagebox.showinfo("CAP-Online", "Se registro de manera correcta el cliente")