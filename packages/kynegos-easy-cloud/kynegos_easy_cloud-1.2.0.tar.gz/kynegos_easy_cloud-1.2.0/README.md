
# Kynegos Easy Cloud

`kynegos_easy_cloud` es una colección de funciones genéricas diseñadas para simplificar las operaciones con Google Cloud Platform (GCP). Este paquete facilita la interacción con servicios como Google Cloud Storage, BigQuery, y otros componentes clave de GCP, permitiendo a los desarrolladores integrar estas herramientas de manera más eficiente en sus proyectos.

Creada por la empresa Kynegos, una plataforma de negocios intersectoriales que integra el vehículo inversor de Capital Energy.

[![Downloads](https://static.pepy.tech/badge/kynegos-easy-cloud/month)](https://pepy.tech/project/kynegos-easy-cloud)

## Licencia

Este proyecto está licenciado bajo la **Kynegos License**. Esto significa que el software está autorizado solo para uso interno por Kynegos.

La redistribución, modificación, o el uso comercial de este código fuera de los equipos internos está prohibida sin el permiso previo por escrito del autor.

Para más detalles, consulta el archivo de la licencia incluido en este paquete.

## Instalación

Para instalar el paquete, utiliza pip:

```bash
pip install kynegos_easy_cloud
```

## Actualización

Para instalar el paquete, utiliza pip:

```bash
pip install --upgrade kynegos_easy_cloud
```

## Uso

### Importar el Paquete

Para comenzar a utilizar las funciones disponibles, simplemente importa el paquete en tu script de Python:

```python
import kynegos_easy_cloud.Kynegos_functions as KYNEGOS_FUNCTIONS
import kynegos_easy_cloud.Download_Catastro_Spain as CATASTRO_SPAIN
import kynegos_easy_cloud.Kynegos_GIS_functions as KYNEGOS_GIS_FUNCTIONS
```

### Exploración de Funciones

Para ver qué funciones están disponibles en el paquete, puedes utilizar la función `dir()` de Python:

```python
print(dir(KYNEGOS_FUNCTIONS))
```

Esto te mostrará una lista de todas las funciones disponibles en `kynegos_easy_cloud`.

### Ejemplo de Uso

Cada función en el paquete está diseñada para realizar una tarea específica en GCP. Aquí te mostramos un ejemplo básico de cómo utilizar una de las funciones para cargar un archivo a Google Cloud Storage:

```python
# Ejemplo de cómo subir un archivo a Google Cloud Storage
KYNEGOS_FUNCTIONS.upload_to_gcs(bucket_name='nombre_del_bucket', source_file='ruta/del/archivo.txt', destination_blob='carpeta/archivo.txt')
```

### Documentación de Funciones

Para obtener detalles sobre cómo usar cada función, puedes consultar la documentación inline mediante `help()`:

```python
help(KYNEGOS_FUNCTIONS.upload_to_gcs)
```

Esto te proporcionará una descripción detallada de los parámetros y el propósito de la función.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, envíe un correo mediante la plataforma Pypy.org

## Enlaces de Interés

- Sitio web: [Kynegos](https://kynegos.com/)
- LinkedIn: [Kynegos en LinkedIn](https://www.linkedin.com/company/kynegos/)
- X: [Kynegos en X](https://x.com/Kynegos_)
- Tracking Uso Librería: [Kynegos Cloud Automations Activity](https://www.pepy.tech/projects/kynegos-easy-cloud?versions=**)

## Posibles Problemas

### Solución a posibles problemas con `ogr2ogr`

Si al ejecutar el paquete encuentras problemas relacionados con `ogr2ogr`, sigue estos pasos para instalar correctamente GDAL en tu entorno:

#### Paso 1: Actualizar los repositorios e instalar `gdal-bin`

Ejecuta los siguientes comandos en una celda de código o en tu terminal:

```bash
# Actualizar la lista de paquetes
!apt-get update

# Instalar gdal-bin y libgdal-dev
!apt-get install -y gdal-bin libgdal-dev
```

##### Explicación:
- **gdal-bin**: Este paquete incluye las herramientas de línea de comandos de GDAL, como `ogr2ogr`, `gdal_translate`, entre otras.
- **libgdal-dev**: Proporciona los archivos necesarios para desarrollar o compilar extensiones que dependen de GDAL.

#### Paso 2: Verificar que `ogr2ogr` está instalado

Después de la instalación, verifica que `ogr2ogr` está disponible ejecutando el siguiente comando en tu terminal o celda de código en Python:

```bash
!ogr2ogr --version
```

La salida debería ser algo como:

```bash
GDAL 3.4.1, released 2021/12/27
```

#### Paso 3: Verificar en Python que `ogr2ogr` está en el `PATH`

Para asegurarte de que `ogr2ogr` está en el `PATH` y accesible desde Python, ejecuta el siguiente código:

```python
import shutil
print(shutil.which('ogr2ogr'))
```

La salida debería ser algo como:

```bash
/usr/bin/ogr2ogr
```

Esto confirma que `ogr2ogr` está disponible en tu entorno y que Python puede encontrarlo correctamente.


