from fastapi import FastAPI, Request

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
