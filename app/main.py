# filepath: /home/c0a23113f7/si-work/Takao/se-T10-Mt.Takao_System/SE-T10-Mt.Takao_System/app/main.py
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

class QRCode(BaseModel):
    qr_code: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "../app_html/test.html")     # ファイルパスを取得(ファイルパス変わるので、今後変更が必要)
        with open(file_path, "r", encoding="utf-8") as file:
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

# アカウントの作成を行う
@app.post("/accounts/")
def create_account(account: Account):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)", (account.username, account.email, account.password))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Account created", "account": account}


# QRコードの検証
@app.post("/verify_qr/")
def verify_qr(qr_code: QRCode):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT route_name FROM stamps WHERE qr_code = %s", (qr_code.qr_code,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return {"message": "QRコードが正しいです", "route_name": result[0]}
    else:
        return {"message": "QRコードが無効です"}