from truck_manager.model import Truck
from truck_manager.truck_repository import TruckRepositoryInMemory
from truck_manager.truck_service import add_truck


def test_add_truck() -> None:
    identifier = add_truck(
        Truck(plate="AAA1111", model_name="civic", tank_capacity=100, status="OK"),
        TruckRepositoryInMemory(),
    )

    print(identifier)
    assert True
