from functools import partial
from typing import Type, Union

import phonenumbers
import sqlalchemy.exc
from fastapi import status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from sqlalchemy import inspect
from sqlalchemy.orm import Session

import models
from db import get_db


def get_object_or_404(db: Session, entity_klass, field, value):
    try:
        instance = (
            db.query(entity_klass).filter(getattr(entity_klass, field) == value).one()
        )
    except sqlalchemy.exc.NoResultFound:
        raise HTTPException(
            detail="{object} with {field}={value} does not exist".format(
                object=entity_klass.__name__, field=field, value=value
            ),
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return instance


def create_db_entity(db: Session, entity_klass, data: BaseModel):
    instance = entity_klass(**data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)

    return instance


def get_db_entity_by_id(db: Session, entity_klass, id):
    return get_object_or_404(db, entity_klass, "id", id)


def delete_by_entity_by_id(
    db: Session, entity_klass, schema_class: Type[BaseModel], id
):
    instance = get_object_or_404(db, entity_klass, "id", id)

    # we need to save the data to return it after the deletion
    data = schema_class.from_orm(instance)

    db.delete(instance)
    db.commit()

    return data


def get_db_entity_list(db: Session, entity_klass, **filters):
    return db.query(entity_klass).filter_by(**filters).all()


def from_orm(schema_klass: Type[BaseModel], db_entity):
    return schema_klass.from_orm(db_entity)


def map_from_orm(schema_klass: Type[BaseModel], db_entities):
    from_type_to_orm = partial(from_orm, schema_klass)
    return list(map(from_type_to_orm, db_entities))


def update_db_entity(
    db: Session,
    entity_klass: Type[models.Base],
    pk_value: Union[str, int],
    data: BaseModel,
    pk_field: str = "id",
):
    def mapper(item):
        return item.name

    pk_fields = map(mapper, inspect(entity_klass).primary_key)

    assert pk_field in pk_fields, (
        f"field={pk_field} is not a primary_key field"
        " or does not exist on {entity_klass.__class__.__name__}"
    )

    instance = get_object_or_404(db, entity_klass, pk_field, pk_value)

    for key, value in data.dict().items():
        setattr(instance, key, value)

    db.commit()
    db.refresh(instance)

    return instance


def validate_phone_number(phone_number: str):
    error_msg = "Invalid phone_number provided"

    try:
        obj = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(obj):
            return phone_number

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_msg)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_msg)


def drop_tables(db):
    engine = db.get_bind()
    models.Base.metadata.drop_all(bind=engine)


def create_tables(db):
    engine = db.get_bind()
    models.Base.metadata.create_all(bind=engine)


def clean_db():
    db = next(get_db())

    drop_tables(db)
    create_tables(db)
