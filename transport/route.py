class Ruta:
    """
    Clase que representa una ruta de transporte compuesta por estaciones.
    """

    def __init__(self, ruta_id, name, estaciones=None):
        """
        Inicializa una nueva ruta.

        Parámetros
        ----------
        ruta_id : str
            Identificador único de la ruta.
        name : str
            Nombre de la ruta.
        estaciones : list, optional
            Lista de estaciones iniciales.
        """
        if not isinstance(name, str):
            raise TypeError('Ruta name must be a string')
        if not isinstance(ruta_id, str):
            raise TypeError('Ruta id must be a string')

        self.ruta_id = ruta_id
        self.name = name
        self.estaciones = estaciones if estaciones else []

    def anadir_estacion(self, estacion):
        """
        Añade una estación a la ruta si no está ya presente.

        Parámetros
        ----------
        estacion : Station
            Estación a añadir.

        Returns
        -------
        bool
            True si se añadió, False si ya existía.
        """
        if estacion not in self.estaciones:
            self.estaciones.append(estacion)
            return True
        return False

    def eliminar_estacion(self, estacion):
        """
        Elimina una estación de la ruta si existe.

        Parámetros
        ----------
        estacion : Station
            Estación a eliminar.

        Returns
        -------
        bool
            True si se eliminó, False si no estaba.
        """
        if estacion in self.estaciones:
            self.estaciones.remove(estacion)
            return True
        return False

    def info(self):
        """
        Devuelve la información de la ruta.

        Returns
        -------
        dict
            Diccionario con datos de la ruta.
        """
        return {
            'ruta_id': self.ruta_id,
            'name': self.name,
            'estaciones': [str(e) for e in self.estaciones],
        }

    def __str__(self):
        """
        Representación en texto de la ruta.

        Returns
        -------
        str
        """
        return f'Ruta {self.ruta_id}: {self.name}'