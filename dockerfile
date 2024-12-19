FROM python:3.10-slim
# 作業ディレクトリ
WORKDIR /app
# 必要なパッケージをインストール
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# アプリケーションのコードをコピー
COPY app/ .
# FastAPI アプリケーションを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8000"]
