class Vehicle:
    """
    Clase que representa a un vehiculo, con una ruta y caracteristicas asociadas.
    """
    def __init__(self, name, id, capacidad, estacion_actual = None, estado = "En estacion"):
        """
        Constructor de la clase Vehiculo.

        Parametros
        ---------
        name: str
            nombre del vehiculo
        id : str
            id del vehiculo
        capacidad: int
            capacidad del vehiculo
        estacion_actual: str
            estacion del vehiculo
        estado: str
            estado del vehiculo
        """
        self.name = name
        self.id = id
        self.capacidad = capacidad
        self.pasajeros = []
        self.estacion_actual = estacion_actual
        self.estado = estado

    def anadir_pasajero_bordo(self, pasajero):
        """
        Añade un pasajero al vehículo si hay espacio disponible.

        Parámetros
        ----------
        pasajero : object
            El pasajero a añadir al vehículo.

        Retorna
        -------
        bool
            True si el pasajero fue añadido, False si el vehículo está lleno.
        """
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            return True
        return False

    def elimina_pasajero(self, pasajero):
        """
        Elimina un pasajero del vehículo si se encuentra a bordo.

        Parámetros
        ----------
        pasajero : object
            El pasajero a eliminar del vehículo.

        Retorna
        -------
        bool
            True si el pasajero fue eliminado, False si no estaba a bordo.
        """
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
            return True
        return False

    def lleno(self):
        """
        Verifica si el vehículo está lleno.

        Retorna
        -------
        bool
            True si el número de pasajeros es igual o mayor a la capacidad, False en caso contrario.
        """
        if len(self.pasajeros) >= self.capacidad:
            return True
        return False


    def info(self):
        """
        Devuelve información relevante del vehículo.

        Retorna
        -------
        dict
            Diccionario con información del vehículo.
        """
        return {
            "ID": self.id,
            "Nombre": self.name,
            "Capacidad": self.capacidad,
            "Pasajeros a bordo": len(self.pasajeros),
            "Estación actual": self.estacion_actual,
            "Estado": self.estado
        }

    def vaciar_vehiculo(self):
        """
        Elimina todos los pasajeros del vehículo.
        """
        self.pasajeros.clear()

    def __str__(self):
        """
        Representación en cadena del vehículo.

        Retorna
        -------
        str
            Cadena descriptiva del vehículo.
        """
        return f"Vehiculo: {self.id} - {self.name}"

