from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from ..db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    fullname = Column(String)
    username = Column(String)