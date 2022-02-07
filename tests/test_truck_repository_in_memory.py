import json
import os

import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepositoryInMemory


def test_add_already_existent_truck_should_raise() -> None:
    repository = TruckRepositoryInMemory()
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    with pytest.raises(KeyError):
        repository.add(truck)


def test_retrieve_by_id_non_existent_truck_should_raise() -> None:
    repository = TruckRepositoryInMemory()

    with pytest.raises(KeyError):
        repository.retrieve_by_id(parse_truck_id("1"))


def test_update_non_existent_truck_should_raise() -> None:
    repository = TruckRepositoryInMemory()

    with pytest.raises(KeyError):
        repository.update(
            Truck(
                plate="AAA1111",
                model_name="civic",
                tank_capacity=100,
                status="OK",
            )
        )


def test_delete_non_existent_truck_should_raise() -> None:
    repository = TruckRepositoryInMemory()

    with pytest.raises(KeyError):
        repository.delete(parse_truck_id("1"))


def test_persist() -> None:
    repository = TruckRepositoryInMemory()
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
        assert truck.identifier in content
        assert truck.json() == content[truck.identifier]

    os.remove("tests/persist.json")


def test_load() -> None:
    repository = TruckRepositoryInMemory()
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)
    repository.persist("tests/load.json")

    other_repo = TruckRepositoryInMemory()
    other_repo.load("tests/load.json")
    assert truck in other_repo.retrieve_all()
