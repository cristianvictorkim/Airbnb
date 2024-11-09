from sqlite_db import insertar_huesped, insertar_propietario, insertar_propiedad
from mongo_db import insertar_servicio

def menu():
    print()
    print("Selecciona una operación:")
    print()
    print("1. Agregar huesped SQLite")
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
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        calificacion = float(input("Calificación: "))
        insertar_propietario(nombre, apellido, telefono, email, calificacion)

    elif opcion == "3":
        id_propietario = int(input("ID del propietario: "))
        precio = float(input("Precio: "))
        ubicacion = input("Ubicacion: ")
        tipo = input("Tipo: ")
        descripcion = input("Descripcion: ")
        insertar_propiedad(id_propietario, precio, ubicacion, tipo, descripcion)

    elif opcion == "4":
        id_servicio = input("Ingresa el ID del servicio: ")
        descripcion = input("Ingresa la descripción del servicio: ")
        insertar_servicio(id_servicio, descripcion)

    elif opcion == "7":
        print("Saliendo del programa.")
        return False

    return True

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if not agregar_datos(opcion):
            break

if __name__ == "__main__":
    main()