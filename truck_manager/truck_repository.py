import json
from typing import Dict, Iterator, Protocol, Set

from truck_manager.model import Truck, TruckId


class TruckRepository(Protocol):
    def add(self, truck: Truck) -> TruckId:
        pass

    def retrieve_all(self) -> Set[Truck]:
        pass

    def retrieve_by_id(self, identifier: TruckId) -> Truck:
        pass

    def update(self, truck: Truck) -> TruckId:
        pass

    def delete(self, identifier: TruckId) -> None:
        pass


class TruckRepositoryInMemory:
    def __init__(self) -> None:
        self._trucks: Dict[TruckId, Truck] = {}

    def add(self, truck: Truck) -> TruckId:
        if truck.identifier in self._trucks:
            raise KeyError("Truck already existent")

        self._trucks[truck.identifier] = truck
        return truck.identifier

    def retrieve_all(self) -> Set[Truck]:
        return set(self._trucks.values())

    def retrieve_by_id(self, identifier: TruckId) -> Truck:
        if identifier not in self._trucks:
            raise KeyError("Truck not found")

        return self._trucks[identifier]

    def update(self, truck: Truck) -> TruckId:
        if truck.identifier not in self._trucks:
            raise KeyError("Truck not found")

        self._trucks[truck.identifier] = truck
        return truck.identifier

    def delete(self, identifier: TruckId) -> None:
        if identifier not in self._trucks:
            raise KeyError("Truck not found")

        del self._trucks[identifier]

    def persist(self, filename: str) -> None:
        with open(filename, "w") as fp:
            json.dump(
                {str(t.identifier): t.json() for t in self._trucks.values()},
                fp,
            )

    def load(self, filename: str) -> None:
        with open(filename, "r") as fp:
            content = json.load(fp)
            self._trucks.update(
                {key: Truck(**json.loads(value)) for key, value in content.items()}
            )


def factory_in_memory_truck_repo(filename: str) -> Iterator[TruckRepositoryInMemory]:
    try:
        repo = TruckRepositoryInMemory()
        repo.load(filename)
        yield repo
    finally:
        repo.persist(filename)
