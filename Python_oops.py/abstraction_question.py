# practice the astraction question
from abc import ABC, abstractmethod

class Deliverypartner(ABC):
    @abstractmethod
    def calculate_delivery_charge(self,distance):
        pass

class Bikedelivery(Deliverypartner):
    def calculate_delivery_charge(self,distance):
        return distance * 10

class DroneDelivery(Deliverypartner):
    def calculate_delivery_charge(self, distance):
        return (distance*25) + 50

bikedelivery = Bikedelivery()
print(bikedelivery.calculate_delivery_charge(10))

droneDelivery = DroneDelivery()
print(droneDelivery.calculate_delivery_charge(10))