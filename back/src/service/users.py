from src.utils.execute_query import execute_query
from src.repository.users import UserQueries

class UserService:
    @staticmethod
    def get_user_by_email(self, email: str):
        """Retrieve a user by their email."""
        results = execute_query(UserQueries.get_user_by_email(email))
        if results:
            return results[0]
        raise Exception(f"User with email {email} not found")

    @staticmethod
    def create_user(self, email: str, name: str):
        """Create a new user with the provided email and name."""
        execute_query(UserQueries.create_user(email, name))
        return {"email": email, "name": name}
