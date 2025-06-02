import sqlite3

def crear_tabla(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orden_produccion (
            ruc TEXT PRIMARY KEY,
            fecha TEXT,
            razon_social TEXT,
            descripcion_trabajo TEXT,
            cantidad INTEGER,
            precio_total REAL,
            estado TEXT
        )
        """
    )

def limpiar_tabla(cursor):
    cursor.execute("DELETE FROM orden_produccion")

def insertar_orden(cursor, orden):
    cursor.execute(
        """
        INSERT OR REPLACE INTO orden_produccion (ruc, fecha, razon_social, descripcion_trabajo, cantidad, precio_total, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        orden
    )
    print(f"Orden insertada o reemplazada: {orden}")

def listar_ordenes(cursor):
    cursor.execute("SELECT * FROM orden_produccion")
    return cursor.fetchall()

def buscar_orden_por_ruc(cursor, ruc):
    cursor.execute("SELECT * FROM orden_produccion WHERE ruc = ?", (ruc,))
    return cursor.fetchone()

def actualizar_orden(cursor, ruc, campo, nuevo_valor):
    cursor.execute(f"UPDATE orden_produccion SET {campo} = ? WHERE ruc = ?", (nuevo_valor, ruc))

def eliminar_orden(cursor, ruc):
    cursor.execute("DELETE FROM orden_produccion WHERE ruc = ?", (ruc,))

if __name__ == "__main__":
    with sqlite3.connect('app.db') as con:
        cursor = con.cursor()
        crear_tabla(cursor)
        limpiar_tabla(cursor)  # Limpia la tabla antes de insertar datos de prueba

        # Insertar ejemplo con RUC único cada vez
        ordenes = [
            ('1234567890', '2023-10-01', 'La favorita', 'revistas', 100, 1500.00, 'Pendiente'),
            ('1234567891', '2023-10-02', 'Supermaxi', 'afiches', 200, 2500.00, 'Pendiente'),
            ('1234567892', '2023-10-03', 'Tía', 'volantes', 300, 3500.00, 'Pendiente')
        ]
        for orden in ordenes:
            insertar_orden(cursor, orden)
        con.commit()  # Guarda los cambios

        # Listar todas las órdenes
        print("\nTodas las órdenes:")
        for row in listar_ordenes(cursor):
            print(row)

        # Buscar por RUC
        ruc_buscar = '1234567891'
        resultado = buscar_orden_por_ruc(cursor, ruc_buscar)
        print(f"\nResultado de búsqueda por RUC {ruc_buscar}:")
        if resultado:
            print(resultado)
        else:
            print("No se encontró ninguna orden con ese RUC.")

        # Actualizar estado de la orden
        actualizar_orden(cursor, ruc_buscar, 'estado', 'Completado')
        con.commit()
        print(f"\nOrden con RUC {ruc_buscar} actualizada:")
        print(buscar_orden_por_ruc(cursor, ruc_buscar))

        # Eliminar la orden
        eliminar_orden(cursor, ruc_buscar)
        con.commit()
        print(f"\nOrden con RUC {ruc_buscar} eliminada.")
        print("Órdenes restantes:")
        for row in listar_ordenes(cursor):
            print(row)

print("salir")