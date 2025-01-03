
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import mysql.connector
import os

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

class Account(BaseModel):
    username: str
    email: str
    password: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "../app_html/test.html")    #ファイルパスを取得。今後変更フロントエンド側待ち
        with open(file_path, "r", encoding="utf-8") as file:
            return HTMLResponse(content=file.read(), status_code=200)
    except Exception as e:
        return HTMLResponse(content=f"Error: {e}", status_code=500)
    
def read_root():
    try:
        with open(os.path.join(os.path.dirname(__file__), "../SE-T10=MT.Takao_System/app/app_html/test.html"), "r", encoding="utf-8") as file:
            return HTMLResponse(content=file.read(), status_code=200)
    except Exception as e:
        return HTMLResponse(content=f"Error: {e}", status_code=500)

@app.post("/items/")
def create_item(item: Item):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Item created", "item": item}

@app.post("/accounts/")
def create_account(account: Account):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)", (account.username, account.email, account.password))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Account created", "account": account}

#アカウント情報を登録するAPI
@app.post("/accounts")
def create_account(item: Item):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts (name, description) VALUES (%s, %s)", (item.name, item.description))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Account created", "item": item}