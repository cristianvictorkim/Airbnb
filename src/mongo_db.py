# servicio.py
from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Cambia esta URL si usas un servidor remoto
db = client["Airbnb"]  # Base de datos Airbnb
servicios_collection = db["servicios"]  # Colección de servicios

def insertar_servicio(id_servicio, descripcion):
    servicio = {
        "id_servicio": id_servicio,
        "descripcion": descripcion
    }
    
    # Insertar en la colección de servicios
    servicios_collection.insert_one(servicio)
    print(f"Servicio {id_servicio} insertado correctamente.")
