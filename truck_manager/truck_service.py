from typing import Set

from truck_manager.model import Truck, TruckId
from truck_manager.truck_repository import TruckRepository


class TruckService:
    def __init__(self, repository: TruckRepository) -> None:
        self._repository = repository

    def retrieve_all(self) -> Set[TruckId]:
        return self._repository.retrieve_all()

    def add(self, truck: Truck) -> TruckId:
        return self._repository.add(truck)
