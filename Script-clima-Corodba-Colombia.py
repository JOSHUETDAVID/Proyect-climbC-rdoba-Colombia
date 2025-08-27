from math import e
import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')



if not API_KEY:
    print("API no encontrada")
    print("Asegúrate de tener un archivo .env en la raíz de tu proyecto con: OPENWEATHER_API_KEY=TU_CLAVE")
    print("Por favor, asegúrate de que el archivo .env contiene la clave API correcta.")
    exit() # Salir del script ni no hay API
else:
    print(f"API encontrada : {API_KEY} continua")
    
    
    