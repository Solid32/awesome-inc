from fastapi import FastAPI, HTTPException
import psycopg2
from src.params import DB_USER, DB_PASSWORD, ALLOWED_TABLES

app = FastAPI()

DB_HOST = "host.docker.internal"  # switch to localhost if you are not using the dev container
DB_NAME = "awesomeinc"
DB_PORT = 5432  

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
    return conn


@app.get("/api/{table}")
def get_data(table : str):
    if table not in ALLOWED_TABLES:
        raise HTTPException(status_code=400, detail="Table non autorisée")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = f'SELECT * FROM {table} LIMIT 10;'
        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return {"data": rows}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Erreur SQL: {str(e)}")

