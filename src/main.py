from sqlite_db import insertar_huesped, insertar_propietario, insertar_propiedad
from mongo_db import insertar_servicio

def menu():
    print()
    print("Selecciona una operación:")
    print()
    print("1. Agregar usuario SQLite")
    print("2. Agregar propietario SQLite")
    print("3. Agregar propiedad SQLite")
    print("4. Agregar servicio MongoDB")
    print("5. Agregar reserva")
    print("6. Agregar pago")
    print("7. Salir")
    print()

def agregar_datos(opcion):
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        insertar_huesped(nombre, apellido, telefono)
    
    elif opcion == "2":
        nombre = float(input("Nombre: "))
        apellido = input("Apellido: ")
        telefono = int(input("Teléfono: "))
        email = input("Email: ")
        calificacion = input("Calificación: ")
        insertar_propietario(nombre, apellido, telefono, email, calificacion)
    
    elif opcion == "3": 
        id_propietario = input("ID del propietario: ")
        precio = input("Precio: ")
        ubicacion = input("Ubicacion: ")
        tipo = input("Tipo: ")
        descripcion = ("Descripcion: ")
        insertar_propiedad(id_propietario, precio, ubicacion, tipo, descripcion)
    
    elif opcion == "4": 
        id_servicio = input("Ingresa el ID del servicio: ")
        descripcion = input("Ingresa la descripción del servicio: ")
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

        #1.	¿Cuántas reservas se realizan en una ciudad específica en el último mes?

        #2.	¿Qué tipos de alojamiento son más populares entre los usuarios?

        #3.	¿Cuántas propiedades han sido agregadas recientemente en la plataforma?

        #4.	¿Qué anfitriones tienen las mejores calificaciones?

        #5.	¿Cuáles son las áreas más demandadas para alquileres en un país?

        #6.	¿Cuántas propiedades tienen una calificación mayor a 4.5 Y están ubicadas en el centro de la ciudad?

        #7.	¿Qué tipos de alojamientos han recibido más de 20 reseñas O están en una zona turística popular?

        if not agregar_datos(opcion):
            break

if __name__ == "__main__":
    main()