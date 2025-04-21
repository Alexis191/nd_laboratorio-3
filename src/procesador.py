import csv

class Analizador:
    def __init__(self, archivo_csv):
        """Inicializa la clase con la ruta al archivo CSV"""
        self.archivo_csv = archivo_csv
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        """Carga los datos del archivo CSV en una lista de diccionarios"""
        datos = []
        with open(self.archivo_csv, mode='r', encoding='latin-1') as archivo:  # Cambié 'utf-8' por 'latin-1'
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        """Retorna un diccionario con el total de ventas por provincia"""
        ventas_por_provincia = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            total_ventas = float(fila['TOTAL_VENTAS'])  # Asegurarse de que se convierte a float

            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += total_ventas
            else:
                ventas_por_provincia[provincia] = total_ventas
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        """Retorna el total de ventas de una provincia determinada"""
        ventas_por_provincia = self.ventas_totales_por_provincia()
        return ventas_por_provincia.get(nombre, 0.0)  # Si no existe la provincia, retorna 0.0