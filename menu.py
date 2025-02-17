import sqlite3
import os

class Menu:
    def __init__(self):
        self.conn = sqlite3.connect('hamburguesa-rapida.db')
        self.c = self.conn.cursor()

    def agregar_producto(self, clave, nombre, precio):
        """Agrega un nuevo producto al menú"""
        self.c.execute("INSERT INTO menu (clave,nombre, precio)VALUES (?,?,?)",(clave,nombre,precio))
        self.conn.commit()
        print("Producto agregado.")

    def eliminar_productos(self, clave):
        """Elimina un producto del menú"""
        self.c.execute("DELETE FROM menu WHERE clave=?",(clave))
        self.conn.commit()
        print("Producto eliminado.")

    def actualizar_producto(self, clave, nombre= None, precio=None):
        """Actualiza un producto."""
        if nombre:
            self.c.execute("UPDATE menu SET nombre=? WHERE clave=?", (nombre,clave))
        if precio is not None:
            self.x.execute("UPDATE menu SET precio=? WHERE clave=?", (precio, clave))
        self.conn.commit()
        print("Producto actualizado.")    

    def obtener_productos(self, nombre):
        """Verifica si un producto existe por su nombre"""
        self.c.execute("SELECT 1 FROM menu WHERE nombre=?", (nombre,))
        return self.c.fetchone() is not None
        
    def existe_producto(self, nombre):
        """Revisa si un producto existe por su nombre"""
        self.c.execute("SELECT 1 FROM menu WHERE nombre=?", (nombre,))
        return self.c.fetchone() is not None
        
                                 