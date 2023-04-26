from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///db.sqlite3", echo=True)
