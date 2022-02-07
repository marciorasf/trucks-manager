from typing import Dict, Protocol, Set

from truck_manager.model import Truck, TruckId


class TruckRepository(Protocol):
    def add(self, truck: Truck) -> TruckId:
        pass

    def retrieve_all(self) -> Set[Truck]:
        pass

    def retrieve_by_id(self, identifier: TruckId) -> Truck:
        pass


class TruckRepositoryInMemory:
    def __init__(self) -> None:
        self._trucks: Dict[TruckId, Truck] = {}

    def add(self, truck: Truck) -> TruckId:
        self._trucks[truck.identifier] = truck
        return truck.identifier

    def retrieve_all(self) -> Set[Truck]:
        return set(self._trucks.values())

    def retrieve_by_id(self, identifier: TruckId) -> Truck:
        if identifier not in self._trucks:
            raise KeyError("Truck not found")

        return self._trucks[identifier]
