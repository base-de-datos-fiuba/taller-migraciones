import datetime
from src.utils.execute_query import execute_query
from src.repository.users import UserQueries
from src.migrations.tables.tables import users
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class UserService:
    @staticmethod
    def get_user_by_email(email: str):
        """Retrieve a user by their email."""
        results = execute_query(UserQueries.get_user_by_email(email))
        if results:
            return results[0]
        raise Exception(f"User with email {email} not found")

    @staticmethod
    def get_user_by_email_sqlalchemy(email: str):
        """Retrieve a user by their email using SQLAlchemy."""
        engine = create_engine("postgresql://salud:salud@db:5432/usuarios")
        Session = sessionmaker(bind=engine)

        with Session() as session:
            stmt = select(users).where(users.c.email == email)
            result = session.execute(stmt).fetchone()
            if result:
                return dict(result._mapping)
            raise Exception(f"User with email {email} not found")

    @staticmethod
    def create_user(email: str, name: str):
        """Create a new user with the provided email and name."""
        execute_query(UserQueries.create_user(email, name))
        return {"email": email, "name": name}

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
