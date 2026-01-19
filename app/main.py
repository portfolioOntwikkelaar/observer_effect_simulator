from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import router

app = FastAPI(title="Observer Effect Simulator")
app.include_router(router)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")