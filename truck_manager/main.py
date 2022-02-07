from typing import Final, Set

from fastapi import FastAPI

from truck_manager.model import Truck
from truck_manager.truck_repository import TruckRepositoryInMemory

DATAFILE: Final[str] = "database.json"

app = FastAPI()
repo = TruckRepositoryInMemory()


@app.on_event("startup")
def startup() -> None:
    repo.load(DATAFILE)


@app.on_event("shutdown")
def shutdown() -> None:
    repo.persist(DATAFILE)


@app.get("/trucks")
def index() -> Set[Truck]:
    return repo.retrieve_all()
