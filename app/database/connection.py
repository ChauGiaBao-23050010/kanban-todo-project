from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

engine = create_engine(
    settings.database_url,
    # echo=settings.database_echo, # Tạm thời tắt echo để đỡ rối terminal
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Thêm hàm này để tạo bảng lúc khởi động (chỉ dùng cho development)
def create_tables():
    Base.metadata.create_all(bind=engine)