from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
from sqlalchemy.orm import Session

from project_slug.api.auth import verify_token
from project_slug.api.db.session import get_db
from project_slug.api.models.foo import Foo as FooModel
from project_slug.api.models.foo import FooSchema
from project_slug.core.foo import core_functionality

router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/ping", status_code=200)
def healthcheck():
    return JSONResponse(content=jsonable_encoder("pong"), status_code=200)


@router.get("/cf", status_code=200)
def healthcheck():
    return {"data": core_functionality()}


@router.get("/foos", status_code=200)
def get_foos(db: Session = Depends(get_db)):
    return db.query(FooModel).all()


@router.get("/foos/{foo_id}", status_code=200)
def get_foo(foo_id: int, db: Session = Depends(get_db)):
    foo = db.query(FooModel).filter(FooModel.id == foo_id).first()
    if not foo:
        return JSONResponse(content=jsonable_encoder({"detail": "Foo not found"}), status_code=404)
    return foo


@router.post("/foo", status_code=201)
def create_foo(foo: FooSchema, db: Session = Depends(get_db)):
    foo_model = FooModel(**foo.model_dump())

    db.add(foo_model)
    db.commit()
    db.refresh(foo_model)
    logger.success("Added a sneaker.")
    return foo_model
