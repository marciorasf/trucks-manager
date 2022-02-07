from typing import Set

from truck_manager.model import Truck, TruckId
from truck_manager.truck_repository import TruckRepository


class TruckService:
    def __init__(self, repository: TruckRepository) -> None:
        self._repository = repository

    def add(self, truck: Truck) -> TruckId:
        return self._repository.add(truck)

    def retrieve_all(self) -> Set[Truck]:
        return self._repository.retrieve_all()

    def retrieve_by_id(self, identifier: TruckId) -> Truck:
        return self._repository.retrieve_by_id(identifier)

    def update(self, truck: Truck) -> None:
        return self._repository.update(truck)

    def delete(self, identifier: TruckId) -> None:
        return self._repository.delete(identifier)
