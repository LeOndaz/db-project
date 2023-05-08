from pathlib import Path
from fastapi import FastAPI

from db import engine
from models import Base
from routers import (
    branch_router,
    customer_router,
    insurance_router,
    inventory_router,
    order_router,
    product_router,
)
from utils.fixtures import setup_db_data


# remove existing db.sqlite3 & re-init on each server run
Path('db.sqlite3').unlink(missing_ok=True)

Base.metadata.create_all(engine)

app = FastAPI()

for router in [
    branch_router,
    customer_router,
    order_router,
    product_router,
    inventory_router,
    insurance_router,
]:
    app.include_router(router)


setup_db_data()
