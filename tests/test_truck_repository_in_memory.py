import json
import os
from uuid import uuid4

import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepositoryInMemory


@pytest.fixture
def repository() -> TruckRepositoryInMemory:
    return TruckRepositoryInMemory()


def test_add_already_existent_truck_should_raise(
    repository: TruckRepositoryInMemory,
) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)
    with pytest.raises(KeyError):
        repository.add(truck)


def test_retrieve_by_id_non_existent_truck_should_raise(
    repository: TruckRepositoryInMemory,
) -> None:
    with pytest.raises(KeyError):
        repository.retrieve_by_id(parse_truck_id(uuid4()))


def test_update_non_existent_truck_should_raise(
    repository: TruckRepositoryInMemory,
) -> None:
    with pytest.raises(KeyError):
        repository.update(
            Truck(
                plate="AAA1111",
                model_name="civic",
                tank_capacity=100,
                status="OK",
            )
        )


def test_delete_non_existent_truck_should_raise(
    repository: TruckRepositoryInMemory,
) -> None:
    with pytest.raises(KeyError):
        repository.delete(parse_truck_id(uuid4()))


def test_persist(
    repository: TruckRepositoryInMemory,
) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    repository.persist("tests/persist.json")

    with open("tests/persist.json", "r") as fp:
        content = json.load(fp)
        assert str(truck.identifier) in content
        assert truck.json() == content[str(truck.identifier)]

    os.remove("tests/persist.json")
