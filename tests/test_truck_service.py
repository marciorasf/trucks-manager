from uuid import uuid4

import pytest

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepositoryInMemory
from truck_manager.truck_service import TruckService


@pytest.fixture
def service() -> TruckService:
    repository = TruckRepositoryInMemory()
    return TruckService(repository)


def test_add_truck(service: TruckService) -> None:
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
