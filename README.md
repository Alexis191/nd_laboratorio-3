Análisis de Ventas SRI - Laboratorio 3

Este proyecto forma parte de una práctica de programación en la universidad. Se trata de una aplicación en Python que analiza información de ventas del SRI (Servicio de Rentas Internas) a partir de un archivo CSV. Se implementaron funcionalidades estadísticas, pruebas unitarias y se evaluó la cobertura de código utilizando `coverage`.

---

📁 Estructura del Proyecto

laboratorio-3/
├── app.py # Archivo principal que ejecuta la aplicación
├── datos/
│ └── sri_ventas_2024.csv # Datos originales del SRI
├── src/
│ └── procesador.py # Lógica del análisis de datos
├── tests/
│ └── test_analizador.py # Pruebas unitarias con unittest
└── README.md # Este documento

---

⚙️ Funcionalidades Principales

La aplicación analiza los siguientes aspectos a partir del archivo `sri_ventas_2024.csv`:

1. ✅ **Ventas totales por provincia**
2. ✅ **Consulta de ventas por una provincia específica (insensible a mayúsculas/minúsculas)**
3. ✅ **Exportaciones totales agrupadas por mes**
4. ✅ **Provincia con mayor volumen de importaciones**
5. ✅ **Porcentaje de ventas con tarifa 0% respecto al total, por provincia**
6. ✅ **Diferencia entre ventas totales y exportaciones por provincia**

---

🧪 Pruebas Unitarias

Se utilizaron pruebas unitarias con el módulo `unittest`. Las pruebas cubren:

- Validación del tipo de retorno (dict)
- Conteo de provincias esperadas (24)
- Existencia de valores mínimos
- Manejo de errores al consultar provincias inexistentes
- Insensibilidad a mayúsculas/minúsculas
- Cálculo correcto de nuevas estadísticas (como importaciones y diferencias)

---
