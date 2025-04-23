import psycopg2
from psycopg2.extras import RealDictCursor

# Function to get database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="add_db",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
