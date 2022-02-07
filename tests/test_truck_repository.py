import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepository, TruckRepositoryInMemory


@pytest.fixture
def repository() -> TruckRepository:
    return TruckRepositoryInMemory()


def test_add_should_return_identifier(repository: TruckRepository) -> None:
    result = repository.add(
        Truck(
            identifier=parse_truck_id("1"),
            plate="AAA1111",
            model_name="civic",
            tank_capacity=100,
            status="OK",
        )
    )

    assert result == "1"


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