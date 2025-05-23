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

            #Descartar los registros que digan "ND"

            if provincia == "ND":
                continue 

            total_ventas = float(fila['TOTAL_VENTAS'])  
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += total_ventas
            else:
                ventas_por_provincia[provincia] = total_ventas
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre):
        """Retorna el total de ventas de una provincia determinada"""
        ventas_por_provincia = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.strip().upper()  # Convertir nombre a mayusculas

        if nombre_normalizado not in ventas_por_provincia:
            raise KeyError(f"La provincia '{nombre}' no se encuentra en los datos.")
        return ventas_por_provincia[nombre_normalizado]
    
    def exportaciones_totales_por_mes(self):
        """Retorna un diccionario con el total de exportaciones agrupadas por mes."""
        exportaciones_por_mes = {}
        for fila in self.datos:
            mes = fila['MES']
            exportaciones = float(fila['EXPORTACIONES']) if fila['EXPORTACIONES'] else 0.0
            if mes in exportaciones_por_mes:
                exportaciones_por_mes[mes] += exportaciones
            else:
                exportaciones_por_mes[mes] = exportaciones
        return exportaciones_por_mes

    def provincia_con_mayor_importacion(self):
        """Retorna la provincia con el mayor volumen de importaciones."""
        importaciones_por_provincia = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue
            importaciones = float(fila['IMPORTACIONES']) if fila['IMPORTACIONES'] else 0.0
            if provincia in importaciones_por_provincia:
                importaciones_por_provincia[provincia] += importaciones
            else:
                importaciones_por_provincia[provincia] = importaciones

        if not importaciones_por_provincia:
            raise ValueError("No hay datos de importaciones disponibles.")

        # Buscar la provincia con la mayor importación
        provincia_max = max(importaciones_por_provincia, key=importaciones_por_provincia.get)
        return provincia_max, importaciones_por_provincia[provincia_max]
    
    def porcentaje_ventas_tarifa_cero(self):
        """Calcula el promedio del porcentaje de ventas con tarifa 0% por provincia"""
        acumulados = {}
        conteos = {}

        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue

            try:
                tarifa_0 = float(fila['VENTAS_NETAS_TARIFA_0'])
                total_ventas = float(fila['TOTAL_VENTAS'])
                if total_ventas == 0:
                    continue
                porcentaje = (tarifa_0 / total_ventas) * 100

                if provincia in acumulados:
                    acumulados[provincia] += porcentaje
                    conteos[provincia] += 1
                else:
                    acumulados[provincia] = porcentaje
                    conteos[provincia] = 1
            except ValueError:
                continue  # Si algún dato no es numérico

        # Calcular promedio por provincia
        promedios = {}
        for provincia in acumulados:
            promedios[provincia] = acumulados[provincia] / conteos[provincia]
        
        return promedios
    
    def diferencia_ventas_exportaciones(self):
        """Calcula la diferencia entre ventas totales y exportaciones por provincia"""
        diferencias = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue
            try:
                ventas = float(fila['TOTAL_VENTAS'])
                exportaciones = float(fila['EXPORTACIONES'])
                if provincia in diferencias:
                    diferencias[provincia] += (ventas - exportaciones)
                else:
                    diferencias[provincia] = ventas - exportaciones
            except (ValueError, KeyError):
                continue
        return diferencias
