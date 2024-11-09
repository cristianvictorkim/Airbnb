import sqlite3

def create_connection():
    connection = sqlite3.connect("airbnb.db")
    return connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    tables = {
        "huesped": """
            CREATE TABLE IF NOT EXISTS huesped (
                id_huesped INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT,
                telefono INTEGER
            );
        """,
        "propietario": """
            CREATE TABLE IF NOT EXISTS propietario (
                id_propietario INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT,
                telefono INTEGER,
                email TEXT,
                calificacion REAL
            );
        """,
        "reserva": """
            CREATE TABLE IF NOT EXISTS reserva (
                id_reserva INTEGER PRIMARY KEY,
                id_pago INTEGER,
                id_huesped INTEGER,
                id_propiedad INTEGER,
                estado TEXT,
                fecha_inicio TEXT,
                fecha_fin TEXT,
                FOREIGN KEY (id_huesped) REFERENCES huesped(id_huesped),
                FOREIGN KEY (id_propiedad) REFERENCES propiedad(id_propiedad)
            );
        """,
        "pago": """
            CREATE TABLE IF NOT EXISTS pago (
                id_pago INTEGER PRIMARY KEY,
                id_reserva INTEGER,
                estado TEXT,
                monto REAL,
                metodo TEXT
                FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva),
            );
        """,
        "propiedad": """
            CREATE TABLE IF NOT EXISTS propiedad (
                id_propiedad INTEGER PRIMARY KEY,
                id_propietario INTEGER,
                precio REAL,
                ubicacion TEXT,
                tipo TEXT,
                descripcion TEXT,
                FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
            );
        """,
        "propiedad_servicio": """
            CREATE TABLE IF NOT EXISTS propiedad_servicio (
                id_propiedad INTEGER,
                id_servicio INTEGER,
                PRIMARY KEY (id_propiedad, id_servicio),
                FOREIGN KEY (id_propiedad) REFERENCES propiedad(id_propiedad),
                FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio)
            );
        """,
        "servicios": """
            CREATE TABLE IF NOT EXISTS servicios (
                id_servicio INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL
            );
        """,
        "reseña": """
            CREATE TABLE IF NOT EXISTS reseña (
                id_reseña INTEGER PRIMARY KEY,
                id_reserva INTEGER,
                id_propietario INTEGER,
                calificacion REAL,
                comentario TEXT,
                FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva),
                FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
                
            );
        """
    }

    for table_name, table_sql in tables.items():
        cursor.execute(table_sql)
        print(f"Tabla {table_name} creada correctamente.")

    # Guardar y cerrar la conexión
    connection.commit()
    connection.close()

def insertar_huesped(nombre, apellido, telefono):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO huesped (nombre, apellido, telefono) VALUES (?, ?, ?)",
                   (nombre, apellido, telefono))
    conn.commit()
    conn.close()

def insertar_propietario(nombre, apellido, telefono, email, calificacion):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO propietario (nombre, apellido, telefono, email, calificacion) VALUES (?, ?, ?, ?, ?)",
        (nombre, apellido, telefono, email, calificacion)
    )
    conn.commit()
    conn.close()

def insertar_reserva(id_pago, id_huesped, id_propiedad, estado, fecha_inicio, fecha_fin):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reserva (id_pago, id_huesped, id_propiedad, estado, fecha_inicio, fecha_fin) VALUES (?, ?, ?, ?, ?, ?)",
        (id_pago, id_huesped, id_propiedad, estado, fecha_inicio, fecha_fin)
    )
    conn.commit()
    conn.close()

def insertar_pago(id_reserva, estado, monto, metodo):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pago (id_reserva, estado, monto, metodo) VALUES (?, ?, ?, ?)",
        (id_reserva, estado, monto, metodo)
    )
    conn.commit()
    conn.close()

def insertar_propiedad(id_propietario, precio, ubicacion, tipo, descripcion):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO propiedad (id_propietario, precio, ubicacion, tipo, descripcion) VALUES (?, ?, ?, ?, ?)",
        (id_propietario, precio, ubicacion, tipo, descripcion)
    )
    conn.commit()
    conn.close()

def insertar_propiedad_servicio(id_propiedad, id_servicio):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO propiedad_servicio (id_propiedad, id_servicio) VALUES (?, ?)",
        (id_propiedad, id_servicio)
    )
    conn.commit()
    conn.close()

def insertar_servicio(nombre):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO servicios (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def insertar_reseña(id_reserva, id_propietario, calificacion, comentario):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reseña (id_reserva, id_propietario, calificacion, comentario) VALUES (?, ?, ?, ?)",
        (id_reserva, id_propietario, calificacion, comentario)
    )
    conn.commit()
    conn.close()

def ver_huespedes():
    conn = sqlite3.connect("airbnb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM huesped")
    huespedes = cursor.fetchall()
    
    for huesped in huespedes:
        print(huesped)
    
    conn.close()

if __name__ == "__main__":
    ver_huespedes()
