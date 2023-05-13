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
    order_router,
    product_router,
)
from utils.auth import init_admin
from utils.fixtures import setup_db_data

Base.metadata.create_all(engine)

middleware = [Middleware(AuthenticationMiddleware, backend=JWTBackend())]

app = FastAPI(middleware=middleware)

for router in [
    branch_router,
    customer_router,
    order_router,
    product_router,
    inventory_router,
    insurance_router,
    auth_router,
]:
    app.include_router(router)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    refill_db_parser = subparsers.add_parser("refilldb")
    init_admin_parser = subparsers.add_parser("initadmin")

    args = parser.parse_args()

    if args.command == "refilldb":
        setup_db_data()

    if args.command == "initadmin":
        init_admin()
