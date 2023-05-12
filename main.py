from fastapi import FastAPI
from fastapi.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from backends.auth import JWTBackend
from db import engine
from models import Base
from routers import (
    auth_router,
    branch_router,
    customer_router,
    insurance_router,
    inventory_router,
    misc_router,
    order_router,
    product_router,
)
from utils.auth import init_admin

Base.metadata.create_all(engine)
init_admin()

middleware = [Middleware(AuthenticationMiddleware, backend=JWTBackend())]

app = FastAPI(middleware=middleware)

for router in [
    branch_router,
    customer_router,
    order_router,
    product_router,
    inventory_router,
    insurance_router,
    misc_router,
    auth_router,
]:
    app.include_router(router)
