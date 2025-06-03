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
(nota, yo corri este comando dentro del directorio `back/src` del proyecto, y tengo este tree:)
```
alex@Alex-PC:~/Desktop/bdd/taller-migraciones$ tree
.
├── LICENSE
├── README.md
├── back
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src
│       ├── alembic.ini
│       ├── main.py
│       ├── migrations
│       │   ├── __pycache__
│       │   │   └── env.cpython-310.pyc
│       │   ├── env.py
│       │   ├── script.py.mako
│       │   ├── tables
│       │   │   ├── __pycache__
│       │   │   │   └── tables.cpython-310.pyc
│       │   │   └── tables.py
│       │   └── versions
│       │       ├── 64fec890be11_database_initialization.py
│       │       └── __pycache__
│       │           └── 64fec890be11_database_initialization.cpython-310.pyc
│       ├── repository
│       │   └── users.py
│       ├── service
│       │   └── users.py
│       └── utils
│           ├── connect_to_db.py
│           └── execute_query.py
└── docker-compose.yaml

11 directories, 18 files
```
3. Configurar el archivo `alembic.ini`:
    - Cambiar la URL de la base de datos a la que se va a conectar. (postgresql://salud:salud@localhost:5432/usuarios)
4. Crear una carpeta para las tablas y modelos:
```python
# tables.py
from sqlalchemy import Table, Column, String, MetaData

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("email", String, primary_key=True, nullable=False),
    Column('name', String, nullable=False),
)
```
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
Dentro del directorio de versions, debería aparecer un archivo con la migración inicial.
7. Aplicamos la migración a la base de datos:
```bash
alembic upgrade head
```