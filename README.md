# Hagamos lo mismo, pero con un ORM como SQLAlchemy.
Falta poco!

Ahora para terminar, vamos a usar SQLAlchemy en vez del conector de postgres.

Empecemos con el repository otra vez:

```python
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.migrations.tables.tables import users

@staticmethod
def get_users_with_birthdate_sqlalchemy() -> str:
    engine = create_engine("postgresql://salud:salud@db:5432/usuarios")
    Session = sessionmaker(bind=engine)

    with Session() as session:
        stmt = select(users).where(users.c.birthdate is not None)
        results = session.execute(stmt).fetchall() # stmt -> statement
        return results
```

Notesé las diferencias y abstracciones frente al conector.

Service:
```python
    @staticmethod
    def get_users_with_age_sqlalchemy():
        """Retrieve users with their birthdate using SQLAlchemy."""
        results = UserQueries.get_users_with_birthdate_sqlalchemy()

        if not results:
            return []

        results_dict = [{"email": user.email, "birthdate": user.birthdate} for user in results]
        for user in results_dict:
            today = datetime.date.today()
            birthdate = user['birthdate']
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            user['age'] = age
        return results_dict
```
Acá, como es de esperar, no cambia nada, porque la idea de la capa de repository es poder abstraer el acceso a la base de datos (y la base de datos usada).

Controller:
```python

@router.get("/users_age_sqlalchemy", summary="Get users with age using SQLAlchemy")
def get_users_with_age_sqlalchemy():
    """
    Retrieve users with their age calculated from birthdate using SQLAlchemy.
    """
    users = UserService.get_users_with_age_sqlalchemy()
    return {"users": users}
```

Probalo, fijate que te ande, y si fuiste el primero en terminar escribime "Ya sé todo de migraciones!" en el chat.


Prueben, experimenten, creen queries, hagan migraciones!
