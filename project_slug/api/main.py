import os

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from project_slug.api.db.session import Base, engine
from project_slug.api.logger import init_logging
from project_slug.api.routes.base import router as main_router

load_dotenv(".env")

Base.metadata.create_all(engine)

root_router = APIRouter()

app = FastAPI(title="FastAPI Base API", version="0.1.0")
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)

init_logging()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
