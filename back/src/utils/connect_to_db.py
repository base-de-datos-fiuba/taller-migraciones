import psycopg2

def connect_to_db(host: str = "localhost", port: str = "5432") -> psycopg2.extensions.connection:
    """Connect to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname="salud",
            user="salud",
            password="salud",
            host=host,
            port=port
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        exit(1)