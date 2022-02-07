from uuid import uuid4

import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepository, TruckRepositoryInMemory


@pytest.fixture
def repository() -> TruckRepository:
    return TruckRepositoryInMemory()


def test_add_should_return_identifier(repository: TruckRepository) -> None:
    expected_id = parse_truck_id(uuid4())

    result = repository.add(
        Truck(
            identifier=expected_id,
            plate="AAA1111",
            model_name="civic",
            tank_capacity=100,
            status="OK",
        )
    )

    assert result == expected_id


def test_retrieve_all_should_retrieve_trucks(repository: TruckRepository) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    result = repository.retrieve_all()

    assert truck in result


def test_retrieve_by_id_should_return_truck(repository: TruckRepository) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    result = repository.retrieve_by_id(truck.identifier)

    assert result == truck


def test_update_should_overwrite_attribute(repository: TruckRepository) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    updated_truck = truck.copy(update={"status": "BROKEN"})
    repository.update(updated_truck)

    final_truck = repository.retrieve_by_id(truck.identifier)
    assert final_truck.status == "BROKEN"


def test_delete_should_delete_truck_from_repository(
    repository: TruckRepository,
) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    repository.add(truck)

    repository.delete(truck.identifier)

    assert truck not in repository.retrieve_all()
