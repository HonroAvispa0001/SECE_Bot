# SECE_Bot


### Descripción del Proyecto

Este script Python permite automatizar el proceso de envío de información sobre alumnos a un servidor específico utilizando el método `GET` de HTTP. El script utiliza bibliotecas comunes como `requests`, `pandas`, y `json` para leer archivos de configuración, cargar un DataFrame con información del alumno y luego enviar esa información a un URL específico mediante requests GET individualizadas.

#### Características

- Creación automática de directorios y archivos necesarios para el funcionamiento del script, si no existen previamente.
- Lectura de configuraciones y detalles de los campos desde archivos JSON.
- Uso de un archivo CSV para mantener un registro organizado de los datos de los alumnos.
- Iteración sobre cada fila en el CSV para enviar las peticiones GET de forma individualizada.
- Personalización de headers HTTP para emular una solicitud de navegador web.

### Requisitos

- Python 3.7+
- Bibliotecas: `requests`, `pandas`, `json`, `os`
- Archivos JSON de configuración (`settings.json` y `campos.json`) y CSV de datos de alumnos (`alumnos.csv`).

### Cómo usar

1. Asegúrate de tener Python 3.7+ instalado junto con las bibliotecas necesarias.
2. Clona o descarga este repositorio.
3. En la carpeta `data`, ajusta tus configuraciones y datos en los archivos JSON y CSV correspondientes.
4. Ejecuta el script con `python sece.py`.
5. Revisa la consola para ver el estado de cada petición enviada.

### Importante

Asegúrate de usar este script responsable y éticamente. Respeta las leyes y regulaciones locales y federales aplicables y asegúrate de tener permiso para interactuar con el servidor y los datos que estás manejando.

### Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún bug o quieres añadir una nueva funcionalidad, siéntete libre de crear un issue o un pull request.
