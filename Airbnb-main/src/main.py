from redis_db import crear_reserva, agregar_pago
from sqlite_db import insertar_usuario, insertar_propiedad, insertar_tipo_propiedad
from mongo_db import insertar_servicio
from datetime import datetime

def menu():
    print()
    print("Selecciona una operación:")
    print()
    print("1. Agregar usuario SQLite")
    print("2. Agregar propiedad SQLite")
    print("3. Agregar tipo de propiedad SQLite")
    print("4. Agregar servicio MongoDB")
    print("5. Agregar reserva Redis")
    print("6. Agregar pago Redis")
    print("7. Salir")
    print()

def agregar_datos(opcion):
    if opcion == "1":
        nombre = input("Nombre: ")
        contacto = input("Contacto: ")
        tipo_cuenta = input("Tipo de cuenta: ")
        insertar_usuario(nombre, contacto, tipo_cuenta)
    
    elif opcion == "2": 
        precio_noche = float(input("Precio por noche: "))
        ubicacion = input("Ubicación: ")
        id_tipo = int(input("ID Tipo de propiedad: "))
        descripcion = input("Descripción: ")
        insertar_propiedad(precio_noche, ubicacion, id_tipo, descripcion)
    
    elif opcion == "3": 
        nombre = input("Nombre del tipo de propiedad: ")
        insertar_tipo_propiedad(nombre)
    
    elif opcion == "4": 
        id_servicio = input("Ingresa el ID del servicio: ")
        descripcion = input("Ingresa la descripción del servicio: ")
        insertar_servicio(id_servicio, descripcion)

    elif opcion == "5":  
        usuario_id = input("DNI del Usuario: ")  
        propiedad_id = input("ID Propiedad: ")
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
        monto = float(input("Monto Total: "))
        metodo_pago = input("Método de pago: ")
        estado_reserva = input("Estado de la reserva: ")

        reserva_id = crear_reserva(usuario_id, propiedad_id, fecha_inicio, fecha_fin, monto, metodo_pago, estado_reserva)
        if reserva_id:
            print(f"Reserva {reserva_id} creada exitosamente en Redis.")

    
    elif opcion == "6": 
        reserva_id = input("ID Reserva: ")
        estado_pago = input("Estado del pago: ")
        monto = float(input("Monto: "))
        metodo_pago = input("Método de pago: ")
        
        pago_id = agregar_pago(reserva_id, estado_pago, monto, metodo_pago)
        if pago_id:
            print(f"Pago {pago_id} registrado exitosamente en Redis.")

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

