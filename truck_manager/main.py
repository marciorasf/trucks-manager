from typing import Final, Set

from fastapi import FastAPI

from truck_manager.model import Truck, TruckId
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
    raise Exception("Not implemented yet")


@app.get("/trucks/{truck_id}")
def retrieve_truck(truck_id: str) -> Set[Truck]:
    raise Exception("Not implemented yet")


@app.post("/trucks")
def create_truck(truck: Truck) -> TruckId:
    raise Exception("Not implemented yet")


@app.put("/trucks/{truck_id}")
def update_truck(truck_id: str, truck: Truck) -> None:
    raise Exception("Not implemented yet")


@app.delete("/trucks/{truck_id}")
def delete_truck(truck_id: str) -> None:
    raise Exception("Not implemented yet")
