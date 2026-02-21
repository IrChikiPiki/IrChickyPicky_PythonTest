import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os
from dotenv import load_dotenv

load_dotenv()

db_db = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

DB_URL = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_db}"


@pytest.fixture(scope="function")
def db():
    """Фикстура для работы с БД"""
    engine = create_engine(DB_URL)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.rollback()
    session.close()
