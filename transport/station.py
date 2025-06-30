class Station:
    """
    Clase que representa una estacion dentro de la red de transporte urbano.
    """
    def __init__(self, name, id, latitud = None, longitud = None, capacidad = 50, servicios = None):
        """
        Inicializa una nueva estacion.

        Parametros
        ----------
        name : str
            nombre de la estacion
        id : str
            id de la estacion
        latitud : float
            latitud geografica de la estacion
        longitud : float
            longitud geografica de la estacion
        capacidad : int
            capacidad de la estacion

        """
        self.name = name
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.capacidad = capacidad
        self.servicios = servicios if servicios else []
        self.pasajeros = []

    def añadir_pasajero(self, pasajero):
        """
        Añade un pasajero a la estacion si hay capacidad disponible

        Parametros
        ----------
        Pasajero : object

        Returns
        -------
            Boolean --> Si se añadió correctamente el pasajero
        """
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            return True
        return False

    def eliminar_pasajero(self, pasajero):
        """
        Elimina un pasajero de la estacion si se encuentra en la lista de pasajeros.

        Parametros
        ----------
        pasajero : object
        """
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
            return True
        return False

    def info(self):
        """
        Resumen con la informacion de la estacion.

        Returns
        -------
            Dict: Diccionario con la informacion de la estacion.
        """
        return {
            "Estacion ID": self.id,
            "Estacion Name": self.name,
            "Estacion Latitud": self.latitud,
            "Estacion Longitud": self.longitud,
            "Estacion Capacidad": self.capacidad,
            "Estacion Servicios": self.servicios,
            "Pasajeros Presentes": self.pasajeros
        }

    def estacion_llena(self):
        if len(self.pasajeros) >= self.capacidad:
            return True
        return False

    def __str__(self):
        return f"Station: {self.name}"