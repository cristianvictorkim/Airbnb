import redis
import uuid
from datetime import datetime
from tabulate import tabulate  

r = redis.Redis(host='localhost', port=6379, db=0)

def crear_reserva(usuario_id, propiedad_id, fecha_inicio, fecha_fin, monto, metodo_pago, estado_reserva):
    reserva_id = f"reserva:{str(uuid.uuid4())}" 
    reserva_data = {
        'usuario_id': usuario_id,
        'propiedad_id': propiedad_id,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'monto': monto,
        'metodo_pago': metodo_pago,
        'estado_reserva': estado_reserva,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    try:
        r.hset(reserva_id, mapping=reserva_data)
        print(f"\nReserva {reserva_id} creada exitosamente en Redis.\n")
        
        stored_reserva = r.hgetall(reserva_id)
        headers = ["Campo", "Valor"]
        rows = [(key.decode('utf-8'), value.decode('utf-8')) for key, value in stored_reserva.items()]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
        return reserva_id
    except redis.RedisError as e:
        print(f"Error al crear la reserva en Redis: {e}")
        return None

def agregar_pago(reserva_id, estado_pago, monto, metodo_pago):
    pago_id = f"pago:{str(uuid.uuid4())}"  
    pago_data = {
        'reserva_id': reserva_id,
        'estado_pago': estado_pago,
        'monto': monto,
        'metodo_pago': metodo_pago,
        'fecha_pago': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    try:
        r.hset(pago_id, mapping=pago_data)
        print(f"\nPago {pago_id} registrado exitosamente en Redis.\n")
        
        stored_pago = r.hgetall(pago_id)
        headers = ["Campo", "Valor"]
        rows = [(key.decode('utf-8'), value.decode('utf-8')) for key, value in stored_pago.items()]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        
        return pago_id
    except redis.RedisError as e:
        print(f"Error al registrar el pago en Redis: {e}")
        return None

def ver_reservas_y_pagos():
    print("\n----- Reservas en Redis -----")
    reservas_keys = r.keys("reserva:*")
    if reservas_keys:
        for reserva_key in reservas_keys:
            tipo_reserva = r.type(reserva_key)
            print(f"Tipo de la clave '{reserva_key.decode('utf-8')}': {tipo_reserva}")
            
            if tipo_reserva == b'hash': 
                reserva_data = r.hgetall(reserva_key)
                print(f"\nReserva ID: {reserva_key.decode('utf-8')}")
                headers = ["Campo", "Valor"]
                rows = [(key.decode('utf-8'), value.decode('utf-8')) for key, value in reserva_data.items()]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print(f"La clave {reserva_key.decode('utf-8')} no es un hash, es de tipo {tipo_reserva}.")
    else:
        print("No hay reservas almacenadas.")

    print("\n----- Pagos en Redis -----")
    pagos_keys = r.keys("pago:*")
    if pagos_keys:
        for pago_key in pagos_keys:
            tipo_pago = r.type(pago_key)
            print(f"Tipo de la clave '{pago_key.decode('utf-8')}': {tipo_pago}")
            
            if tipo_pago == b'hash': 
                pago_data = r.hgetall(pago_key)
                print(f"\nPago ID: {pago_key.decode('utf-8')}")
                headers = ["Campo", "Valor"]
                rows = [(key.decode('utf-8'), value.decode('utf-8')) for key, value in pago_data.items()]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print(f"La clave {pago_key.decode('utf-8')} no es un hash, es de tipo {tipo_pago}.")
    else:
        print("No hay pagos almacenados.")

if __name__ == "__main__":
    ver_reservas_y_pagos()
