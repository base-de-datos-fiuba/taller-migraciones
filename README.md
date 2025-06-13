# Analicemos el conector psycopg para PostgreSQL

El conector nos sirve para ejecutar consultas SQL y obtener resultados de una base de datos PostgreSQL.

Para eso, tiene que crear una conexión, definir un cursor, y ejecutar las consultas.

La conexión es un objeto que representa la conexión a la base de datos, y se crea con la función `psycopg.connect()`.

```python
import psycopg2

connection = psycopg2.connect(
    dbname="salud",
    user="salud",
    password="salud",
    host=host,
    port=port
)
```

El cursor es un objeto que actua como interfaz frente al servidor de la base de datos, nos deja ejecutar y obtener el resultado de las consultas en si.
Este necesita de una conexión para ser creado, y se crea con el método `connection.cursor()`.

```python
with connect_to_db() as db_connection:
    cursor = db_connection.cursor() # db_connection es del tipo psycopg2.extensions.connection
    try:
        cursor.execute(query) # query, podría ser el string literal "SELECT * FROM table_name"
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error executing query: {e}")
        raise e
    finally:
        cursor.close()
```

## Hagamos una query
En el branch pasado, agregamos el campo `birthdate` a la table `users`. Siguiendo la lógica del repo, que tiene una arquitectura `layers`, vamos a obtener la edad actual de los usuarios.

Hay 3 layers en el repo:
1. **service**: es la capa que se encarga de la lógica de negocio.
2. **repository**: es la capa que se encarga de interactuar con la base de datos.
3. **control**: es la capa que se encarga de recibir las peticiones HTTP y devolver las respuestas.

Vamos a crear una función en el layer `repository` que se encargue de obtener la edad de los usuarios.

```python

class UserQueries:
    # ...
    @staticmethod
    def get_users_with_birthdate() -> str:
        return f"SELECT email, birthdate FROM users WHERE birthdate IS NOT NULL"
    # ...
```

Si ejecutamos esa query, nos va a devolver una lista de tuplas con el siguiente formato:

```python
[
    ('user1@example.com', '1990-01-01'),
    ('user2@example.com', '1985-05-05'),
    ('user3@example.com', '2000-10-10')
]
```

Deberíamos traducirlo a un objeto que sea del dominio del negocio, en este caso, un objeto `User` que tenga los campos `email` y `birthdate`.

Pero para mantener el scope chico, vamos a hacer una lista de diccionarios con los campos `email` y `birthdate`.

```python
[{"email": email, "birthdate": birthdate} for email, birthdate in results] # Results es la lista de tuplas después de ser ejecutada la query
```

Entonces, en nuestra capa `service`, nos quedaría una función así:

```python
@staticmethod
def get_users_with_age():
    """Retrieve users with their birthdate."""
    results = execute_query(UserQueries.get_users_with_birthdate())

    if not results:
        return []

    results_dict = [{"email": email, "birthdate": birthdate} for email, birthdate in results]
    for user in results_dict:
        today = datetime.date.today()
        birthdate = user['birthdate']
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        user['age'] = age
    return results_dict
```

En la capa de `control`, hay que descomentar la linea que llama a la función `get_users_with_age()` y retornar el resultado.

```python
@router.get("/")
def get_users_with_age():
    """
    Retrieve users with their age calculated from birthdate.
    """
    users = []
    # users = UserService.get_users_with_age() # <- Esta
    return {"users": users}
```

Si llenamos nuestra db con unos datos corriendo `fill_db.sql`:

```bash
 docker exec -i <nombre_container> psql -U salud -d usuarios < fill_db.sql
```
Y corremos el servidor:

```bash
docker compose up --build back
```

deberíamos poder entrar a la interfaz de fastAPI en `http://localhost:8000/docs` y ver el endpoint `/users/` que nos devuelve una lista de usuarios con su edad calculada.