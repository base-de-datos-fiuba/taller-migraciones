# taller-migraciones
Para este taller vamos a ver por arriba las siguientes herramientas:

- `sqlalchemy`: ORM para Python.
- `psycopg`: Adaptador de PostgreSQL para Python.
- `alembic`: Herramienta para migraciones de bases de datos.


# Set up de alembic:

1. Instalar las dependencias:
```bash
pip install sqlalchemy alembic
```
2. Inicializar el proyecto de alembic:
```bash 
alembic init <dir>
```
En este caso, decidi poner el directorio `migrations` dentro del proyecto, pero puede ser cualquier directorio.
3. Configurar el archivo `alembic.ini`:
    - Cambiar la URL de la base de datos a la que se va a conectar.
    - Cambiar el directorio de migraciones al que se inicializó en el paso 2.
4. Configurar el archivo `env.py`:
    - Importar la metadata de sqlalchemy. (Hay que crearla)
    - - Creamos un directorio donde van a estar nuestras tablas y modelos.
    - - Creamos las tablas, e instanciamos la metadata.

5. Levantamos nuestra base de datos:
```bash
docker compose up --build db
```
6. Creamos una migración inicial:
```bash
alembic revision --autogenerate -m "Initial migration"
```
7. Aplicamos la migración a la base de datos:
```bash
alembic upgrade head
```