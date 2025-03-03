from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
from params import DB_USER, DB_PASSWORD

app = FastAPI()

DB_HOST = "host.docker.internal"  # switch to localhost if you are not using the dev container
DB_NAME = "awesomeinc"
DB_PORT = 5432  

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
    return conn

class Row(BaseModel):
    column1: str
    column2: str
    column3: str

@app.get("/api/data")
def get_data():
    conn = get_db_connection()
    pointer = conn.cursor()
    pointer.execute('SELECT * FROM country LIMIT 10;') 
    rows = pointer.fetchall()
   
    pointer.close()
    conn.close()

    return rows

