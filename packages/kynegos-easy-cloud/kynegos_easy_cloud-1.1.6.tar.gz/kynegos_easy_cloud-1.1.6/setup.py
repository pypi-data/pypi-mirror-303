from setuptools import setup, find_packages

setup(
    name='kynegos_easy_cloud',      # Nombre del paquete
    version='1.1.6',                     # Versión
    packages=find_packages(),            # Encuentra automáticamente los paquetes en la estructura
    install_requires=[                   # Lista de dependencias necesarias
        'google-auth',
        'google-cloud-bigquery',
        'google-cloud-storage',
        'google-cloud-aiplatform',
        'pandas',
        'atoma',
        #'gdal==3.6.4',
        'geopandas',
    ],

    author='Kynegos - Capital Energy',
    author_email='digital.data@capitalenergy.com',
    description='Automatización de procesos de Data para Kynegos',
    long_description = open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/GabiAnt95/kynegoeasy-dataflow',  # Repositorio de GitLab
    
    # Agregar el campo de la licencia personalizada
    license='Kynegos License',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',  # Refleja tu propia licencia
        'Operating System :: OS Independent',
    ],
    
    python_requires='>=3.6',
    include_package_data=True,  # Incluir archivos adicionales en la distribución
    package_data={
        '': ['LICENSE'],  # Asegurar que el archivo LICENSE esté en la distribución
    },
)
