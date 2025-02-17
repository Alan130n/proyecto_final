import sqlite3
import os


def crear_tablas():
    conn = sqlite3.connect('hamburguesa-rapida.db')
    c = conn.cursor()


    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
              clave TEXT PRIMARY KEY,
              nombre TEXT,
              direccion TEXT,
              correo TEXT,
              telefono TEXT
              )''')
    
    c.execute(''' CREATE TABLE IF NOT EXISTS menu(
              clave TEXT PRIMARY KEY,
              nombre TEXT,
              precio REAL
              )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS pedidos (
              pedido_id INTEGER PRIMARY KEY,
              cliente TEXT,
              producto TEXT,
              precio REAL
              )''')
    
    conn.commit()
    conn.close()
