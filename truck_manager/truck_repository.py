from typing import Protocol

from truck_manager.model import Truck, TruckId


class TruckRepository(Protocol):
    def add(self, truck: Truck) -> TruckId:
        pass


class TruckRepositoryInMemory:
    def add(self, truck: Truck) -> TruckId:
        return truck.identifier
