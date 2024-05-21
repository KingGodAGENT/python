from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
