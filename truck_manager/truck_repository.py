from typing import Dict, Protocol, Set

from truck_manager.model import Truck, TruckId


class TruckRepository(Protocol):
    def add(self, truck: Truck) -> TruckId:
        pass

    def retrieve_all(self) -> Set[TruckId]:
        pass


class TruckRepositoryInMemory:
    def __init__(self) -> None:
        self._trucks: Dict[TruckId, Truck] = {}

    def add(self, truck: Truck) -> TruckId:
        self._trucks[truck.identifier] = truck
        return truck.identifier

    def retrieve_all(self) -> Set[TruckId]:
        return set(self._trucks.keys())
