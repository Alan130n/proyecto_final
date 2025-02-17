import sqlite3

class Pedido:
    def __init__(self):
        self.conn = sqlite3.connect('hamburguesa-rapida.db')
        self.c = self.conn.cursor()

    def crear_pedido(self, pedido_id, cliente, producto, precio):
        """Crea un nuevo pedido"""
        self.c.execute("INSERT INTO pedidos (pedido_id, cliente, producto, precio) VALUES(?,?,?,?)",
                       (pedido_id, cliente, producto, precio))
        self.conn.commit()
        print("Pedido creado.")
        self.generar_ticket(pedido_id, cliente, producto, precio)

    def cancelar_pedido(self, pedido_id):
        """Cancela un pedido existente"""
        self.c.execute("DELETE FROM pedidos WHERE pedido_id=?", (pedido_id,))
        self.conn.commit()
        print("Pedido cancelado.")

    def obtener_pedidos(self):
        """Obtener todos los pedidos"""
        self.c.execute("SELECT * FROM pedidos")
        return self.c.fetchall()

    def obtener_pedido_por_id(self, pedido_id):
        """Obtiene un pedido por su ID"""
        self.c.execute("SELECT * FROM pedidos WHERE pedido_id=?", (pedido_id,))
        return self.c.fetchone()

    def generar_ticket(self, pedido_id, cliente, producto, precio):
        """Genera un ticket por pedido en TXT"""
        with open(f'ticket_{pedido_id}.txt','w') as f:
            f.write(f"Ticket de pedido\n")
            f.write(f"ID del Pedido: {pedido_id}\n")
            f.write(f"Cliente: {cliente}\n")   
            f.write(f"Producto: {producto}\n")
            f.write(f"Precio: ${precio}\n")
        print(f"Ticket generado: ticket_{pedido_id}.txt")

    