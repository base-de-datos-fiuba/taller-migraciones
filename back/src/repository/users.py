
class UserQueries:

    @staticmethod
    def get_user_by_email(email: str) -> str:
        return f"SELECT * FROM users WHERE email = '{email}'"

    @staticmethod
    def create_user(email: str, password: str) -> str:
        return f"INSERT INTO users (email, password) VALUES ('{email}', '{password}')"

    @staticmethod
    def update_user_password(user_id: str, new_password: str) -> str:
        return f"UPDATE users SET password = '{new_password}' WHERE id = '{user_id}'"

    @staticmethod
    def get_users_with_birthdate() -> str:
        return "SELECT email, birthdate FROM users WHERE birthdate IS NOT NULL"
