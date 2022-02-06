from uuid import uuid4

from truck_manager.model import Truck, parse_truck_id
from truck_manager.truck_repository import TruckRepositoryInMemory
from truck_manager.truck_service import add_truck


def test_add_truck() -> None:
    expected_id = parse_truck_id(uuid4())

    result = add_truck(
        Truck(
            identifier=expected_id,
            plate="AAA1111",
            model_name="civic",
            tank_capacity=100,
            status="OK",
        ),
        TruckRepositoryInMemory(),
    )

    assert result == expected_id
