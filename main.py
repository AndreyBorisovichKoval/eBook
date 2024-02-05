from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from sqlalchemy.orm import Session, sessionmaker
from routes import app as routes_app
from models import Base
from connection import engine
from datetime import timedelta

# создаем таблицы
Base.metadata.create_all(bind=engine)

app = Flask(__name__)

# Настройки для JWT
# Замените на свой секретный ключ
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
# Алгоритм подписи (по умолчанию 'HS256')
app.config['JWT_ALGORITHM'] = 'HS256'
# Срок действия токена
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)

jwt = JWTManager(app)

app.register_blueprint(routes_app)
# print('Tests')
if __name__ == '__main__':
    app.run(debug=False, port=7000)
