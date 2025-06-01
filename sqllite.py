import sqlite3

with sqlite3.connect('app.db') as con:
    cursor = con.cursor()
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
    cursor.execute(
        """
        INSERT INTO orden_produccion (ruc, fecha, razon_social, descripcion_trabajo, cantidad, precio_total, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        ('1234567890', '2023-10-01', 'La favorita', 'revistas', 100, 1500.00, 'Pendiente')
    )

print("salir")