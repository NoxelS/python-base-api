from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String

from project_slug.api.db.session import Base


class Foo(Base):
    __tablename__ = "foo"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    class Config:
        orm_mode = True


class FooSchema(BaseModel):
    name: str = Field()
