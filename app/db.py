from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func
import enum, os

DB_URL = os.getenv("DB_URL", "sqlite:///app/data.db")

engine = create_engine(DB_URL, connect_args={"check_same_thread": False} if DB_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class FileStatus(str, enum.Enum):
    uploading = "uploading"
    processing = "processing"
    ready = "ready"
    failed = "failed"

class File(Base):
    __tablename__ = "files"
    id = Column(String, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    mime_type = Column(String, nullable=True)
    size_bytes = Column(Integer, nullable=True)
    storage_path = Column(Text, nullable=False)
    status = Column(Enum(FileStatus), nullable=False, default=FileStatus.uploading)
    upload_progress = Column(Integer, default=0)
    parse_progress = Column(Integer, default=0)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    parsed_rows = relationship("ParsedRow", back_populates="file", cascade="all, delete-orphan")

class ParsedRow(Base):
    __tablename__ = "parsed_rows"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String, ForeignKey("files.id", ondelete="CASCADE"), index=True, nullable=False)
    row_index = Column(Integer, nullable=False)
    data_json = Column(Text, nullable=False)

    file = relationship("File", back_populates="parsed_rows")

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

def init_db():
    Base.metadata.create_all(bind=engine)
