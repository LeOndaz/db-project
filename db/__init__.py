from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///db.sqlite3", echo=True)


def get_db():
    db = Session(engine)

    try:
        yield db
    finally:
        db.close()
