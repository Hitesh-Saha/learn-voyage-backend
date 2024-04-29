import contextlib
import os

from sqlalchemy import exc, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
# from sqlmodel import Session, SQLModel

Base = declarative_base()

def create_db_engine():
    return create_engine(os.environ["DATABASE_URL"],echo=False)


@contextlib.contextmanager
def db_session(autocommit: bool = False, autoflush: bool = False) -> Session:
    engine = create_db_engine()
    SessionLocal = sessionmaker(
        autocommit=autocommit, autoflush=autoflush, bind=engine
    )

    session = SessionLocal()
    try:
        yield session
        session.commit()
    except exc.SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()
        # SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    with db_session() as session:
        yield session