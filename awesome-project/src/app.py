from fastapi import HTTPException
import psycopg2
from src.params import DB_USER, DB_PASSWORD, ALLOWED_TABLES, DB_HOST, DB_NAME, DB_PORT


class DataApi(): 
    def __init__(self): 
        self.conn = self.get_db_connection()

    def get_db_connection(self):
        try : 
            conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
            return conn
        except psycopg2.Error as e:
            raise HTTPException(status_code=401, detail=f"Unauthorized, you probably use a bad login: {str(e)}")
    
    def get_data(self,table : str):
        if table not in ALLOWED_TABLES:
            self.conn.close()
            raise HTTPException(status_code=404, detail="Table non authorized")
            
            
        try: 
            cursor = self.conn.cursor()
            query = f'SELECT * FROM {table};'
            cursor.execute(query)
            rows = cursor.fetchall()
    
            return {"data": rows}
        
        except psycopg2.Error as e:
            raise HTTPException(status_code=500, detail=f"Error SQL: {str(e)}")
