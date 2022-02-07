from uuid import uuid4

import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepositoryInMemory
from truck_manager.truck_service import TruckService


@pytest.fixture
def service() -> TruckService:
    repository = TruckRepositoryInMemory()
    return TruckService(repository)


def test_add_should_return_identifier(service: TruckService) -> None:
    expected_id = parse_truck_id(uuid4())

    result = service.add(
        Truck(
            identifier=expected_id,
            plate="AAA1111",
            model_name="civic",
            tank_capacity=100,
            status="OK",
        )
    )

    assert result == expected_id


def test_add_already_existent_truck_should_raise(service: TruckService) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    service.add(truck)
    with pytest.raises(KeyError):
        service.add(truck)


def test_retrieve_all_should_retrieve_trucks(service: TruckService) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    service.add(truck)

    result = service.retrieve_all()

    assert truck in result


def test_retrieve_by_id_should_return_truck(service: TruckService) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    service.add(truck)

    result = service.retrieve_by_id(truck.identifier)

    assert result == truck


def test_retrieve_by_id_non_existent_truck_should_raise(service: TruckService) -> None:
    with pytest.raises(KeyError):
        service.retrieve_by_id(parse_truck_id(uuid4()))


def test_update_should_overwrite_attribute(service: TruckService) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    service.add(truck)

    updated_truck = truck.copy(update={"status": "BROKEN"})
    service.update(updated_truck)

    final_truck = service.retrieve_by_id(truck.identifier)
    assert final_truck.status == "BROKEN"


def test_update_non_existent_truck_should_raise(service: TruckService) -> None:
    with pytest.raises(KeyError):
        service.update(
            Truck(
                plate="AAA1111",
                model_name="civic",
                tank_capacity=100,
                status="OK",
            )
        )


def test_delete_should_delete_truck_from_repository(service: TruckService) -> None:
    truck = Truck(
        plate="AAA1111",
        model_name="civic",
        tank_capacity=100,
        status="OK",
    )
    service.add(truck)

    service.delete(truck.identifier)

    assert truck not in service.retrieve_all()


def test_delete_non_existent_truck_should_raise(service: TruckService) -> None:
    with pytest.raises(KeyError):
        service.delete(parse_truck_id(uuid4()))
