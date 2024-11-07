from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  
db = client["Airbnb"]  
servicios_collection = db["servicios"]
def insertar_servicio(id_servicio, descripcion):
    servicio = {
        "id_servicio": id_servicio,
        "descripcion": descripcion
    }
    
    servicios_collection.insert_one(servicio)
    print(f"Servicio {id_servicio} insertado correctamente.")
