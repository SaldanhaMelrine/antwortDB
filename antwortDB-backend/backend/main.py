from fastapi import FastAPI
from backend.routes.query import router

app = FastAPI(title="antwortDB API")

app.include_router(router)