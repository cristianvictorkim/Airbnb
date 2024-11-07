import sqlite3

def create_connection():
    # Conexión a la base de datos SQLite (creará el archivo si no existe)
    connection = sqlite3.connect("airbnb.db")
    return connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Definimos las sentencias SQL para crear cada tabla
    tables = {
        "usuario": """
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                contacto TEXT,
                tipo_cuenta TEXT
            );
        """,
        "reserva": """
            CREATE TABLE IF NOT EXISTS reserva (
                id_reserva INTEGER PRIMARY KEY,
                id_pago INTEGER,
                estado TEXT,
                fecha_inicio TEXT,
                fecha_fin TEXT,
                id_usuario INTEGER,
                id_propiedad INTEGER,
                FOREIGN KEY (id_pago) REFERENCES pago(id_pago),
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
                FOREIGN KEY (id_propiedad) REFERENCES propiedad(id_propiedad)
            );
        """,
        "pago": """
            CREATE TABLE IF NOT EXISTS pago (
                id_pago INTEGER PRIMARY KEY,
                estado TEXT,
                monto REAL,
                metodo TEXT
            );
        """,
        "propiedad": """
            CREATE TABLE IF NOT EXISTS propiedad (
                id_propiedad INTEGER PRIMARY KEY,
                precio_noche REAL,
                ubicacion TEXT,
                id_tipo INTEGER,
                descripcion TEXT,
                FOREIGN KEY (id_tipo) REFERENCES tipo_propiedad(id_tipo)
            );
        """,
        "tipo_propiedad": """
            CREATE TABLE IF NOT EXISTS tipo_propiedad (
                id_tipo INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL
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
                descripcion TEXT NOT NULL
            );
        """,
        "propiedad_usuario": """
            CREATE TABLE IF NOT EXISTS propiedad_usuario (
                id_propiedad INTEGER,
                id_usuario INTEGER,
                rol TEXT,
                PRIMARY KEY (id_propiedad, id_usuario),
                FOREIGN KEY (id_propiedad) REFERENCES propiedad(id_propiedad),
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
            );
        """,
        "reseña": """
            CREATE TABLE IF NOT EXISTS reseña (
                id_reseña INTEGER PRIMARY KEY,
                id_usuario INTEGER,
                calificacion REAL,
                comentario TEXT,
                promedio REAL,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
            );
        """
    }

    # Ejecutar cada creación de tabla en SQLite
    for table_name, table_sql in tables.items():
        cursor.execute(table_sql)
        print(f"Tabla {table_name} creada correctamente.")

    # Guardar y cerrar la conexión
    connection.commit()
    connection.close()

def insertar_usuario(nombre, contacto, tipo_cuenta):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (nombre, contacto, tipo_cuenta) VALUES (?, ?, ?)", (nombre, contacto, tipo_cuenta))
    conn.commit()
    conn.close()

def insertar_propiedad(precio_noche, ubicacion, id_tipo, descripcion):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO propiedad (precio_noche, ubicacion, id_tipo, descripcion) VALUES (?, ?, ?, ?)", (precio_noche, ubicacion, id_tipo, descripcion))
    conn.commit()
    conn.close()

def insertar_tipo_propiedad(nombre):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tipo_propiedad (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def ver_usuarios():
    conn = sqlite3.connect("airbnb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    
    for usuario in usuarios:
        print(usuario)
    
    conn.close()

# Ejecutar el script para crear las tablas
if __name__ == "__main__":
    ver_usuarios()