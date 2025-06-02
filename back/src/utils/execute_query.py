from src.utils.connect_to_db import connect_to_db

def execute_query(query):
    """
    Executes a SQL query using the provided database connection.

    Args:
        query (str): The SQL query to execute.
        db_connection: The database connection object.

    Returns:
        list: A list of tuples containing the results of the query.
    """
    with connect_to_db() as db_connection:
        cursor = db_connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            print(f"Error executing query: {e}")
            raise e
        finally:
            cursor.close()
