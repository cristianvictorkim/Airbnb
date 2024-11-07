from SQLite_db import insertar_usuario, insertar_propiedad, insertar_tipo_propiedad
from mongo_db import insertar_servicio
from cassandra_db import insertar_reserva, insertar_pago

def menu():
    print()
    print("Selecciona una operación:")
    print()
    print("1. Agregar usuario SQLite")
    print("2. Agregar propiedad SQLite")
    print("3. Agregar tipo de propiedad SQLite")
    print("4. Agregar servicio MongoDB")
    print("5. Agregar reserva")
    print("6. Agregar pago")
    print("7. Salir")
    print()

def agregar_datos(opcion):
    if opcion == "1":  # Agregar usuario en SQLite
        nombre = input("Nombre: ")
        contacto = input("Contacto: ")
        tipo_cuenta = input("Tipo de cuenta: ")
        insertar_usuario(nombre, contacto, tipo_cuenta)
    
    elif opcion == "2":  # Agregar propiedad en SQLite
        precio_noche = float(input("Precio por noche: "))
        ubicacion = input("Ubicación: ")
        id_tipo = int(input("ID Tipo de propiedad: "))
        descripcion = input("Descripción: ")
        insertar_propiedad(precio_noche, ubicacion, id_tipo, descripcion)
    
    elif opcion == "3":  # Agregar tipo de propiedad en SQLite
        nombre = input("Nombre del tipo de propiedad: ")
        insertar_tipo_propiedad(nombre)
    
    elif opcion == "4":  # Agregar servicio en MongoDB
        id_servicio = input("Ingresa el ID del servicio: ")
        descripcion = input("Ingresa la descripción del servicio: ")

        # Llamar a la función para insertar el servicio en la base de datos
        insertar_servicio(id_servicio, descripcion)

    elif opcion == "7":
        print("Saliendo del programa.")
        return False

    return True
'''
elif opcion == "5":  # Agregar reserva en Cassandra
        id_reserva = int(input("ID Reserva: "))
        id_usuario = int(input("ID Usuario: "))
        id_propiedad = int(input("ID Propiedad: "))
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
        estado = input("Estado de la reserva: ")
        insertar_reserva(id_reserva, id_usuario, id_propiedad, fecha_inicio, fecha_fin, estado)
    
    elif opcion == "6":  # Agregar pago en Cassandra
        id_pago = int(input("ID Pago: "))
        estado = input("Estado del pago: ")
        monto = float(input("Monto: "))
        metodo = input("Método de pago: ")
        insertar_pago(id_pago, estado, monto, metodo)
'''
    



def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if not agregar_datos(opcion):
            break

if __name__ == "__main__":
    main()