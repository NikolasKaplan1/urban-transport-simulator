class Pasajero:
    """
    Clase que representa a un pasajero en la red de transporte urbano.
    """

    def __init__(self, id, nombre, estacion_origen=None, estacion_destino=None):
        """
        Inicializa un nuevo pasajero.

        Parámetros
        ----------
        id : str
            Identificador único del pasajero.
        nombre : str
            Nombre del pasajero.
        estacion_origen : str, optional
            Estación de origen del pasajero.
        estacion_destino : str, optional
            Estación de destino del pasajero.
        """
        self.id = id
        self.nombre = nombre
        self.estacion_origen = estacion_origen
        self.estacion_destino = estacion_destino

    def info(self):
        """
        Devuelve la información del pasajero en forma de diccionario.

        Returns
        -------
        dict
            Información del pasajero.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'estacion_origen': self.estacion_origen,
            'estacion_destino': self.estacion_destino,
        }

    def __str__(self):
        """
        Devuelve una representación en texto del pasajero.

        Returns
        -------
        str
            Cadena representativa del pasajero.
        """
        return f"Pasajero {self.id}: {self.nombre}"