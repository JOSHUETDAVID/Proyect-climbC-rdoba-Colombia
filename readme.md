## En este proyecto extraeremos los datos de la API de OpenWeatherMap
Esto con el finde aumentar mis habilidades en Python 
Mejorar mi logica de programación y hacer un portafolio

En el Archivo " .env.example " le quitaras el .example y colocaras tus variables para que el proyecto Funcione 

Para Ejecuatar este proyecto debesa saber si tienes Python Instalado en tu PC

Para saberlo Abre la terminal y coloca "Python --version" debe aparecerte->Python 3.x.x

En VScode te iras al apartado de extenciones de VScode y descargaras la version de Microsoft

Cuando se termine buscaras la terminal y crearas un ambiente con este comando "python -m venv venv"

Esto creara una carpeta en tu proyecto en donde descargaras las dependencias 

En Windows (PowerShell/CMD):

.\venv\Scripts\activate

En macOS/Linux:



source venv/bin/activate

Verás (venv) al inicio de tu línea de comando, indicando que el entorno está activo. ¡Ahora lo que instales solo estará en esta "caja"

Las librerias que vamos usar son :requests pandas openpyxl python-dotenv
##Instalar las Dependencias DENTRO del Entorno Virtual Activo

Con (venv) activo en tu terminal, ejecuta cada comando uno por uno:

pip install request
pip install pandas 
pip install openpyxl
pip install python-dotenv

Después de instalar, puedes ejecutar pip list para ver todas las librerías instaladas en este entorno virtual. Deberías ver requests, pandas, openpyxl, python-dotenv en la lista.

VS Code necesita saber qué instalación de Python usar.

En VS Code, presiona Ctrl + Shift + P (o Cmd + Shift + P en Mac) para abrir la paleta de comandos.

Escribe "Python: Select Interpreter" y selecciónalo.

Debería aparecer una lista de intérpretes disponibles. Busca el que dice Python 3.x.x ('venv') o Python 3.x.x (.venv) y selecciónalo. Esto le dice a VS Code que use la instalación de Python de tu entorno virtual, donde están tus librerías.

Estara listo para Ejecuatar el programa 