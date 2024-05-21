class Inventory:
    def __init__(self):
        self.items = {}

    def add_product(self, product):
        self.items[product.get_name()] = product

    def get_inventory(self):
        return self.items
