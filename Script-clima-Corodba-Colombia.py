from math import e
import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
# Asegúrate de tener un archivo .env en la raíz de tu proyecto con: OPENWEATHER_API_KEY=TU_CLAVE
# 1. configuracion del proyecto y configuracion de la API
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

#probamos la API 

if not API_KEY:
    print("API no encontrada")
    print("Asegúrate de tener un archivo .env en la raíz de tu proyecto con: OPENWEATHER_API_KEY=TU_CLAVE")
    print("Por favor, asegúrate de que el archivo .env contiene la clave API correcta.")
    exit() # Salir del script ni no hay API
else:
    print(f"API encontrada : {API_KEY} continua")
    
# Municipios de Córdoba, Colombia con sus coordenadas aproximadas
# Diccionario de coordenadas 
municipios_cordoba = [
    {"nombre": "Montería", "lat": 8.749999, "lon": -75.883331},
    {"nombre": "Cereté", "lat": 8.877861, "lon": -75.795115},
    {"nombre": "Lorica", "lat": 9.231221, "lon": -75.814323},
    {"nombre": "Sahagún", "lat": 8.932824, "lon": -75.541484},
    {"nombre": "Planeta Rica", "lat": 8.361667, "lon": -75.584167},
]

print(municipios_cordoba[2])

UNITS = "metric"
LANG = "es"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
OUTPUT_CSV_NAME = "datos_cordoba_clima.csv"

#configuracion del caching
cache_file = "clima_cache.csv"
cache_expiration_hours = 1

def obtener_datos_de_cache(municipio_nombre):
    """
    Busca los datos de un municipio en el archivo de caché.
    Si los datos existen y no han expirado, los retorna.
    si no retorna los empieza a estraer de la API    """
    if not os.path.exists(cache_file):
        return None
    
    try:
        df_cache= pd.read_csv(cache_file)
        df_cache['timestamp'] = pd.to_datetime(df_cache['timestamp'])
        cached_data = df_cache[df_cache['municipio'].str.lower() == municipio_nombre.lower()]
        if not cached_data.empty:
            cached_time = cached_data.iloc[0]['timestamp']
            if (datetime.now() - cached_time) < timedelta(hours=cache_expiration_hours):
                print(f"Datos de {municipio_nombre} obtenidos en la cache no se llama a la API")
                return cached_data.iloc[0].to_dict()
    except(pd.errors.EmptyDataError, KeyError) as e:
        print(f"Erro al leero o procesar datos de caché. se procedera con la API")
    return None
