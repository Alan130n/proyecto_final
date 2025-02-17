import sqlite3


class Cliente:
    def __init__(self):
        self.conn = sqlite3.connect('hamburguesa-rapida.db')
        self.c = self.conn.cursor()

    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        """Agrega un nuevo cliente"""
        self.c.execute("INSERT INTO clientes (clave, nombre, direccion, correo, telefono) VALUES(?,?,?,?,?)",(clave, nombre, direccion, correo, telefono))
        self.conn.commit()
        print("Cliente agregado.")

    def eliminar_cliente(self,clave):
        """Elimina clientes"""
        self.c.execute("DELETE FROM clientes WHERE clave=?", (clave,))
        self.conn.commit()
        print("Cliente eliminado.")

    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo=None, telefono=None ):
        """Actualiza datos de cliente"""

        if nombre:
           self.c.execute("UPDATE clientes SET nombre=? WHERE clave=?", (nombre, clave))

        if direccion:
            self.c.execute("UPDATE clientes SET direccion=? WHERE clave=?", (direccion, clave))
        if correo:
            self.c.execute("UPDATE clientes SET correo=? WHERE clave=?", (correo,clave))
        if telefono:
            self.c.execute("UPDATE clientes SET telefono=? WHERE clave=?", (telefono,clave))
        self.conn.commit()
        print("Cliente actualizado.") 
    def obtener_clientes(self):
        """Obtiene todos los clientes"""
        self.c.execute("SELECT * FROM clientes")
        return self.c.fetchall() 
    
    def existe_cliente(self, nombre):
        """Verifica por nombre si existe un cliente""" 
        self.c.execute("SELECT 1 FROM clientes WHERE nombre=?", (nombre,))
        return self.c.fetchone() is not None
              

