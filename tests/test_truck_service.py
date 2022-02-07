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


def test_retrieve_all_should_retrieve_truck_ids(service: TruckService) -> None:
    expected_id = service.add(
        Truck(
            plate="AAA1111",
            model_name="civic",
            tank_capacity=100,
            status="OK",
        )
    )

    result = service.retrieve_all()

    assert expected_id in result
