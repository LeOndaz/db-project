import random

from faker import Faker
from faker.providers import address, barcode, company, person, phone_number
from sqlalchemy.orm import Session

from db import engine
from models import Branch, Customer, CustomerInsurance, Insurance, Inventory
from utils import get_db_entity_list


def setup_faker():
    fake = Faker()

    for provider in [phone_number, person, address, company, barcode]:
        fake.add_provider(provider)

    return fake


def setup_db_data():
    fake = setup_faker()

    with Session(engine) as db:
        for i in range(1000):
            customer = Customer(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number="+201111111111",
                address=fake.address(),
            )
            db.add(customer)
            db.commit()

        for i in range(20):
            insurance = Insurance(
                name=fake.company(),
                discount_percentage=random.randint(0, 100),
            )
            db.add(insurance)
            db.commit()

        for customer in get_db_entity_list(db, Customer):
            customer_insurance = CustomerInsurance(
                customer_id=customer.id,
                insurance_id=random.randint(
                    1, 20
                ),  # ids of insurances are under 20 since we created 20 insurances
            )
            db.add(customer_insurance)
            db.commit()

        for i in range(10):
            branch = Branch(
                name=fake.company(),
                address=fake.address(),
                phone_number="+201111111111",
            )
            db.add(branch)
            db.commit()

            inventory = Inventory(
                name=f"inv#{i}", barcode=fake.ean(), branch_id=branch.id
            )
            db.add(inventory)
            db.commit()
