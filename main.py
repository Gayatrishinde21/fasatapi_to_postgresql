from fastapi import FastAPI
from database import get_db_connection
from model import Employee
from typing import List
from psycopg2.extras import RealDictCursor

# Initialize FastAPI app
app = FastAPI()

# GET endpoint to fetch all employees
@app.get("/employees", response_model=List[Employee])
async def get_employees():
    conn = get_db_connection()
    if conn is None:
        return []  # Return empty list instead of error dict
    
    try:
        # Create a cursor to execute queries
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        # Execute SELECT query
        cursor.execute("SELECT * FROM public.employees")
        # Fetch all rows
        employees = cursor.fetchall()
        # Close cursor and connection
        cursor.close()
        conn.close()
        # Return data as JSON
        return employees
    except Exception as e:
        print(f"Query error: {e}")
        return []  # Return empty list on error
