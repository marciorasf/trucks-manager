from truck_manager.model import Truck, TruckId
from truck_manager.truck_repository import TruckRepository


def add_truck(truck: Truck, repository: TruckRepository) -> TruckId:
    return repository.add(truck)
