class TransportNetwork:
    """
    Clase que representa la red de transporte completa.
    Contiene estaciones, vehículos, rutas y viajes.
    """

    def __init__(self):
        """
        Inicializa la red vacía.
        """
        self.estaciones = []
        self.vehiculos = []
        self.rutas = []
        self.viajes = []

    def agregar_estacion(self, estacion):
        """
        Añade una estación a la red.

        Parámetros
        ----------
        estacion : Station
            Estación que se quiere añadir.
        """
        self.estaciones.append(estacion)

    def agregar_vehiculo(self, vehiculo):
        """
        Añade un vehículo a la red.

        Parámetros
        ----------
        vehiculo : Vehicle
            Vehículo que se quiere añadir.
        """
        self.vehiculos.append(vehiculo)

    def agregar_ruta(self, ruta):
        """
        Añade una ruta a la red.

        Parámetros
        ----------
        ruta : Ruta
            Ruta que se quiere añadir.
        """
        self.rutas.append(ruta)

    def agregar_viaje(self, viaje):
        """
        Añade un viaje a la red.

        Parámetros
        ----------
        viaje : Trip
            Viaje que se quiere añadir.
        """
        self.viajes.append(viaje)

    def obtener_estacion_por_id(self, estacion_id):
        """
        Busca una estación por su identificador.

        Parámetros
        ----------
        estacion_id : str
            ID de la estación.

        Returns
        -------
        Station or None
            La estación encontrada o None si no existe.
        """
        for e in self.estaciones:
            if e.id == estacion_id:
                return e
        return None

    def obtener_vehiculo_por_id(self, vehiculo_id):
        """
        Busca un vehículo por su identificador.

        Parámetros
        ----------
        vehiculo_id : str
            ID del vehículo.

        Returns
        -------
        Vehicle or None
            El vehículo encontrado o None si no existe.
        """
        for v in self.vehiculos:
            if v.id == vehiculo_id:
                return v
        return None

    def obtener_ruta_por_id(self, ruta_id):
        """
        Busca una ruta por su identificador.

        Parámetros
        ----------
        ruta_id : str
            ID de la ruta.

        Returns
        -------
        Ruta or None
            La ruta encontrada o None si no existe.
        """
        for r in self.rutas:
            if r.ruta_id == ruta_id:
                return r
        return None

    def obtener_viaje_por_id(self, viaje_id):
        """
        Busca un viaje por su identificador.

        Parámetros
        ----------
        viaje_id : str
            ID del viaje.

        Returns
        -------
        Trip or None
            El viaje encontrado o None si no existe.
        """
        for t in self.viajes:
            if t.trip_id == viaje_id:
                return t
        return None

    def info(self):
        """
        Devuelve un resumen de la red.

        Returns
        -------
        dict
            Información general del sistema.
        """
        return {
            "estaciones": len(self.estaciones),
            "vehiculos": len(self.vehiculos),
            "rutas": len(self.rutas),
            "viajes": len(self.viajes)
        }

    def __str__(self):
        """
        Representación en texto de la red.

        Returns
        -------
        str
        """
        return f"Red de Transporte: {len(self.estaciones)} estaciones, {len(self.vehiculos)} vehículos, {len(self.rutas)} rutas, {len(self.viajes)} viajes."