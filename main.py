from transport import Station, Vehicle, Ruta, Trip, TransportNetwork

def main():
    red = TransportNetwork()
    viaje_actual = None

    seguir = True
    while seguir:
        print("print\n==== MENÚ DEL SISTEMA DE TRANSPORTE ====")
        print("1. Crear estación")
        print("2. Crear vehículo")
        print("3. Crear ruta")
        print("4. Crear viaje")
        print("5. Mover viaje a la siguiente estación")
        print("6. Mostrar información de la red")
        print("7. Salir")

        opcion = int(input("Introduce una opcion: "))
        while opcion < 1 or opcion > 7:
            print("Siga correctamente el menú e introduzca una opcion del 1 al 7")
            opcion = int(input("Introduce una opcion: "))

        if opcion == 1:
            # Creamos una estacion
            nombre = input("Introduce el nombre de la estacion: ")
            id = input("Introduce el id de la estacion: ")
            estacion = Station(nombre, id)
            red.agregar_estacion(estacion)
            print("Estacion creada correctamente")

        elif opcion == 2:
            # Crear vehículo
            nombre = input("Nombre del vehículo: ")
            id_vehiculo = input("ID del vehículo: ")
            capacidad = int(input("Capacidad del vehículo: "))
            vehiculo = Vehicle(nombre, id_vehiculo, capacidad)
            red.agregar_vehiculo(vehiculo)
            print("Vehículo creado correctamente.")

        elif opcion == 3:
            # Crear ruta
            ruta_id = input("ID de la ruta: ")
            nombre_ruta = input("Nombre de la ruta: ")
            estaciones_ids = input("IDs de las estaciones separadas por comas: ").split(",")
            estaciones = []
            for eid in estaciones_ids:
                est = red.obtener_estacion_por_id(eid.strip())
                if est:
                    estaciones.append(est)
                else:
                    print(f"Estación con ID {eid.strip()} no encontrada.")
            ruta = Ruta(ruta_id, nombre_ruta, estaciones)
            red.agregar_ruta(ruta)
            print("Ruta creada correctamente.")


        elif opcion == 4:
            # Crear viaje
            trip_id = input("ID del viaje: ")
            id_vehiculo = input("ID del vehículo asignado: ")
            id_ruta = input("ID de la ruta asignada: ")

            vehiculo = red.obtener_vehiculo_por_id(id_vehiculo)
            ruta = red.obtener_ruta_por_id(id_ruta)

            if vehiculo and ruta:
                viaje_actual = Trip(trip_id, vehiculo, ruta)
                red.agregar_viaje(viaje_actual)
                viaje_actual.comenzar_viaje()
                print("Viaje creado e iniciado correctamente.")
            else:
                print("Vehículo o ruta no encontrados.")

        elif opcion == 5:
            # Mover viaje a la siguiente estación
            if viaje_actual:
                viaje_actual.mover_a_siguiente_estacion()
                print("El viaje avanzó a la siguiente estación.")
                print("Estación actual:", viaje_actual.estacion_actual)
            else:
                print("No hay un viaje activo.")


        elif opcion == 6:
            # Mostrar información general de la red
            print("Información de la red:")
            print(red.info())

        elif opcion == 7:
            print("Saliendo de la red de transporte...!")
            seguir = False
            break

        else:
            print("Opcion no válida. ")
main()




