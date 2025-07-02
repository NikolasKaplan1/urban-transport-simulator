class Trip:
    """
    Clase que representa un viaje de un vehículo en una ruta.
    """

    def __init__(self, trip_id, vehiculo, ruta):
        """
        Inicializa el viaje.

        Parámetros
        ----------
        trip_id : str
            Identificador del viaje.
        vehiculo : Vehicle
            Vehículo que realiza el viaje.
        ruta : Ruta
            Ruta que seguirá el vehículo.
        """
        self.trip_id = trip_id
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.estacion_actual = None
        self.completo = False

    def comenzar_viaje(self):
        """
        Empieza el viaje asignando la primera estación de la ruta.
        """
        if self.ruta.estaciones:
            self.estacion_actual = self.ruta.estaciones[0]
            self.vehiculo.estado = "En ruta"

    def mover_a_siguiente_estacion(self):
        """
        Avanza el viaje a la siguiente estación de la ruta.
        Si no hay más estaciones, marca el viaje como completo.
        """
        estaciones = self.ruta.estaciones
        if self.estacion_actual in estaciones:
            indice = estaciones.index(self.estacion_actual)
            if indice + 1 < len(estaciones):
                self.estacion_actual = estaciones[indice + 1]
            else:
                self.completar_viaje()

    def completar_viaje(self):
        """
        Marca el viaje como completado.
        """
        self.completo = True
        self.vehiculo.estado = "En estación"

    def info(self):
        """
        Devuelve un resumen del viaje.

        Returns
        -------
        dict
            Información del viaje.
        """
        return {
            "trip_id": self.trip_id,
            "vehiculo": str(self.vehiculo),
            "ruta": str(self.ruta),
            "estacion_actual": str(self.estacion_actual) if self.estacion_actual else None,
            "completo": self.completo
        }

    def __str__(self):
        """
        Devuelve la representación en texto del viaje.

        Returns
        -------
        str
        """
        return f"Viaje {self.trip_id}"

