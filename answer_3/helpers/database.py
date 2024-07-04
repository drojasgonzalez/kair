from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env.local
load_dotenv('.env.local')

# Configuración de la conexión a PostgreSQL con SQLAlchemy
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

SQLALCHEMY_DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importa los modelos aquí para asegurarte de que estén registrados antes de crear las tablas
from interfaces.users import Base, User
from interfaces.posts import Base, Post

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)
