from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# MySQL 接続設定
db_config = {
    "host": "db",
    "user": "root",
    "password": "password",
    "database": "example_db"
}

class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Docker and MySQL!"}

@app.post("/items/")
def create_item(item: Item):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Item created", "item": item}
