import os

import pytest
from dotenv import load_dotenv

from project_slug.api.db.mock_session import engine, test_client
from project_slug.api.db.session import Base

load_dotenv(".env")

X_TOKEN = os.environ["X_TOKEN"]
HEADERS = {"X-Token": X_TOKEN}


@pytest.fixture(autouse=True)
def client():
    return test_client()


def pytest_configure(config):
    # It drops everything from the db and then recreate each time tests runs
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def pytest_unconfigure(config):
    pass
