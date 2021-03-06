import json
import os

from truck_manager.model import Truck
from truck_manager.truck_repository import TruckRepositoryInMemory


def test_persist_repo_with_truck() -> None:
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


def test_persist_empty_repo_should_not_raise() -> None:
    repository = TruckRepositoryInMemory()
    repository.persist("tests/persist.json")

    assert os.path.exists("tests/persist.json")

    os.remove("tests/persist.json")


def test_load_existent_json() -> None:
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

    os.remove("tests/load.json")


def test_load_empty_json_should_not_raise() -> None:
    repository = TruckRepositoryInMemory()
    repository.persist("tests/load.json")

    other_repo = TruckRepositoryInMemory()
    other_repo.load("tests/load.json")

    os.remove("tests/load.json")


def test_load_non_existent_json_should_not_raise() -> None:
    other_repo = TruckRepositoryInMemory()
    other_repo.load("tests/load.json")
