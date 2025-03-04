from src.app import DataApi
from fastapi import FastAPI

app = FastAPI()

data_app= DataApi()

@app.get("/api/{table}")
def app_data(table): 
    return data_app.get_data(table)
